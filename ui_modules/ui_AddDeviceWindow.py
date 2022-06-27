from PyQt5 import QtCore
from PyQt5.QtWidgets import QDialog
from ui_modules.sampleWindow import SampleDialog
from ui_modules.ui.create_new_device import UiAddDeviceWindow
from ui_modules.ui_ErrWindow import ErrWindow

# класс логики окна регистрации нового прибора
class AddDeviceWindow(SampleDialog, UiAddDeviceWindow):
    create = QtCore.pyqtSignal(str, str)
    # 1.	Инициализатор класса
    def __init__(self, parent=None):
        QDialog.__init__(self)
        self.setupUi(self)
        self.titleWindowLoad()

        self.ui_notif = ErrWindow()

        self.pushButton_create.clicked.connect(self.__create)
        self.pushButton_cancel.clicked.connect(self.close)
    # 2.	Создание нового прибора
    def __create(self):
        typeDev = self.lineEdit_type.text()

        if typeDev == '':
            self.ui_notif.setData('Ошибка ввода', 'Введите тип аппарата', [])
            return 0

        numbDev = self.lineEdit_number.text()

        if numbDev == '':
            self.ui_notif.setData('Ошибка ввода', 'Введите номер аппарата', [])
            return 0

        self.close()
        self.create.emit(typeDev, numbDev)
    # 3.	Очистка окна
    def clearText(self):
        self.lineEdit_number.clear()
        self.lineEdit_type.clear()
