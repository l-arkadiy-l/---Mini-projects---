import sys

from PyQt5.QtWidgets import QApplication, QMainWindow
from qt import Ui_MainWindow
import os.path


class Main(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setup()

    def setup(self):
        self.pushButton_create.clicked.connect(self.create_file)
        self.pushButton_open.clicked.connect(self.open_file)
        self.pushButton_save.clicked.connect(self.save_file)

    def create_file(self):
        if self.lineEdit.text():
            title = self.lineEdit.text()
            text = self.plainTextEdit.toPlainText()
            if not os.path:
                with open(title, 'w') as f:
                    f.write(text)
                self.lineEdit.clear()
                self.plainTextEdit.clear()

    def open_file(self):
        if self.lineEdit.text():
            title = self.lineEdit.text()
            with open(title) as f:
                self.plainTextEdit.setPlainText(f.read())

    def save_file(self):
        if self.lineEdit.text():
            title = self.lineEdit.text()
            text = self.plainTextEdit.toPlainText()
            if os.path:
                with open(title, 'w') as f:
                    f.write(text)
                self.lineEdit.clear()
                self.plainTextEdit.clear()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Main()
    ex.show()
    sys.exit(app.exec())
