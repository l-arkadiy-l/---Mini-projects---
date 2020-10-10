import sys

from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QApplication, QFileDialog, \
    QMainWindow, QGraphicsOpacityEffect

from qt import Ui_MainWindow


class Window(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(Window, self).__init__()
        self.setupUi(self)
        fname = QFileDialog.getOpenFileName(self, 'Выбрать картинку', '')[0]
        self.opacity_effect = QGraphicsOpacityEffect()
        self.opacity_effect.setOpacity(1)
        self.pixmap = QPixmap(fname)
        self.label.setPixmap(self.pixmap)
        self.label.setGraphicsEffect(self.opacity_effect)
        self.verticalSlider.valueChanged.connect(self.change_alpha)

        self.show()

    def change_alpha(self, value):
        print(value)
        print(1 - (value / 100))
        self.opacity_effect.setOpacity(1 - (value / 100))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    wnd = Window()
    wnd.show()
    sys.exit(app.exec())
