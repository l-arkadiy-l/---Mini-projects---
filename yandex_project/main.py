import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QMainWindow, QMessageBox, QCalendarWidget
from director_window import Ui_MainWindow
from show_ads import Ui_Form_ads
from title_body import Ui_Form_title_body
from edit import Ui_Edit_Form
import sqlite3

con = sqlite3.connect('dates.db')
data_dates = con.cursor()
try:
    data_dates.execute('''CREATE TABLE dates (
        date text,
        title text,
        message text,
        star text
        )''')
except sqlite3.OperationalError:
    pass


class Edit_Form(QWidget, Ui_Edit_Form):
    def __init__(self, btn, date_id, parent=None):
        parent.hide()
        super(Edit_Form, self).__init__()
        self.setupUi(self)
        self.btn = btn
        con = sqlite3.connect('dates.db')
        cur = con.cursor()
        text = cur.execute(f'''SELECT * FROM dates WHERE rowid = {date_id}''').fetchone()
        # self.lineEdit.setText(text[1])
        self.lineEdit.setText(text[1])
        self.textEdit.setText(text[-2])
        self.pushButton.clicked.connect(lambda: self.update_entry(date_id))

    def update_entry(self, date_id):
        con = sqlite3.connect('dates.db')
        cur = con.cursor()
        cur.execute(
            f'''UPDATE dates SET title = "{self.lineEdit.text()}", message = "{self.textEdit.toPlainText()}"
                WHERE rowid = {date_id}''')
        con.commit()
        cur.execute(f'SELECT * FROM dates WHERE rowid = {date_id}')
        self.btn.setText(self.lineEdit.text())


class Show_title_body(QWidget, Ui_Form_title_body):
    def __init__(self, title, date):
        super(Show_title_body, self).__init__()
        self.setupUi(self)
        self.update()
        # date base
        con = sqlite3.connect('dates.db')
        data_dates = con.cursor()
        self.btn = title
        print(title.text())
        self.id_date = \
        data_dates.execute(f'SELECT rowid FROM dates WHERE title = "{title.text()}" AND date = "{date}"').fetchone()[0]
        data_dates.execute(f'SELECT * FROM dates WHERE title = "{title.text()}" AND date = "{date}"')
        print(self.id_date)
        date_note = data_dates.fetchall()
        for date, title_, message, boolean in date_note:
            if title.text() == title_:
                self.label_title.setText(title.text())
                self.textBrowser.append(message)
            self.message = message
        self.pushButton_pen.clicked.connect(self.edit_entry)

    def edit_entry(self):
        self.edit = Edit_Form(self.btn, self.id_date, self)
        self.edit.show()


class Show_Ads(QWidget, Ui_Form_ads):
    def __init__(self, date):
        super(Show_Ads, self).__init__()
        self.setupUi(self)
        self.setup(date)

    def setup(self, date):

        self.label.setText(f'Заметки за {date}')
        self.pushButton_clear.clicked.connect(lambda: self.delete_date(date))
        # date base
        con = sqlite3.connect('dates.db')
        data_dates = con.cursor()
        data_dates.execute(f'SELECT * FROM dates WHERE date = "{date}" ORDER BY star')
        for date_, title, message, boolean in reversed(data_dates.fetchall()):
            self.btn = QPushButton(title, self)
            if boolean == 'True':
                self.btn.setStyleSheet(
                    'QPushButton{\n	background-color: yellow;\n	border: 1px solid; padding: 5px 0;\n}'
                    'QPushButton:hover{\n	background-color: #DAA520}'
                )
            else:
                self.btn.setStyleSheet(
                    'QPushButton{\n	background-color: white;\n	border: 1px solid; padding: 5px 0;\n}'
                    'QPushButton:hover{\n	background-color: #DCDCDC}'
                )
            self.btn.clicked.connect(lambda: self.show_ads(self.btn, date))
            self.verticalLayout.addWidget(self.btn)

    def show_ads(self, title, date):

        self.show_title_body = Show_title_body(self.sender(), date)
        self.show_title_body.show()

    def delete_date(self, date):
        messagebox = QMessageBox.question(self, 'Delete notes?', 'Вы хотиту удалить все заметки на эту дату?',
                                          QMessageBox.Yes | QMessageBox.No)
        if messagebox == QMessageBox.Yes:
            print('yes')
            con = sqlite3.connect('dates.db')
            data_dates = con.cursor()
            data_dates.execute(f'DELETE from dates WHERE date = "{date}"')
            con.commit()
            # clear vertical layout
            for i in reversed(range(self.verticalLayout.count())):
                self.verticalLayout.itemAt(i).widget().setParent(None)
        self.show()


class Director_Window(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(Director_Window, self).__init__()
        self.setupUi(self)
        self.setWindowTitle('Замтеки на день')
        self.pushButton.clicked.connect(self.create_ad)
        self.pushButton_3.clicked.connect(lambda: self.show_ads(self.calendarWidget.selectedDate().toString()))
        self.pushButton_star.clicked.connect(self.change_color_star)
        self.boolean = 'False'

    def create_ad(self):
        con = sqlite3.connect('dates.db')
        data_dates = con.cursor()
        title = self.lineEdit.text()
        body = self.plainTextEdit.toPlainText()
        date = self.calendarWidget.selectedDate().toString()
        print(self.boolean)
        if not data_dates.execute(
                f'SELECT * FROM dates WHERE date = "{date}" AND title = "{title}"').fetchone() and self.lineEdit.text() \
                and self.plainTextEdit.toPlainText():
            data_dates.execute(f"INSERT INTO dates VALUES ('{date}', '{title}', '{body}', '{self.boolean}')")
            con.commit()
            # clear all
            self.lineEdit.clear()
            self.plainTextEdit.clear()
            self.pushButton_star.setStyleSheet('')
            self.boolean = 'False'
            # change statusbar
            self.statusbar.setStyleSheet('background-color: green;')
            self.statusbar.showMessage('Заметка создана')
        else:
            self.statusbar.setStyleSheet('background-color: red;')
            self.statusbar.showMessage('Такая заметка уже имеется')

    def show_ads(self, date):
        self.ads = Show_Ads(date)
        self.ads.show()

    def change_color_star(self):
        if not self.pushButton_star.styleSheet():
            self.pushButton_star.setStyleSheet(
                'QPushButton{\n	background-color: yellow;\n	border: 1px solid; padding: 0 31px\n}')
            self.boolean = 'True'
        else:
            self.pushButton_star.setStyleSheet('')
            self.boolean = 'False'


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Director_Window()
    ex.show()
    data_dates.close()
    sys.exit(app.exec())
# возможность редактировать заметки
