"""Last pipeline step for one course: links, validation, then loading.

    python content/ingest/publish.py --course "CSC 551"

Runs content/apply_links.py, then content/validate.py for the course, and
only if that reports 0 errors runs content/load.py for the course. Stops at
the first failure, so a course with errors never reaches Supabase.
"""

import argparse
import subprocess
import sys
from pathlib import Path

CONTENT = Path(__file__).resolve().parent.parent


def run(args: list[str]) -> subprocess.CompletedProcess:
    return subprocess.run([sys.executable, "-I", "-W", "ignore", *args], capture_output=True, text=True)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--course", required=True, help='course code, e.g. "CSC 551"')
    args = parser.parse_args()

    links = run([str(CONTENT / "apply_links.py")])
    if links.returncode:
        print(links.stdout + links.stderr)
        return 1
    validate = run([str(CONTENT / "validate.py"), "--course", args.course])
    print(validate.stdout.strip().splitlines()[-1] if validate.stdout.strip() else validate.stderr)
    if validate.returncode:
        print("\n".join(l for l in validate.stdout.splitlines() if l.startswith("ERROR")))
        print("Not loaded: fix the errors above and run again.")
        return 1
    load = run([str(CONTENT / "load.py"), "--course", args.course])
    print((load.stdout + load.stderr).strip())
    return load.returncode


if __name__ == "__main__":
    sys.exit(main())
