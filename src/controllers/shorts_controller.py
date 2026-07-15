from engine.script_engine import ScriptEngine


class ShortsController:

    def __init__(self):

        self.engine = ScriptEngine()

    def generate(
        self,
        topic,
        duration,
        style,
        platform,
        voice,
        extra
    ):

        return self.engine.generate(
            topic,
            duration,
            style,
            platform,
            voice,
            extra
        )