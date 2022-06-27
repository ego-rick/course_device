from PyQt5 import QtCore, QtGui, QtWidgets
from .ui_resources import *


class UiEngWorkWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 305)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(800, 305))
        MainWindow.setMaximumSize(QtCore.QSize(800, 305))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet("#frame {\n"
"    background-color: rgb(0, 1, 171);\n"
"}\n"
"#frame_main {\n"
"    background-color: rgb(238, 238, 238);\n"
"}\n"
"#label_title {\n"
"    font: 9pt \"Flexi IBM VGA False\";\n"
"    color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QListView, QLineEdit { \n"
"    border-style: groove;\n"
"      border-width: 2px;\n"
"      border-top-color: rgb(120, 120, 120);\n"
"      border-left-color: rgb(120, 120, 120);\n"
"      border-right-color: rgb(200, 200, 200);\n"
"      border-bottom-color: rgb(200, 200, 200);\n"
"}\n"
"QLineEdit:!enabled { background-color: rgb(240, 240, 240); }\n"
"\n"
"/*QCOMBOBOX*/\n"
"QComboBox { \n"
"    border-style: groove;\n"
"      border-width: 2px;\n"
"      border-top-color: rgb(120, 120, 120);\n"
"      border-left-color: rgb(120, 120, 120);\n"
"      border-right-color: rgb(200, 200, 200);\n"
"      border-bottom-color: rgb(200, 200, 200);\n"
"}\n"
"QComboBox::drop-down {\n"
"    border-style: groove;\n"
"      border-width: 2px;\n"
"      border-top-color: rgb(200, 200, 200);\n"
"      border-left-color: rgb(200, 200, 200);\n"
"      border-right-color: rgb(100, 100, 100);\n"
"      border-bottom-color: rgb(100, 100, 100);\n"
"    background-color: rgb(238, 238, 238);\n"
"    image: url(:/icon/resources/icon/downarrow.png);\n"
"}\n"
"QComboBox::drop-down:pressed {\n"
"    border-style: groove;\n"
"      border-width: 2px;\n"
"      border-top-color: rgb(100, 100, 100);\n"
"      border-left-color: rgb(100, 100, 100);\n"
"      border-right-color: rgb(200, 200, 200);\n"
"      border-bottom-color: rgb(200, 200, 200);\n"
"}\n"
"QComboBox QAbstractItemView {\n"
"    selection-background-color: rgb(240, 240, 240);\n"
"    selection-color: rgb(1, 1, 1);\n"
"}\n"
"QComboBox:!enabled { background-color: rgb(240, 240, 240); }\n"
"\n"
"/*QPUSHBUTTON*/\n"
"QPushButton { \n"
"    border-style: groove;\n"
"      border-width: 2px;\n"
"      border-top-color: rgb(200, 200, 200);\n"
"      border-left-color: rgb(200, 200, 200);\n"
"      border-right-color: rgb(100, 100, 100);\n"
"      border-bottom-color: rgb(100, 100, 100);\n"
"    background-color: rgb(238, 238, 238); \n"
"}\n"
"QPushButton:pressed { \n"
"    background-color: rgb(249, 249, 249);\n"
"    border-style: groove;\n"
"      border-width: 2px;\n"
"      border-top-color: rgb(100, 100, 100);\n"
"      border-left-color: rgb(100, 100, 100);\n"
"      border-right-color: rgb(200, 200, 200);\n"
"      border-bottom-color: rgb(200, 200, 200);\n"
"}")
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setObjectName("frame")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout_2.setContentsMargins(5, 5, 5, 5)
        self.verticalLayout_2.setSpacing(5)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.frame_top = QtWidgets.QFrame(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_top.sizePolicy().hasHeightForWidth())
        self.frame_top.setSizePolicy(sizePolicy)
        self.frame_top.setObjectName("frame_top")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frame_top)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.pushButton_info = QtWidgets.QPushButton(self.frame_top)
        self.pushButton_info.setMinimumSize(QtCore.QSize(25, 25))
        self.pushButton_info.setMaximumSize(QtCore.QSize(25, 25))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        self.pushButton_info.setFont(font)
        self.pushButton_info.setObjectName("pushButton_info")
        self.horizontalLayout_2.addWidget(self.pushButton_info)
        self.label_title = QtWidgets.QLabel(self.frame_top)
        self.label_title.setMaximumSize(QtCore.QSize(16777215, 25))
        self.label_title.setAlignment(QtCore.Qt.AlignCenter)
        self.label_title.setObjectName("label_title")
        self.horizontalLayout_2.addWidget(self.label_title)
        self.pushButton_hide = QtWidgets.QPushButton(self.frame_top)
        self.pushButton_hide.setMinimumSize(QtCore.QSize(25, 25))
        self.pushButton_hide.setMaximumSize(QtCore.QSize(25, 25))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        self.pushButton_hide.setFont(font)
        self.pushButton_hide.setObjectName("pushButton_hide")
        self.horizontalLayout_2.addWidget(self.pushButton_hide)
        self.pushButton_close = QtWidgets.QPushButton(self.frame_top)
        self.pushButton_close.setMinimumSize(QtCore.QSize(25, 25))
        self.pushButton_close.setMaximumSize(QtCore.QSize(25, 25))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        self.pushButton_close.setFont(font)
        self.pushButton_close.setObjectName("pushButton_close")
        self.horizontalLayout_2.addWidget(self.pushButton_close)
        self.verticalLayout_2.addWidget(self.frame_top)
        self.frame_main = QtWidgets.QFrame(self.frame)
        self.frame_main.setObjectName("frame_main")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.frame_main)
        self.verticalLayout_3.setContentsMargins(11, 11, 11, 11)
        self.verticalLayout_3.setSpacing(11)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setSpacing(11)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setSpacing(11)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.lineEdit_user = QtWidgets.QLineEdit(self.frame_main)
        self.lineEdit_user.setMinimumSize(QtCore.QSize(0, 25))
        self.lineEdit_user.setObjectName("lineEdit_user")
        self.horizontalLayout_5.addWidget(self.lineEdit_user)
        self.label_5 = QtWidgets.QLabel(self.frame_main)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_5.addWidget(self.label_5)
        self.lineEdit_date = QtWidgets.QLineEdit(self.frame_main)
        self.lineEdit_date.setMinimumSize(QtCore.QSize(0, 25))
        self.lineEdit_date.setInputMask("00-00-0000")
        self.lineEdit_date.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_date.setObjectName("lineEdit_date")
        self.horizontalLayout_5.addWidget(self.lineEdit_date)
        self.label_2 = QtWidgets.QLabel(self.frame_main)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_5.addWidget(self.label_2)
        self.lineEdit_time = QtWidgets.QLineEdit(self.frame_main)
        self.lineEdit_time.setMinimumSize(QtCore.QSize(0, 25))
        self.lineEdit_time.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_time.setObjectName("lineEdit_time")
        self.horizontalLayout_5.addWidget(self.lineEdit_time)
        self.gridLayout_2.addLayout(self.horizontalLayout_5, 0, 1, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.frame_main)
        self.label_4.setObjectName("label_4")
        self.gridLayout_2.addWidget(self.label_4, 0, 0, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.frame_main)
        self.label_3.setObjectName("label_3")
        self.gridLayout_2.addWidget(self.label_3, 1, 0, 1, 1)
        self.lineEdit_com = QtWidgets.QLineEdit(self.frame_main)
        self.lineEdit_com.setMinimumSize(QtCore.QSize(0, 25))
        self.lineEdit_com.setObjectName("lineEdit_com")
        self.gridLayout_2.addWidget(self.lineEdit_com, 1, 1, 1, 1)
        self.verticalLayout_3.addLayout(self.gridLayout_2)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setSpacing(11)
        self.gridLayout.setObjectName("gridLayout")
        self.pushButton_repFinish = QtWidgets.QPushButton(self.frame_main)
        self.pushButton_repFinish.setEnabled(False)
        self.pushButton_repFinish.setMinimumSize(QtCore.QSize(90, 25))
        self.pushButton_repFinish.setObjectName("pushButton_repFinish")
        self.gridLayout.addWidget(self.pushButton_repFinish, 1, 4, 1, 1)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setContentsMargins(0, -1, -1, -1)
        self.horizontalLayout_4.setSpacing(11)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.comboBox_repTo = QtWidgets.QComboBox(self.frame_main)
        self.comboBox_repTo.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboBox_repTo.sizePolicy().hasHeightForWidth())
        self.comboBox_repTo.setSizePolicy(sizePolicy)
        self.comboBox_repTo.setMinimumSize(QtCore.QSize(90, 25))
        self.comboBox_repTo.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.comboBox_repTo.setEditable(False)
        self.comboBox_repTo.setCurrentText("")
        self.comboBox_repTo.setObjectName("comboBox_repTo")
        self.horizontalLayout_4.addWidget(self.comboBox_repTo)
        self.lineEdit_repTo = QtWidgets.QLineEdit(self.frame_main)
        self.lineEdit_repTo.setEnabled(False)
        self.lineEdit_repTo.setMinimumSize(QtCore.QSize(0, 25))
        self.lineEdit_repTo.setReadOnly(True)
        self.lineEdit_repTo.setObjectName("lineEdit_repTo")
        self.horizontalLayout_4.addWidget(self.lineEdit_repTo)
        self.gridLayout.addLayout(self.horizontalLayout_4, 1, 2, 1, 1)
        self.pushButton_operFinish = QtWidgets.QPushButton(self.frame_main)
        self.pushButton_operFinish.setEnabled(True)
        self.pushButton_operFinish.setMinimumSize(QtCore.QSize(90, 25))
        self.pushButton_operFinish.setObjectName("pushButton_operFinish")
        self.gridLayout.addWidget(self.pushButton_operFinish, 0, 4, 1, 1)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setContentsMargins(0, -1, -1, -1)
        self.horizontalLayout_3.setSpacing(11)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.lineEdit_operNumb = QtWidgets.QLineEdit(self.frame_main)
        self.lineEdit_operNumb.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_operNumb.sizePolicy().hasHeightForWidth())
        self.lineEdit_operNumb.setSizePolicy(sizePolicy)
        self.lineEdit_operNumb.setMinimumSize(QtCore.QSize(90, 25))
        self.lineEdit_operNumb.setMaximumSize(QtCore.QSize(90, 16777215))
        self.lineEdit_operNumb.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_operNumb.setReadOnly(True)
        self.lineEdit_operNumb.setObjectName("lineEdit_operNumb")
        self.horizontalLayout_3.addWidget(self.lineEdit_operNumb)
        self.lineEdit_operText = QtWidgets.QLineEdit(self.frame_main)
        self.lineEdit_operText.setEnabled(True)
        self.lineEdit_operText.setMinimumSize(QtCore.QSize(0, 25))
        self.lineEdit_operText.setReadOnly(True)
        self.lineEdit_operText.setObjectName("lineEdit_operText")
        self.horizontalLayout_3.addWidget(self.lineEdit_operText)
        self.gridLayout.addLayout(self.horizontalLayout_3, 0, 2, 1, 1)
        self.label = QtWidgets.QLabel(self.frame_main)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.pushButton_rep = QtWidgets.QPushButton(self.frame_main)
        self.pushButton_rep.setMinimumSize(QtCore.QSize(0, 25))
        self.pushButton_rep.setObjectName("pushButton_rep")
        self.gridLayout.addWidget(self.pushButton_rep, 1, 0, 1, 1)
        self.verticalLayout_3.addLayout(self.gridLayout)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setSpacing(11)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton_print = QtWidgets.QPushButton(self.frame_main)
        self.pushButton_print.setMinimumSize(QtCore.QSize(124, 65))
        self.pushButton_print.setObjectName("pushButton_print")
        self.horizontalLayout.addWidget(self.pushButton_print)
        self.pushButton_save = QtWidgets.QPushButton(self.frame_main)
        self.pushButton_save.setMinimumSize(QtCore.QSize(0, 65))
        self.pushButton_save.setObjectName("pushButton_save")
        self.horizontalLayout.addWidget(self.pushButton_save)
        self.pushButton_back = QtWidgets.QPushButton(self.frame_main)
        self.pushButton_back.setMinimumSize(QtCore.QSize(124, 65))
        self.pushButton_back.setObjectName("pushButton_back")
        self.horizontalLayout.addWidget(self.pushButton_back)
        self.pushButton_exit = QtWidgets.QPushButton(self.frame_main)
        self.pushButton_exit.setMinimumSize(QtCore.QSize(124, 65))
        self.pushButton_exit.setObjectName("pushButton_exit")
        self.horizontalLayout.addWidget(self.pushButton_exit)
        self.verticalLayout_3.addLayout(self.horizontalLayout)
        self.verticalLayout_2.addWidget(self.frame_main)
        self.verticalLayout.addWidget(self.frame)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.comboBox_repTo.setCurrentIndex(-1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton_info.setText(_translate("MainWindow", "?"))
        self.label_title.setText(_translate("MainWindow", "Инженер - работа с базой данных"))
        self.pushButton_hide.setText(_translate("MainWindow", "_"))
        self.pushButton_close.setText(_translate("MainWindow", "X"))
        self.lineEdit_user.setPlaceholderText(_translate("MainWindow", "Ввод исполнителя..."))
        self.label_5.setText(_translate("MainWindow", "Дата:"))
        self.lineEdit_date.setToolTip(_translate("MainWindow", "ДД-ММ-ГГГГ"))
        self.label_2.setText(_translate("MainWindow", "Время:"))
        self.lineEdit_time.setToolTip(_translate("MainWindow", "ЧЧ-ММ-СС"))
        self.lineEdit_time.setInputMask(_translate("MainWindow", "00:00:00"))
        self.label_4.setText(_translate("MainWindow", "Выполняет:"))
        self.label_3.setText(_translate("MainWindow", "Примечание:"))
        self.lineEdit_com.setPlaceholderText(_translate("MainWindow", "Ввод примечания..."))
        self.pushButton_repFinish.setText(_translate("MainWindow", "Завершить"))
        self.pushButton_operFinish.setText(_translate("MainWindow", "Завершить"))
        self.label.setText(_translate("MainWindow", "Текущая операция:"))
        self.pushButton_rep.setText(_translate("MainWindow", "Ремонт"))
        self.pushButton_print.setText(_translate("MainWindow", "Вывести список\n"
"завершенных\n"
"операций"))
        self.pushButton_save.setText(_translate("MainWindow", "Сохранить данные"))
        self.pushButton_back.setText(_translate("MainWindow", "Назад"))
        self.pushButton_exit.setText(_translate("MainWindow", "Выход"))
