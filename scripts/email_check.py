"""Check of the email reminders (Prompt 6), in dry-run mode for the three demo accounts.

    1. A forced dry run (ignoring the clock, not the content rules) gives each demo student the
       right emails: Tolu (active today) no streak email but a weekly summary, and a digest when
       there are unread recommendation notifications; Kemi and Ngozi (nothing today) a streak email
       and a weekly summary. Every email has one button into the app and an unsubscribe link.
    2. Running again sends nothing: never the same kind twice on the same day.
    3. The unsubscribe link turns email reminders off without logging in; a bad token is refused.
    4. Students read only their own email log and cannot write it.
    5. Screenshots of the three dry-run emails as rendered HTML, and of the Profile settings.

Needs the ML service (for /recommend and /email/unsubscribe) and, for the Profile shot, the Vite dev server.
Run python scripts/seed_demo.py --demo-only first.

    python scripts/email_check.py [--shots DIR]
"""

import argparse
import re
import sys
from pathlib import Path

import httpx
from playwright.sync_api import expect, sync_playwright

import testkit

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "ml"))
from app import emails  # noqa: E402  (the ML service's own sender, run in dry-run mode)

APP, ML = "http://localhost:5173", "http://localhost:8000"
DEMO_PASSWORD = "DemoPass2026!"
NEW, ACTIVE, DIAGNOSTIC = ("new.student@demo.example.com", "active.student@demo.example.com",
                           "diagnostic.student@demo.example.com")

results: list[bool] = []


def check(name: str, passed: bool, detail: str = "") -> None:
    results.append(passed)
    print(f"{'PASS' if passed else 'FAIL'}  {name}" + (f"  ({detail})" if detail else ""))


def ids(db) -> dict[str, str]:
    return {u.email: u.id for u in db.auth.admin.list_users(page=1, per_page=1000) if u.email in (NEW, ACTIVE, DIAGNOSTIC)}


