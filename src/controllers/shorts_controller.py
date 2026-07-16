from engine.script_engine import ScriptEngine


class ShortsController:

    def __init__(self):
        self.script_engine = ScriptEngine()

    def generate(
        self,
        topic,
        duration,
        style,
        platform,
        voice,
        extra,
    ):

        return self.script_engine.generate(
            topic=topic,
            duration=duration,
            style=style,
            platform=platform,
            voice=voice,
            extra=extra,
        )