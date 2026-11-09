"""Email reminders (Prompt 6), sent through an SMTP relay (Brevo) to students who opted in.

Three kinds, each at most once a day per student (email_log enforces it):

    streak_at_risk  on the student's study days, at or after their preferred study time
                    (Africa/Lagos), if they have done no quiz or study session today
    digest          from 19:00, one email combining today's unread "weak topic" and
                    "new recommendations" notifications (none sent if there are none)
    weekly_summary  Sunday from 18:00: minutes this week against last week, topics
                    improved, and the next topic to focus on

Every email has one button into the app (APP_URL + path) and an unsubscribe link with a
signed token that turns email reminders off without logging in. With EMAIL_DRY_RUN=true
(the default whenever the SMTP settings are missing) emails are logged and written to
ml/outbox/ instead of being sent.

    python -m app.emails --once                 # one scheduled check, as the service does every 15 minutes
    python -m app.emails --once --force         # build every email whose content applies now, ignoring the clock
    python -m app.emails --once --force --send --to-test --student active.student@demo.example.com
                                                # really send, but to TEST_EMAIL_TO only

SMTP settings live only in ml/.env: SMTP_HOST, SMTP_PORT (587 = STARTTLS, 465 = SSL), SMTP_USER and
SMTP_PASSWORD (the relay login, e.g. Brevo's, which is not an email address), SMTP_FROM (the sender
students see), TEST_EMAIL_TO (the only address test sends go to), APP_URL and EMAIL_DRY_RUN.
"""

import argparse
import base64
import hashlib
import hmac
import html
import os
import smtplib
import ssl
import time
from dataclasses import dataclass
from datetime import datetime, time as dtime, timedelta
from email.message import EmailMessage
from pathlib import Path
from zoneinfo import ZoneInfo

from dotenv import load_dotenv

from app.config import ATTENTION_PROBABILITY, ML_DIR

load_dotenv(ML_DIR / ".env")

LAGOS = ZoneInfo("Africa/Lagos")
KINDS = ("streak_at_risk", "digest", "weekly_summary")
DIGEST_FROM = dtime(19, 0)
WEEKLY_DAY, WEEKLY_FROM = 6, dtime(18, 0)  # Sunday (Monday is 0)
DIGEST_NOTIFICATION_KINDS = ("weak_topic_unstudied", "new_recommendations")
CHECK_EVERY_SECONDS = 15 * 60
OUTBOX = ML_DIR / "outbox"
# Addresses on reserved test domains (the demo and simulated students) never get a real email.
TEST_DOMAINS = ("example.com", "example.org", "example.net")
MONTHS = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]


@dataclass
class Settings:
    host: str | None
    port: int
    user: str | None
    password: str | None
    app_url: str
    api_url: str
    dry_run: bool
    sender: str | None = None   # SMTP_FROM, the From address (the login may not be an address)
    test_to: str | None = None  # TEST_EMAIL_TO, the only recipient of test sends

    @classmethod
    def from_env(cls) -> "Settings":
        user, password, sender = os.getenv("SMTP_USER"), os.getenv("SMTP_PASSWORD"), os.getenv("SMTP_FROM")
        dry = os.getenv("EMAIL_DRY_RUN", "true").strip().lower() != "false" or not (user and password and sender)
        return cls(os.getenv("SMTP_HOST", "smtp-relay.brevo.com"), int(os.getenv("SMTP_PORT", "587")), user, password,
                   os.getenv("APP_URL", "http://localhost:5173").rstrip("/"),
                   os.getenv("EMAIL_API_URL", "http://localhost:8000").rstrip("/"), dry,
                   sender, os.getenv("TEST_EMAIL_TO"))


@dataclass
class Email:
    kind: str
    to: str
    subject: str
    text: str
    html: str
    unsubscribe: str


# --- unsubscribe tokens -------------------------------------------------------------------

