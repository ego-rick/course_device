from PyQt5 import QtCore, QtGui, QtWidgets
from .ui_resources import *


class UiLoginWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(343, 235)
        MainWindow.setMinimumSize(QtCore.QSize(0, 0))
        MainWindow.setMaximumSize(QtCore.QSize(343, 235))
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
"QLineEdit:read-only { background-color: rgb(240, 240, 240); }\n"
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
        self.verticalLayout_3.setContentsMargins(30, 30, 30, 30)
        self.verticalLayout_3.setSpacing(11)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setSpacing(11)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(self.frame_main)
        self.label.setMinimumSize(QtCore.QSize(0, 25))
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.frame_main)
        self.label_2.setMinimumSize(QtCore.QSize(0, 25))
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.lineEdit_login = QtWidgets.QLineEdit(self.frame_main)
        self.lineEdit_login.setMinimumSize(QtCore.QSize(190, 25))
        self.lineEdit_login.setObjectName("lineEdit_login")
        self.gridLayout.addWidget(self.lineEdit_login, 0, 1, 1, 1)
        self.lineEdit_password = QtWidgets.QLineEdit(self.frame_main)
        self.lineEdit_password.setMinimumSize(QtCore.QSize(0, 25))
        self.lineEdit_password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_password.setObjectName("lineEdit_password")
        self.gridLayout.addWidget(self.lineEdit_password, 1, 1, 1, 1)
        self.verticalLayout_3.addLayout(self.gridLayout)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton_enter = QtWidgets.QPushButton(self.frame_main)
        self.pushButton_enter.setMinimumSize(QtCore.QSize(0, 25))
        self.pushButton_enter.setObjectName("pushButton_enter")
        self.horizontalLayout.addWidget(self.pushButton_enter)
        self.pushButton_database = QtWidgets.QPushButton(self.frame_main)
        self.pushButton_database.setMinimumSize(QtCore.QSize(0, 25))
        self.pushButton_database.setObjectName("pushButton_database")
        self.horizontalLayout.addWidget(self.pushButton_database)
        self.verticalLayout_3.addLayout(self.horizontalLayout)
        self.verticalLayout_2.addWidget(self.frame_main)
        self.label_3 = QtWidgets.QLabel(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        self.label_3.setText("")
        self.label_3.setPixmap(QtGui.QPixmap(":/icon/resources/icon/logo.png"))
        self.label_3.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_2.addWidget(self.label_3)
        self.verticalLayout.addWidget(self.frame)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_title.setText(_translate("MainWindow", "Авторизация"))
        self.pushButton_hide.setText(_translate("MainWindow", "_"))
        self.pushButton_close.setText(_translate("MainWindow", "X"))
        self.label.setText(_translate("MainWindow", "Логин:"))
        self.label_2.setText(_translate("MainWindow", "Пароль:"))
        self.pushButton_enter.setText(_translate("MainWindow", "Enter"))
        self.pushButton_database.setText(_translate("MainWindow", "Database"))
