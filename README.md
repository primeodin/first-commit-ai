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

**Expected stdout** (deterministic on `--mock` — yours should match):

```text
# pytest
.......                                                                  [100%]
7 passed

# mock ask
[mock] canned reply | system='You are a clear shop-style teacher. Keep answers short, concrete, and honest.' | you said: 'hi'
```

That `[mock]` line means the wiring works before you spend a token. If the system string drifts, `DEFAULT_SYSTEM` in `client.py` changed — open an issue before "fixing" mock text by eye.

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
3. Add a second command (e.g. `--system "..."`) and a test for it — see [good first issues](https://github.com/primeodin/first-commit-ai/issues?q=is%3Aissue+is%3Aopen+label%3A%22good+first+issue%22)

## Help / good first issues

Scoped tickets live in [Issues](https://github.com/primeodin/first-commit-ai/issues). Start with [`CONTRIBUTING.md`](CONTRIBUTING.md) (fork → test → PR map), then pick an open idea:

- **#5** — [`--json` CLI output](https://github.com/primeodin/first-commit-ai/issues/5) for reply + mock/real mode
- **#6** — [Ollama / local server walkthrough](https://github.com/primeodin/first-commit-ai/issues/6) under `docs/`

Claim one in a comment, ask questions in the thread, ship it. Docs count.

## Daily builds series

Tiny, tested teaching repos — starter → mid. Ship one, read it, then climb:

| Lane | Repo | Why open it |
| --- | --- | --- |
| Starter (this) | [first-commit-ai](https://github.com/primeodin/first-commit-ai) | Mock-first chat CLI + pytest |
| Starter RAG | [notes-rag](https://github.com/primeodin/notes-rag) | Retrieve, cite, answer over Markdown notes |
| Starter tokenizer | [tiny-bpe-tokenizer](https://github.com/primeodin/tiny-bpe-tokenizer) | Watch text become token IDs — train, encode, decode |
| Mid tool agent | [tiny-tool-agent](https://github.com/primeodin/tiny-tool-agent) | ReAct: Thought, Action, Observation, Final Answer |
| Mid prompt lab | [prompt-lab](https://github.com/primeodin/prompt-lab) | A/B eval: two prompts, fixed cases, score, winner |
| Attention mid | [attention-warrior](https://github.com/primeodin/attention-warrior) | Transformer attention you can hold in one hand |
| Shop skills | [mister-jay](https://github.com/primeodin/mister-jay) | Interactive DIY drills (vehicle, electrical, plumbing) — [live](https://primeodin.github.io/mister-jay/) |
| Literacy (Sinhala) | [jay-ai-sinhala](https://github.com/primeodin/jay-ai-sinhala) | Friends 70+ learning GitHub + AI — [live](https://primeodin.github.io/jay-ai-sinhala/) |
| Systems DIY | [camera-selector](https://github.com/primeodin/camera-selector) | NVR/Frigate camera planning — [live](https://primeodin.github.io/camera-selector/) |

Weekday cadence, in order: chat CLI → RAG → tokenizer → tool agent → **prompt lab (shipped)** → embeddings → vision → memory → shop-skill explainer.

Profile forge: [github.com/primeodin](https://github.com/primeodin)

## Why this exists

Most "AI starter" repos bury you under frameworks. This one is small enough to read on a coffee break, then push as **your** first public AI commit.

## License

MIT
