"""Command-line entry for first-commit-ai."""

from __future__ import annotations

import argparse
import sys

from first_commit_ai.client import ChatClient


def build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(
        prog="first-commit-ai",
        description="Tiny OpenAI-compatible chat CLI. Use --mock to run without a key.",
    )
    p.add_argument("prompt", help="What you want to ask")
    p.add_argument(
        "--mock",
        action="store_true",
        help="Return a deterministic local reply (no network, no API key)",
    )
    return p


def main(argv: list[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    client = ChatClient.from_env(mock=args.mock)
    try:
        print(client.chat(args.prompt))
    except Exception as exc:  # noqa: BLE001 — teach failures clearly
        print(f"error: {exc}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
