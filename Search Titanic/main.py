import sys

from PyQt5.QtGui import QColor
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QMainWindow, QTableWidgetItem
from PyQt5.uic.properties import QtGui

from qt import Ui_MainWindow
import csv


class Example(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.write_people()
        self.lineEdit.textChanged.connect(lambda: self.valueChanged(self.lineEdit.text()))

    def write_people(self):
        with open('titanic.csv') as titanic_csv:
            reader = csv.reader(titanic_csv)
            self.list_all = [i for i in reader]
        labels = self.list_all[0]
        self.tableWidget.setColumnCount(len(labels))
        self.tableWidget.setRowCount(len(self.list_all) - 1)
        self.tableWidget.setHorizontalHeaderLabels(labels)
        passengers = self.list_all[1:]
        counter = 0
        for passenger in passengers:
            for i in range(7):
                self.tableWidget.setItem(counter, i, QTableWidgetItem(str(passenger[i])))
            if int(passenger[5]) == 1:
                self.colorRow(counter, QColor(10, 255, 10))
            else:
                self.colorRow(counter, QColor(255, 10, 10))
            counter += 1

    def colorRow(self, row, color):
        for i in range(self.tableWidget.columnCount()):
            self.tableWidget.item(row, i).setBackground(color)

    def filter_human(self, text, human):
        if text in human[1].lower() or text == human[1].lower():
            return human

    def valueChanged(self, text):
        if len(text) >= 3:
            list_filter = list(filter(lambda x:
                                      self.filter_human(text.lower(), x), self.list_all))
            self.tableWidget.setRowCount(len(list_filter))
            counter = 0
            for passenger in list_filter:
                for i in range(7):
                    self.tableWidget.setItem(counter, i,
                                             QTableWidgetItem(str(passenger[i])))
                if int(passenger[5]) == 1:
                    self.colorRow(counter, QColor(10, 255, 10))
                else:
                    self.colorRow(counter, QColor(255, 10, 10))
                counter += 1
        else:
            self.write_people()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())
