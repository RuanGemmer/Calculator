import sys
from PySide6.QtWidgets import QApplication
from PySide6.QtGui import QIcon
from main_window import MainWindow
from display import Display
from variables import WINDOW_ICON_PATH

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()

    # Icon
    icon = QIcon(str(WINDOW_ICON_PATH))
    window.setWindowIcon(icon)
    app.setWindowIcon(icon)

    # Display
    display = Display()
    display.configStyle()
    window.addToVLayout(display)

    window.show()
    app.exec()
