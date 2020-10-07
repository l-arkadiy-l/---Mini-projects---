import sys

from PyQt5.QtWidgets import QApplication, QMainWindow
from qt import Ui_MainWindow


class Main(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setup()

    def setup(self):
        self.pushButton.clicked.connect(self.open_file)
        self.pushButton_2.clicked.connect(self.save_file)
        self.pushButton_3.clicked.connect(self.create_file)

    def open_file(self):
        file = self.lineEdit.text()
        try:
            with open(file) as f:
                self.plainTextEdit.setPlainText(f.read())
            self.label.setText('Редактор файлов')
        except Exception:
            self.label.setText('Такой файл не найден')

    def save_file(self):
        file = self.lineEdit.text()
        try:
            open(file)
            with open(file, 'w') as f:
                f.write(self.plainTextEdit.toPlainText())
        except Exception:
            self.label.setText('Такой файл не найден')

    def create_file(self):
        file = self.lineEdit.text()
        with open(file, 'w') as f:
            f.write(self.plainTextEdit.toPlainText())
        self.label.setText('Редактор файлов')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Main()
    ex.show()
    sys.exit(app.exec())