def sign_in(email: str):
    client = testkit.anon()
    client.auth.sign_in_with_password({"email": email, "password": DEMO_PASSWORD})
    return client


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--shots", type=Path)
    args = parser.parse_args()
    if args.shots:
        args.shots.mkdir(parents=True, exist_ok=True)
    db = testkit.admin()
    who = ids(db)
    settings = emails.Settings.from_env()
    settings.dry_run = True  # this check never sends

    print("-- Setup")
    db.table("email_log").delete().in_("student_id", list(who.values())).execute()
    db.table("profiles").update({"email_reminders": True, "email_streak": True, "email_digest": True,
                                 "email_weekly": True}).in_("id", list(who.values())).execute()
    token = sign_in(ACTIVE).auth.get_session().access_token
    check("/recommend for Tolu (writes today's recommendation notifications)",
          httpx.post(f"{ML}/recommend", headers={"Authorization": f"Bearer {token}"}, timeout=120).status_code == 200)
    unread = emails.unread_digest_notifications(db, who[ACTIVE], emails.datetime.now(emails.LAGOS))
    print(f"      Tolu has {len(unread)} unread recommendation notification(s) today")

    print("\n-- Dry run (forced: every email whose content applies now)")
    sent = emails.run_once(db, force=True, students=set(who), settings=settings)
    by = {(r["student"], r["kind"]): r for r in sent}
    for r in sent:
        print(f"      {r['status']:8} {r['kind']:15} {r['student']:38} {r['subject']}")
    check("Tolu: no streak email (already active today)", (ACTIVE, "streak_at_risk") not in by)
    check("Tolu: a digest exactly when there are unread notifications",
          ((ACTIVE, "digest") in by) == bool(unread), f"{len(unread)} unread")
    check("Kemi and Ngozi: a streak email (nothing done today)",
          (NEW, "streak_at_risk") in by and (DIAGNOSTIC, "streak_at_risk") in by)
    check("all three: a weekly summary", all((e, "weekly_summary") in by for e in who))
    check("Kemi and Ngozi get no digest (no unread recommendation notifications)",
          (NEW, "digest") not in by and (DIAGNOSTIC, "digest") not in by)
    check("every email is a dry run", sent and all(r["status"] == "dry_run" for r in sent), f"{len(sent)} emails")

    log = db.table("email_log").select("student_id, kind, day, status").in_("student_id", list(who.values())).execute().data
    check("each email is in email_log", len(log) == len(sent), f"{len(log)} rows")
    day = emails.datetime.now(emails.LAGOS).date()
    files = sorted((emails.OUTBOX / day.isoformat()).glob("*.html"))
    mine = [f for f in files if any(f.name.startswith(sid[:8]) for sid in who.values())]
    check("each email is written to ml/outbox/", len(mine) == len(sent), f"{len(mine)} files")
    bodies = [f.read_text() for f in mine]
    check("every email has exactly one button into the app",
          all(b.count('style="display:inline-block') == 1 and settings.app_url in b for b in bodies))
    check("every email has an unsubscribe link", all("/email/unsubscribe?token=" in b for b in bodies))

    print("\n-- No duplicates")
    again = emails.run_once(db, force=True, students=set(who), settings=settings)
    check("a second forced run sends nothing", again == [], f"{len(again)} emails")
    scheduled = emails.run_once(db, students=set(who), settings=settings)
    check("a scheduled check right after sends nothing", scheduled == [], f"{len(scheduled)} emails")
    dupes = len(log) - len({(r["student_id"], r["kind"], r["day"]) for r in log})
    check("no student has the same kind twice today", dupes == 0)

    print("\n-- Unsubscribe")
    good = httpx.get(f"{ML}/email/unsubscribe", params={"token": emails.sign_token(who[DIAGNOSTIC])}, timeout=30)
    off = db.table("profiles").select("email_reminders").eq("id", who[DIAGNOSTIC]).single().execute().data
    check("the link turns email reminders off without logging in",
          good.status_code == 200 and "Email reminders are off" in good.text and off["email_reminders"] is False)
    tampered = emails.sign_token(who[DIAGNOSTIC])[:-2] + "00"
    bad = httpx.get(f"{ML}/email/unsubscribe", params={"token": tampered}, timeout=30)
    check("a tampered token is refused", bad.status_code == 400)
    recipients = {r["email"] for r in db.rpc("email_recipients").execute().data}
    check("Ngozi is no longer a recipient", DIAGNOSTIC not in recipients and ACTIVE in recipients)
    db.table("profiles").update({"email_reminders": True}).eq("id", who[DIAGNOSTIC]).execute()

    print("\n-- Access")
    kemi = sign_in(NEW)
    own = kemi.table("email_log").select("student_id").execute().data
    check("a student reads only their own email log", own and all(r["student_id"] == who[NEW] for r in own), f"{len(own)} rows")
    try:
        kemi.table("email_log").insert({"student_id": who[NEW], "kind": "digest", "day": day.isoformat(),
                                        "subject": "x", "status": "sent"}).execute()
        check("a student cannot write the email log", False)
    except Exception as e:
        check("a student cannot write the email log", True, str(e)[:60])
    try:
        kemi.rpc("email_recipients").execute()
        check("a student cannot list email addresses", False)
    except Exception:
        check("a student cannot list email addresses", True)

    if args.shots:
        print("\n-- Screenshots")
        with sync_playwright() as p:
            browser = p.chromium.launch(channel="chrome", headless=True)
            page = browser.new_page(viewport={"width": 640, "height": 900})
            for student, kind in ((NEW, "streak_at_risk"), (ACTIVE, "digest"), (ACTIVE, "weekly_summary")):
                path = emails.OUTBOX / day.isoformat() / f"{who[student][:8]}-{kind}.html"
                if path.exists():
                    page.goto(path.as_uri())
                    page.screenshot(path=str(args.shots / f"dry-run-{kind.replace('_', '-')}.png"), full_page=True)
            page.close()
            page = browser.new_page(viewport={"width": 1280, "height": 900})
            page.goto(f"{APP}/login")
            page.get_by_label("Email").fill(ACTIVE)
            page.get_by_label("Password").fill(DEMO_PASSWORD)
            page.get_by_role("button", name="Sign in").click()
            page.wait_for_url(f"{APP}/")
            page.goto(f"{APP}/profile")
            settings_box = page.get_by_test_id("email-settings")
            expect(settings_box.get_by_role("checkbox").first).to_be_visible(timeout=20_000)
            check("Profile shows 'Email me reminders' and a tick box per kind",
                  settings_box.get_by_role("checkbox").count() == 3, settings_box.inner_text().split("\n")[0])
            page.add_style_tag(content="header { position: static !important; }")
            settings_box.locator("xpath=ancestor::div[contains(@class,'rounded-2xl')][1]").screenshot(
                path=str(args.shots / "profile-email-settings.png"))
            browser.close()

    print(f"\n{sum(results)}/{len(results)} checks passed")
    return 0 if all(results) else 1


if __name__ == "__main__":
    sys.exit(main())
