from PySide6.QtCore import Qt
from PySide6.QtWidgets import (
    QWidget,
    QListWidget,
    QHBoxLayout,
    QVBoxLayout,
    QStackedWidget,
    QLabel,
    QSizePolicy,
)

from ui.shorts_page import ShortsPage
from ui.research_page import ResearchPage
from ui.trend_page import TrendPage


class MainWindow(QWidget):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("Project Atlas Studio")
        self.setMinimumSize(1280, 860)
        self.resize(1440, 900)
        self.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)

        root = QHBoxLayout(self)
        root.setContentsMargins(0, 0, 0, 0)
        root.setSpacing(0)

        self.menu = QListWidget()
        self.menu.addItems([
            "🎬 Shorts Studio",
            "📹 Long Videos",
            "🔥 Trend Analyzer",
            "🧠 AI Research",
            "🎙 Voice Profiles",
            "🎨 Branding",
            "⚙ Settings",
        ])
        self.menu.setFixedWidth(240)
        self.menu.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.menu.setVerticalScrollMode(QListWidget.ScrollMode.ScrollPerPixel)
        self.menu.setSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Expanding)

        root.addWidget(self.menu)

        right = QVBoxLayout()
        right.setContentsMargins(24, 20, 24, 20)
        right.setSpacing(12)

        title = QLabel("🚀 Project Atlas Studio")
        title.setStyleSheet(
            """
            font-size:30px;
            font-weight:bold;
            padding:8px 0;
        """
        )
        right.addWidget(title)

        self.pages = QStackedWidget()
        self.pages.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)

        self.pages.addWidget(ShortsPage())
        self.pages.addWidget(QWidget())
        self.pages.addWidget(TrendPage())
        self.pages.addWidget(ResearchPage())
        self.pages.addWidget(QWidget())
        self.pages.addWidget(QWidget())
        self.pages.addWidget(QWidget())

        right.addWidget(self.pages)
        root.addLayout(right)

        self.menu.currentRowChanged.connect(self.pages.setCurrentIndex)
        self.menu.setCurrentRow(0)
