import sys

from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidgetItem, QWidget
from add_film import Ui_add_film
from qt import Ui_MainWindow
from add_genre import Ui_add_genre
from edit_film import Ui_edit_film
from edit_genre import Ui_edit_genre
import sqlite3


class Create_Movie(QWidget, Ui_add_film):
    def __init__(self, max_id, len_list_all, con, cur, tableWidget):
        super(Create_Movie, self).__init__()
        self.setupUi(self)
        self.max_id = max_id
        self.con = con
        self.cur = cur
        self.tableWidget = tableWidget
        self.len_list_all = len_list_all
        self.initUI()

    def initUI(self):
        self.cur.execute('''SELECT title FROM genres''')
        for i in self.cur.fetchall():
            self.comboBox.addItem(i[0])
        self.pushButton.clicked.connect(lambda: self.add_item(
            self.lineEdit.text(),
            self.lineEdit_2.text(),
            self.comboBox.currentText(),
            self.lineEdit_4.text()
        ))

    def add_item(self, title, year, genre, duration):
        # инициализировать событие для таблицы
        if title and year and genre and duration:
            list_all = [self.max_id + 1,
                        self.lineEdit.text(),
                        self.lineEdit_2.text(),
                        self.comboBox.currentText(),
                        self.lineEdit_4.text()
                        ]
            self.cur.execute(f"INSERT INTO films VALUES ({self.max_id + 1}, '{self.lineEdit.text()}', "
                             f"{int(self.lineEdit_2.text())}, "
                             f"(SELECT id FROM genres WHERE title = '{self.comboBox.currentText()}'), "
                             f"{int(self.lineEdit_4.text())})")
            self.con.commit()
            list_all = self.cur.execute('''SELECT * FROM films''').fetchall()
            self.len_list_all = len(list_all)
            self.tableWidget.setColumnCount(5)
            self.tableWidget.setHorizontalHeaderLabels(
                ['ИД', 'Название фильма', 'Год выпуска', 'Жанр', 'Продолжительность'])
            self.tableWidget.setRowCount(len(list_all))
            for i, row in enumerate(reversed(list_all)):
                for j in range(5):
                    a = row[j]
                    if j == 3:
                        l_a = self.cur.execute(f'''SELECT title FROM genres WHERE id = {a}''').fetchone()
                        self.tableWidget.setItem(i, j, QTableWidgetItem(str(l_a[0])))
                    else:
                        self.tableWidget.setItem(i, j, QTableWidgetItem(str(row[j])))
        else:
            self.label_5.setText('Вы неправильно заполнили поля!')


class ChangeMovie(QWidget, Ui_edit_film):
    def __init__(self, id_movie, table_id, con, cur, tableWidget):
        super(ChangeMovie, self).__init__()
        self.setupUi(self)
        self.id_movie = id_movie
        self.con = con
        self.cur = cur
        self.table_id = table_id
        self.tableWidget = tableWidget
        self.setup()

    def setup(self):
        self.cur.execute('''SELECT title FROM genres''')
        for i in self.cur.fetchall():
            self.comboBox.addItem(i[0])
        result = self.cur.execute(f'''SELECT * FROM films WHERE id = {self.id_movie}''').fetchone()
        self.lineEdit.setText(result[1])
        self.lineEdit_2.setText(str(result[2]))
        self.lineEdit_4.setText(str(result[-1]))
        self.comboBox.setCurrentIndex(result[-2] - 1)
        self.pushButton.clicked.connect(lambda: self.change_movie(
            self.lineEdit.text(),
            int(self.lineEdit_2.text()),
            self.comboBox.currentText(),
            int(self.lineEdit_4.text())
        ))

    def change_movie(self, title, year, genre, duration):
        list_all = [self.id_movie + 1,
                    self.lineEdit.text(),
                    self.lineEdit_2.text(),
                    self.comboBox.currentText(),
                    self.lineEdit_4.text()
                    ]
        r = self.cur.execute(f'''SELECT * FROM films WHERE id = {self.id_movie}''').fetchone()
        self.cur.execute(f"UPDATE films SET title = '{self.lineEdit.text()}', "
                         f"year = {int(year)},"
                         f"genre = (SELECT id FROM genres WHERE title = '{genre}'),"
                         f"duration = {int(duration)} WHERE year = {r[2]} AND title = '{r[1]}'")
        self.con.commit()
        for i in range(5):
            self.tableWidget.setItem(self.table_id, i, QTableWidgetItem(str(list_all[i])))
        self.tableWidget.update()


