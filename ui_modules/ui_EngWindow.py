import datetime
from PyQt5 import QtGui, QtCore
from PyQt5.QtWidgets import QAbstractItemView
from ui_modules.sampleWindow import SampleWindow
from ui_modules.ui.eng import UiEngWindow
from ui_modules.ui_AddDeviceWindow import AddDeviceWindow
from ui_modules.ui_ErrWindow import ErrWindow

# класс логики окна выбора прибора
class EngWindow(SampleWindow, UiEngWindow):
    load = QtCore.pyqtSignal(int, list)
    # 1.	Инициализатор класса
    def __init__(self, parent=None):
        SampleWindow.__init__(self)
        self.parent = parent
        self.setupUi(self)
        self.titleWindowLoad()

        self.ui_notif = ErrWindow()

        self.tableData = []

        self.model = QtGui.QStandardItemModel()
        self.treeView.setModel(self.model)
        self.treeView.setRootIsDecorated(False)
        self.treeView.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.treeView.clicked.connect(self.setData)

        self.addWindow = AddDeviceWindow(self)
        self.addWindow.create.connect(self.__createDevice)

        self.pushButton_new.clicked.connect(self.addWindow.showWind)
        self.pushButton_select.clicked.connect(self.selectDevice)
        self.pushButton_exit.clicked.connect(lambda: self.load.emit(3, []))
    # 2.	Заполнение таблицы с приборами
    def setData(self, index):
        row = index.row()
        self.tableData = [
            self.model.item(row, 0).data(QtCore.Qt.EditRole),
            self.model.item(row, 1).data(QtCore.Qt.EditRole)
        ]
    # 3.	Выбор прибора
    def selectDevice(self):
        if len(self.tableData) == 0:
            self.ui_notif.setData('Ошибка выбора', 'Прибор не выбран')
            return 0

        self.load.emit(2, self.tableData)
    # 4.	Вызов окна создания нового прибора
    def __createDevice(self, typeDev: str, numbDev: str):
        id = self.parent.db.getDataCondition('device', ['id'], [f'type = "{typeDev}"', f'numb = "{numbDev}"'])

        if len(id) == 0:
            self.addWindow.clearText()
            try:
                self.parent.db.insertMany(
                    'device',
                    ['type', 'numb'],
                    ['?', '?'],
                    [[typeDev, numbDev]]
                )
            except Exception as a:
                self.ui_notif.setData('Ошибка создания', f'{a}')
                return 0

            id = self.parent.db.getDataCondition('device', ['id'], [f'type = "{typeDev}"', f'numb = "{numbDev}"'])[0][0]


            date = datetime.datetime.today()
            time = date.strftime('%H:%M:%S')
            date = date.strftime("%d-%m-%Y")

            self.parent.db.insertMany(
                'jornal',
                ['id_dev', 'note', 'date', 'time'],
                ['?', '?', '?', '?'],
                [[id, f'Регистрация', date, time]]
            )

            self.__printListView()
        else:
            self.ui_notif.setData('Ошибка создания', 'Прибор с такими параметрами уже имеется')
    # 5.	Декоратор таблицы с приборами
    def showWindAdd(self):
        self.__printListView()
        self.tableData.clear()
    # 6.	Переопределённый дополнительный метод открытия окна
    def __printListView(self):
        data = self.parent.db.getDataCondition('device', ['type', 'numb'])
        self.model.clear()
        self.model.setHorizontalHeaderLabels(['Тип', '№'])

        for i in data:
            item1 = QtGui.QStandardItem(i[0])
            item2 = QtGui.QStandardItem(i[1])
            self.model.appendRow([item1, item2])
        self.treeView.resizeColumnToContents(0)
        self.treeView.resizeColumnToContents(1)

