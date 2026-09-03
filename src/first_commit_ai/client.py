"""OpenAI-compatible chat client with a deterministic mock mode."""

from __future__ import annotations

import os
from dataclasses import dataclass

import httpx

DEFAULT_SYSTEM = (
    "You are a clear shop-style teacher. Keep answers short, concrete, and honest."
)


@dataclass
class ChatClient:
    api_key: str | None = None
    base_url: str = "https://api.openai.com/v1"
    model: str = "gpt-4o-mini"
    system: str = DEFAULT_SYSTEM
    mock: bool = False

    @classmethod
    def from_env(cls, *, mock: bool = False) -> "ChatClient":
        return cls(
            api_key=os.environ.get("OPENAI_API_KEY"),
            base_url=os.environ.get("OPENAI_BASE_URL", "https://api.openai.com/v1").rstrip("/"),
            model=os.environ.get("OPENAI_MODEL", "gpt-4o-mini"),
            mock=mock,
        )

    def chat(self, prompt: str) -> str:
        if self.mock:
            return (
                "[mock] canned reply"
                f" | system={self.system!r}"
                f" | you said: {prompt!r}"
            )
        if not self.api_key:
            raise RuntimeError(
                "OPENAI_API_KEY is not set. Export a key, or pass --mock to practice offline."
            )
        url = f"{self.base_url}/chat/completions"
        payload = {
            "model": self.model,
            "messages": [
                {"role": "system", "content": self.system},
                {"role": "user", "content": prompt},
            ],
            "temperature": 0.2,
        }
        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json",
        }
        with httpx.Client(timeout=60.0) as client:
            resp = client.post(url, json=payload, headers=headers)
            resp.raise_for_status()
            data = resp.json()
        return data["choices"][0]["message"]["content"].strip()
