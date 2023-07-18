import sys
from PySide6.QtWidgets import QApplication
from PySide6.QtGui import QIcon
from components.main_window import MainWindow
from components.display import Display
from variables import WINDOW_ICON_PATH
from components.info import Info
from components.styles import setupTheme
from components.buttons import ButtonGrid

if __name__ == "__main__":
    app = QApplication(sys.argv)
    # Style
    setupTheme()

    window = MainWindow()

    # Icon
    icon = QIcon(str(WINDOW_ICON_PATH))
    window.setWindowIcon(icon)
    app.setWindowIcon(icon)

    # info
    info = Info("Exemplo: 2.0 * 4.0 = 8.0")
    window.addWidgetToVLayout(info)

    # Display
    display = Display()
    window.addWidgetToVLayout(display)

    # Buttons Grid
    buttonGrid = ButtonGrid()
    window.vLayout.addLayout(buttonGrid)

    window.adjustFixedSize()
    window.show()
    app.exec()
