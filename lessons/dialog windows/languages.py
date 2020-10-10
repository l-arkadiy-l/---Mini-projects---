import sys

from PyQt5.QtWidgets import QApplication, QWidget, QInputDialog, QPushButton


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
        name, is_ok = QInputDialog.getText(self, 'Языки', 'Какие языки вы знаете?')
        if is_ok:
            self.pushButton.setText(name)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    wnd = Window()
    wnd.show()
    sys.exit(app.exec())
