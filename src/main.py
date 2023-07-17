import sys
from PySide6.QtWidgets import QApplication, QLabel
from PySide6.QtGui import QIcon
from main_window import MainWindow
from files.variables import WINDOW_ICON_PATH

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()

    label1 = QLabel("Texto exemplo")
    label1.setStyleSheet("font-size: 50px")
    window.addWidgetToVLayout(label1)

    # Icon
    icon = QIcon(str(WINDOW_ICON_PATH))
    window.setWindowIcon(icon)
    app.setWindowIcon(icon)

    window.show()
    app.exec()
