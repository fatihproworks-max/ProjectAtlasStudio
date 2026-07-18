from __future__ import annotations

from PySide6.QtCore import Qt
from PySide6.QtWidgets import QGroupBox, QTextEdit, QVBoxLayout


class ShortsDetailWidget(QGroupBox):

    def __init__(self, title: str):
        super().__init__(title)
        self._field = QTextEdit()
        self._field.setReadOnly(True)
        self._field.setAlignment(Qt.AlignmentFlag.AlignTop)
        self._field.setMinimumHeight(56)
        self._field.setMaximumHeight(110)

        layout = QVBoxLayout(self)
        layout.setContentsMargins(8, 10, 8, 8)
        layout.setSpacing(6)
        layout.addWidget(self._field)

    def set_text(self, text: str) -> None:
        self._field.setPlainText(text or "")

    def clear_text(self) -> None:
        self._field.clear()
