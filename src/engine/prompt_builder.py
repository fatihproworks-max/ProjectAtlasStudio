from dataclasses import dataclass


@dataclass(slots=True)
class ShortsPromptRequest:
    topic: str
    platform: str
    duration: str
    style: str
    voice: str
    extra: str = ""


class PromptBuilder:

    @staticmethod
    def build_shorts(request: ShortsPromptRequest) -> str:

        return f"""
You are an elite YouTube Shorts script writer.

Your job is to create an engaging, high-retention short video.

Platform:
{request.platform}

Topic:
{request.topic}

Duration:
{request.duration}

Style:
{request.style}

Narration Style:
{request.voice}

Extra Instructions:
{request.extra}

Rules:

- Start with a powerful hook.
- Keep the pacing fast.
- Make every sentence valuable.
- Create curiosity.
- End with a memorable closing.
- Return ONLY the narration script.
- Do not use markdown.
- Do not explain your reasoning.
- Do not add titles unless requested.
""".strip()