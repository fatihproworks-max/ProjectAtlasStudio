from __future__ import annotations

from PySide6.QtCore import QThread, Signal

from controllers.shorts_controller import ShortsController


class ScriptWorker(QThread):
    started_message = Signal(str)
    finished_script = Signal(str)
    failed = Signal(str)

    def __init__(
        self,
        topic: str,
        duration: str,
        style: str,
        platform: str,
        voice: str,
        extra: str,
        parent=None,
    ):
        super().__init__(parent)
        self.topic = topic
        self.duration = duration
        self.style = style
        self.platform = platform
        self.voice = voice
        self.extra = extra
        self.controller = ShortsController()

    def run(self) -> None:
        try:
            self.started_message.emit("Building prompt...")
            self.started_message.emit("Sending to Ollama...")
            script = self.controller.generate(
                topic=self.topic,
                duration=self.duration,
                style=self.style,
                platform=self.platform,
                voice=self.voice,
                extra=self.extra,
            )
            self.started_message.emit("Formatting output...")
            self.finished_script.emit(script)
        except Exception as exc:
            self.failed.emit(str(exc))
