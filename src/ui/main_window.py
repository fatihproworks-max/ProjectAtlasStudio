from PySide6.QtWidgets import (
    QWidget,
    QListWidget,
    QHBoxLayout,
    QVBoxLayout,
    QStackedWidget,
    QLabel
)

from ui.shorts_page import ShortsPage
from ui.research_page import ResearchPage
from ui.trend_page import TrendPage


class MainWindow(QWidget):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("Project Atlas Studio")
        self.resize(1400, 850)

        root = QHBoxLayout(self)

        # SOL MENÜ
        self.menu = QListWidget()

        self.menu.addItems([
            "🎬 Shorts Studio",
            "📹 Long Videos",
            "🔥 Trend Analyzer",
            "🧠 AI Research",
            "🎙 Voice Profiles",
            "🎨 Branding",
            "⚙ Settings"
        ])

        self.menu.setMaximumWidth(220)

        root.addWidget(self.menu)

        # SAĞ TARAF
        right = QVBoxLayout()

        title = QLabel("🚀 Project Atlas Studio")

        title.setStyleSheet("""
        font-size:30px;
        font-weight:bold;
        padding:15px;
        """)

        right.addWidget(title)

        self.pages = QStackedWidget()

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