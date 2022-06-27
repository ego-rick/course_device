from PyQt5 import QtCore, QtWidgets, QtGui

# Базовый класс окон
class SampleMain:
    # Инициализация класса
    def __init__(self):
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.setWindowIcon(QtGui.QIcon(":/icon/resources/icon/main_ico.png"))
    # Преопределение тайтлбара
    def titleWindowLoad(self):
        def windowMove(event):
            try:
                if QtCore.Qt.LeftButton:
                    self.move(event.globalPos() - self.movePosition)
                    event.accept()
            except:
                pass

        def windowMovePress(event):
            try:
                if event.button() == QtCore.Qt.LeftButton:
                    self.moveFlag = True
                    self.movePosition = event.globalPos() - self.pos()
                    event.accept()
            except:
                pass

        def windowMoveRelease(event):
            self.moveFlag = False

        self.label_title.mouseMoveEvent = windowMove
        self.label_title.mousePressEvent = windowMovePress
        self.label_title.mouseReleaseEvent = windowMoveRelease

        self.shadow = QtWidgets.QGraphicsDropShadowEffect(self)
        self.shadow.setBlurRadius(0)
        self.shadow.setXOffset(5)
        self.shadow.setYOffset(5)
        self.shadow.setColor(QtGui.QColor(0, 0, 0, 150))
        self.frame.setGraphicsEffect(self.shadow)

        self.pushButton_close.clicked.connect(self.close)

        try:
            self.pushButton_hide.clicked.connect(self.showMinimized)
        except:
            pass

        self.setWindowTitle(self.label_title.text())

# Шаблон диалогового окна
class SampleDialog(QtWidgets.QDialog, SampleMain):
    # Инициализация класса
    def __init__(self):
        QtWidgets.QDialog.__init__(self)
    # Функция отображения окна
    def showWind(self):
        qtRectangle = self.frameGeometry()
        centerPoint = QtWidgets.QDesktopWidget().availableGeometry().center()
        qtRectangle.moveCenter(centerPoint)
        self.move(qtRectangle.topLeft())
        self.exec()


class SampleWindow(QtWidgets.QMainWindow, SampleMain):
    # Инициализация класса
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)

    def showWindAdd(self):
        pass
    # Функция отображения окна
    def showWind(self):
        frameGm = self.frameGeometry()
        screen = QtWidgets.QApplication.desktop().screenNumber(QtWidgets.QApplication.desktop().cursor().pos())
        centerPoint = QtWidgets.QApplication.desktop().screenGeometry(screen).center()
        frameGm.moveCenter(centerPoint)
        self.move(frameGm.topLeft())

        self.showWindAdd()
        self.show()
