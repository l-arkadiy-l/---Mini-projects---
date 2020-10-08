import sys

from PyQt5.QtWidgets import QApplication, QMainWindow
from qt import Ui_MainWindow


class Main(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setup()

    def setup(self):
        self.pushButton.clicked.connect(self.get_value)

    def get_value(self):
        try:
            with open(self.lineEdit.text(), 'r') as f:
                text = f.read().replace(' ', ',')
                print(text)
                text = text.replace('\t', ',')
                text = text.replace('\n', ',')
                try:
                    all_numbers = list(map(int, [i for i in text.split(',') if i != '']))
                    print(all_numbers)
                    min_range = min(all_numbers)
                    max_range = max(all_numbers)
                    self.spinBox.setRange(min_range, max_range)
                    self.spinBox_2.setRange(min_range, max_range)
                    self.doubleSpinBox_3.setRange(min_range, max_range)
                    self.spinBox.setValue(max(all_numbers))
                    self.spinBox_2.setValue(min(all_numbers))
                    self.doubleSpinBox_3.setValue(sum(all_numbers) / len(all_numbers))
                except Exception:
                    self.label_war.setText('Данные в файле не корректны')
        except Exception:
            self.label_war.setText('Такого файла не существует')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Main()
    ex.show()
    sys.exit(app.exec())
