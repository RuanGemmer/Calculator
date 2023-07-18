from PySide6.QtWidgets import QPushButton, QGridLayout
from PySide6.QtCore import Slot
from variables import MEDIUM_FONT_SIZE
from utils import isNumOrDot, isEmpty, isValidNumber
from .display import Display
from .info import Info


class Button(QPushButton):
    def __init__(self, *args, **kwarg) -> None:
        super().__init__(*args, **kwarg)
        self.configStyle()

    def configStyle(self):
        font = self.font()
        font.setPixelSize(MEDIUM_FONT_SIZE)
        self.setFont(font)
        self.setMinimumSize(75, 75)


class ButtonGrid(QGridLayout):
    def __init__(self, display: Display, info: Info, *args, **kwarg) -> None:
        super().__init__(*args, **kwarg)

        self._gridMask = [
            ['C', '◀', '^', '/'],
            ['7', '8', '9', '*'],
            ['4', '5', '6', '-'],
            ['1', '2', '3', '+'],
            ['+/-',  '0', '.', '=']
        ]
        self.display = display
        self.info = info
        self._equation = ''
        self._makeGrid()

    @property
    def equation(self):
        return self._equation

    @equation.setter
    def equation(self, value):
        self._equation = value
        self.info.setText(value)

    def _makeGrid(self):
        for i, row in enumerate(self._gridMask):
            for j, buttonText in enumerate(row):
                button = Button(buttonText)

                if not isNumOrDot(buttonText) and not isEmpty(buttonText):
                    button.setProperty('cssClass', 'specialButton')
                    self._configSpecialButtons(button)

                self.addWidget(button, i, j)
                slot = self._makeSlot(self._insertButtonTextToDisplay, button)
                self._connectButtonCliked(button, slot)

    def _connectButtonCliked(self, button, slot):
        button.clicked.connect(slot)

    def _configSpecialButtons(self, button):
        function_ = button.text()

        if function_ == "C":
            self._connectButtonCliked(button, self._clear)

    def _makeSlot(self, method, *args, **kwargs):
        @Slot(bool)
        def realSlot():
            method(*args, **kwargs)
        return realSlot

    def _insertButtonTextToDisplay(self, button):
        buttonText = button.text()
        self.newDisplayValue = self.display.text() + buttonText

        if not isValidNumber(self.newDisplayValue):
            return

        self.display.insert(buttonText)

    def _clear(self):
        self.display.clear()
