from __future__ import annotations

from controllers.shorts_controller import ShortsController
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

        self.preview = QTextEdit()
        self.preview.setReadOnly(True)
        self.preview.setPlaceholderText("Generated Script...")
        layout.addWidget(self.preview)

        self.log = QTextEdit()
        self.log.setReadOnly(True)
        self.log.setPlaceholderText("Logs...")
        self.log.setFixedHeight(120)
        layout.addWidget(self.log)

    def generate_script(self):
        print("Generate butonuna basıldı")

        try:
            self.log.append("Generating script...")

            script = self.controller.generate(
                topic=self.topic.text(),
                duration=self.duration.currentText(),
                style=self.style.currentText(),
                platform=self.platform.currentText(),
                voice=self.voice.currentText(),
                extra=self.prompt.toPlainText(),
            )

            self.preview.setPlainText(script)
            self.log.append("Done.")

        except Exception as e:
            print("HATA:", e)
            import traceback
            traceback.print_exc()
            self.log.append(str(e))
