import sys

from PyQt5.QtGui import QColor
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QMainWindow, QTableWidgetItem
from qt import Ui_MainWindow
import csv


class Example(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())
