from __future__ import annotations

import argparse
import subprocess
import sys
from pathlib import Path

from .warden import inspect_delivery, render_markdown


def read_stdin() -> str:
    if sys.stdin.isatty():
        return ""
    return sys.stdin.read()


def read_git_diff() -> str:
    try:
        proc = subprocess.run(
            ["git", "diff", "--", "."],
            check=False,
            capture_output=True,
            text=True,
        )
    except FileNotFoundError:
        return ""
    return proc.stdout


def build_input(args: argparse.Namespace) -> str:
    chunks: list[str] = []

    if args.file:
        chunks.append(Path(args.file).read_text())

    stdin_text = read_stdin()
    if stdin_text:
        chunks.append(stdin_text)

    if args.git_diff:
        diff = read_git_diff()
        if diff:
            chunks.append("## Git diff\n\n" + diff)

    return "\n\n".join(chunks).strip()


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        prog="ai-delivery-warden",
        description="Inspect AI-generated delivery notes, handoffs, and diffs for real-delivery risks.",
    )
    parser.add_argument("file", nargs="?", help="Delivery or handoff markdown/text file to inspect.")
    parser.add_argument("--git-diff", action="store_true", help="Append current git diff to the inspection input.")
    parser.add_argument("--output", "-o", help="Write markdown report to this file.")
    parser.add_argument("--lang", choices=("en", "zh"), default="en", help="Report language. Defaults to en.")
    args = parser.parse_args(argv)

    text = build_input(args)
    if not text:
        parser.error("No input. Pass a file, pipe text, or use --git-diff in a git repo.")

    report = inspect_delivery(text)
    rendered = render_markdown(report, lang=args.lang)

    if args.output:
        Path(args.output).write_text(rendered)
    else:
        sys.stdout.write(rendered)

    return 1 if report.status == "BLOCK" else 0


if __name__ == "__main__":
    raise SystemExit(main())
