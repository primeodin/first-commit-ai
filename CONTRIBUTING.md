# Contributing to first-commit-ai

Welcome. This repo is meant to be someone's **first public AI commit** — keep that bar in mind.

## Map (fork → PR)

1. **Fork** this repo on GitHub, then clone your fork:
   ```bash
   git clone https://github.com/<you>/first-commit-ai.git
   cd first-commit-ai
   ```
2. **Install** in editable mode with test deps:
   ```bash
   pip install -e ".[dev]"
   ```
3. **Prove the wiring** before you change anything:
   ```bash
   pytest
   python -m first_commit_ai --mock "hi"
   ```
   You want `7 passed` and a `[mock]` reply line. No API key needed.
4. **Branch** for one small change:
   ```bash
   git checkout -b my-first-pr
   ```
5. **Ship** a focused PR back to `primeodin/first-commit-ai`:
   - one idea per PR
   - include or update a test when behavior changes
   - say what you ran (`pytest`, the mock command)

## Good first issues

Scoped tickets (file named in the issue body):

- [#5 — `--json` CLI output for reply + mode](https://github.com/primeodin/first-commit-ai/issues/5)
- [#6 — Ollama / local server walkthrough under `docs/`](https://github.com/primeodin/first-commit-ai/issues/6)

Claim one with a comment, ask questions in the thread, then open the PR. Docs count.

## Shop rules

- **Keep it small.** No framework pile-ons, no extra services "while we're here."
- **Mock stays sacred.** Offline tests and `--mock` must keep working without secrets.
- **Teach by running.** If a change needs a paragraph of theory, prefer a runnable example or a test instead.
- **Match the voice.** Short, concrete, honest — shop notes, not pitch decks.

## What to skip

Please don't open PRs that:

- add a heavy agent/framework stack
- require paid APIs in the default path
- rewrite the README for marketing tone
- bundle unrelated refactors with a feature

Questions? Comment on the issue you're claiming — that thread is the right place.
