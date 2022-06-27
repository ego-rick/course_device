from PyQt5 import QtCore
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent
from PyQt5.QtWidgets import QDialogButtonBox
from ui_modules.sampleWindow import SampleWindow
from ui_modules.ui.login import UiLoginWindow
from ui_modules.ui_DataBaseSettingsWindow import DBSettingsWindow

# класс логики окна авторизаци
class LoginWindow(SampleWindow, UiLoginWindow):
    notification = QtCore.pyqtSignal(str, str, list)
    load = QtCore.pyqtSignal(int)
    # 1.	Инициализатор класса
    def __init__(self, parent=None):
        SampleWindow.__init__(self)
        self.parent = parent
        self.setupUi(self)
        self.titleWindowLoad()

        self.settings = DBSettingsWindow(self)

        self.pushButton_enter.clicked.connect(self.loginAction)
        self.pushButton_database.clicked.connect(self.__showSettings)

        self.player = QMediaPlayer()
        self.sound = QMediaContent(QtCore.QUrl.fromLocalFile('resources/sound/ding.wav'))
        self.player.setMedia(self.sound)
    # 2.	Авторизация
    def loginAction(self):
        dataSQL = self.settings.readINI()

        if dataSQL[0] == '1':
            try:
                self.parent.db.connect(mode=1, path=dataSQL[1])
            except Exception as a:
                self.notification.emit(
                    'Ошибка базы данных',
                    f'Не удаётся подключиться к базе данных\n\n< {a} >', [])
                return 0
        elif dataSQL[0] == '2':
            self.notification.emit('Ошибка', 'Поддержка MySQL не реализованна', [])
            return 0
        else:
            self.notification.emit('Ошибка базы данных', 'Не указана база данных', [])
            return 0

        tables = self.parent.db.checkTable()

        if len(tables) == 0:
            self.notification.emit(
                'Ошибка базы данных',
                'База данных пуста и не имеет таблиц.\n\nСоздать?',
                [QDialogButtonBox.Yes, QDialogButtonBox.No]
            )

            if self.parent.ui_notif.getButtonName() == '&Yes':
                self.parent.db.createTablesSQLite()
        else:
            name = ['account', 'operation', 'device', 'jornal']
            text = 'База данных не имеет следующие таблицы:\n'
            flag = False
            for i in name:
                if i not in tables:
                    flag = True
                    text += f'\n{i}'

            if flag:
                text += '\n\nСоздать?'
                self.notification.emit('Ошибка базы данных', text, [QDialogButtonBox.Yes, QDialogButtonBox.No])

                if self.parent.ui_notif.getButtonName() == '&Yes':
                    self.parent.db.createTablesSQLite()

                return 0

        login = self.lineEdit_login.text()

        if login == '':
            self.notification.emit('Ошибка', 'Введите логин', [])
            return 0

        rec = self.parent.db.getDataCondition('account', ['password', 'status'], [f'login = "{login}"'])

        if len(rec) == 0:
            self.notification.emit('Ошибка', 'Пользователя с таким логином не существует', [])
            return 0

        password = self.lineEdit_password.text()

        if password != rec[0][0]:
            self.notification.emit('Ошибка', 'Неверный пароль', [])
            return 0

        self.parent.login = self.lineEdit_login.text()
        self.player.play()
        self.load.emit(rec[0][1])
    # 3.	Вызов окна настроек подключения к базе данных
    def __showSettings(self):
        self.settings.readINI(update=True)
        self.settings.showWind()