class Create_Genre(QWidget, Ui_add_genre):
    def __init__(self, len_list_genres, tableWidget_2):
        super(Create_Genre, self).__init__()
        self.setupUi(self)
        self.tableWidget_2 = tableWidget_2
        self.len_list_genres = len_list_genres
        self.pushButton.clicked.connect(self.create_genre)

    def create_genre(self):
        con = sqlite3.connect('films_db.sqlite')
        cur = con.cursor()
        cur.execute(f'''INSERT OR REPLACE INTO genres VALUES ({self.len_list_genres * 2},"{self.lineEdit.text()}")''')
        con.commit()
        list_genres = cur.execute('''SELECT rowid, title FROM genres''').fetchall()
        self.tableWidget_2.setColumnCount(2)
        self.tableWidget_2.setHorizontalHeaderLabels(
            ['ИД', 'Название жанра'])
        self.tableWidget_2.setRowCount(len(list_genres))
        for i, row in enumerate(list_genres):
            for j in range(2):
                self.tableWidget_2.setItem(i, j, QTableWidgetItem(str(row[j])))


class EditGenre(QWidget, Ui_edit_genre):
    def __init__(self, id_genre, table_id, title, tableWidget_2):
        super(EditGenre, self).__init__()
        self.setupUi(self)
        self.id_genre = id_genre
        self.title = title
        self.tableWidget_2 = tableWidget_2
        self.table_id = table_id
        self.lineEdit.setText(title)
        self.pushButton.clicked.connect(self.change_genre)

    def change_genre(self):
        con = sqlite3.connect('films_db.sqlite')
        cur = con.cursor()
        cur.execute(f'''UPDATE genres SET title = "{self.lineEdit.text()}" WHERE id = {self.id_genre}''')
        con.commit()
        list_all = [
            self.id_genre,
            self.lineEdit.text()
        ]
        for i in range(2):
            self.tableWidget_2.setItem(self.table_id, i, QTableWidgetItem(str(list_all[i])))


