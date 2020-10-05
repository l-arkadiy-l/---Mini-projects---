import sys

from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtWidgets import QApplication, QPushButton, QMainWindow
from PyQt5.QtWidgets import QInputDialog
from qt import Ui_MainWindow
from random import randint


class Example(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.initUI()
        self.do_paint = False
        self.number = 0

    def initUI(self):
        self.setWindowTitle('Диалоговые окна')
        self.pushButton.clicked.connect(self.run)

    def run(self):
        self.do_paint = False
        number, ok_pressed = QInputDialog.getInt(self, "Количество цветов", "Сколько цветов?", 3, 0, 100, 1)
        if ok_pressed:
            self.number = number
            self.paint()

    def paintEvent(self, event):
        if self.do_paint:
            qp = QPainter()
            qp.begin(self)
            self.draw_flag(qp)
            qp.end()

    def paint(self):
        self.do_paint = True
        self.update()

    def draw_flag(self, qp):
        for i in range(self.number):
            qp.setBrush(QColor(randint(0, 255), randint(0, 255), randint(0, 255)))
            qp.drawRect(90, (i * 30) + 120, 120, 30)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec_())
