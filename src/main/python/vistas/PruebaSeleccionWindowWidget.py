# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'vistaSeleccion.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class PruebaSeleccionWindowWidget(object):
    def __init__(self, Form):
        self.setupUi(Form)

    def setupUi(self, Form):
        self.resize = False
        Form.setObjectName("Form")
        Form.resize(450, 616)
        self.centralwidget = QtWidgets.QWidget(Form)
        self.centralwidget.setObjectName("centralwidget")

        self.listWidgetPruebas = QtWidgets.QListWidget(self.centralwidget)
        self.listWidgetPruebas.setGeometry(QtCore.QRect(10, 61, 430, 485))
        self.listWidgetPruebas.setObjectName("listWidgetPruebas")
        self.widgetPruebas = QtWidgets.QWidget(self.listWidgetPruebas)
        self.formPruebas = QtWidgets.QFormLayout(self.widgetPruebas)
        self.formPruebas.setVerticalSpacing(4)

        self.checkBoxPruebaEMD = QtWidgets.QCheckBox()
        self.checkBoxPruebaEMD.setObjectName("checkBoxPruebaEMD")

        self.checkBoxPruebaBussyPerry = QtWidgets.QCheckBox()
        self.checkBoxPruebaBussyPerry.setObjectName("checkBoxPruebaBussyPerry")

        self.checkBoxPruebaFluidezVerbal = QtWidgets.QCheckBox( self.widgetPruebas)
        self.checkBoxPruebaFluidezVerbal.setObjectName("checkBoxPruebaFluidezVerbal")

        self.checkBoxPruebaDenominacion = QtWidgets.QCheckBox( self.widgetPruebas)
        self.checkBoxPruebaDenominacion.setObjectName("checkBoxPruebaDenominacion")

        self.checkBoxComprensionVerbal = QtWidgets.QCheckBox( self.centralwidget)
        self.checkBoxComprensionVerbal.setObjectName("checkBoxComprensionVerbal")

        self.checkBoxPruebaMemoriaVisoespacial = QtWidgets.QCheckBox( self.centralwidget)
        self.checkBoxPruebaMemoriaVisoespacial.setObjectName("checkBoxPruebaMemoriaVisoespacial")

        self.checkBoxPruebaTMT = QtWidgets.QCheckBox()
        self.checkBoxPruebaTMT.setObjectName("checkBoxPruebaTMT")

        self.checkBoxPruebaAbstraccion = QtWidgets.QCheckBox( self.centralwidget)
        self.checkBoxPruebaAbstraccion.setObjectName("checkBoxPruebaAbstraccion")

        self.checkBoxPruebaDigitos = QtWidgets.QCheckBox()
        self.checkBoxPruebaDigitos.setObjectName("checkBoxPruebaDigitos")

        self.checkBoxPruebaSDMT = QtWidgets.QCheckBox()
        self.checkBoxPruebaSDMT.setObjectName("checkBoxPruebaSDMT")

        self.checkBoxPruebaLNS = QtWidgets.QCheckBox()
        self.checkBoxPruebaLNS.setObjectName("checkBoxPruebaLNS")

        self.checkBoxPruebaD2 = QtWidgets.QCheckBox()
        self.checkBoxPruebaD2.setObjectName("checkBoxPruebaD2")

        self.checkBoxPruebaHopkins = QtWidgets.QCheckBox()
        self.checkBoxPruebaHopkins.setObjectName("checkBoxPruebaHopkins")

        self.checkBoxPruebaStroop = QtWidgets.QCheckBox()
        self.checkBoxPruebaStroop.setObjectName("checkBoxPruebaStroop")

        self.checkBoxTorreDeLondres = QtWidgets.QCheckBox()
        self.checkBoxTorreDeLondres.setObjectName("checkBoxTorreDeLondres")

        self.checkBoxPruebaMotivosDeportivos = QtWidgets.QCheckBox( self.centralwidget)
        self.checkBoxPruebaMotivosDeportivos.setObjectName("checkBoxPruebaMotivosDeportivos")

        self.checkBoxPruebaDePittsburgh = QtWidgets.QCheckBox( self.centralwidget)
        self.checkBoxPruebaDePittsburgh.setObjectName("checkBoxPruebaDePittsburgh")

        self.checkBoxPruebaSCL90 = QtWidgets.QCheckBox()
        self.checkBoxPruebaSCL90.setObjectName("checkBoxPruebaSCL90")

        self.checkBoxPruebaBSI18 = QtWidgets.QCheckBox()
        self.checkBoxPruebaBSI18.setObjectName("checkBoxPruebaBSI18")
        
        self.formPruebas.addRow(self.checkBoxPruebaEMD)
        self.formPruebas.addRow(self.checkBoxPruebaBussyPerry)
        self.formPruebas.addRow(self.checkBoxPruebaFluidezVerbal)
        self.formPruebas.addRow(self.checkBoxPruebaDenominacion)
        self.formPruebas.addRow(self.checkBoxComprensionVerbal)
        self.formPruebas.addRow(self.checkBoxPruebaMemoriaVisoespacial)
        self.formPruebas.addRow(self.checkBoxPruebaTMT)
        self.formPruebas.addRow(self.checkBoxPruebaAbstraccion)
        self.formPruebas.addRow(self.checkBoxPruebaDigitos)
        self.formPruebas.addRow(self.checkBoxPruebaSDMT)
        self.formPruebas.addRow(self.checkBoxPruebaLNS)
        self.formPruebas.addRow(self.checkBoxPruebaD2)
        self.formPruebas.addRow(self.checkBoxPruebaHopkins)
        self.formPruebas.addRow(self.checkBoxPruebaStroop)
        self.formPruebas.addRow(self.checkBoxTorreDeLondres)
        self.formPruebas.addRow(self.checkBoxPruebaMotivosDeportivos)
        self.formPruebas.addRow(self.checkBoxPruebaDePittsburgh)
        self.formPruebas.addRow(self.checkBoxPruebaSCL90)
        self.formPruebas.addRow(self.checkBoxPruebaBSI18)

        self.labelPruebasSeleccionadas = QtWidgets.QLabel(self.centralwidget)
        self.labelPruebasSeleccionadas.setGeometry( QtCore.QRect(30, 545, 170, 25))
        self.labelPruebasSeleccionadas.setObjectName("labelPruebasSeleccionadas")

        self.labelPruebasSeleccionadasDisplay = QtWidgets.QLabel( self.centralwidget)
        self.labelPruebasSeleccionadasDisplay.setGeometry( QtCore.QRect(10, 545, 16, 25))
        self.labelPruebasSeleccionadasDisplay.setObjectName("labelPruebasSeleccionadasDisplay")

        self.pushButtonContinuar = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonContinuar.setGeometry(QtCore.QRect(250, 550, 85, 25))
        self.pushButtonContinuar.setObjectName("pushButtonContinuar")

        self.backButton = QtWidgets.QPushButton(Form)
        self.backButton.setGeometry(QtCore.QRect(250, 580, 85, 30))
        self.backButton.setObjectName("returnButton")

        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 0, 300, 61))
        self.label.setObjectName("label")
        self.label.setScaledContents(True)

        self.listWidgetPruebas.raise_()
        self.checkBoxPruebaFluidezVerbal.raise_()
        self.checkBoxPruebaEMD.raise_()
        self.checkBoxPruebaBussyPerry.raise_()
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
        self.checkBoxPruebaBSI18.raise_()
        self.labelPruebasSeleccionadas.raise_()
        self.labelPruebasSeleccionadasDisplay.raise_()
        self.pushButtonContinuar.raise_()
        self.label.raise_()

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Seleccion de Pruebas"))

        self.checkBoxPruebaEMD.setText(_translate("Form", "Prueba EMD"))
        self.checkBoxPruebaBussyPerry.setText(_translate("Form", "Prueba Buss y Perry"))
        self.checkBoxPruebaFluidezVerbal.setText(_translate("Form", "Prueba Fluidez Verbal"))
        self.checkBoxPruebaDenominacion.setText(_translate("Form", "Prueba Denominación"))
        self.checkBoxComprensionVerbal.setText(_translate("Form", "Prueba Comprensión Verbal"))
        self.checkBoxPruebaMemoriaVisoespacial.setText(_translate("Form", "Prueba Memoria Visoespacial"))
        self.checkBoxPruebaTMT.setText(_translate("Form", "Prueba TMT"))
        self.checkBoxPruebaAbstraccion.setText(_translate("Form", "Prueba Abstracción"))
        self.checkBoxPruebaDigitos.setText(_translate("Form", "Prueba Dígitos"))
        self.checkBoxPruebaSDMT.setText(_translate("Form", "Prueba SDMT"))
        self.checkBoxPruebaLNS.setText(_translate("Form", "Prueba LNS"))
        self.checkBoxPruebaD2.setText(_translate("Form", "Prueba D2"))
        self.checkBoxPruebaHopkins.setText(_translate("Form", "Prueba Hopkins"))
        self.checkBoxPruebaStroop.setText(_translate("Form", "Prueba Stroop"))
        self.checkBoxTorreDeLondres.setText(_translate("Form", "Prueba Torre de Londres"))
        self.checkBoxPruebaMotivosDeportivos.setText(_translate("Form", "Prueba Motivos Deportivos"))
        self.checkBoxPruebaDePittsburgh.setText(_translate("Form", "Prueba de Pittsburgh"))
        self.checkBoxPruebaSCL90.setText(_translate("Form", "Prueba SCL-90"))
        self.checkBoxPruebaBSI18.setText(_translate("Form", "Prueba BSI-18"))

        self.labelPruebasSeleccionadas.setText(_translate("Form", "prueba(s) seleccionadas"))
        self.labelPruebasSeleccionadasDisplay.setText(_translate("Form", "0"))

        self.pushButtonContinuar.setText(_translate("Form", "Continuar"))
        self.label.setText(_translate("Form", "<html><head/><body><p><img src=\":/newPrefix/logoChico.png\"/></p></body></html>"))

        self.backButton.setText(_translate("Form", "Importar Reporte"))