import sys

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QApplication, QPushButton, QMainWindow, QTableWidgetItem
import PyQt5.QtGui as QtGui
from qt import Ui_MainWindow
import sqlite3


class Example(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()

        self.setupUi(self)
        self.initUI()

    def initUI(self):
        # connect db
        con = sqlite3.connect('films_db.sqlite')
        cur = con.cursor()
        # choose all
        list_all = cur.execute('''SELECT * FROM films''').fetchall()
        # create labels and width column and width row
        self.tableWidget.setColumnCount(5)
        self.tableWidget.setHorizontalHeaderLabels(['id', 'title', 'year', 'genre', 'duration'])
        self.tableWidget.setRowCount(len(list_all))
        # reflect values in db
        for i, row in enumerate(list_all):
            for j in range(5):
                self.tableWidget.setItem(i, j, QTableWidgetItem(str(row[j])))
        # click btn
        self.pushButton.clicked.connect(lambda: self.change_table(
            self.lineEdit.text(),
            self.lineEdit_name.text(),
            self.lineEdit_len.text()
        ))

    def change_table(self, year='> 1', title="LIKE '%'", duration='> 0'):
        con = sqlite3.connect('films_db.sqlite')
        cur = con.cursor()
        # separate symbol and number ( > ) ( 20 )
        list_symbol_year = [i for i in year if i not in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', ' ']]
        list_symbol_duration = [i for i in duration if i not in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', ' ']]
        print(list_symbol_duration)
        print(duration[len(list_symbol_duration):])
        if year and title and duration:
            cur.execute(f'SELECT * FROM films WHERE '
                        f'duration {"".join(list_symbol_duration)} {int(duration[len(list_symbol_duration):])} AND '
                        f'year {"".join(list_symbol_year)} {int(year[len(list_symbol_year):])} AND '
                        f'title {title}')
        elif year and title:
            cur.execute(f'SELECT * FROM films WHERE '
                        f'year {"".join(list_symbol_year)} {int(year[len(list_symbol_year):])} AND '
                        f'title {title}')
        elif title and duration:
            cur.execute(f'SELECT * FROM films WHERE '
                        f'duration {"".join(list_symbol_duration)} {int(duration[len(list_symbol_duration):])} AND '
                        f'title {title}')
        elif year and duration:
            cur.execute(f'SELECT * FROM films WHERE '
                        f'duration {"".join(list_symbol_duration)} {int(duration[len(list_symbol_duration):])} AND '
                        f'year {"".join(list_symbol_year)} {int(year[len(list_symbol_year):])}')
        elif year:
            cur.execute(f'SELECT * FROM films WHERE '
                        f'year {"".join(list_symbol_year)} {int(year[len(list_symbol_year):])}')
        elif title:
            cur.execute(f'SELECT * FROM films WHERE title {title}')
        elif duration:
            cur.execute(f'SELECT * FROM films WHERE '
                        f'duration {"".join(list_symbol_duration)} {int(duration[len(list_symbol_duration):])}')
        list_filter = cur.fetchall()
        self.tableWidget.setRowCount(len(list_filter))
        for i, row in enumerate(list_filter):
            for j in range(5):
                self.tableWidget.setItem(i, j, QTableWidgetItem(str(row[j])))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())
