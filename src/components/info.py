from PySide6.QtWidgets import QLabel
from variables import SMALL_FONT_SIZE, MINIMUM_WIDTH
from PySide6.QtCore import Qt


class Info(QLabel):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.configStyle()

    def configStyle(self):
        self.setStyleSheet(f"font-size: {SMALL_FONT_SIZE}px")
        self.setAlignment(Qt.AlignmentFlag.AlignRight)
        self.setMinimumWidth(MINIMUM_WIDTH)
