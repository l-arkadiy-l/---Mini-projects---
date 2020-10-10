import sys

from PyQt5.QtWidgets import QApplication, QWidget, QInputDialog, QPushButton, QMessageBox


class Window(QWidget):
    def __init__(self):
        super(Window, self).__init__()
        self.pushButton = QPushButton('открыть диалоговое окно', self)
        self.setup()

    def setup(self):
        self.pushButton.move(0, 50)
        self.pushButton.clicked.connect(self.open_dialog)
        self.setGeometry(200, 200, 200, 200)

    def open_dialog(self):
        name, is_ok = QInputDialog.getInt(self, 'Возраст', 'Сколько вам лет?')
        if is_ok and name >= 5:
            self.pushButton.setText(f'Вы выглядите на {name - 5}')
            self.pushButton.adjustSize()
        elif name < 5:
            self.message = QMessageBox.warning(self, 'Молодая душа', "Вы слишком молоды!",
                                         QMessageBox.Cancel)
            self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    wnd = Window()
    wnd.show()
    sys.exit(app.exec())
