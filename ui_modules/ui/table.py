from PyQt5 import QtCore, QtGui, QtWidgets


class UiTableWindow(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(950, 550)
        Dialog.setMinimumSize(QtCore.QSize(950, 550))
        Dialog.setMaximumSize(QtCore.QSize(950, 550))
        Dialog.setStyleSheet("#frame {\n"
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
"QTableView { \n"
"    border-style: groove;\n"
"      border-width: 2px;\n"
"      border-top-color: rgb(120, 120, 120);\n"
"      border-left-color: rgb(120, 120, 120);\n"
"      border-right-color: rgb(200, 200, 200);\n"
"      border-bottom-color: rgb(200, 200, 200);\n"
"}\n"
"QLineEdit:read-only { background-color: rgb(240, 240, 240); }\n"
"\n"
"QTableView::item:selected, QTableView::item:hover {\n"
"    background-color: rgb(0, 1, 171);\n"
"    color: white;\n"
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
        self.verticalLayout = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame = QtWidgets.QFrame(Dialog)
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
        self.pushButton_save = QtWidgets.QPushButton(self.frame_top)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_save.sizePolicy().hasHeightForWidth())
        self.pushButton_save.setSizePolicy(sizePolicy)
        self.pushButton_save.setMinimumSize(QtCore.QSize(25, 25))
        self.pushButton_save.setMaximumSize(QtCore.QSize(25, 16777215))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icon/resources/icon/save.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_save.setIcon(icon)
        self.pushButton_save.setObjectName("pushButton_save")
        self.horizontalLayout_2.addWidget(self.pushButton_save)
        self.label_title = QtWidgets.QLabel(self.frame_top)
        self.label_title.setMaximumSize(QtCore.QSize(16777215, 25))
        self.label_title.setAlignment(QtCore.Qt.AlignCenter)
        self.label_title.setObjectName("label_title")
        self.horizontalLayout_2.addWidget(self.label_title)
        self.pushButton_close = QtWidgets.QPushButton(self.frame_top)
        self.pushButton_close.setMinimumSize(QtCore.QSize(25, 25))
        self.pushButton_close.setMaximumSize(QtCore.QSize(25, 25))
        self.pushButton_close.setObjectName("pushButton_close")
        self.horizontalLayout_2.addWidget(self.pushButton_close)
        self.verticalLayout_2.addWidget(self.frame_top)
        self.frame_main = QtWidgets.QFrame(self.frame)
        self.frame_main.setObjectName("frame_main")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.frame_main)
        self.verticalLayout_3.setContentsMargins(11, 11, 11, 11)
        self.verticalLayout_3.setSpacing(11)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.tableView = QtWidgets.QTableView(self.frame_main)
        self.tableView.setMinimumSize(QtCore.QSize(0, 0))
        self.tableView.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.tableView.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.tableView.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.tableView.setObjectName("tableView")
        self.verticalLayout_3.addWidget(self.tableView)
        self.verticalLayout_2.addWidget(self.frame_main)
        self.verticalLayout.addWidget(self.frame)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label_title.setText(_translate("Dialog", "Инженер - список завершенных операций"))
        self.pushButton_close.setText(_translate("Dialog", "X"))
