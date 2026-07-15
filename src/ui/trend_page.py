from PySide6.QtWidgets import QWidget,QVBoxLayout,QLabel


class TrendPage(QWidget):

    def __init__(self):
        super().__init__()

        layout=QVBoxLayout()

        title=QLabel("🔥 Trend Analyzer")

        title.setStyleSheet("""
        font-size:28px;
        font-weight:bold;
        """)

        layout.addWidget(title)

        self.setLayout(layout)