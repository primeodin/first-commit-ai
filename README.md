# first-commit-ai

> Your first AI GitHub repo — tiny chat CLI with mock tests. Clone, run, understand.

Karpathy energy for regular people: **one idea**, runnable in a minute, tests that pass with no API key.

## 60-second start

```bash
git clone https://github.com/primeodin/first-commit-ai.git
cd first-commit-ai
pip install -e ".[dev]"
pytest
python -m first_commit_ai --mock "hi"
```

You should see a `[mock]` reply. That means the wiring works before you spend a token.

## Real chat (optional)

```bash
export OPENAI_API_KEY=sk-...
# optional local / compatible servers:
# export OPENAI_BASE_URL=http://localhost:11434/v1
# export OPENAI_MODEL=llama3.2
python -m first_commit_ai "Explain Git remotes like a shop dad."
```

## What you just built

| File | Job |
| --- | --- |
| `src/first_commit_ai/cli.py` | Args + exit codes |
| `src/first_commit_ai/client.py` | OpenAI-compatible HTTP + `--mock` |
| `tests/` | Proof it works offline |
| `.github/workflows/ci.yml` | Same checks on every push |

## Change one thing

1. Edit `DEFAULT_SYSTEM` in `client.py` — make the voice yours  
2. Point `OPENAI_BASE_URL` at Ollama or another compatible server  
3. Add a second command (e.g. `--system "..."`) and a test for it  

## Why this exists

Most “AI starter” repos bury you under frameworks. This one is small enough to read on a coffee break, then push as **your** first public AI commit.

Part of [PrimeOdin](https://github.com/primeodin)’s daily public builds for people learning AI by shipping.

## License

MIT
