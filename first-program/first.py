import sys

from PyQt5.QtWidgets import QApplication, QLabel, QMainWindow, QPushButton
from random import choice


class Example(QMainWindow):
    def __init__(self):
        super().__init__()
        # название окна
        self.setWindowTitle('Наша первая программа')
        # задаем ширину окна
        self.setGeometry(100, 500, 500, 200)
        # создание надписи
        self.label = QLabel('Крути барабан!', self)
        # передвигаем нашу надпись на 200 пикселей по x и 100 по y
        self.label.move(185, 100)

        # создание кнопки
        self.btn = QPushButton('крутить', self)
        self.btn.clicked.connect(self.text_shuffle)
        self.btn.move(180, 150)

    def text_shuffle(self, text):
        numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        if choice(numbers) == 10:
            self.btn.setText('Вы выиграли ааавтомобиль')
            self.btn.adjustSize()
        else:
            self.btn.setText('вы проиграли')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())
