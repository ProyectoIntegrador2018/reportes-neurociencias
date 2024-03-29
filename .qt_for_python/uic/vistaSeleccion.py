# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\Users\rodri\Documents\GitHub\reportes-neurociencias\src\main\python\vistas\vistaSeleccion.ui'
#
# Created by: PyQt5 UI code generator 5.15.3
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(271, 616)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.checkBoxInformacionDeSujeto = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBoxInformacionDeSujeto.setGeometry(QtCore.QRect(20, 80, 101, 16))
        self.checkBoxInformacionDeSujeto.setObjectName("checkBoxInformacionDeSujeto")
        self.listWidgetPruebas = QtWidgets.QListWidget(self.centralwidget)
        self.listWidgetPruebas.setGeometry(QtCore.QRect(10, 61, 251, 481))
        self.listWidgetPruebas.setObjectName("listWidgetPruebas")
        self.checkBoxPruebaEMD = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBoxPruebaEMD.setGeometry(QtCore.QRect(0, 50, 91, 16))
        self.checkBoxPruebaEMD.setObjectName("checkBoxPruebaEMD")
        self.checkBoxPruebaBussyPerry = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBoxPruebaBussyPerry.setGeometry(QtCore.QRect(0, 106, 91, 16))
        self.checkBoxPruebaBussyPerry.setObjectName("checkBoxPruebaBussyPerry")
        self.checkBoxPruebaFluidezVerbal = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBoxPruebaFluidezVerbal.setGeometry(QtCore.QRect(20, 106, 91, 16))
        self.checkBoxPruebaFluidezVerbal.setObjectName("checkBoxPruebaFluidezVerbal")
        self.checkBoxPruebaDenominacion = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBoxPruebaDenominacion.setGeometry(QtCore.QRect(20, 132, 91, 16))
        self.checkBoxPruebaDenominacion.setObjectName("checkBoxPruebaDenominacion")
        self.checkBoxComprensionVerbal = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBoxComprensionVerbal.setGeometry(QtCore.QRect(20, 158, 121, 16))
        self.checkBoxComprensionVerbal.setObjectName("checkBoxComprensionVerbal")
        self.checkBoxPruebaMemoriaVisoespacial = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBoxPruebaMemoriaVisoespacial.setGeometry(QtCore.QRect(20, 184, 121, 16))
        self.checkBoxPruebaMemoriaVisoespacial.setObjectName("checkBoxPruebaMemoriaVisoespacial")
        self.checkBoxPruebaTMT = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBoxPruebaTMT.setGeometry(QtCore.QRect(20, 210, 61, 16))
        self.checkBoxPruebaTMT.setObjectName("checkBoxPruebaTMT")
        self.checkBoxPruebaAbstraccion = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBoxPruebaAbstraccion.setGeometry(QtCore.QRect(20, 236, 91, 16))
        self.checkBoxPruebaAbstraccion.setObjectName("checkBoxPruebaAbstraccion")
        self.checkBoxPruebaDigitos = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBoxPruebaDigitos.setGeometry(QtCore.QRect(20, 262, 81, 16))
        self.checkBoxPruebaDigitos.setObjectName("checkBoxPruebaDigitos")
        self.checkBoxPruebaSDMT = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBoxPruebaSDMT.setGeometry(QtCore.QRect(20, 288, 71, 16))
        self.checkBoxPruebaSDMT.setObjectName("checkBoxPruebaSDMT")
        self.checkBoxPruebaLNS = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBoxPruebaLNS.setGeometry(QtCore.QRect(20, 314, 61, 16))
        self.checkBoxPruebaLNS.setObjectName("checkBoxPruebaLNS")
        self.checkBoxPruebaD2 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBoxPruebaD2.setGeometry(QtCore.QRect(20, 340, 53, 14))
        self.checkBoxPruebaD2.setObjectName("checkBoxPruebaD2")
        self.checkBoxPruebaHopkins = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBoxPruebaHopkins.setGeometry(QtCore.QRect(20, 366, 71, 16))
        self.checkBoxPruebaHopkins.setObjectName("checkBoxPruebaHopkins")
        self.checkBoxPruebaStroop = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBoxPruebaStroop.setGeometry(QtCore.QRect(20, 392, 71, 16))
        self.checkBoxPruebaStroop.setObjectName("checkBoxPruebaStroop")
        self.checkBoxTorreDeLondres = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBoxTorreDeLondres.setGeometry(QtCore.QRect(20, 418, 111, 16))
        self.checkBoxTorreDeLondres.setObjectName("checkBoxTorreDeLondres")
        self.checkBoxPruebaMotivosDeportivos = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBoxPruebaMotivosDeportivos.setGeometry(QtCore.QRect(20, 444, 111, 16))
        self.checkBoxPruebaMotivosDeportivos.setObjectName("checkBoxPruebaMotivosDeportivos")
        self.checkBoxPruebaDePittsburgh = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBoxPruebaDePittsburgh.setGeometry(QtCore.QRect(20, 470, 101, 16))
        self.checkBoxPruebaDePittsburgh.setObjectName("checkBoxPruebaDePittsburgh")
        self.checkBoxPruebaSCL90 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBoxPruebaSCL90.setGeometry(QtCore.QRect(20, 496, 71, 16))
        self.checkBoxPruebaSCL90.setObjectName("checkBoxPruebaSCL90")
        self.checkBoxReporte = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBoxReporte.setGeometry(QtCore.QRect(20, 522, 53, 14))
        self.checkBoxReporte.setObjectName("checkBoxReporte")
        self.labelPruebasSeleccionadas = QtWidgets.QLabel(self.centralwidget)
        self.labelPruebasSeleccionadas.setGeometry(QtCore.QRect(20, 540, 91, 16))
        self.labelPruebasSeleccionadas.setObjectName("labelPruebasSeleccionadas")
        self.labelPruebasSeleccionadasDisplay = QtWidgets.QLabel(self.centralwidget)
        self.labelPruebasSeleccionadasDisplay.setGeometry(QtCore.QRect(10, 540, 16, 16))
        self.labelPruebasSeleccionadasDisplay.setObjectName("labelPruebasSeleccionadasDisplay")
        self.pushButtonContinuar = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonContinuar.setGeometry(QtCore.QRect(200, 550, 56, 17))
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
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.checkBoxInformacionDeSujeto.setText(_translate("MainWindow", "Información de Sujeto"))
        self.checkBoxPruebaEMD.setText(_translate("MainWindow", "Prueba EMD"))
        self.checkBoxPruebaBussyPerry.setText(_translate("MainWindow", "Prueba Buss y Perry"))
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
        self.labelPruebasSeleccionadas.setText(_translate("MainWindow", "pruebas seleccionadas"))
        self.labelPruebasSeleccionadasDisplay.setText(_translate("MainWindow", "0"))
        self.pushButtonContinuar.setText(_translate("MainWindow", "Continuar"))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p><img src=\":/newPrefix/logoChico.png\"/></p></body></html>"))
import fotoLogo_rc
