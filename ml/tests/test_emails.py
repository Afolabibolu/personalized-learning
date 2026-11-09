"""Email reminders: when each email is due (Lagos time), the unsubscribe token, and the email content."""

from datetime import datetime, time
from zoneinfo import ZoneInfo

import pytest

from app import emails

LAGOS = ZoneInfo("Africa/Lagos")
WEEKDAYS = ["mon", "tue", "wed", "thu", "fri"]


@pytest.fixture(autouse=True)
def secret(monkeypatch):
    monkeypatch.setenv("EMAIL_TOKEN_SECRET", "test-secret")


def at(day: int, hour: int, minute: int = 0) -> datetime:
    """November 2026: the 2nd is a Monday, the 8th a Sunday."""
    return datetime(2026, 11, day, hour, minute, tzinfo=LAGOS)


SETTINGS = emails.Settings("smtp.gmail.com", 465, "me@gmail.com", "x", "http://localhost:5173", "http://localhost:8000", True)
STUDENT = {"student_id": "11111111-2222-3333-4444-555555555555", "email": "tolu@example.com", "full_name": "Tolu Adeyemi",
           "preferred_study_time": "18:00:00"}


# -- when each email is due ----------------------------------------------------------------

def test_streak_due_on_a_study_day_from_the_preferred_time_if_nothing_done():
    assert emails.streak_due(at(4, 18, 0), WEEKDAYS, time(18), active_today=False)  # Wednesday 18:00
    assert not emails.streak_due(at(4, 17, 59), WEEKDAYS, time(18), active_today=False)
    assert not emails.streak_due(at(4, 19, 0), WEEKDAYS, time(18), active_today=True)
    assert not emails.streak_due(at(7, 19, 0), WEEKDAYS, time(18), active_today=False)  # Saturday, not a study day


def test_streak_uses_lagos_time_not_utc():
    utc_evening = datetime(2026, 11, 4, 17, 30, tzinfo=ZoneInfo("UTC"))  # 18:30 in Lagos
    assert emails.streak_due(utc_evening.astimezone(LAGOS), WEEKDAYS, time(18), active_today=False)


def test_digest_from_19_00_only_with_unread_notifications():
    assert emails.digest_due(at(4, 19, 0), 2)
    assert not emails.digest_due(at(4, 18, 59), 2)
    assert not emails.digest_due(at(4, 21, 0), 0)


def test_weekly_summary_on_sunday_evening_only():
    assert emails.weekly_due(at(8, 18, 0))
    assert not emails.weekly_due(at(8, 17, 45))
    assert not emails.weekly_due(at(7, 20, 0))


# -- unsubscribe tokens --------------------------------------------------------------------

def test_token_round_trip_and_tampering():
    token = emails.sign_token(STUDENT["student_id"])
    assert emails.verify_token(token) == STUDENT["student_id"]
    body, mac = token.split(".")
    other = emails.sign_token("99999999-2222-3333-4444-555555555555").split(".")[0]
    assert emails.verify_token(f"{other}.{mac}") is None
    assert emails.verify_token(token[:-1] + ("0" if token[-1] != "0" else "1")) is None
    assert emails.verify_token("not-a-token") is None


# -- content -------------------------------------------------------------------------------

def test_streak_email_names_the_streak_and_links_to_the_logger():
    e = emails.streak_email(STUDENT, {"streak": 7}, SETTINGS)
    assert e.subject == "Keep your 7-day streak going"
    assert "http://localhost:5173/log" in e.html and "18:00" in e.text
    assert e.html.count('style="display:inline-block') == 1  # one button
    assert e.unsubscribe.startswith("http://localhost:8000/email/unsubscribe?token=") and e.unsubscribe in e.html


def test_streak_email_with_no_streak_yet():
    assert emails.streak_email(STUDENT, {"streak": 0}, SETTINGS).subject == "A few minutes today starts a streak"


def test_digest_combines_notifications_into_one_email():
    notes = [{"title": f"Note {i}", "body": f"Body {i}"} for i in range(7)]
    e = emails.digest_email(STUDENT, notes, at(4, 19).date(), SETTINGS)
    assert e.subject == "Your study update for 4 Nov 2026"
    assert "Note 0: Body 0" in e.text and "Note 4: Body 4" in e.text and "Note 5" not in e.text
    assert "and 2 more in the app" in e.text


def test_weekly_summary_content():
    e = emails.weekly_email(STUDENT, {"minutes_this_week": 120, "minutes_last_week": 90,
                                      "improved": [{"title": "Fuzzy Logic", "from": 40, "to": 80}],
                                      "next_topic": "Cognitive Psychology (CSC 531)"}, SETTINGS)
    assert e.subject == "Your week: 120 minutes studied"
    assert "120 minutes this week, up from 90 last week" in e.text
    assert "Fuzzy Logic (40% to 80%)" in e.text and "Focus next: Cognitive Psychology (CSC 531)." in e.text


