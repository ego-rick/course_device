from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QDialogButtonBox
from ui_modules.sampleWindow import SampleWindow
from ui_modules.ui.run_db import UiEngWorkWindow
from ui_modules.ui_ErrWindow import ErrWindow
from ui_modules.ui_TableWindow import TableWindow
import os

# класс логики окна работы с прибором
class EngWorkWindow(SampleWindow, UiEngWorkWindow):
    load = QtCore.pyqtSignal(int)
    # 1.	Инициализатор класса
    def __init__(self, parent=None):
        SampleWindow.__init__(self)
        self.parent = parent
        self.setupUi(self)
        self.titleWindowLoad()

        self.id = None
        self.id_dev = None
        self.repair = None
        self.device = None
        self.id_oper = None
        self.comboName = None
        self.comboBox_repTo.currentIndexChanged.connect(self.__comboBoxUpdate)

        self.ui_notif = ErrWindow()
        self.ui_table = TableWindow()

        self.pushButton_info.clicked.connect(self.__info)
        self.pushButton_exit.clicked.connect(lambda: self.load.emit(3))
        self.pushButton_back.clicked.connect(lambda: self.load.emit(0))

        self.pushButton_save.clicked.connect(self.saveData)
        self.pushButton_operFinish.clicked.connect(self.operFinish)
        self.pushButton_repFinish.clicked.connect(self.operFinish)
        self.pushButton_rep.clicked.connect(self.operRep)
        self.pushButton_print.clicked.connect(self.__printTable)
    # 2.	Формирование данных и вызова окна таблицы
    def __printTable(self):
        if self.id_dev is None:
            self.ui_table.setData('Ошибка', 'Загрузите денные по прибору')
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
    # 3.	Открытие текстового файла с информацией по работе окна
    def __info(self):
        path = r'.\infoEngWork.txt'
        if os.path.isfile(path):
            os.startfile(path)
    # 4.	Вывода информации по прибору
    def printData(self):
        self.__clearData()
        rec = '''
            SELECT id_oper, rep_to, note, executor, date, time, id, id_dev
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

        data = self.parent.db.cursor.execute(rec.format(typeDev=self.device[0], numbDev=self.device[1])).fetchone()

        if data[0] == 1:
            self.__setMode(True)
            self.__comboBoxSet()

            if data[1] is None:
                self.comboBox_repTo.setCurrentText('NULL')
            else:
                self.comboBox_repTo.setCurrentIndex(data[1])
        else:
            operText = self.parent.db.getDataCondition('operation', ['code', 'name'], [f'id = {data[0]}'])[0]
            self.__setMode(False)
            self.lineEdit_operNumb.setText(operText[0])
            self.lineEdit_operText.setText(operText[1])

        self.lineEdit_com.setText(data[2])
        self.lineEdit_user.setText(data[3])
        self.lineEdit_date.setText(data[4])
        self.lineEdit_time.setText(data[5])
        self.id = data[6]
        self.id_dev = data[7]
        self.id_oper = data[0]
    # 5.	Предустановки окна
    def __setMode(self, mode: bool):
        a1 = False if mode else True
        a2 = True if mode else False

        self.repair = mode

        self.lineEdit_operNumb.setEnabled(a1)
        self.lineEdit_operText.setEnabled(a1)
        self.pushButton_operFinish.setEnabled(a1)
        self.pushButton_rep.setEnabled(a1)

        self.comboBox_repTo.setEnabled(a2)
        self.lineEdit_repTo.setEnabled(a2)
        self.pushButton_repFinish.setEnabled(a2)
    # 6.	Обновление выпадающего списка
    def __comboBoxUpdate(self, index):
        try:
            self.lineEdit_repTo.setText(self.comboName[index])
        except:
            pass
    # 6.	Обновление выпадающего списка
    def __comboBoxSet(self):
        data = self.parent.db.getDataCondition('operation', ['code', 'name'])[1:]
        comboBoxData = ['NULL'] + [i[0] for i in data]
        self.comboBox_repTo.addItems(comboBoxData)
        self.comboName = ['Не указано'] + [i[1] for i in data]
    # 7.	Очистка окна
    def __clearData(self):
        self.lineEdit_user.clear()
        self.lineEdit_date.clear()
        self.lineEdit_time.clear()
        self.lineEdit_com.clear()
        self.lineEdit_operNumb.clear()
        self.lineEdit_operText.clear()
        self.comboBox_repTo.clear()
        self.lineEdit_repTo.clear()
    # 8.	Проверка заполняемости полей ввода
    def checkData(self):
        user = self.lineEdit_user.text()
        date = self.lineEdit_date.text()
        time = self.lineEdit_time.text()
        com = self.lineEdit_com.text()

        clearItem = []

        if user == '':
            clearItem.append('"Выполняет"')
        if date == '--':
            clearItem.append('"Дата"')
        if time == '::':
            clearItem.append('"Время"')
        if com == '':
            clearItem.append('"Примечание"')

        if len(clearItem) != 0:
            text = 'Следующие поля не заполнены:\n\n'
            text += '\n'.join(clearItem)
            text += '\n\nПродолжить?'

            self.ui_notif.setData(
                'Внимание!',
                text,
                [QDialogButtonBox.Yes, QDialogButtonBox.No],
                titleWind='Подтверждение'
            )

            if self.ui_notif.getButtonName() == '&Yes':
                return 1

            return 0

        return 1
    # 9.	Сохранение данных
    def saveData(self):
        if self.checkData():
            text = ''
            if self.repair:
                temp = self.comboBox_repTo.currentIndex()
                if temp != 0:
                    text = f', rep_to={temp}'

            rec = '''
                UPDATE jornal
                SET note="{note}", executor="{executor}", date="{date}", time="{time}"{rep}
                WHERE id = {id};
            '''

            self.parent.db.cursor.execute(rec.format(
                id=self.id,
                note=self.lineEdit_com.text() if self.lineEdit_com.text() != '' else '',
                executor=self.lineEdit_user.text() if self.lineEdit_user.text() != '--' else '',
                date=self.lineEdit_date.text() if self.lineEdit_date.text() != '--' else '',
                time=self.lineEdit_time.text() if self.lineEdit_time.text() != '::' else '',
                rep=text
            ))
            self.parent.db.connection.commit()

            return 1

        return 0
    # 10.	Завершение операции ремонта
    def operFinish(self):
        if self.saveData():
            id_oper = self.id_oper + 1
            if self.repair:
                if self.comboBox_repTo.currentIndex() == 0:
                    self.ui_notif.setData(
                        'Ошибка завершения ремонта',
                        'Не указан код отката.'
                    )
                    return 0
                id_oper = self.comboBox_repTo.currentIndex()

            self.parent.db.insertMany('jornal', ['id_dev', 'id_oper'], ['?', '?'], [[self.id_dev, id_oper]])
            self.printData()
    # 11.	Перевод прибора на ремонт
    def operRep(self):
        self.ui_notif.setData(
            'Внимание!',
            'Вы собираетесь перевести прибор на ремонт.\n\nПродолжить?',
            [QDialogButtonBox.Yes, QDialogButtonBox.No],
            titleWind='Подтверждение'
        )

        if self.ui_notif.getButtonName() == '&Yes':
            if self.saveData():
                self.parent.db.insertMany('jornal', ['id_dev', 'id_oper'], ['?', '?'], [[self.id_dev, 1]])
                self.printData()
    # 12.	Переопределение метода открытия окна
    def showWind(self, data: list):
        self.device = data

        frameGm = self.frameGeometry()
        screen = QtWidgets.QApplication.desktop().screenNumber(QtWidgets.QApplication.desktop().cursor().pos())
        centerPoint = QtWidgets.QApplication.desktop().screenGeometry(screen).center()
        frameGm.moveCenter(centerPoint)
        self.move(frameGm.topLeft())

        self.printData()
        self.show()