def _secret() -> bytes:
    """EMAIL_TOKEN_SECRET if set; otherwise derived from the service key, which never leaves ml/.env."""
    explicit = os.getenv("EMAIL_TOKEN_SECRET")
    if explicit:
        return explicit.encode()
    return hashlib.sha256(("unsubscribe:" + os.environ["SUPABASE_SERVICE_ROLE_KEY"]).encode()).digest()


def sign_token(student_id: str) -> str:
    body = base64.urlsafe_b64encode(student_id.encode()).decode().rstrip("=")
    mac = hmac.new(_secret(), body.encode(), hashlib.sha256).hexdigest()[:32]
    return f"{body}.{mac}"


def verify_token(token: str) -> str | None:
    """The student id in a valid token, or None."""
    try:
        body, mac = token.split(".", 1)
    except ValueError:
        return None
    expected = hmac.new(_secret(), body.encode(), hashlib.sha256).hexdigest()[:32]
    if not hmac.compare_digest(mac, expected):
        return None
    return base64.urlsafe_b64decode(body + "=" * (-len(body) % 4)).decode()


# --- when each email is due (pure, tested in tests/test_emails.py) ------------------------

def weekday_key(now: datetime) -> str:
    return ["mon", "tue", "wed", "thu", "fri", "sat", "sun"][now.weekday()]


def streak_due(now: datetime, study_days: list[str], preferred: dtime, active_today: bool) -> bool:
    return weekday_key(now) in study_days and now.time() >= preferred and not active_today


def digest_due(now: datetime, unread_today: int) -> bool:
    return now.time() >= DIGEST_FROM and unread_today > 0


def weekly_due(now: datetime) -> bool:
    return now.weekday() == WEEKLY_DAY and now.time() >= WEEKLY_FROM


def format_day(d) -> str:
    return f"{d.day} {MONTHS[d.month - 1]} {d.year}"


# --- the emails -----------------------------------------------------------------------------

def render(kind: str, to: str, subject: str, greeting: str, lines: list[str], button: tuple[str, str],
           settings: Settings, student_id: str) -> Email:
    """A short plain email: a greeting, a few lines, one button, and the unsubscribe link."""
    label, path = button
    link = settings.app_url + path
    unsubscribe = f"{settings.api_url}/email/unsubscribe?token={sign_token(student_id)}"
    footer = "You get these emails because you turned on email reminders in Learning Support."
    text = "\n\n".join([greeting, *lines, f"{label}: {link}", f"{footer}\nTurn them off: {unsubscribe}"]) + "\n"
    paragraphs = "".join(f'<p style="margin:0 0 12px">{html.escape(line)}</p>' for line in lines)
    body = f"""<!doctype html>
<html><body style="margin:0;background:#f8fafc;font-family:Inter,Segoe UI,Arial,sans-serif;color:#0f172a">
<div style="max-width:520px;margin:0 auto;padding:24px 16px">
<div style="background:#ffffff;border:1px solid #e2e8f0;border-radius:16px;padding:24px">
<p style="margin:0 0 16px;font-weight:700;color:#4f46e5">Learning Support</p>
<p style="margin:0 0 12px">{html.escape(greeting)}</p>
{paragraphs}
<p style="margin:20px 0 4px"><a href="{html.escape(link)}" style="display:inline-block;background:#4f46e5;color:#ffffff;text-decoration:none;font-weight:600;padding:10px 18px;border-radius:10px">{html.escape(label)}</a></p>
</div>
<p style="margin:16px 4px 0;font-size:12px;color:#64748b">{html.escape(footer)} <a href="{html.escape(unsubscribe)}" style="color:#64748b">Turn off email reminders</a></p>
</div></body></html>
"""
    return Email(kind, to, subject, text, body, unsubscribe)