def test_names_are_escaped_in_html():
    e = emails.streak_email(STUDENT | {"full_name": "<b>Tolu</b>"}, {"streak": 1}, SETTINGS)
    assert "<b>Tolu</b>" not in e.html and "&lt;b&gt;Tolu&lt;/b&gt;" in e.html


def test_dry_run_is_the_default_without_smtp_settings(monkeypatch):
    monkeypatch.delenv("SMTP_USER", raising=False)
    monkeypatch.setenv("EMAIL_DRY_RUN", "false")
    assert emails.Settings.from_env().dry_run is True


# -- SMTP relay (Brevo: port 587, STARTTLS, a login that is not an address) ----------------

class FakeSMTP:
    instances: list["FakeSMTP"] = []

    def __init__(self, host, port, **kwargs):
        self.host, self.port, self.calls = host, port, []
        FakeSMTP.instances.append(self)

    def __enter__(self):
        return self

    def __exit__(self, *exc):
        return False

    def ehlo(self):
        self.calls.append("ehlo")

    def starttls(self, context=None):
        self.calls.append("starttls")

    def login(self, user, password):
        self.calls.append(("login", user))

    def send_message(self, msg):
        self.calls.append(("send", msg["From"], msg["To"]))


def brevo(**changes) -> emails.Settings:
    s = emails.Settings("smtp-relay.brevo.com", 587, "9a1b2c@smtp-brevo.com", "key", "http://localhost:5173",
                        "http://localhost:8000", False, "Learning Support <reminders@example.org>", "me@example.org")
    for k, v in changes.items():
        setattr(s, k, v)
    return s


def test_port_587_uses_starttls_and_sends_from_smtp_from(monkeypatch):
    FakeSMTP.instances = []
    monkeypatch.setattr(emails.smtplib, "SMTP", FakeSMTP)
    e = emails.streak_email(STUDENT, {"streak": 3}, brevo())
    emails.smtp_send(emails.mime(e, brevo()), brevo())
    calls = FakeSMTP.instances[0].calls
    assert calls.index("starttls") < calls.index(("login", "9a1b2c@smtp-brevo.com"))
    assert calls[-1] == ("send", "Learning Support <reminders@example.org>", "tolu@example.com")


def test_port_465_uses_ssl(monkeypatch):
    FakeSMTP.instances = []
    monkeypatch.setattr(emails.smtplib, "SMTP_SSL", FakeSMTP)
    e = emails.streak_email(STUDENT, {"streak": 3}, brevo(port=465))
    emails.smtp_send(emails.mime(e, brevo(port=465)), brevo(port=465))
    assert FakeSMTP.instances[0].port == 465 and "starttls" not in FakeSMTP.instances[0].calls


def test_a_bare_smtp_from_gets_the_app_name():
    e = emails.streak_email(STUDENT, {"streak": 3}, brevo())
    assert emails.mime(e, brevo(sender="reminders@example.org"))["From"] == "Learning Support <reminders@example.org>"


def test_dry_run_without_smtp_from(monkeypatch):
    monkeypatch.setenv("SMTP_USER", "9a1b2c@smtp-brevo.com")
    monkeypatch.setenv("SMTP_PASSWORD", "key")
    monkeypatch.delenv("SMTP_FROM", raising=False)
    monkeypatch.setenv("EMAIL_DRY_RUN", "false")
    assert emails.Settings.from_env().dry_run is True
    monkeypatch.setenv("SMTP_FROM", "reminders@example.org")
    assert emails.Settings.from_env().dry_run is False


class FakeTable:
    def __init__(self):
        self.rows = []

    def table(self, name):
        return self

    def insert(self, row):
        self.rows.append(row)
        return self

    def execute(self):
        return self


def test_test_sends_go_to_test_email_to_only(monkeypatch):
    sent = []
    monkeypatch.setattr(emails, "smtp_send", lambda msg, s: sent.append(msg["To"]))
    db = FakeTable()
    e = emails.streak_email(STUDENT, {"streak": 3}, brevo())
    assert emails.deliver(db, e, STUDENT["student_id"], at(4, 19).date(), brevo(), to_self=True) == "sent"
    assert sent == ["me@example.org"] and db.rows[0]["to_self"] is True


def test_test_sends_refuse_without_test_email_to():
    e = emails.streak_email(STUDENT, {"streak": 3}, brevo())
    with pytest.raises(RuntimeError, match="TEST_EMAIL_TO"):
        emails.deliver(FakeTable(), e, STUDENT["student_id"], at(4, 19).date(), brevo(test_to=None), to_self=True)
