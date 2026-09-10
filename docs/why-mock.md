# Why `--mock` exists (not “fake AI,” not a skip)

Short shop note. The README already shows the **60-second** path ending in a deterministic `[mock]` line. This page is the *wiring* table: when you first open GitHub + AI, why does the safe path refuse to call a model until you ask?

## The inheritance rule

`ChatClient.chat` has two doors:

1. **`mock=True`** — build a canned string from `system` + your prompt. No HTTP. No key. Same input → same bytes.
2. **`mock=False`** — require `OPENAI_API_KEY`, then POST `/chat/completions`. Network, money, and model drift all enter the room.

After that:

- A green `pytest` without a key is **proof of plumbing**, not proof of model quality
- Editing `DEFAULT_SYSTEM` while you still run `--mock` shows up in the canned line (it echoes `system=...`) — you can see the voice change before you spend a token
- CI (`.github/workflows/ci.yml`) only trusts the mock door — Actions should not need your secret to answer “does the CLI still wire?”

So `--mock` is a **shop dry-fit**: assemble the pipe, pressure-test offline, open the live valve later.

## Hand-worked trap (same prompt, two doors)

Prompt: `hi`. Default system: *You are a clear shop-style teacher…*

| Door | What runs | Output shape (truncated) | Key needed? | Deterministic? |
| --- | --- | --- | --- | --- |
| **`--mock`** | string format in `client.py` | `[mock] canned reply \| system='You are…' \| you said: 'hi'` | no | **yes** — bit-for-bit |
| **live** | `httpx` → chat completions | whatever the model returns | **yes** | no — temperature, model, day |

Read the table left → right:

1. Mock proves `cli.py` → `ChatClient` → stdout without leaving the machine.
2. Live proves the *provider* path. A failure there is keys, URLs, quotas, or model mood — not “your first commit is broken.”
3. If you “fix” a flaky live reply by eye while rewriting the CLI, you A/B-test the weather. Prefer mock + assertions for the wiring; use live only when you mean to check the provider.

## Why “just delete mock and always hit the API” fails

Tempting shortcut for a teaching repo: drop `--mock`, require a key on day one, “feel real.”

Shop judgment:

- **Safe teaching drill:** keep mock as the default smoke. Run `pytest` and `python -m first_commit_ai --mock "hi"` before you export a key. When `DEFAULT_SYSTEM` changes, assert the new voice appears in the mock line (see `test_system_flag_overrides_default`).
- **Unsafe on a live desk:** making CI call a paid endpoint on every PR. Secrets leak into forks, bills spike on retries, and a provider outage looks like *your* regression. Keep Actions on mock; treat live as an optional manual check (or a secret-gated job you opt into later).

## What to check (in order)

1. **Does mock still start with `[mock]` and echo the prompt?** — If not, you broke the dry-fit before you touched the network.
2. **Does missing key without mock raise `OPENAI_API_KEY`?** — That error is a feature: it points you at `--mock` or a real export, not a silent empty chat.
3. **Only then** open the live valve — `OPENAI_API_KEY`, optional `OPENAI_BASE_URL` / `OPENAI_MODEL` for Ollama-compatible servers. Keep the case (your prompt) fixed while you swap models.

## Shop tip (with judgment)

**When a teammate says “tests are green but chat is weird,” ask which door they used.** Safe teaching hack: print the first token of stdout — `[mock]` means trust the wiring table; anything else means trust the provider logs.

Unsafe in production teaching: grading first-PR success by whether a live model “sounded smart.” First commits should prove *you can run and test offline*. Models come after the pipe fits.

Related open tickets: [#5 `--json` mode](https://github.com/primeodin/first-commit-ai/issues/5) (reply + mock/real flag), [#6 Ollama walkthrough](https://github.com/primeodin/first-commit-ai/issues/6) under `docs/`.
