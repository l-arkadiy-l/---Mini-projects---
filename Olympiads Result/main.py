import sys

from PyQt5.QtGui import QColor
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QMainWindow, QTableWidgetItem
from qt import Ui_MainWindow
import csv


class Example(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.record_comboBox()
        self.pushButton.clicked.connect(
            lambda: self.filter_students(self.comboBox.currentText(),
                                         self.comboBox_2.currentText()))

    def determine_place(self, keys, list_max, counter):
        # -------gold
        if keys == max(list_max):
            self.colorRow(counter, QColor(205, 181, 6))
        # -------silver
        elif keys == list_max[list_max.index(max(list_max)) + 1]:
            self.colorRow(counter, QColor(192, 192, 192))
        # -------bronze
        elif keys == list_max[list_max.index(max(list_max)) + 2]:
            self.colorRow(counter, QColor(177, 86, 15))

    def filter_students(self, school, classroom):
        def check_match(x):
            index_x = x[0].split(',')[1].replace('"', '').split()
            if school != 'Все' and classroom != 'Все':
                if int(class_school[0]) == int(index_x[1]) \
                        and int(class_school[-1]) == int(index_x[2].replace('б', '')):
                    return x
            elif school == 'Все' and classroom != 'Все':
                if int(class_school[-1]) == int(index_x[2].replace('б', '')):
                    return x
            elif classroom == 'Все' and school != 'Все':
                if int(class_school[0]) == int(index_x[1].replace('б', '')):
                    return x
            else:
                return x

        self.tableWidget.clear()
        with open('rez.csv', encoding='UTF-8') as file_csv:
            class_school = [school, classroom]
            reader = csv.reader(file_csv, delimiter=';')
            # column width
            title = next(reader)
            self.tableWidget.setColumnCount(len(title[0].split(',')) - 5)
            self.tableWidget.setHorizontalHeaderLabels(['Фамилия', 'Результат', 'Логин'])
            # dict students
            dict_names = {}
            counter = 0
            # filter student
            list_students = list(filter(lambda x: check_match(x), [i for i in reader][1:]))
            self.tableWidget.setRowCount(len(list_students))
            # add keys ( points students )
            for key in list_students:
                index_key = key[0].split(',')
                try:
                    dict_names[int(index_key[-1].replace('"', ''))].append(index_key[1].split())
                except KeyError:
                    dict_names[int(index_key[-1].replace('"', ''))] = [index_key[1].split()]
            # list for 1-st 2-nd 3-rd place
            list_max = [i for i in reversed(sorted(dict_names.keys()))]
            # ascending sort
            for keys in reversed(sorted(dict_names.keys())):
                if len(dict_names.get(keys)) >= 2:
                    for student in reversed(sorted(dict_names.get(keys))):
                        # add last_name
                        self.tableWidget.setItem(counter, 0, QTableWidgetItem(student[-2]))
                        # add number ( points student )
                        self.tableWidget.setItem(counter, 1, QTableWidgetItem(str(keys)))
                        # add login
                        self.tableWidget.setItem(counter, 2, QTableWidgetItem(''.join(student)))
                        self.determine_place(keys, list_max, counter)
                        counter += 1

                else:
                    last_name = ','.join(*dict_names.get(keys)).split(',')[-2]
                    # add last_name
                    self.tableWidget.setItem(counter, 0, QTableWidgetItem(last_name))
                    # add number ( points student )
                    self.tableWidget.setItem(counter, 1, QTableWidgetItem(str(keys)))
                    # add login
                    self.tableWidget.setItem(counter, 2,
                                             QTableWidgetItem(''.join(*dict_names.get(keys))))
                    self.determine_place(keys, list_max, counter)
                    counter += 1

    def record_comboBox(self):
        with open('rez.csv', encoding='UTF-8') as file_csv:
            reader = csv.reader(file_csv, delimiter=';')
            set_numbers_1 = set()
            for i in reader:
                try:
                    numbers = i[0].split(',')[1].replace('"', '').split()
                    set_numbers_1.add(numbers[1])
                except IndexError:
                    pass
            self.comboBox.addItems(list(set_numbers_1))
            self.comboBox_2.addItems(['09', '10', '11'])

    def colorRow(self, row, color):
        for i in range(self.tableWidget.columnCount()):
            self.tableWidget.item(row, i).setBackground(color)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())