class Example(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.con = sqlite3.connect('films_db.sqlite')
        self.cur = self.con.cursor()
        self.setupUi(self)
        self.initUI()

    def initUI(self):
        # create table movies
        list_all = self.cur.execute('''SELECT * FROM films''').fetchall()
        self.len_list_all = len(list_all)
        self.tableWidget.setColumnCount(5)
        self.tableWidget.setHorizontalHeaderLabels(
            ['ИД', 'Название фильма', 'Год выпуска', 'Жанр', 'Продолжительность'])
        self.tableWidget.setRowCount(len(list_all))
        for i, row in enumerate(reversed(list_all)):
            for j in range(5):
                a = row[j]
                if j == 3:
                    l_a = self.cur.execute(f'''SELECT title FROM genres WHERE id = {a}''').fetchone()
                    self.tableWidget.setItem(i, j, QTableWidgetItem(str(l_a[0])))
                else:
                    self.tableWidget.setItem(i, j, QTableWidgetItem(str(row[j])))
        # create table genres
        list_genres = self.cur.execute('''SELECT rowid, title FROM genres''').fetchall()
        self.len_list_genres = len(list_genres)
        self.tableWidget_2.setColumnCount(2)
        self.tableWidget_2.setHorizontalHeaderLabels(
            ['ИД', 'Название жанра'])
        self.tableWidget_2.setRowCount(len(list_genres))
        for i, row in enumerate(list_genres):
            for j in range(2):
                self.tableWidget_2.setItem(i, j, QTableWidgetItem(str(row[j])))
        # click btn movies
        self.pushButton_add_film.clicked.connect(self.create_movie)
        self.pushButto_change_film.clicked.connect(self.change_movies)
        self.pushButton_remove_film.clicked.connect(self.delete_movie)
        # click btn genres
        self.pushButton_add_genre.clicked.connect(self.create_genre)
        self.pushButton_edit_genre.clicked.connect(self.edit_genre)
        self.pushButton_remove_genre.clicked.connect(self.delete_genre)

    def create_genre(self):
        self.create = Create_Genre(self.len_list_genres, self.tableWidget_2)
        self.create.show()

    def edit_genre(self):
        self.sender()
        list_all = self.cur.execute('''SELECT * FROM genres''').fetchall()
        for i, row in enumerate(list_all):
            if i == self.tableWidget_2.currentRow():
                id_genre = row[0]
                self.movie = EditGenre(id_genre, i, row[1], self.tableWidget_2)
                self.movie.show()
                break

    def delete_genre(self):
        list_genres = self.cur.execute('''SELECT rowid, title FROM genres''').fetchall()
        for i, row in enumerate(list_genres):
            if i == self.tableWidget_2.currentRow():
                self.cur.execute(f'''DELETE FROM genres WHERE id = {row[0]}''')
                self.cur.execute(f'''DELETE FROM films WHERE genre = {row[0]}''')
                self.con.commit()
                list_genres = self.cur.execute('''SELECT rowid, title FROM genres''').fetchall()
                self.tableWidget_2.setColumnCount(2)
                self.tableWidget_2.setHorizontalHeaderLabels(
                    ['ИД', 'Название жанра'])
                self.tableWidget_2.setRowCount(len(list_genres))
                for i, row in enumerate(list_genres):
                    for j in range(2):
                        print(row)
                        self.tableWidget_2.setItem(i, j, QTableWidgetItem(str(row[j])))
                break

    def create_movie(self):
        list_all = self.cur.execute('''SELECT * FROM films''').fetchall()
        max_id = 0
        for i, row in enumerate(reversed(list_all)):
            max_id = row[0]
            break
        self.movie = Create_Movie(max_id, self.len_list_all, self.con, self.cur, self.tableWidget)
        self.movie.show()

    def change_movies(self):
        self.sender()
        list_all = self.cur.execute('''SELECT * FROM films''').fetchall()
        for i, row in enumerate(reversed(list_all)):
            if i == self.tableWidget.currentRow():
                id_movie = row[0]
                self.movie = ChangeMovie(id_movie, i, self.con, self.cur, self.tableWidget)
                self.movie.show()
                break
        self.update()

    def delete_movie(self):
        self.sender()
        list_all = self.cur.execute('''SELECT * FROM films''').fetchall()
        for i, row in enumerate(reversed(list_all)):
            if i == self.tableWidget.currentRow():
                print(row)
                self.cur.execute(f'''DELETE FROM films WHERE id = {row[0]}''')
                self.con.commit()
                list_all = self.cur.execute('''SELECT * FROM films''').fetchall()
                self.len_list_all = len(list_all)
                self.tableWidget.setColumnCount(5)
                self.tableWidget.setHorizontalHeaderLabels(
                    ['ИД', 'Название фильма', 'Год выпуска', 'Жанр', 'Продолжительность'])
                self.tableWidget.setRowCount(len(list_all))
                for i, row in enumerate(reversed(list_all)):
                    for j in range(5):
                        a = row[j]
                        if j == 3:
                            l_a = self.cur.execute(f'''SELECT title FROM genres WHERE id = {a}''').fetchone()
                            self.tableWidget.setItem(i, j, QTableWidgetItem(str(l_a[0])))
                        else:
                            self.tableWidget.setItem(i, j, QTableWidgetItem(str(row[j])))
                break
        self.update()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())
