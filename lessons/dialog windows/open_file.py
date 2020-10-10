import sys

from PyQt5.QtWidgets import QApplication, QWidget, QInputDialog, QPushButton, QMessageBox, QTextBrowser


class Window(QWidget):
    def __init__(self):
        super(Window, self).__init__()
        self.pushButton = QPushButton('открыть диалоговое окно', self)
        self.textBrowser = QTextBrowser(self)
        self.textBrowser.move(50, 100)
        self.setup()

    def setup(self):
        self.pushButton.move(90, 50)
        self.pushButton.clicked.connect(self.open_dialog)
        self.setGeometry(600, 600, 400, 400)

    def open_dialog(self):
        name, is_ok = QInputDialog.getText(self, 'Файл', 'Какой файл вы хотите открыть?')
        if is_ok:
            try:
                with open(name) as f:
                    self.textBrowser.setText(f.read())
            except Exception:
                self.message = QMessageBox.warning(self, 'Ошибка', 'Такого файла нет')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    wnd = Window()
    wnd.show()
    sys.exit(app.exec())
