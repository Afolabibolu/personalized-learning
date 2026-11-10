"""Sets a user's role (student or course_manager). Roles change only here or in SQL, never from the app.

    python scripts/set_role.py someone@example.com course_manager
    python scripts/set_role.py --env ml/.env:TEST_EMAIL_TO course_manager   # the address in an .env file, never printed
    python scripts/set_role.py --list                                       # who is a course manager

The user must already have signed up in the app.
"""

import argparse
import sys
from pathlib import Path

from dotenv import dotenv_values

import testkit

ROOT = Path(__file__).resolve().parent.parent


def find_user(db, email: str):
    page = 1
    while True:
        users = db.auth.admin.list_users(page=page, per_page=1000)
        for u in users:
            if (u.email or "").lower() == email.lower():
                return u
        if len(users) < 1000:
            return None
        page += 1


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("email", nargs="?")
    parser.add_argument("role", nargs="?", choices=["student", "course_manager"])
    parser.add_argument("--env", help="FILE:KEY, take the email from an .env file without printing it")
    parser.add_argument("--list", action="store_true")
    args = parser.parse_args()
    db = testkit.admin()

    if args.list:
        for p in db.table("profiles").select("full_name").eq("role", "course_manager").execute().data:
            print(f"  course_manager: {p['full_name']}")
        return 0

    if args.env:
        file, key = args.env.split(":", 1)
        email, role, shown = (dotenv_values(ROOT / file).get(key) or "").strip(), args.email, f"{key} from {file}"
    else:
        email, role, shown = (args.email or "").strip(), args.role, args.email
    if not email or role not in ("student", "course_manager"):
        parser.error("give an email (or --env FILE:KEY) and a role: student or course_manager")

    user = find_user(db, email)
    if user is None:
        print(f"No account for {shown}. Sign up in the app first, then run this again.")
        return 1
    db.table("profiles").update({"role": role}).eq("id", user.id).execute()
    name = db.table("profiles").select("full_name").eq("id", user.id).single().execute().data["full_name"]
    print(f"{name} ({shown}) is now {role}.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
