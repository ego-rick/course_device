from PyQt5 import QtCore, QtGui, QtWidgets
from .ui_resources import *


class UiAdminWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(585, 349)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(0, 0))
        MainWindow.setMaximumSize(QtCore.QSize(585, 16777215))
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
"#pushButton_print {\n"
"    background-color: rgb(0, 1, 171);\n"
"    font: 9pt \"Flexi IBM VGA False\";\n"
"    color: rgb(255, 255, 255);\n"
"}\n"
"#pushButton_print:pressed  {\n"
"    background-color: rgb(0, 3, 227);\n"
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
"\n"
"/*QPUSHBUTTON*/\n"
"QPushButton, #frame_2 { \n"
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
        self.label_title = QtWidgets.QLabel(self.frame_top)
        self.label_title.setMaximumSize(QtCore.QSize(16777215, 25))
        self.label_title.setAlignment(QtCore.Qt.AlignCenter)
        self.label_title.setObjectName("label_title")
        self.horizontalLayout_2.addWidget(self.label_title)
        self.pushButton_hide = QtWidgets.QPushButton(self.frame_top)
        self.pushButton_hide.setMinimumSize(QtCore.QSize(25, 25))
        self.pushButton_hide.setMaximumSize(QtCore.QSize(25, 25))
        self.pushButton_hide.setObjectName("pushButton_hide")
        self.horizontalLayout_2.addWidget(self.pushButton_hide)
        self.pushButton_close = QtWidgets.QPushButton(self.frame_top)
        self.pushButton_close.setMinimumSize(QtCore.QSize(25, 25))
        self.pushButton_close.setMaximumSize(QtCore.QSize(25, 25))
        self.pushButton_close.setObjectName("pushButton_close")
        self.horizontalLayout_2.addWidget(self.pushButton_close)
        self.verticalLayout_2.addWidget(self.frame_top)
        self.frame_main = QtWidgets.QFrame(self.frame)
        self.frame_main.setObjectName("frame_main")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.frame_main)
        self.verticalLayout_3.setSpacing(11)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setSpacing(11)
        self.gridLayout.setObjectName("gridLayout")
        self.comboBox_numb = QtWidgets.QComboBox(self.frame_main)
        self.comboBox_numb.setMinimumSize(QtCore.QSize(116, 25))
        self.comboBox_numb.setObjectName("comboBox_numb")
        self.gridLayout.addWidget(self.comboBox_numb, 1, 1, 1, 1)
        self.comboBox_type = QtWidgets.QComboBox(self.frame_main)
        self.comboBox_type.setMinimumSize(QtCore.QSize(116, 25))
        self.comboBox_type.setObjectName("comboBox_type")
        self.gridLayout.addWidget(self.comboBox_type, 1, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.frame_main)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 0, 1, 1, 1)
        self.label = QtWidgets.QLabel(self.frame_main)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 1, 3, 1, 1)
        self.pushButton_load = QtWidgets.QPushButton(self.frame_main)
        self.pushButton_load.setMinimumSize(QtCore.QSize(80, 25))
        self.pushButton_load.setObjectName("pushButton_load")
        self.gridLayout.addWidget(self.pushButton_load, 1, 2, 1, 1)
        self.pushButton_exit = QtWidgets.QPushButton(self.frame_main)
        self.pushButton_exit.setMinimumSize(QtCore.QSize(80, 25))
        self.pushButton_exit.setObjectName("pushButton_exit")
        self.gridLayout.addWidget(self.pushButton_exit, 1, 4, 1, 1)
        self.verticalLayout_3.addLayout(self.gridLayout)
        self.line = QtWidgets.QFrame(self.frame_main)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout_3.addWidget(self.line)
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setSpacing(11)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.lineEdit_user = QtWidgets.QLineEdit(self.frame_main)
        self.lineEdit_user.setEnabled(True)
        self.lineEdit_user.setMinimumSize(QtCore.QSize(0, 25))
        self.lineEdit_user.setReadOnly(True)
        self.lineEdit_user.setObjectName("lineEdit_user")
        self.gridLayout_2.addWidget(self.lineEdit_user, 2, 1, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.frame_main)
        self.label_4.setObjectName("label_4")
        self.gridLayout_2.addWidget(self.label_4, 1, 0, 1, 1)
        self.lineEdit_oper = QtWidgets.QLineEdit(self.frame_main)
        self.lineEdit_oper.setEnabled(True)
        self.lineEdit_oper.setMinimumSize(QtCore.QSize(0, 25))
        self.lineEdit_oper.setReadOnly(True)
        self.lineEdit_oper.setObjectName("lineEdit_oper")
        self.gridLayout_2.addWidget(self.lineEdit_oper, 0, 1, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.frame_main)
        self.label_5.setObjectName("label_5")
        self.gridLayout_2.addWidget(self.label_5, 3, 0, 1, 1)
        self.label_7 = QtWidgets.QLabel(self.frame_main)
        self.label_7.setObjectName("label_7")
        self.gridLayout_2.addWidget(self.label_7, 2, 0, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.frame_main)
        self.label_3.setObjectName("label_3")
        self.gridLayout_2.addWidget(self.label_3, 0, 0, 1, 1)
        self.lineEdit_com = QtWidgets.QLineEdit(self.frame_main)
        self.lineEdit_com.setEnabled(True)
        self.lineEdit_com.setMinimumSize(QtCore.QSize(0, 25))
        self.lineEdit_com.setReadOnly(True)
        self.lineEdit_com.setObjectName("lineEdit_com")
        self.gridLayout_2.addWidget(self.lineEdit_com, 1, 1, 1, 1)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setSpacing(11)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.lineEdit_date = QtWidgets.QLineEdit(self.frame_main)
        self.lineEdit_date.setEnabled(True)
        self.lineEdit_date.setMinimumSize(QtCore.QSize(0, 25))
        self.lineEdit_date.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_date.setReadOnly(True)
        self.lineEdit_date.setObjectName("lineEdit_date")
        self.horizontalLayout_3.addWidget(self.lineEdit_date)
        self.label_6 = QtWidgets.QLabel(self.frame_main)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_3.addWidget(self.label_6)
        self.lineEdit_time = QtWidgets.QLineEdit(self.frame_main)
        self.lineEdit_time.setEnabled(True)
        self.lineEdit_time.setMinimumSize(QtCore.QSize(0, 25))
        self.lineEdit_time.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_time.setReadOnly(True)
        self.lineEdit_time.setObjectName("lineEdit_time")
        self.horizontalLayout_3.addWidget(self.lineEdit_time)
        self.gridLayout_2.addLayout(self.horizontalLayout_3, 3, 1, 1, 1)
        self.pushButton_print = QtWidgets.QPushButton(self.frame_main)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_print.sizePolicy().hasHeightForWidth())
        self.pushButton_print.setSizePolicy(sizePolicy)
        self.pushButton_print.setMinimumSize(QtCore.QSize(0, 25))
        self.pushButton_print.setObjectName("pushButton_print")
        self.gridLayout_2.addWidget(self.pushButton_print, 4, 1, 1, 1)
        self.verticalLayout_3.addLayout(self.gridLayout_2)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout_3.addLayout(self.horizontalLayout)
        self.verticalLayout_2.addWidget(self.frame_main)
        self.verticalLayout.addWidget(self.frame)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_title.setText(_translate("MainWindow", "Начальник - отображение операций"))
        self.pushButton_hide.setText(_translate("MainWindow", "_"))
        self.pushButton_close.setText(_translate("MainWindow", "X"))
        self.label_2.setText(_translate("MainWindow", "№ прибора"))
        self.label.setText(_translate("MainWindow", "Тип прибора"))
        self.pushButton_load.setText(_translate("MainWindow", "Загрузить"))
        self.pushButton_exit.setText(_translate("MainWindow", "  Выход  "))
        self.label_4.setText(_translate("MainWindow", "Примечание:"))
        self.label_5.setText(_translate("MainWindow", "Дата:"))
        self.label_7.setText(_translate("MainWindow", "Выполняет:"))
        self.label_3.setText(_translate("MainWindow", "Операция:"))
        self.label_6.setText(_translate("MainWindow", "Время:"))
        self.pushButton_print.setText(_translate("MainWindow", "Отобразить все операции по прибору"))
