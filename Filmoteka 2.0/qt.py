# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'qt.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(660, 577)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.tab)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.pushButton_add_film = QtWidgets.QPushButton(self.tab)
        self.pushButton_add_film.setObjectName("pushButton_add_film")
        self.gridLayout_2.addWidget(self.pushButton_add_film, 0, 0, 1, 1)
        self.pushButton_remove_film = QtWidgets.QPushButton(self.tab)
        self.pushButton_remove_film.setObjectName("pushButton_remove_film")
        self.gridLayout_2.addWidget(self.pushButton_remove_film, 0, 3, 1, 1)
        self.tableWidget = QtWidgets.QTableWidget(self.tab)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.gridLayout_2.addWidget(self.tableWidget, 1, 0, 1, 4)
        self.pushButto_change_film = QtWidgets.QPushButton(self.tab)
        self.pushButto_change_film.setObjectName("pushButto_change_film")
        self.gridLayout_2.addWidget(self.pushButto_change_film, 0, 1, 1, 2)
        self.gridLayout_3.addLayout(self.gridLayout_2, 0, 0, 1, 1)
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.tab_2)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.gridLayout_4 = QtWidgets.QGridLayout()
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.pushButton_add_genre = QtWidgets.QPushButton(self.tab_2)
        self.pushButton_add_genre.setObjectName("pushButton_add_genre")
        self.gridLayout_4.addWidget(self.pushButton_add_genre, 0, 0, 1, 1)
        self.pushButton_remove_genre = QtWidgets.QPushButton(self.tab_2)
        self.pushButton_remove_genre.setObjectName("pushButton_remove_genre")
        self.gridLayout_4.addWidget(self.pushButton_remove_genre, 0, 3, 1, 1)
        self.tableWidget_2 = QtWidgets.QTableWidget(self.tab_2)
        self.tableWidget_2.setObjectName("tableWidget_2")
        self.tableWidget_2.setColumnCount(0)
        self.tableWidget_2.setRowCount(0)
        self.gridLayout_4.addWidget(self.tableWidget_2, 1, 0, 1, 4)
        self.pushButton_edit_genre = QtWidgets.QPushButton(self.tab_2)
        self.pushButton_edit_genre.setObjectName("pushButton_edit_genre")
        self.gridLayout_4.addWidget(self.pushButton_edit_genre, 0, 1, 1, 2)
        self.gridLayout_5.addLayout(self.gridLayout_4, 0, 0, 1, 1)
        self.tabWidget.addTab(self.tab_2, "")
        self.gridLayout.addWidget(self.tabWidget, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 660, 26))
        self.menubar.setObjectName("menubar")
        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setObjectName("menu")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar.addAction(self.menu.menuAction())

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton_add_film.setText(_translate("MainWindow", "Добавить фильм"))
        self.pushButton_remove_film.setText(_translate("MainWindow", "Удалить фильм"))
        self.pushButto_change_film.setText(_translate("MainWindow", "Изменить фильм"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Tab 1"))
        self.pushButton_add_genre.setText(_translate("MainWindow", "Добавить жанр"))
        self.pushButton_remove_genre.setText(_translate("MainWindow", "Удалить жанр"))
        self.pushButton_edit_genre.setText(_translate("MainWindow", "Редактировать жанр"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Tab 2"))
        self.menu.setTitle(_translate("MainWindow", "Файл"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