def streak_email(r: dict, card: dict, settings: Settings) -> Email:
    first = (r.get("full_name") or "there").split()[0]
    streak, at = card["streak"], r["preferred_study_time"][:5]
    if streak > 0:
        subject = f"Keep your {streak}-day streak going"
        lines = [f"You planned to study at {at} today and nothing is logged yet.",
                 f"One quiz or a short study session keeps your {streak}-day streak alive."]
    else:
        subject = "A few minutes today starts a streak"
        lines = [f"You planned to study at {at} today.", "One quiz or a short study session starts a new streak."]
    return render("streak_at_risk", r["email"], subject, f"Hi {first},", lines, ("Log a study session", "/log"),
                  settings, r["student_id"])


def digest_email(r: dict, notifications: list[dict], today, settings: Settings) -> Email:
    first = (r.get("full_name") or "there").split()[0]
    lines = ["Here is what changed in your recommendations today:"]
    lines += [f"• {n['title']}: {n['body']}" for n in notifications[:5]]
    if len(notifications) > 5:
        lines.append(f"…and {len(notifications) - 5} more in the app.")
    return render("digest", r["email"], f"Your study update for {format_day(today)}", f"Hi {first},", lines,
                  ("See your recommendations", "/"), settings, r["student_id"])


def weekly_email(r: dict, summary: dict, settings: Settings) -> Email:
    first = (r.get("full_name") or "there").split()[0]
    this, last = summary["minutes_this_week"], summary["minutes_last_week"]
    change = ("up from" if this > last else "down from" if this < last else "the same as") + f" {last} last week"
    lines = [f"You studied {this} minutes this week, {change}."]
    if summary["improved"]:
        lines.append("Topics improved: " + "; ".join(f"{t['title']} ({t['from']}% to {t['to']}%)" for t in summary["improved"][:3]) + ".")
    else:
        lines.append("No topic scores went up this week. A topic quiz is a quick way to see progress.")
    if summary["next_topic"]:
        lines.append(f"Focus next: {summary['next_topic']}.")
    return render("weekly_summary", r["email"], f"Your week: {this} minutes studied", f"Hi {first},", lines,
                  ("Open your dashboard", "/"), settings, r["student_id"])


# --- data -----------------------------------------------------------------------------------

def unread_digest_notifications(db, student_id: str, now: datetime) -> list[dict]:
    start = now.replace(hour=0, minute=0, second=0, microsecond=0)
    return (db.table("notifications").select("kind, title, body, created_at").eq("student_id", student_id)
            .in_("kind", list(DIGEST_NOTIFICATION_KINDS)).is_("read_at", "null")
            .gte("created_at", start.isoformat())  # no upper bound: the database clock may run a little ahead
            .order("created_at").execute().data)


def weekly_summary(db, student_id: str, now: datetime) -> dict:
    """Minutes over the last 7 days against the 7 before (as the app's weekly card), topics whose latest
    attempt in the last 7 days beat the previous one, and the top pending recommendation's topic."""
    week, fortnight = now - timedelta(days=7), now - timedelta(days=14)
    logs = (db.table("study_logs").select("duration_minutes, logged_at").eq("student_id", student_id)
            .gte("logged_at", fortnight.isoformat()).lte("logged_at", now.isoformat()).execute().data)
    this = sum(l["duration_minutes"] for l in logs if datetime.fromisoformat(l["logged_at"]) >= week)
    last = sum(l["duration_minutes"] for l in logs) - this
    progress = db.rpc("topic_progress_for", {"p_student": student_id}).execute().data
    gains = [p for p in progress if p["previous_score"] is not None and float(p["latest_score"]) > float(p["previous_score"])
             and datetime.fromisoformat(p["latest_completed_at"]) >= week]
    titles = {}
    if gains:
        titles = {t["id"]: t["title"] for t in db.table("topics").select("id, title")
                  .in_("id", [g["topic_id"] for g in gains]).execute().data}
    gains.sort(key=lambda p: float(p["latest_score"]) - float(p["previous_score"]), reverse=True)
    improved = [{"title": titles.get(g["topic_id"], "A topic"), "from": round(float(g["previous_score"])),
                 "to": round(float(g["latest_score"]))} for g in gains]
    recs = (db.table("recommendations").select("rank, source, priority_score, topic:topics(title, course:courses(code))")
            .eq("student_id", student_id).eq("status", "pending").execute().data)

    def order(r):  # needs attention, then the diagnostic list, then getting started, then keep it up
        if r["source"] == "ml":
            return (0 if (r["priority_score"] or 0) >= ATTENTION_PROBABILITY else 3, r["rank"])
        return (1 if r["source"] == "diagnostic" else 2, r["rank"])

    top = min(recs, key=order) if recs else None
    next_topic = f"{top['topic']['title']} ({top['topic']['course']['code']})" if top else None
    return {"minutes_this_week": this, "minutes_last_week": last, "improved": improved, "next_topic": next_topic}


