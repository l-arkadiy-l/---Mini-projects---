import sys

from PyQt5.QtWidgets import QApplication, QPushButton, QMainWindow
from qt import Ui_MainWindow


class Example(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Задачник')
        self.all_dates = {}
        self.pushButton.clicked.connect(self.find_date)

    def find_date(self):
        # получаем дату
        string_date = self.calendarWidget.selectedDate().getDate()
        # добавляем ноль, елси месяц <= 9
        if int(string_date[1]) <= 9:
            string_date = (string_date[0], '0' + str(string_date[1]), string_date[-1])
        # добавляем ноль, елси день <= 9
        if int(string_date[2]) <= 9:
            string_date = (string_date[0], str(string_date[1]), '0' + str(string_date[-1]))
        # берем текст из line edit
        line_edit = self.lineEdit.text()
        # задаем словарю новое значение или переопределяем старое
        self.all_dates[
            f'{string_date[0]}-{string_date[1]}-{string_date[2]}-{self.timeEdit.time().toString()}'] = line_edit
        # изюавляемся от повторов
        self.textBrowser.clear()
        # сортируем даты и выводим их
        for key in sorted(self.all_dates.keys()):
            self.textBrowser.append(f'{key} - {self.all_dates[key]}')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec_())
