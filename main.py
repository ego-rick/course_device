import sys
from PyQt5 import QtGui
from PyQt5.QtWidgets import QApplication
from ui_modules.dataBase import DataBase
from ui_modules.ui_AdminWindow import AdminWindow
from ui_modules.ui_EngWindow import EngWindow
from ui_modules.ui_EngWorkWindow import EngWorkWindow
from ui_modules.ui_ErrWindow import ErrWindow
from ui_modules.ui_LoginWindow import LoginWindow

# ГЛАВНЫЙ МОДУЛЬ ПРОГРАММЫ
class MainModule:
    # 1.	Инициализатор класса
    def __init__(self):
        self.ui_login = None
        self.ui_eng = None
        self.ui_eng_work = None
        self.ui_admin = None
        self.ui_notif = ErrWindow()
        self.login = None
        self.db = DataBase()
        self.loginWindowShow()
    # 2.	Вызов окна авторизации
    def loginWindowShow(self):
        if self.ui_login is None:
            self.ui_login = LoginWindow(self)
            self.ui_login.notification.connect(self.ui_notif.setData)
            self.ui_login.load.connect(self.load)

        self.ui_login.show()
    # 3.	Логика смены око
    def load(self, status: int, data: list = None):
        ui = [self.ui_login, self.ui_eng, self.ui_eng_work, self.ui_admin]

        for i in ui:
            if i is not None and not i.isHidden():
                i.hide()

        if status == 1: # окно админа
            self.adminAccountWindowLoad()
        elif status == 0: # окно инж - выбор
            self.engAccountWindowLoad()
        elif status == 2: # окно инж - работа
            self.engWorkAccountWindowLoad(data)
        elif status == 3: # окно авторизации
            self.loginWindowShow()
    # 4.	Вызов окна инженера — выбор прибора
    def engAccountWindowLoad(self):
        if self.ui_eng is None:
            self.ui_eng = EngWindow(self)
            self.ui_eng.load.connect(self.load)
        self.ui_eng.showWind()
    # 5.	Вызов окна инженера — работа с прибором
    def engWorkAccountWindowLoad(self, data):
        if self.ui_eng_work is None:
            self.ui_eng_work = EngWorkWindow(self)
            self.ui_eng_work.load.connect(self.load)
        self.ui_eng_work.showWind(data)
    # 6.	Вызов окна начальника
    def adminAccountWindowLoad(self):
        if self.ui_admin is None:
            self.ui_admin = AdminWindow(self)
            self.ui_admin.load.connect(self.load)
        self.ui_admin.showWind()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    QtGui.QFontDatabase.addApplicationFont(':font/resources/font/Flexi_IBM_VGA_False.ttf')
    window = MainModule()
    sys.exit(app.exec())
