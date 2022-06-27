from PyQt5 import QtCore
from ui_modules.sampleWindow import SampleWindow
from ui_modules.ui.admin import UiAdminWindow
from ui_modules.ui_ErrWindow import ErrWindow
from ui_modules.ui_TableWindow import TableWindow

# класс логики окна начальника
class AdminWindow(SampleWindow, UiAdminWindow):
    load = QtCore.pyqtSignal(int)
    # 1.	Инициализатор класса
    def __init__(self, parent=None):
        SampleWindow.__init__(self)
        self.parent = parent
        self.setupUi(self)
        self.titleWindowLoad()

        self.id_dev = None
        self.ui_table = TableWindow()
        self.ui_notif = ErrWindow()

        self.pushButton_exit.clicked.connect(lambda: self.load.emit(3))
        self.comboBox_type.currentTextChanged.connect(self.__updateComboBox)
        self.pushButton_load.clicked.connect(self.__updateText)
        self.pushButton_print.clicked.connect(self.__printTable)
    # 2.	Формирование данных и вызова окна таблицы
    def __printTable(self):
        if self.id_dev is None:
            self.ui_notif.setData('Ошибка', 'Загрузите денные по прибору')
            return 0

        data = self.parent.db.getDataCondition(
            'jornal',
            ['id_oper', 'rep_to', 'note', 'executor', 'date', 'time'],
            [f'id_dev = {self.id_dev}']
        )

        for i in range(len(data)):
            if data[i][1] is not None:
                new = self.parent.db.getDataCondition('operation', ['code'], [f'id = {data[i][1]}'])[0]
                data[i] = data[i][:1] + new + data[i][2:]

            new = self.parent.db.getDataCondition('operation', ['code', 'name'], [f'id = {data[i][0]}'])[0]
            data[i] = new + data[i][1:]
            data[i] = [('' if j == 'rep' or j is None else str(j)) for j in data[i]]

        self.ui_table.setData(data)
    # 3.	Получение информации по текущему этапу прибора
    def __updateText(self):
        try:
            self.clearText()
            typeDev = self.comboBox_type.currentText()
            numbDev = self.comboBox_numb.currentText()

            rec = '''
                SELECT id_oper, rep_to, note, executor, date, time, id_dev
                FROM jornal
                WHERE id = (
                    SELECT MAX(id)
                    FROM jornal
                    WHERE id_dev = (
                        SELECT id
                        FROM device
                        WHERE type = "{typeDev}" AND numb = "{numbDev}"
                    )
                );
            '''

            data = self.parent.db.cursor.execute(rec.format(typeDev=typeDev, numbDev=numbDev)).fetchone()

            if data[0] == 1:
                text = self.parent.db.getDataCondition('operation', ['code', 'name'], [f'id = {data[1]}'])[0]
                operText = f'Ремонт. Откат до: {", ".join(text)}'
            else:
                operText = ', '.join(self.parent.db.getDataCondition('operation', ['code', 'name'], [f'id = {data[0]}'])[0])

            self.lineEdit_oper.setText(operText)
            self.lineEdit_com.setText(data[2])
            self.lineEdit_user.setText(data[3])
            self.lineEdit_date.setText(data[4])
            self.lineEdit_time.setText(data[5])
            self.id_dev = data[6]
        except:
            pass
    # 4.	Обновление выпадающего списка с номером прибора
    def __updateComboBox(self, text: str):
        try:
            data = [i[0] for i in self.parent.db.getDataCondition(
                tableName='device',
                objects=['numb'],
                condition=[f'type = "{text}"']
            )]
            self.comboBox_numb.clear()
            self.comboBox_numb.addItems(data)
        except:
            pass
    # 5.	Очистка окна
    def clearText(self):
        self.lineEdit_oper.clear()
        self.lineEdit_com.clear()
        self.lineEdit_user.clear()
        self.lineEdit_date.clear()
        self.lineEdit_time.clear()
    # 6.	Переопределённый дополнительный метод открытия окна
    def showWindAdd(self):
        data = [i[0] for i in self.parent.db.getDataCondition(tableName='device', objects=['type'], distinct=True)]
        self.id_dev = None
        self.comboBox_type.clear()
        self.comboBox_type.addItems(data)
        self.clearText()
