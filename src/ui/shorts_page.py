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

        layout = QVBoxLayout(self)

        # Başlık
        title = QLabel("🎬 Shorts Studio")
        title.setStyleSheet("""
            font-size:28px;
            font-weight:bold;
        """)
        layout.addWidget(title)

        # Topic
        self.topic = QLineEdit()
        self.topic.setPlaceholderText("Video Topic...")
        layout.addWidget(self.topic)

        # Platform
        self.platform = QComboBox()
        self.platform.addItems([
            "YouTube Shorts",
            "TikTok",
            "Instagram Reels"
        ])
        layout.addWidget(self.platform)

        # Duration
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
            "Custom"
        ])
        layout.addWidget(self.duration)

        # Style
        self.style = QComboBox()
        self.style.addItems([
            "Documentary",
            "Mystery",
            "Educational",
            "Luxury",
            "Storytelling",
            "News",
            "Cinematic"
        ])
        layout.addWidget(self.style)

        # Profile
        self.profile = QComboBox()
        self.profile.addItems([
            "Project Atlas Prime"
        ])
        layout.addWidget(self.profile)

        # Voice
        self.voice = QComboBox()
        self.voice.addItems([
            "Atlas Documentary",
            "Atlas Mystery",
            "Kitten Female",
            "Kitten Male"
        ])
        layout.addWidget(self.voice)

        # Ek Talimat
        self.prompt = QTextEdit()
        self.prompt.setPlaceholderText(
            "Extra Instructions...\n\n"
            "Example:\n"
            "- Make it cinematic\n"
            "- Strong hook\n"
            "- Netflix documentary style"
        )
        self.prompt.setFixedHeight(120)
        layout.addWidget(self.prompt)

        # Butonlar
        buttons = QHBoxLayout()

        self.generate = QPushButton("🚀 Generate Script")
        self.render = QPushButton("🎥 Render Video")

        buttons.addWidget(self.generate)
        buttons.addWidget(self.render)

        layout.addLayout(buttons)

        # Log Alanı
        self.log = QTextEdit()
        self.log.setPlaceholderText("Logs...")
        layout.addWidget(self.log)