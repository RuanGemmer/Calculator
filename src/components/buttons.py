from PySide6.QtWidgets import QPushButton, QGridLayout
from PySide6.QtCore import Slot
from variables import MEDIUM_FONT_SIZE
from utils import isNumOrDot, isEmpty, isValidNumber, formatFloat
from .display import Display
from .info import Info
import math
from .main_window import MainWindow


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
    def __init__(self,
                 display: Display,
                 info: Info,
                 window: MainWindow,
                 *args,
                 **kwarg) -> None:
        super().__init__(*args, **kwarg)

        self._gridMask = [
            ['C', 'Back', '^', '/'],
            ['7', '8', '9', '*'],
            ['4', '5', '6', '-'],
            ['1', '2', '3', '+'],
            ['+/-',  '0', '.', '=']
        ]
        self.display = display
        self.info = info
        self._equation = ''
        self._left = None
        self._rigth = None
        self._operator = None
        self.window = window
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

        if function_ == "Back":
            self._connectButtonCliked(button, self.display.backspace)

        if function_ == "+/-":
            self._connectButtonCliked(button, self._invertSignal)

        if function_ in "+-/*^":
            self._connectButtonCliked(
                button,
                self._makeSlot(self._operatorClicked, function_)
                )

        if function_ == "=":
            self._connectButtonCliked(button, self._eq)

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
        self._left = None
        self._rigth = None
        self._operator = None
        self.equation = ''
        self.display.clear()

    def _operatorClicked(self, operatorButton):
        displayText = self.display.text()
        self.display.clear()

        if not isValidNumber(displayText) and self._left is None:
            self._showError("Você não digitou nada!")
            return

        if self._left is None:
            self._left = formatFloat(float(displayText))

        self._operator = operatorButton
        self.equation = f'{self._left} {self._operator} ??'

    def _eq(self):
        displayText = self.display.text()

        if not isValidNumber(displayText):
            self._showError("Sem valor para calcular")
            return

        self._rigth = formatFloat(float(displayText))
        self.equation = f'{self._left} {self._operator} {self._rigth}'
        result = 'error'

        try:
            if "^" in self.equation \
                and isinstance(self._rigth, (float | int)) \
                    and isinstance(self._left, (float | int)):
                result = formatFloat(float(math.pow(self._left, self._rigth)))
            else:
                result = formatFloat(float(eval(self.equation)))
        except ZeroDivisionError:
            self._showError("Divisão por zero")
        except OverflowError:
            self._showError("Número muito grande")

        self.display.setText(str(result))
        self.info.setText(f'{self.equation} = {result}')
        self._left = None
        self._rigth = None
        self._operator = None

        if result == 'error':
            self._left = None

    def _invertSignal(self):
        number = formatFloat(float(self.display.text()))
        newNumber = number * (-1)
        self.display.setText(str(newNumber))

    def _showError(self, text: str):
        msgBox = self.window.makeMsgbox()
        msgBox.setText(text)
        msgBox.setIcon(msgBox.Icon.Critical)
        msgBox.exec()
