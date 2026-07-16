from engine.prompt_builder import PromptBuilder, ShortsPromptRequest
from services.ollama_service import OllamaService


class ScriptEngine:

    def __init__(self):
        self.ollama = OllamaService()

    def generate(
        self,
        topic,
        duration,
        style,
        platform,
        voice,
        extra,
    ):

        request = ShortsPromptRequest(
            topic=topic,
            platform=platform,
            duration=duration,
            style=style,
            voice=voice,
            extra=extra,
        )

        prompt = PromptBuilder.build_shorts(request)
        print("ScriptEngine çalıştı")
        print(prompt)

        return self.ollama.generate(prompt)