def already_sent(db, student_id: str, kind: str, day) -> bool:
    return bool(db.table("email_log").select("id").eq("student_id", student_id).eq("kind", kind)
                .eq("day", day.isoformat()).neq("status", "failed").eq("to_self", False).limit(1).execute().data)


# --- sending ----------------------------------------------------------------------------------

def mime(email: Email, settings: Settings) -> EmailMessage:
    msg = EmailMessage()
    msg["Subject"], msg["To"] = email.subject, email.to
    sender = settings.sender or "reminders@localhost"
    msg["From"] = sender if "<" in sender else f"Learning Support <{sender}>"
    msg["List-Unsubscribe"] = f"<{email.unsubscribe}>"
    msg.set_content(email.text)
    msg.add_alternative(email.html, subtype="html")
    return msg


def smtp_send(msg: EmailMessage, settings: Settings) -> None:
    """Port 465: SSL from the start. Any other port (587 for Brevo): plain, then STARTTLS."""
    context = ssl.create_default_context()
    if settings.port == 465:
        with smtplib.SMTP_SSL(settings.host, settings.port, context=context, timeout=30) as s:
            s.login(settings.user, settings.password)
            s.send_message(msg)
    else:
        with smtplib.SMTP(settings.host, settings.port, timeout=30) as s:
            s.ehlo()
            s.starttls(context=context)
            s.ehlo()
            s.login(settings.user, settings.password)
            s.send_message(msg)


def write_outbox(email: Email, student_id: str, day) -> Path:
    folder = OUTBOX / day.isoformat()
    folder.mkdir(parents=True, exist_ok=True)
    path = folder / f"{student_id[:8]}-{email.kind}.html"
    path.write_text(email.html)
    path.with_suffix(".txt").write_text(f"To: {email.to}\nSubject: {email.subject}\n\n{email.text}")
    return path


def deliver(db, email: Email, student_id: str, day, settings: Settings, to_self: bool) -> str:
    """Sends (retrying once) or, in dry run, writes to the outbox; logs the result. Returns the status."""
    status, error = "dry_run", None
    if to_self:
        if not settings.test_to:
            raise RuntimeError("TEST_EMAIL_TO is not set in ml/.env")
        email.to = settings.test_to
    if settings.dry_run:
        write_outbox(email, student_id, day)
    elif not to_self and email.to.lower().endswith(TEST_DOMAINS):  # students' reserved addresses only
        status, error = "failed", "not sent: reserved test address (use --to-test)"
    else:
        for attempt in (1, 2):
            try:
                smtp_send(mime(email, settings), settings)
                status, error = "sent", None
                break
            except Exception as e:  # network or SMTP error: retry once, then log it
                status, error = "failed", f"{e.__class__.__name__}: {e}"[:500]
                if attempt == 1:
                    time.sleep(5)
    db.table("email_log").insert({"student_id": student_id, "kind": email.kind, "day": day.isoformat(),
                                  "subject": email.subject, "status": status, "error": error,
                                  "to_self": to_self}).execute()
    return status


