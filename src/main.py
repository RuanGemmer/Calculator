import sys
from PySide6.QtWidgets import QApplication
from PySide6.QtGui import QIcon
from main_window import MainWindow
from display import Display
from variables import WINDOW_ICON_PATH
from info import Info
from styles import setupTheme

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()

    # Style
    setupTheme()

    # Icon
    icon = QIcon(str(WINDOW_ICON_PATH))
    window.setWindowIcon(icon)
    app.setWindowIcon(icon)

    # info
    info = Info("Exemplo: 2.0 * 4.0 = 8.0")
    window.addToVLayout(info)

    # Display
    display = Display()
    display.setPlaceholderText("Digite aqui...")
    window.addToVLayout(display)

    window.adjustFixedSize()
    window.show()
    app.exec()
