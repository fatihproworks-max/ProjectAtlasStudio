from __future__ import annotations

import requests
from requests import Session
from requests.exceptions import RequestException, Timeout


class OllamaService:

    def __init__(
        self,
        base_url: str = "http://localhost:11434",
        model: str = "gemma3:4b",
        timeout: int = 180,
    ):

        self.base_url = base_url.rstrip("/")
        self.model = model
        self.timeout = timeout

        self.session: Session = requests.Session()

    def set_model(self, model: str) -> None:
        self.model = model

    def get_model(self) -> str:
        return self.model

    def is_running(self) -> bool:

        try:

            response = self.session.get(
                f"{self.base_url}/api/tags",
                timeout=5,
            )

            return response.status_code == 200

        except RequestException:

            return False

    def generate(self, prompt: str) -> str:

        print("===== OLLAMA DEBUG =====")

        url = f"{self.base_url}/api/generate"

        payload = {
            "model": self.model,
            "prompt": prompt,
            "stream": False,
        }

        print("URL:", url)
        print("Payload:", payload)

        try:

            response = self.session.post(
                url,
                json=payload,
                timeout=self.timeout,
            )

            print("Status:", response.status_code)
            print("Response:", response.text)

            response.raise_for_status()

            data = response.json()

            return data.get("response", "").strip()

        except Timeout:
            raise RuntimeError("Ollama zaman aşımına uğradı.")

        except RequestException as exc:
            raise RuntimeError(f"Ollama bağlantı hatası: {exc}")

    def close(self) -> None:
        self.session.close()