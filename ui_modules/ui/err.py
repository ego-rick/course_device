from PyQt5 import QtCore, QtGui, QtWidgets
from .ui_resources import *


class UiErrWindow(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(343, 129)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Dialog.sizePolicy().hasHeightForWidth())
        Dialog.setSizePolicy(sizePolicy)
        Dialog.setMinimumSize(QtCore.QSize(343, 0))
        Dialog.setMaximumSize(QtCore.QSize(343, 235))
        Dialog.setStyleSheet("#frame {\n"
"    \n"
"    background-color: rgb(255, 0, 0);\n"
"}\n"
"#frame_main {\n"
"    background-color: rgb(238, 238, 238);\n"
"}\n"
"#label_title {\n"
"    font: 9pt \"Flexi IBM VGA False\";\n"
"    color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QDialogButtonBox::Yes {\n"
"    text: \"Да\";\n"
"}\n"
"QDialogButtonBox > QPushButton {\n"
"    padding-left: 10px;\n"
"    padding-right: 10px;\n"
"    min-height: 21px;\n"
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
        self.verticalLayout = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame = QtWidgets.QFrame(Dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
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
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label = QtWidgets.QLabel(self.frame_main)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setWordWrap(True)
        self.label.setObjectName("label")
        self.verticalLayout_4.addWidget(self.label)
        self.label_2 = QtWidgets.QLabel(self.frame_main)
        self.label_2.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.label_2.setWordWrap(True)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_4.addWidget(self.label_2)
        self.verticalLayout_3.addLayout(self.verticalLayout_4)
        self.buttonBox = QtWidgets.QDialogButtonBox(self.frame_main)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.NoButton)
        self.buttonBox.setCenterButtons(False)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout_3.addWidget(self.buttonBox)
        self.verticalLayout_2.addWidget(self.frame_main)
        self.verticalLayout.addWidget(self.frame)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label_title.setText(_translate("Dialog", "Ошибка"))
        self.pushButton_close.setText(_translate("Dialog", "X"))
        self.label.setText(_translate("Dialog", "Заголовок"))
        self.label_2.setText(_translate("Dialog", "Текст"))
