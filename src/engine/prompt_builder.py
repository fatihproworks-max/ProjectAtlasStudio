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
You are an elite YouTube Shorts strategist and documentary script writer.

Create a concise JSON object only. Do not write markdown, explanations, or code fences.

The output must match this shape:
{{
  "hook": "...",
  "script": "...",
  "title": "...",
  "description": "...",
  "tags": ["...", "..."],
  "status": "..."
}}

Rules:
- Write a powerful opening hook.
- Write only the narration script in the script field.
- Do not include timecodes.
- Do not include voiceover labels.
- Do not include scene labels.
- Do not include camera notes.
- Do not include SFX notes.
- Do not include markdown.
- Keep the script high-retention and cinematic.
- The hook should be 1-2 short sentences.
- The title should be clickable and curiosity-driven.
- The description should be short and SEO-friendly.
- The tags should be relevant YouTube tags.
- The status field should be a short success note.

Context:
Platform: {request.platform}
Topic: {request.topic}
Duration: {request.duration}
Style: {request.style}
Voice: {request.voice}
Extra Instructions: {request.extra}

Return the JSON object only.
""".strip()
