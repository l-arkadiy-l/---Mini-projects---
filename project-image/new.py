import sys

from IPython.external.qt_for_kernel import QtGui, QtCore
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QFileDialog
from qt import Ui_MainWindow
from PIL import Image


class Img(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.img = QFileDialog.getOpenFileName(self, 'Выбрать картинку', '')[0]
        self.pixmap = QPixmap(self.img)
        self.label.setPixmap(self.pixmap)
        self.rotation = 0
        self.main_setup()

    def main_setup(self):
        self.pushButton_4.clicked.connect(self.rotate_left)
        self.pushButton_2.clicked.connect(self.red)

    def rotate_left(self):
        pixmap = QtGui.QPixmap(self.img)
        self.rotation += 90
        transform = QtGui.QTransform().rotate(self.rotation)
        pixmap = pixmap.transformed(transform, QtCore.Qt.SmoothTransformation)
        self.label.setPixmap(pixmap)

    def red(self):
        pass


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Img()
    ex.show()
    sys.exit(app.exec())
