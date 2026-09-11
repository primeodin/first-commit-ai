# Local Ollama Walkthrough

Run `first-commit-ai` against a local Ollama server without paying for an API key.

## 1. Install and Start Ollama

1. Download Ollama from [ollama.com](https://ollama.com) and install it.
2. Start the Ollama service:
   ```bash
   ollama serve
   ```
3. Pull a lightweight model:
   ```bash
   ollama pull llama3.2:1b
   ```

## 2. Configure Environment Variables

Point the CLI at your local Ollama endpoint:

**Linux / macOS:**
```bash
export OPENAI_BASE_URL="http://localhost:11434/v1"
export OPENAI_API_KEY="ollama"
export OPENAI_MODEL="llama3.2:1b"
```

**Windows (Command Prompt):**
```cmd
set OPENAI_BASE_URL=http://localhost:11434/v1
set OPENAI_API_KEY=ollama
set OPENAI_MODEL=llama3.2:1b
```

**Windows (PowerShell):**
```powershell
$env:OPENAI_BASE_URL="http://localhost:11434/v1"
$env:OPENAI_API_KEY="ollama"
$env:OPENAI_MODEL="llama3.2:1b"
```

## 3. Run a Live Prompt

Run a real prompt without the `--mock` flag:
```bash
python -m first_commit_ai "Why is the sky blue?"
```

## Troubleshooting: Server Down

If Ollama is not running or unreachable at the target port, the command will exit with a connection error:
```text
error: Connection error. Ensure Ollama is running (`ollama serve`) and reachable at http://localhost:11434.
```
Check that the service is running and accessible via:
```bash
curl http://localhost:11434/api/tags
```
