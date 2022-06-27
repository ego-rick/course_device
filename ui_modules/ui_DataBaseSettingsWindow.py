import configparser
import os
import sqlite3
from PyQt5 import QtCore
from PyQt5.QtWidgets import QDialog, QFileDialog
from ui_modules.sampleWindow import SampleDialog
from ui_modules.ui.settings import UiDBSettingsWindow

# класс логики окна настройки базы данных
class DBSettingsWindow(SampleDialog, UiDBSettingsWindow):
    save = QtCore.pyqtSignal()
    # 1.	Инициализатор класса
    def __init__(self, parent=None):
        QDialog.__init__(self)
        self.setupUi(self)
        self.titleWindowLoad()

        self.path = 'config.ini'

        self.config = configparser.ConfigParser()
        self.config.add_section("Database")
        self.config.set("Database", "database", '')
        self.config.set("Database", "path", '')
        self.config.set("Database", "host", '')
        self.config.set("Database", "user", '')
        self.config.set("Database", "password", '')
        self.config.set("Database", "name", '')

        self.groupBox_SQLite.clicked.connect(lambda: self.__setCheck(1))
        self.groupBox_MySQL.clicked.connect(lambda: self.__setCheck(2))
        self.pushButton_save.clicked.connect(self.__writeINI)
        self.pushButton_liteSet.clicked.connect(self.__getPathToFile)
        self.pushButton_liteCreate.clicked.connect(self.__createFile)
    # 2.	Чтение INI-файла
    def readINI(self, update: bool = False):
        if os.path.isfile(self.path) is True:
            self.config.read(self.path)

            database = self.config.get("Database", "database")
            path = self.config.get("Database", "path")
            host = self.config.get("Database", "host")
            user = self.config.get("Database", "user")
            password = self.config.get("Database", "password")
            name = self.config.get("Database", "name")

            if update:
                try:
                    self.__setCheck(int(database))
                except:
                    self.__setCheck()

                self.lineEdit_litePath.setText(path)
                self.lineEdit_myHost.setText(host)
                self.lineEdit_myUser.setText(user)
                self.lineEdit_myPassword.setText(password)
                self.lineEdit_myName.setText(name)

            return [database, path, host, user, password, name]
    # 3.	Запись INI-файла
    def __writeINI(self):
        database = '0'
        if self.groupBox_SQLite.isChecked():
            database = '1'
        elif self.groupBox_MySQL.isChecked():
            database = '2'

        self.config.set("Database", "database", database)
        self.config.set("Database", "path", self.lineEdit_litePath.text())
        self.config.set("Database", "host", self.lineEdit_myHost.text())
        self.config.set("Database", "user", self.lineEdit_myUser.text())
        self.config.set("Database", "password", self.lineEdit_myPassword.text())
        self.config.set("Database", "name", self.lineEdit_myName.text())

        with open(self.path, 'w') as file:
            self.config.write(file)
    # 4.	Предустановка окна
    def __setCheck(self, status: int = 0):
        self.groupBox_SQLite.setChecked(False)
        self.groupBox_MySQL.setChecked(False)

        if status == 1:
            self.groupBox_SQLite.setChecked(True)
        elif status == 2:
            self.groupBox_MySQL.setChecked(True)
    # 5.	Выбор пути к базе данных SQLite
    def __getPathToFile(self):
        dirlist = QFileDialog.getOpenFileName(self, 'Выбрать файл', '', 'SQLite (*.sqlite3)')
        if dirlist[0] != '':
            self.lineEdit_litePath.setText(dirlist[0])
    # 6.	Создание файла базы данных SQLite
    def __createFile(self):
        dirlist = QFileDialog.getSaveFileName(self, 'Создать файл', '', 'SQLite (*.sqlite3)')
        if dirlist[0] != '':
            connection = sqlite3.connect(dirlist[0])
            connection.close()
            self.lineEdit_litePath.setText(dirlist[0])
