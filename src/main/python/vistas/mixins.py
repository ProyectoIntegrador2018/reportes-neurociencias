from PyQt5 import QtCore, QtGui, QtWidgets

class WindowWidgetMixin(object):
    def __init__(self, Form):
        self.setupUi(Form)

    def setupUI(self, Form):
        self.backButton = QtWidgets.QPushButton(Form)
        self.backButton.setGeometry(QtCore.QRect(15, 50, 20, 30))
        self.backButton.setObjectName("returnButton")