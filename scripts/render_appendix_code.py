"""Renders the code excerpts for the report appendix as syntax-highlighted PNGs.

    python scripts/render_appendix_code.py

Writes docs/appendix-code/<name>.png and docs/appendix-code/README.md. Each
excerpt is taken from the source files as they are now, with their real line
numbers; lines left out are shown as a "lines N–M not shown" bar, so an excerpt
never pretends to be the whole function. Rerun after changing any of the files.
"""

import html
import sys
from dataclasses import dataclass
from pathlib import Path

from playwright.sync_api import sync_playwright
from pygments import highlight
from pygments.formatters import HtmlFormatter
from pygments.lexers import PostgresLexer, PythonLexer

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "docs" / "appendix-code"
QUIZ = "supabase/migrations/20261018140400_quiz_functions.sql"
RLS = "supabase/migrations/20261018140200_rls_and_grants.sql"
MAX_LINES = 40


@dataclass
class Chunk:
    file: str
    start: int
    end: int


@dataclass
class Excerpt:
    name: str
    title: str
    description: str
    chunks: list[Chunk]
    skipped: dict[tuple[int, int], str]  # (first, last) line left out -> what those lines do


EXCERPTS = [
    Excerpt("01-start-quiz-picks-unseen-questions-first", "start_quiz: choosing the questions",
            "The security-definer SQL function that starts a quiz for the signed-in student and picks each topic's questions, unseen ones first and then the longest unseen, so answers never reach the browser.",
            [Chunk(QUIZ, 93, 99), Chunk(QUIZ, 105, 108), Chunk(QUIZ, 115, 143)],
            {(100, 104): "variable declarations", (109, 114): "loads the quiz, or stops if it does not exist"}),
    Excerpt("02-start-quiz-returns-questions-without-answers", "start_quiz: creating the attempt",
            "The second half of start_quiz: it stores the chosen question ids on a new attempt and returns the questions without their correct answers or explanations.",
            [Chunk(QUIZ, 145, 172)], {}),
    Excerpt("03-submit-quiz-grades-only-stored-questions", "submit_quiz: grading on the server",
            "The SQL function that grades only the questions stored on the student's own attempt, refuses a second submission, and writes the answers and score itself, so students can never write their own scores.",
            [Chunk(QUIZ, 179, 185), Chunk(QUIZ, 199, 231)],
            {(186, 198): "variable declarations, the sign-in check and the response-format check"}),
    Excerpt("04-recommender-cold-start-and-fallback", "Cold start and the fallback to it",
            "The cold-start rule (fewer than three completed quizzes on a course, or no trained model) and the introductory list it returns, including the fallback that keeps a student on that list if ML ranking ever fails.",
            [Chunk("ml/app/config.py", 7, 9), Chunk("ml/app/recommender.py", 84, 98), Chunk("ml/app/recommender.py", 162, 178)],
            {(99, 161): "model_probabilities and ml_recommendations (excerpt 05)"}),
    Excerpt("05-recommender-ranking-by-averaged-probability", "Ranking topics by averaged probability",
            "How topics are ranked by the average of the Logistic Regression and Random Forest probabilities, and how each top topic gets its resource (the student's preferred type first) or its topic quiz.",
            [Chunk("ml/app/recommender.py", 101, 106), Chunk("ml/app/recommender.py", 129, 159)],
            {(107, 128): "attention_probabilities, and the signature and docstring of ml_recommendations"}),
    Excerpt("06-explain-reason-and-explanation", "Building each recommendation's explanation",
            "The reason line shown on every card (last score, days since studied, minutes studied) and the explanation object the ML service stores with each recommendation.",
            [Chunk("ml/app/explain.py", 32, 43), Chunk("ml/app/explain.py", 89, 104)],
            {(44, 88): "keep_it_up_reason, and top_factors (excerpt 07)"}),
    Excerpt("07-explain-top-factors", "The top factors behind a prediction",
            "How the \"Why this?\" panel's top factors are computed: each feature's Logistic Regression coefficient times its standardised value, keeping the factors that push towards the verdict shown.",
            [Chunk("ml/app/explain.py", 57, 57), Chunk("ml/app/explain.py", 66, 86)],
            {(58, 65): "docstring"}),
    Excerpt("08-simulation-config-block", "The simulation's parameters",
            "The single config block at the top of the simulation, with the fixed random seed and every parameter of the forgetting curve, practice effect, noise and study habits used to generate the training data.",
            [Chunk("ml/training/synthetic.py", 31, 31), Chunk("ml/training/synthetic.py", 42, 80)],
            {(32, 41): "the Habit record (name, share of students, daily study chance, session length, cramming chance)"}),
    Excerpt("09-rls-study-logs-policies", "Row-level security on study logs",
            "Row-level security and grants on study_logs: a student can read and create only their own study sessions, and cannot log one with a future date.",
            [Chunk(RLS, 13, 13), Chunk(RLS, 53, 61)],
            {(14, 52): "row-level security and grants for the other tables"}),
]

