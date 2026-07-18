from __future__ import annotations

from PySide6.QtWidgets import QGroupBox, QFormLayout, QTextEdit, QVBoxLayout


class ShortsDetailWidget(QGroupBox):

    def __init__(self, title: str):
        super().__init__(title)
        self._field = QTextEdit()
        self._field.setReadOnly(True)
        self._field.setMinimumHeight(90)

        layout = QVBoxLayout(self)
        form = QFormLayout()
        form.addRow(self._field)
        layout.addLayout(form)

    def set_text(self, text: str) -> None:
        self._field.setPlainText(text or "")

    def clear_text(self) -> None:
        self._field.clear()
