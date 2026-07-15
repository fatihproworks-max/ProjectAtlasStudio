from PySide6.QtWidgets import QWidget,QVBoxLayout,QLabel


class ResearchPage(QWidget):

    def __init__(self):
        super().__init__()

        layout=QVBoxLayout()

        title=QLabel("🧠 AI Research")

        title.setStyleSheet("""
        font-size:28px;
        font-weight:bold;
        """)

        layout.addWidget(title)

        self.setLayout(layout)