CSS = """
body { margin: 0; background: #ffffff; font-family: -apple-system, 'Helvetica Neue', Arial, sans-serif; }
.frame { display: inline-block; margin: 0; border: 1px solid #d0d7de; border-radius: 10px; overflow: hidden; background: #ffffff; }
.head { padding: 10px 16px; background: #f6f8fa; border-bottom: 1px solid #d0d7de; }
.title { font-size: 15px; font-weight: 600; color: #1f2328; }
.path { margin-top: 2px; font: 12px Menlo, 'SF Mono', Consolas, monospace; color: #57606a; }
.file { padding: 6px 16px; font: 12px Menlo, 'SF Mono', Consolas, monospace; color: #57606a; background: #f6f8fa; border-top: 1px solid #eaeef2; border-bottom: 1px solid #eaeef2; }
.skip { padding: 4px 16px 4px 64px; font: italic 12px Menlo, 'SF Mono', Consolas, monospace; color: #6e7781; background: #f6f8fa; border-top: 1px dashed #d0d7de; border-bottom: 1px dashed #d0d7de; }
table.code { border-collapse: collapse; font: 13px/1.5 Menlo, 'SF Mono', Consolas, monospace; }
td.ln { width: 40px; padding: 0 12px 0 8px; text-align: right; color: #8c959f; user-select: none; vertical-align: top; }
td.src { padding: 0 24px 0 8px; white-space: pre; color: #1f2328; vertical-align: top; }
.pad td { height: 6px; }
td.src, td.src * { background: transparent !important; }
td.src .err { border: none !important; color: inherit; }
"""


def lexer_for(path: str):
    return PostgresLexer() if path.endswith(".sql") else PythonLexer()


def highlighted_lines(path: str) -> list[str]:
    """Every line of the file as highlighted HTML (highlighting the whole file keeps multi-line strings right)."""
    source = (ROOT / path).read_text()
    formatter = HtmlFormatter(nowrap=True, style="default")
    body = highlight(source, lexer_for(path), formatter)
    # Tokens can span lines (docstrings); close and reopen open spans at each newline.
    lines, open_spans, current = [], [], ""
    i = 0
    while i < len(body):
        if body.startswith("<span", i):
            j = body.index(">", i) + 1
            open_spans.append(body[i:j]); current += body[i:j]; i = j
        elif body.startswith("</span>", i):
            open_spans.pop(); current += "</span>"; i += 7
        elif body[i] == "\n":
            lines.append(current + "</span>" * len(open_spans)); current = "".join(open_spans); i += 1
        else:
            current += body[i]; i += 1
    lines.append(current)
    return lines


def render_html(ex: Excerpt) -> str:
    files = sorted({c.file for c in ex.chunks}, key=[c.file for c in ex.chunks].index)
    ranges = "; ".join(
        f"{f}, lines " + ", ".join(f"{c.start}–{c.end}" if c.start != c.end else f"{c.start}" for c in ex.chunks if c.file == f)
        for f in files)
    parts = [f'<div class="frame"><div class="head"><div class="title">{html.escape(ex.title)}</div>'
             f'<div class="path">{html.escape(ranges)}</div></div>']
    previous: Chunk | None = None
    cache: dict[str, list[str]] = {}
    for chunk in ex.chunks:
        lines = cache.setdefault(chunk.file, highlighted_lines(chunk.file))
        if len(files) > 1 and (previous is None or previous.file != chunk.file):
            parts.append(f'<div class="file">{html.escape(chunk.file)}</div>')
        elif previous is not None and chunk.start > previous.end + 1:
            gap = (previous.end + 1, chunk.start - 1)
            what = ex.skipped.get(gap, "")
            parts.append(f'<div class="skip">⋯ lines {gap[0]}–{gap[1]} not shown{": " + html.escape(what) if what else ""}</div>')
        rows = "".join(f'<tr><td class="ln">{n}</td><td class="src">{lines[n - 1] or " "}</td></tr>'
                       for n in range(chunk.start, chunk.end + 1))
        parts.append(f'<table class="code"><tr class="pad"><td></td><td></td></tr>{rows}<tr class="pad"><td></td><td></td></tr></table>')
        previous = chunk
    parts.append("</div>")
    style = HtmlFormatter(style="default").get_style_defs("td.src")
    return f"<!doctype html><html><head><meta charset='utf-8'><style>{style}{CSS}</style></head><body>{''.join(parts)}</body></html>"


def main() -> int:
    OUT.mkdir(parents=True, exist_ok=True)
    for old in OUT.glob("*.png"):
        old.unlink()
    with sync_playwright() as p:
        browser = p.chromium.launch(channel="chrome")
        page = browser.new_page(device_scale_factor=2, viewport={"width": 1400, "height": 800})
        for ex in EXCERPTS:
            shown = sum(c.end - c.start + 1 for c in ex.chunks)
            if shown > MAX_LINES:
                raise SystemExit(f"{ex.name}: {shown} lines, over {MAX_LINES}")
            page.set_content(render_html(ex))
            page.locator(".frame").screenshot(path=str(OUT / f"{ex.name}.png"))
            print(f"{ex.name}.png  ({shown} lines)")
        browser.close()
    rows = "\n".join(f"| [`{ex.name}.png`]({ex.name}.png) | {ex.description} |" for ex in EXCERPTS)
    (OUT / "README.md").write_text(
        "# Code excerpts for the report appendix\n\n"
        "Syntax-highlighted excerpts of the key code, each under 40 lines, with the file and real line numbers in the "
        "header. Lines left out are marked \"lines N–M not shown\". Regenerate with "
        "`python scripts/render_appendix_code.py` after changing any of these files.\n\n"
        "| File | What it shows |\n| --- | --- |\n"
        f"{rows}\n"
    )
    print(f"README.md, {len(EXCERPTS)} excerpts")
    return 0


if __name__ == "__main__":
    sys.exit(main())
