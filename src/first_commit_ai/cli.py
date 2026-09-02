"""Command-line entry for first-commit-ai."""

from __future__ import annotations

import argparse
import sys

from first_commit_ai.client import ChatClient

CUSTOM_EPILOG = """
Quick Start Flow:
  1. clone   -> git clone https://github.com/primeodin/first-commit-ai.git
  2. install -> pip install -e ".[dev]"
  3. mock    -> python -m first_commit_ai --mock "hi"
  4. real    -> export OPENAI_API_KEY=sk-... && python -m first_commit_ai "your prompt"
"""

NO_ARGS_TIP = """Tip: Run with --mock "your prompt" to test offline without an API key.
See README.md for full usage instructions."""


def build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(
        prog="first-commit-ai",
        description="Tiny OpenAI-compatible chat CLI.",
        epilog=CUSTOM_EPILOG,
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    p.add_argument(
        "prompt",
        nargs="?",
        default=None,
        help="What you want to ask",
    )
    p.add_argument(
        "--mock",
        action="store_true",
        help="Return a deterministic local reply (no network, no API key)",
    )
    return p


def main(argv: list[str] | None = None) -> int:
    args = build_parser().parse_args(argv)

    if not args.prompt:
        print(NO_ARGS_TIP)
        return 0

    client = ChatClient.from_env(mock=args.mock)
    try:
        print(client.chat(args.prompt))
    except Exception as exc:  # noqa: BLE001 — teach failures clearly
        print(f"error: {exc}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
