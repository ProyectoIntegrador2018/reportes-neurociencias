# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'vistaSeleccion.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
pruebasSeleccionadas = []

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(450, 616)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.checkBoxInformacionDeSujeto = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBoxInformacionDeSujeto.setGeometry(QtCore.QRect(20, 80, 250, 20))
        self.checkBoxInformacionDeSujeto.setObjectName("checkBoxInformacionDeSujeto")
        #self.checkBoxInformacionDeSujeto.adjustSize()
        self.checkBoxInformacionDeSujeto.stateChanged.connect(lambda:self.changeCheckboxState("Informacion De Sujeto"))

        self.listWidgetPruebas = QtWidgets.QListWidget(self.centralwidget)
        self.listWidgetPruebas.setGeometry(QtCore.QRect(10, 61, 430, 485))
        self.listWidgetPruebas.setObjectName("listWidgetPruebas")

        self.checkBoxPruebaFluidezVerbal = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBoxPruebaFluidezVerbal.setGeometry(QtCore.QRect(20, 106, 250, 20))
        self.checkBoxPruebaFluidezVerbal.setObjectName("checkBoxPruebaFluidezVerbal")
        self.checkBoxPruebaFluidezVerbal.stateChanged.connect(lambda:self.changeCheckboxState("Prueba Fluidez Verbal"))

        self.checkBoxPruebaDenominacion = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBoxPruebaDenominacion.setGeometry(QtCore.QRect(20, 132, 250, 20))
        self.checkBoxPruebaDenominacion.setObjectName("checkBoxPruebaDenominacion")
        self.checkBoxPruebaDenominacion.stateChanged.connect(lambda:self.changeCheckboxState("Prueba Denominacion"))

        self.checkBoxComprensionVerbal = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBoxComprensionVerbal.setGeometry(QtCore.QRect(20, 158, 250, 20))
        self.checkBoxComprensionVerbal.setObjectName("checkBoxComprensionVerbal")
        self.checkBoxComprensionVerbal.stateChanged.connect(lambda:self.changeCheckboxState("Comprension Verbal"))

        self.checkBoxPruebaMemoriaVisoespacial = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBoxPruebaMemoriaVisoespacial.setGeometry(QtCore.QRect(20, 184, 250, 20))
        self.checkBoxPruebaMemoriaVisoespacial.setObjectName("checkBoxPruebaMemoriaVisoespacial")
        self.checkBoxPruebaMemoriaVisoespacial.stateChanged.connect(lambda:self.changeCheckboxState("Prueba Memoria Visoespacial"))

        self.checkBoxPruebaTMT = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBoxPruebaTMT.setGeometry(QtCore.QRect(20, 210, 250, 20))
        self.checkBoxPruebaTMT.setObjectName("checkBoxPruebaTMT")
        self.checkBoxPruebaTMT.stateChanged.connect(lambda:self.changeCheckboxState("Prueba TMT"))

        self.checkBoxPruebaAbstraccion = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBoxPruebaAbstraccion.setGeometry(QtCore.QRect(20, 236, 250, 20))
        self.checkBoxPruebaAbstraccion.setObjectName("checkBoxPruebaAbstraccion")
        self.checkBoxPruebaAbstraccion.stateChanged.connect(lambda:self.changeCheckboxState("Prueba Abstraccion"))

        self.checkBoxPruebaDigitos = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBoxPruebaDigitos.setGeometry(QtCore.QRect(20, 262, 250, 20))
        self.checkBoxPruebaDigitos.setObjectName("checkBoxPruebaDigitos")
        self.checkBoxPruebaDigitos.stateChanged.connect(lambda:self.changeCheckboxState("Prueba Digitos"))

        self.checkBoxPruebaSDMT = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBoxPruebaSDMT.setGeometry(QtCore.QRect(20, 288, 250, 20))
        self.checkBoxPruebaSDMT.setObjectName("checkBoxPruebaSDMT")
        self.checkBoxPruebaSDMT.stateChanged.connect(lambda:self.changeCheckboxState("Prueba SDMT"))

        self.checkBoxPruebaLNS = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBoxPruebaLNS.setGeometry(QtCore.QRect(20, 314, 250, 20))
        self.checkBoxPruebaLNS.setObjectName("checkBoxPruebaLNS")
        self.checkBoxPruebaLNS.stateChanged.connect(lambda:self.changeCheckboxState("Prueba LNS"))

        self.checkBoxPruebaD2 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBoxPruebaD2.setGeometry(QtCore.QRect(20, 340, 250, 20))
        self.checkBoxPruebaD2.setObjectName("checkBoxPruebaD2")
        self.checkBoxPruebaD2.stateChanged.connect(lambda:self.changeCheckboxState("Prueba D2"))

        self.checkBoxPruebaHopkins = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBoxPruebaHopkins.setGeometry(QtCore.QRect(20, 366, 250, 20))
        self.checkBoxPruebaHopkins.setObjectName("checkBoxPruebaHopkins")
        self.checkBoxPruebaHopkins.stateChanged.connect(lambda:self.changeCheckboxState("Prueba Hopkins"))

        self.checkBoxPruebaStroop = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBoxPruebaStroop.setGeometry(QtCore.QRect(20, 392, 250, 20))
        self.checkBoxPruebaStroop.setObjectName("checkBoxPruebaStroop")
        self.checkBoxPruebaStroop.stateChanged.connect(lambda:self.changeCheckboxState("Prueba Stroop"))

        self.checkBoxTorreDeLondres = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBoxTorreDeLondres.setGeometry(QtCore.QRect(20, 418, 250, 20))
        self.checkBoxTorreDeLondres.setObjectName("checkBoxTorreDeLondres")
        self.checkBoxTorreDeLondres.stateChanged.connect(lambda:self.changeCheckboxState("Torre De Londres"))

        self.checkBoxPruebaMotivosDeportivos = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBoxPruebaMotivosDeportivos.setGeometry(QtCore.QRect(20, 444, 250, 20))
        self.checkBoxPruebaMotivosDeportivos.setObjectName("checkBoxPruebaMotivosDeportivos")
        self.checkBoxPruebaMotivosDeportivos.stateChanged.connect(lambda:self.changeCheckboxState("Prueba Motivos Deportivos"))

        self.checkBoxPruebaDePittsburgh = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBoxPruebaDePittsburgh.setGeometry(QtCore.QRect(20, 470, 250, 20))
        self.checkBoxPruebaDePittsburgh.setObjectName("checkBoxPruebaDePittsburgh")
        self.checkBoxPruebaDePittsburgh.stateChanged.connect(lambda:self.changeCheckboxState("Prueba De Pittsburgh"))

        self.checkBoxPruebaSCL90 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBoxPruebaSCL90.setGeometry(QtCore.QRect(20, 496, 250, 20))
        self.checkBoxPruebaSCL90.setObjectName("checkBoxPruebaSCL90")
        self.checkBoxPruebaSCL90.stateChanged.connect(lambda:self.changeCheckboxState("Prueba SCL90"))

        self.checkBoxReporte = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBoxReporte.setGeometry(QtCore.QRect(20, 522, 250, 20))
        self.checkBoxReporte.setObjectName("checkBoxReporte")
        self.checkBoxReporte.stateChanged.connect(lambda:self.changeCheckboxState("Reporte"))

        self.labelPruebasSeleccionadas = QtWidgets.QLabel(self.centralwidget)
        self.labelPruebasSeleccionadas.setGeometry(QtCore.QRect(30, 545, 170, 25))
        self.labelPruebasSeleccionadas.setObjectName("labelPruebasSeleccionadas")

        self.labelPruebasSeleccionadasDisplay = QtWidgets.QLabel(self.centralwidget)
        self.labelPruebasSeleccionadasDisplay.setGeometry(QtCore.QRect(10, 545, 16, 25))
        self.labelPruebasSeleccionadasDisplay.setObjectName("labelPruebasSeleccionadasDisplay")

        self.pushButtonContinuar = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonContinuar.setGeometry(QtCore.QRect(355, 550, 85, 25))
        self.pushButtonContinuar.setObjectName("pushButtonContinuar")
        
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 0, 251, 61))
        self.label.setObjectName("label")
        self.listWidgetPruebas.raise_()
        self.checkBoxInformacionDeSujeto.raise_()
        self.checkBoxPruebaFluidezVerbal.raise_()
        self.checkBoxPruebaDenominacion.raise_()
        self.checkBoxComprensionVerbal.raise_()
        self.checkBoxPruebaMemoriaVisoespacial.raise_()
        self.checkBoxPruebaTMT.raise_()
        self.checkBoxPruebaAbstraccion.raise_()
        self.checkBoxPruebaDigitos.raise_()
        self.checkBoxPruebaSDMT.raise_()
        self.checkBoxPruebaLNS.raise_()
        self.checkBoxPruebaD2.raise_()
        self.checkBoxPruebaHopkins.raise_()
        self.checkBoxPruebaStroop.raise_()
        self.checkBoxTorreDeLondres.raise_()
        self.checkBoxPruebaMotivosDeportivos.raise_()
        self.checkBoxPruebaDePittsburgh.raise_()
        self.checkBoxPruebaSCL90.raise_()
        self.checkBoxReporte.raise_()
        self.labelPruebasSeleccionadas.raise_()
        self.labelPruebasSeleccionadasDisplay.raise_()
        self.pushButtonContinuar.raise_()
        self.label.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 271, 18))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Seleeccion de Pruebas"))
        self.checkBoxInformacionDeSujeto.setText(_translate("MainWindow", "Información de Sujeto"))
        self.checkBoxPruebaFluidezVerbal.setText(_translate("MainWindow", "Prueba Fluidez Verbal"))
        self.checkBoxPruebaDenominacion.setText(_translate("MainWindow", "Prueba Denominación"))
        self.checkBoxComprensionVerbal.setText(_translate("MainWindow", "Prueba Comprensión Verbal"))
        self.checkBoxPruebaMemoriaVisoespacial.setText(_translate("MainWindow", "Prueba Memoria Visoespacial"))
        self.checkBoxPruebaTMT.setText(_translate("MainWindow", "Prueba TMT"))
        self.checkBoxPruebaAbstraccion.setText(_translate("MainWindow", "Prueba Abstracción"))
        self.checkBoxPruebaDigitos.setText(_translate("MainWindow", "Prueba Dígitos"))
        self.checkBoxPruebaSDMT.setText(_translate("MainWindow", "Prueba SDMT"))
        self.checkBoxPruebaLNS.setText(_translate("MainWindow", "Prueba LNS"))
        self.checkBoxPruebaD2.setText(_translate("MainWindow", "Prueba D2"))
        self.checkBoxPruebaHopkins.setText(_translate("MainWindow", "Prueba Hopkins"))
        self.checkBoxPruebaStroop.setText(_translate("MainWindow", "Prueba Stroop"))
        self.checkBoxTorreDeLondres.setText(_translate("MainWindow", "Prueba Torre de Londres"))
        self.checkBoxPruebaMotivosDeportivos.setText(_translate("MainWindow", "Prueba Motivos Deportivos"))
        self.checkBoxPruebaDePittsburgh.setText(_translate("MainWindow", "Prueba de Pittsburgh"))
        self.checkBoxPruebaSCL90.setText(_translate("MainWindow", "Prueba SCL-90"))
        self.checkBoxReporte.setText(_translate("MainWindow", "Reporte"))
        self.labelPruebasSeleccionadas.setText(_translate("MainWindow", "prueba(s) seleccionadas"))
        self.labelPruebasSeleccionadasDisplay.setText(_translate("MainWindow", "0"))
        self.pushButtonContinuar.setText(_translate("MainWindow", "Continuar"))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p><img src=\":/newPrefix/logoChico.png\"/></p></body></html>"))

    def changeCheckboxState(self, checkboxName):
        if checkboxName not in pruebasSeleccionadas:
            pruebasSeleccionadas.append(checkboxName)
        else:
            pruebasSeleccionadas.remove(checkboxName)
        self.labelPruebasSeleccionadasDisplay.setText(str(len(pruebasSeleccionadas)))
        print(pruebasSeleccionadas)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
