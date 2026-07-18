from __future__ import annotations

import json

from controllers.shorts_controller import ShortsController
from ui.shorts_detail_widget import ShortsDetailWidget
from workers.script_worker import ScriptWorker
from PySide6.QtWidgets import (
    QWidget,
    QLabel,
    QPushButton,
    QTextEdit,
    QLineEdit,
    QVBoxLayout,
    QHBoxLayout,
    QComboBox,
)


class ShortsPage(QWidget):

    def __init__(self):
        super().__init__()
        self.controller = ShortsController()
        self.worker = None

        layout = QVBoxLayout(self)

        title = QLabel("🎬 Shorts Studio")
        title.setStyleSheet(
            """
            font-size:28px;
            font-weight:bold;
        """
        )
        layout.addWidget(title)

        self.topic = QLineEdit()
        self.topic.setPlaceholderText("Video Topic...")
        layout.addWidget(self.topic)

        self.platform = QComboBox()
        self.platform.addItems([
            "YouTube Shorts",
            "TikTok",
            "Instagram Reels",
        ])
        layout.addWidget(self.platform)

        self.duration = QComboBox()
        self.duration.addItems([
            "15 sec",
            "20 sec",
            "30 sec",
            "45 sec",
            "60 sec",
            "90 sec",
            "3 min",
            "5 min",
            "10 min",
            "Custom",
        ])
        layout.addWidget(self.duration)

        self.style = QComboBox()
        self.style.addItems([
            "Documentary",
            "Mystery",
            "Educational",
            "Luxury",
            "Storytelling",
            "News",
            "Cinematic",
        ])
        layout.addWidget(self.style)

        self.profile = QComboBox()
        self.profile.addItems([
            "Project Atlas Prime",
        ])
        layout.addWidget(self.profile)

        self.voice = QComboBox()
        self.voice.addItems([
            "Atlas Documentary",
            "Atlas Mystery",
            "Kitten Female",
            "Kitten Male",
        ])
        layout.addWidget(self.voice)

        self.prompt = QTextEdit()
        self.prompt.setPlaceholderText(
            "Extra Instructions...\n\n"
            "Example:\n"
            "- Strong Hook\n"
            "- Cinematic\n"
            "- Netflix Documentary Style"
        )
        self.prompt.setFixedHeight(120)
        layout.addWidget(self.prompt)

        buttons = QHBoxLayout()

        self.generate = QPushButton("🚀 Generate Script")
        self.generate.clicked.connect(self.generate_script)

        self.render = QPushButton("🎥 Render Video")

        buttons.addWidget(self.generate)
        buttons.addWidget(self.render)
        layout.addLayout(buttons)

        self.hook_box = ShortsDetailWidget("🔥 Hook")
        self.script_box = ShortsDetailWidget("📝 Script")
        self.title_box = ShortsDetailWidget("🏷 Title")
        self.description_box = ShortsDetailWidget("📄 Description")
        self.tags_box = ShortsDetailWidget("🔍 Tags")

        layout.addWidget(self.hook_box)
        layout.addWidget(self.script_box)
        layout.addWidget(self.title_box)
        layout.addWidget(self.description_box)
        layout.addWidget(self.tags_box)

        self.log = QTextEdit()
        self.log.setReadOnly(True)
        self.log.setPlaceholderText("Logs...")
        self.log.setFixedHeight(120)
        layout.addWidget(self.log)

    def generate_script(self):
        self.generate.setEnabled(False)
        self.clear_output()
        self.log.append("Generating script...")

        self.worker = ScriptWorker(
            topic=self.topic.text().strip(),
            duration=self.duration.currentText(),
            style=self.style.currentText(),
            platform=self.platform.currentText(),
            voice=self.voice.currentText(),
            extra=self.prompt.toPlainText().strip(),
            parent=self,
        )
        self.worker.started_message.connect(self.log.append)
        self.worker.finished_script.connect(self.on_script_finished)
        self.worker.failed.connect(self.on_script_failed)
        self.worker.finished.connect(self.on_worker_finished)
        self.worker.start()

    def clear_output(self) -> None:
        self.hook_box.clear_text()
        self.script_box.clear_text()
        self.title_box.clear_text()
        self.description_box.clear_text()
        self.tags_box.clear_text()

    def on_script_finished(self, script: str):
        try:
            payload = json.loads(script)
        except json.JSONDecodeError:
            self.script_box.set_text(script)
            self.log.append("JSON parse failed; raw output shown.")
            return

        self.hook_box.set_text(payload.get("hook", ""))
        self.script_box.set_text(payload.get("script", ""))
        self.title_box.set_text(payload.get("title", ""))
        self.description_box.set_text(payload.get("description", ""))

        tags = payload.get("tags", [])
        if isinstance(tags, list):
            tags_text = ", ".join(str(tag) for tag in tags)
        else:
            tags_text = str(tags)
        self.tags_box.set_text(tags_text)

        self.log.append(payload.get("status", "Done."))

    def on_script_failed(self, error: str):
        self.log.append(f"HATA: {error}")

    def on_worker_finished(self):
        self.generate.setEnabled(True)
        self.worker = None
