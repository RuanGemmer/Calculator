from PySide6.QtCore import Qt
from PySide6.QtGui import QKeyEvent
from utils import isEmpty, isNumOrDot


def keyPressEvent_(self, event: QKeyEvent) -> None:
    text = event.text().strip()
    key = event.key()
    KEYS = Qt.Key

    isEnter = key in [KEYS.Key_Enter, KEYS.Key_Return]
    isDelete = key in [KEYS.Key_Backspace, KEYS.Key_Delete]
    isEsc = key in [KEYS.Key_Escape]

    if text == ",":
        text = "."

    if isEnter or text == "=":
        self.eqPressed.emit()
        return event.ignore()

    if isDelete:
        self.delPressed.emit()
        return event.ignore()

    if isEsc or text.lower() == "c":
        self.clearPressed.emit()
        return event.ignore()

    if isEmpty(text):
        return event.ignore()

    if isNumOrDot(text):
        self.inputPressed.emit(text)
        return event.ignore()

    if text in "+-*/^":
        self.operatorPressed.emit(text)
        return event.ignore()
