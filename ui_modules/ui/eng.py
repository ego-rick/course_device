from PyQt5 import QtCore, QtGui, QtWidgets
from .ui_resources import *


class UiEngWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(450, 318)
        MainWindow.setMinimumSize(QtCore.QSize(450, 240))
        MainWindow.setMaximumSize(QtCore.QSize(450, 550))
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
"QTreeView, QLineEdit { \n"
"    border-style: groove;\n"
"      border-width: 2px;\n"
"      border-top-color: rgb(120, 120, 120);\n"
"      border-left-color: rgb(120, 120, 120);\n"
"      border-right-color: rgb(200, 200, 200);\n"
"      border-bottom-color: rgb(200, 200, 200);\n"
"}\n"
"QLineEdit:read-only { background-color: rgb(240, 240, 240); }\n"
"\n"
"QTreeView::item:selected, QTreeView::item:hover {\n"
"    background-color: rgb(0, 1, 171);\n"
"    color: white;\n"
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
"    image: url(:/icons/resources/icon/downarrow.png);\n"
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
"}\n"
"\n"
"\n"
"QScrollBar:vertical\n"
"{\n"
"    border: none;\n"
"    margin: 21px 0px 21px 0px;\n"
"    background-image: url(:/pattern/resources/pattern/p_1x1_x6.png);\n"
"    background-color: rgb(225, 225, 225);\n"
"}\n"
"QScrollBar::handle:vertical\n"
"{\n"
"    background-color: rgb(240, 240, 240);\n"
"    border-style: groove;\n"
"      border-width: 2px;\n"
"      border-top-color: rgb(200, 200, 200);\n"
"      border-left-color: rgb(200, 200, 200);\n"
"      border-right-color: rgb(100, 100, 100);\n"
"      border-bottom-color: rgb(100, 100, 100);\n"
"}\n"
"QScrollBar::handle:vertical:disabled\n"
"{\n"
"    background-image: url(:/pattern/resources/pattern/p_1x1_x6.png);\n"
"    background-color: rgb(225, 225, 225);\n"
"    border-style: groove;\n"
"      border-width: 2px;\n"
"      border-top: none;\n"
"      border-left: none;\n"
"      border-right: none;\n"
"      border-bottom: none;\n"
"}\n"
"QScrollBar::add-line:vertical\n"
"{\n"
"    image: url(:/icon/resources/icon/downarrow.png);\n"
"    border-style: groove;\n"
"      border-width: 2px;\n"
"      border-top-color: rgb(200, 200, 200);\n"
"      border-left-color: rgb(200, 200, 200);\n"
"      border-right-color: rgb(100, 100, 100);\n"
"      border-bottom-color: rgb(100, 100, 100);\n"
"    background-color: rgb(237, 237, 237);\n"
"\n"
"    subcontrol-position: bottom;\n"
"    subcontrol-origin: margin;\n"
"    width: 17px;\n"
"    height: 17px;\n"
"}\n"
"QScrollBar::sub-line:vertical\n"
"{\n"
"    image: url(:/icon/resources/icon/uparrow.png);\n"
"    border-style: groove;\n"
"      border-width: 2px;\n"
"      border-top-color: rgb(200, 200, 200);\n"
"      border-left-color: rgb(200, 200, 200);\n"
"      border-right-color: rgb(100, 100, 100);\n"
"      border-bottom-color: rgb(100, 100, 100);\n"
"    background-color: rgb(237, 237, 237);\n"
"\n"
"    subcontrol-position: top;\n"
"    subcontrol-origin: margin;\n"
"    width: 17px;\n"
"    height: 17px;\n"
"}\n"
"QScrollBar::sub-line:vertical:pressed\n"
"{\n"
"    border-style: groove;\n"
"      border-width: 2px;\n"
"      border-top-color: rgb(100, 100, 100);\n"
"      border-left-color: rgb(100, 100, 100);\n"
"      border-right-color: rgb(200, 200, 200);\n"
"      border-bottom-color: rgb(200, 200, 200);\n"
"    subcontrol-position: top;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::add-line:vertical:pressed\n"
"{\n"
"    border-style: groove;\n"
"      border-width: 2px;\n"
"      border-top-color: rgb(100, 100, 100);\n"
"      border-left-color: rgb(100, 100, 100);\n"
"      border-right-color: rgb(200, 200, 200);\n"
"      border-bottom-color: rgb(200, 200, 200);\n"
"    subcontrol-position: bottom;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical { background: none; }\n"
"QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical { background: none; }\n"
"\n"
"QScrollBar:horizontal\n"
"{\n"
"    border: none;\n"
"    margin: 0px 21px 0px 21px;\n"
"    background-image: url(:/pattern/resources/pattern/p_1x1_x6.png);\n"
"    background-color: rgb(240, 240, 240);\n"
"}\n"
"QScrollBar::handle:horizontal\n"
"{\n"
"    background-color: rgb(240, 240, 240);\n"
"    border-style: groove;\n"
"      border-width: 2px;\n"
"      border-top-color: rgb(200, 200, 200);\n"
"      border-left-color: rgb(200, 200, 200);\n"
"      border-right-color: rgb(100, 100, 100);\n"
"      border-bottom-color: rgb(100, 100, 100);\n"
"}\n"
"QScrollBar::handle:horizontal:disabled\n"
"{\n"
"    background-image: url(:/pattern/resources/pattern/p_1x1_x6.png);\n"
"    background-color: rgb(240, 240, 240);\n"
"    border-style: groove;\n"
"      border-width: 2px;\n"
"      border-top: none;\n"
"      border-left: none;\n"
"      border-right: none;\n"
"      border-bottom: none;\n"
"}\n"
"QScrollBar::add-line:horizontal\n"
"{\n"
"    image: url(:/icon/resources/icon/rightarrow.png);\n"
"    border-style: groove;\n"
"      border-width: 2px;\n"
"      border-top-color: rgb(200, 200, 200);\n"
"      border-left-color: rgb(200, 200, 200);\n"
"      border-right-color: rgb(100, 100, 100);\n"
"      border-bottom-color: rgb(100, 100, 100);\n"
"    background-color: rgb(237, 237, 237);\n"
"\n"
"    subcontrol-position: right;\n"
"    subcontrol-origin: margin;\n"
"    width: 17px;\n"
"    height: 17px;\n"
"}\n"
"QScrollBar::sub-line:horizontal\n"
"{\n"
"    image: url(:/icon/resources/icon/leftarrow.png);\n"
"    border-style: groove;\n"
"      border-width: 2px;\n"
"      border-top-color: rgb(200, 200, 200);\n"
"      border-left-color: rgb(200, 200, 200);\n"
"      border-right-color: rgb(100, 100, 100);\n"
"      border-bottom-color: rgb(100, 100, 100);\n"
"    background-color: rgb(237, 237, 237);\n"
"\n"
"    subcontrol-position: left;\n"
"    subcontrol-origin: margin;\n"
"    width: 17px;\n"
"    height: 17px;\n"
"}\n"
"QScrollBar::sub-line:horizontal:pressed\n"
"{\n"
"    border-style: groove;\n"
"      border-width: 2px;\n"
"      border-top-color: rgb(100, 100, 100);\n"
"      border-left-color: rgb(100, 100, 100);\n"
"      border-right-color: rgb(200, 200, 200);\n"
"      border-bottom-color: rgb(200, 200, 200);\n"
"    subcontrol-position: left;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::add-line:horizontal:pressed\n"
"{\n"
"    border-style: groove;\n"
"      border-width: 2px;\n"
"      border-top-color: rgb(100, 100, 100);\n"
"      border-left-color: rgb(100, 100, 100);\n"
"      border-right-color: rgb(200, 200, 200);\n"
"      border-bottom-color: rgb(200, 200, 200);\n"
"    subcontrol-position: right;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::up-arrow:horizontal, QScrollBar::down-arrow:horizontal { background: none; }\n"
"QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal { background: none; }")
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
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame_main)
        self.horizontalLayout.setContentsMargins(11, 11, 11, 11)
        self.horizontalLayout.setSpacing(11)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.pushButton_select = QtWidgets.QPushButton(self.frame_main)
        self.pushButton_select.setMinimumSize(QtCore.QSize(0, 25))
        self.pushButton_select.setMaximumSize(QtCore.QSize(16777215, 25))
        self.pushButton_select.setObjectName("pushButton_select")
        self.verticalLayout_4.addWidget(self.pushButton_select)
        self.pushButton_new = QtWidgets.QPushButton(self.frame_main)
        self.pushButton_new.setMinimumSize(QtCore.QSize(0, 25))
        self.pushButton_new.setMaximumSize(QtCore.QSize(16777215, 25))
        self.pushButton_new.setObjectName("pushButton_new")
        self.verticalLayout_4.addWidget(self.pushButton_new)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_4.addItem(spacerItem)
        self.pushButton_exit = QtWidgets.QPushButton(self.frame_main)
        self.pushButton_exit.setMinimumSize(QtCore.QSize(0, 25))
        self.pushButton_exit.setMaximumSize(QtCore.QSize(16777215, 25))
        self.pushButton_exit.setObjectName("pushButton_exit")
        self.verticalLayout_4.addWidget(self.pushButton_exit)
        self.horizontalLayout.addLayout(self.verticalLayout_4)
        self.frame_2 = QtWidgets.QFrame(self.frame_main)
        self.frame_2.setMaximumSize(QtCore.QSize(200, 16777215))
        self.frame_2.setObjectName("frame_2")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.frame_2)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.lineEdit = QtWidgets.QLineEdit(self.frame_2)
        self.lineEdit.setMinimumSize(QtCore.QSize(25, 0))
        self.lineEdit.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.lineEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit.setReadOnly(True)
        self.lineEdit.setObjectName("lineEdit")
        self.verticalLayout_3.addWidget(self.lineEdit)
        self.treeView = QtWidgets.QTreeView(self.frame_2)
        self.treeView.setMinimumSize(QtCore.QSize(0, 0))
        self.treeView.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.treeView.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.treeView.setObjectName("treeView")
        self.verticalLayout_3.addWidget(self.treeView)
        self.horizontalLayout.addWidget(self.frame_2)
        self.verticalLayout_2.addWidget(self.frame_main)
        self.verticalLayout.addWidget(self.frame)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_title.setText(_translate("MainWindow", "Инженер - выбор прибора"))
        self.pushButton_hide.setText(_translate("MainWindow", "_"))
        self.pushButton_close.setText(_translate("MainWindow", "X"))
        self.pushButton_select.setText(_translate("MainWindow", "Выбрать прибор"))
        self.pushButton_new.setText(_translate("MainWindow", "Новый прибор"))
        self.pushButton_exit.setText(_translate("MainWindow", "Выход"))
        self.lineEdit.setText(_translate("MainWindow", "Cписок приборов"))