def run_once(db, now: datetime | None = None, force: bool = False, to_self: bool = False,
             students: set[str] | None = None, settings: Settings | None = None,
             kinds: set[str] | None = None) -> list[dict]:
    """One check: every email that is due for every opted-in student, unless already sent today.
    force ignores the clock (study time, 19:00, Sunday) but not the content rules or the daily limit."""
    settings = settings or Settings.from_env()
    now = (now or datetime.now(LAGOS)).astimezone(LAGOS)
    today = now.date()
    results = []
    for r in db.rpc("email_recipients").execute().data:
        if students and r["email"] not in students and r["student_id"] not in students:
            continue
        sid = r["student_id"]
        if not settings.dry_run and not to_self and r["email"].lower().endswith(TEST_DOMAINS):
            continue  # demo and simulated students: never a real email, and no failed row every 15 minutes
        candidates: list[Email] = []
        if r["email_streak"] and (to_self or not already_sent(db, sid, "streak_at_risk", today)):
            card = db.rpc("gamification_for", {"p_student": sid, "p_now": now.isoformat()}).execute().data
            preferred = dtime.fromisoformat(r["preferred_study_time"])
            if (force and not card["today_active"]) or streak_due(now, r["study_days"], preferred, card["today_active"]):
                candidates.append(streak_email(r, card, settings))
        if r["email_digest"] and (to_self or not already_sent(db, sid, "digest", today)):
            notes = unread_digest_notifications(db, sid, now)
            if notes and (force or digest_due(now, len(notes))):
                candidates.append(digest_email(r, notes, today, settings))
        if r["email_weekly"] and (to_self or not already_sent(db, sid, "weekly_summary", today)):
            if force or weekly_due(now):
                candidates.append(weekly_email(r, weekly_summary(db, sid, now), settings))
        for email in (e for e in candidates if not kinds or e.kind in kinds):
            try:
                status = deliver(db, email, sid, today, settings, to_self)
            except Exception as e:  # the unique index: another check got there first
                status = f"skipped ({e.__class__.__name__})"
            results.append({"student": r["email"], "kind": email.kind, "subject": email.subject, "status": status})
    return results


def main() -> int:
    from app.data import service_client

    parser = argparse.ArgumentParser()
    parser.add_argument("--once", action="store_true", help="run one check and exit")
    parser.add_argument("--force", action="store_true", help="ignore the clock (content rules and the daily limit still apply)")
    parser.add_argument("--now", help="ISO time to check at, for tests (default: now)")
    parser.add_argument("--student", action="append", help="only this student (email or id); repeatable")
    parser.add_argument("--kind", action="append", choices=KINDS, help="only this kind; repeatable")
    parser.add_argument("--send", action="store_true", help="really send even if EMAIL_DRY_RUN is true")
    parser.add_argument("--to-test", "--to-self", dest="to_test", action="store_true",
                        help="send to TEST_EMAIL_TO instead of the student")
    args = parser.parse_args()
    settings = Settings.from_env()
    if args.send:
        if not (settings.user and settings.password and settings.sender and settings.test_to):
            raise SystemExit("SMTP_USER, SMTP_PASSWORD, SMTP_FROM and TEST_EMAIL_TO must be set in ml/.env to send.")
        if not args.to_test:
            raise SystemExit("--send is only for tests here: use it with --to-test.")
        settings.dry_run = False
    now = datetime.fromisoformat(args.now) if args.now else None
    results = run_once(service_client(), now, args.force, args.to_test, set(args.student or []) or None, settings,
                       set(args.kind or []) or None)
    mode = "dry run (outbox: ml/outbox/)" if settings.dry_run else "sending"
    print(f"{len(results)} email(s), {mode}")
    for r in results:
        print(f"  {r['status']:8} {r['kind']:15} {r['student']:40} {r['subject']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
