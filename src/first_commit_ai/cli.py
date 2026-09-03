"""Command-line entry for first-commit-ai."""

from __future__ import annotations

import argparse
import sys

from first_commit_ai.client import DEFAULT_SYSTEM, ChatClient


def build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(
        prog="first-commit-ai",
        description=(
            "Tiny OpenAI-compatible chat CLI for your first AI GitHub commit. "
            "Start with --mock (no API key). Point OPENAI_BASE_URL at Ollama when ready."
        ),
        epilog=(
            "Examples:\n"
            "  python -m first_commit_ai --mock \"hi\"\n"
            "  python -m first_commit_ai --mock --system \"Answer like a shop dad\" \"What is git?\"\n"
            "  OPENAI_API_KEY=sk-... python -m first_commit_ai \"Explain remotes\"\n"
        ),
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    p.add_argument("prompt", help="What you want to ask")
    p.add_argument(
        "--mock",
        action="store_true",
        help="Return a deterministic local reply (no network, no API key)",
    )
    p.add_argument(
        "--system",
        default=None,
        metavar="TEXT",
        help=f"Override the system prompt (default: {DEFAULT_SYSTEM!r})",
    )
    return p


def main(argv: list[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    client = ChatClient.from_env(mock=args.mock)
    if args.system is not None:
        client.system = args.system
    try:
        print(client.chat(args.prompt))
    except Exception as exc:  # noqa: BLE001 — teach failures clearly
        print(f"error: {exc}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
