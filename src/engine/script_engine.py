import requests


class ScriptEngine:

    def __init__(self):
        self.url = "http://localhost:11434/api/generate"
        self.model = "gemma3:4b"

    def generate(
        self,
        topic,
        duration,
        style,
        platform,
        voice,
        extra,
    ):

        prompt = f"""
You are a professional YouTube content writer.

Platform:
{platform}

Topic:
{topic}

Duration:
{duration}

Style:
{style}

Voice:
{voice}

Extra Instructions:
{extra}

Write ONLY the final script.

No explanations.
No markdown.
No titles.
"""

        response = requests.post(
            self.url,
            json={
                "model": self.model,
                "prompt": prompt,
                "stream": False
            }
        )

        return response.json()["response"]