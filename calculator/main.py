#!/usr/bin/env python3

# -*- coding: utf-8 -*-

import sys

from PyQt5.QtWidgets import QWidget, QApplication, QPushButton, QMainWindow

from PyQt5.QtWidgets import QInputDialog, QColorDialog

from PyQt5.QtWidgets import QLineEdit, QLabel
from qt import Ui_MainWindow


class Example(QMainWindow, Ui_MainWindow):

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setup()
        self.number_print = 0
        self.number = ''
        self.operation = ''

    def setup(self):
        # buttons 0 ... 9
        self.pushButton_n0.clicked.connect(lambda: self.definition_number(self.pushButton_n0.text()))
        self.pushButton_n1.clicked.connect(lambda: self.definition_number(self.pushButton_n1.text()))
        self.pushButton_n2.clicked.connect(lambda: self.definition_number(self.pushButton_n2.text()))
        self.pushButton_n3.clicked.connect(lambda: self.definition_number(self.pushButton_n3.text()))
        self.pushButton_n4.clicked.connect(lambda: self.definition_number(self.pushButton_n4.text()))
        self.pushButton_n5.clicked.connect(lambda: self.definition_number(self.pushButton_n5.text()))
        self.pushButton_n6.clicked.connect(lambda: self.definition_number(self.pushButton_n6.text()))
        self.pushButton_n7.clicked.connect(lambda: self.definition_number(self.pushButton_n7.text()))
        self.pushButton_n8.clicked.connect(lambda: self.definition_number(self.pushButton_n8.text()))
        self.pushButton_n9.clicked.connect(lambda: self.definition_number(self.pushButton_n9.text()))
        self.pushButton_2.clicked.connect(lambda: self.definition_number(self.pushButton_2.text()))
        # CE
        self.pushButton.clicked.connect(self.clean_number)
        # C
        self.pushButton_3.clicked.connect(self.clean_all)
        # + - = *
        self.pushButton_add.clicked.connect(lambda: self.operation_with_numbers(self.pushButton_add.text()))
        self.pushButton_eq.clicked.connect(lambda: self.operation_with_numbers(self.pushButton_eq.text()))
        self.pushButton_mul.clicked.connect(lambda: self.operation_with_numbers(self.pushButton_mul.text()))
        self.pushButton_sub.clicked.connect(lambda: self.operation_with_numbers(self.pushButton_sub.text()))
        self.pushButton_div.clicked.connect(lambda: self.operation_with_numbers(self.pushButton_div.text()))
        self.pushButton_pc.clicked.connect(self.change_symbol)

    def float_or_not(self, number):
        print(number.split('.'), self.number_print)
        if number.split('.')[0] == number:
            return int(number)
        return float(number)

    def definition_number(self, number):
        self.number += number
        self.lcdNumber.display(self.number)

    def clean_number(self):
        self.number = ''
        self.lcdNumber.display(0)

    def clean_all(self):
        self.number_print = 0
        self.clean_number()

    def operation_with_numbers(self, operation):
        if operation != '=':
            self.operation = operation
        try:
            if self.operation == '+' or self.number_print == 0:
                self.number_print += float(self.number)
            elif self.operation == 'x':
                self.number_print *= float(self.number)
            elif self.operation == '÷':
                self.number_print /= float(self.number)
            elif self.operation == '-':
                self.number_print -= float(self.number)
            self.label.setText('{} {}'.format(self.number_print, self.operation))
        except Exception:
            self.label.setText('{} {}'.format(self.number_print, self.operation))
        self.number = ''

        if operation == '=':
            self.lcdNumber.display(self.number_print)
            self.label.setText('')

    def change_symbol(self):
        if not self.number:
            self.number_print *= -1
            self.lcdNumber.display(self.number_print)
        else:
            self.number = str(self.float_or_not(self.number) * -1)
            self.lcdNumber.display(self.number)


if __name__ == '__main__':
    app = QApplication(sys.argv)

    ex = Example()
    ex.show()
    sys.exit(app.exec_())
