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
        Form.setObjectName("Form")
        Form.resize(450, 616)
        self.centralwidget = QtWidgets.QWidget(Form)
        self.centralwidget.setObjectName("centralwidget")

        self.listWidgetPruebas = QtWidgets.QListWidget(self.centralwidget)
        self.listWidgetPruebas.setGeometry(QtCore.QRect(10, 61, 430, 485))
        self.listWidgetPruebas.setObjectName("listWidgetPruebas")

        self.checkBoxPruebaBussyPerry = QtWidgets.QCheckBox(
            self.centralwidget)
        self.checkBoxPruebaBussyPerry.setGeometry(
            QtCore.QRect(20, 80, 250, 20))
        self.checkBoxPruebaBussyPerry.setObjectName(
            "checkBoxPruebaBussyPerry")

        self.checkBoxPruebaFluidezVerbal = QtWidgets.QCheckBox(
            self.centralwidget)
        self.checkBoxPruebaFluidezVerbal.setGeometry(
            QtCore.QRect(20, 106, 250, 20))
        self.checkBoxPruebaFluidezVerbal.setObjectName(
            "checkBoxPruebaFluidezVerbal")
        # self.checkBoxPruebaFluidezVerbal.stateChanged.connect(lambda:self.changeCheckboxState("Prueba Fluidez Verbal"))

        self.checkBoxPruebaDenominacion = QtWidgets.QCheckBox(
            self.centralwidget)
        self.checkBoxPruebaDenominacion.setGeometry(
            QtCore.QRect(20, 132, 250, 20))
        self.checkBoxPruebaDenominacion.setObjectName(
            "checkBoxPruebaDenominacion")
        # self.checkBoxPruebaDenominacion.stateChanged.connect(lambda:self.changeCheckboxState("Prueba Denominacion"))

        self.checkBoxComprensionVerbal = QtWidgets.QCheckBox(
            self.centralwidget)
        self.checkBoxComprensionVerbal.setGeometry(
            QtCore.QRect(20, 158, 250, 20))
        self.checkBoxComprensionVerbal.setObjectName(
            "checkBoxComprensionVerbal")
        # self.checkBoxComprensionVerbal.stateChanged.connect(lambda:self.changeCheckboxState("Comprension Verbal"))

        self.checkBoxPruebaMemoriaVisoespacial = QtWidgets.QCheckBox(
            self.centralwidget)
        self.checkBoxPruebaMemoriaVisoespacial.setGeometry(
            QtCore.QRect(20, 184, 250, 20))
        self.checkBoxPruebaMemoriaVisoespacial.setObjectName(
            "checkBoxPruebaMemoriaVisoespacial")
        # self.checkBoxPruebaMemoriaVisoespacial.stateChanged.connect(lambda:self.changeCheckboxState("Prueba Memoria Visoespacial"))

        self.checkBoxPruebaTMT = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBoxPruebaTMT.setGeometry(QtCore.QRect(20, 210, 250, 20))
        self.checkBoxPruebaTMT.setObjectName("checkBoxPruebaTMT")
        # self.checkBoxPruebaTMT.stateChanged.connect(lambda:self.changeCheckboxState("Prueba TMT"))

        self.checkBoxPruebaAbstraccion = QtWidgets.QCheckBox(
            self.centralwidget)
        self.checkBoxPruebaAbstraccion.setGeometry(
            QtCore.QRect(20, 236, 250, 20))
        self.checkBoxPruebaAbstraccion.setObjectName(
            "checkBoxPruebaAbstraccion")
        # self.checkBoxPruebaAbstraccion.stateChanged.connect(lambda:self.changeCheckboxState("Prueba Abstraccion"))

        self.checkBoxPruebaDigitos = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBoxPruebaDigitos.setGeometry(QtCore.QRect(20, 262, 250, 20))
        self.checkBoxPruebaDigitos.setObjectName("checkBoxPruebaDigitos")
        # self.checkBoxPruebaDigitos.stateChanged.connect(lambda:self.changeCheckboxState("Prueba Digitos"))

        self.checkBoxPruebaSDMT = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBoxPruebaSDMT.setGeometry(QtCore.QRect(20, 288, 250, 20))
        self.checkBoxPruebaSDMT.setObjectName("checkBoxPruebaSDMT")
        # self.checkBoxPruebaSDMT.stateChanged.connect(lambda:self.changeCheckboxState("Prueba SDMT"))

        self.checkBoxPruebaLNS = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBoxPruebaLNS.setGeometry(QtCore.QRect(20, 314, 250, 20))
        self.checkBoxPruebaLNS.setObjectName("checkBoxPruebaLNS")
        # self.checkBoxPruebaLNS.stateChanged.connect(lambda:self.changeCheckboxState("Prueba LNS"))

        self.checkBoxPruebaD2 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBoxPruebaD2.setGeometry(QtCore.QRect(20, 340, 250, 20))
        self.checkBoxPruebaD2.setObjectName("checkBoxPruebaD2")
        # self.checkBoxPruebaD2.stateChanged.connect(lambda:self.changeCheckboxState("Prueba D2"))

        self.checkBoxPruebaHopkins = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBoxPruebaHopkins.setGeometry(QtCore.QRect(20, 366, 250, 20))
        self.checkBoxPruebaHopkins.setObjectName("checkBoxPruebaHopkins")
        # self.checkBoxPruebaHopkins.stateChanged.connect(lambda:self.changeCheckboxState("Prueba Hopkins"))

        self.checkBoxPruebaStroop = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBoxPruebaStroop.setGeometry(QtCore.QRect(20, 392, 250, 20))
        self.checkBoxPruebaStroop.setObjectName("checkBoxPruebaStroop")
        # self.checkBoxPruebaStroop.stateChanged.connect(lambda:self.changeCheckboxState("Prueba Stroop"))

        self.checkBoxTorreDeLondres = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBoxTorreDeLondres.setGeometry(QtCore.QRect(20, 418, 250, 20))
        self.checkBoxTorreDeLondres.setObjectName("checkBoxTorreDeLondres")
        # self.checkBoxTorreDeLondres.stateChanged.connect(lambda:self.changeCheckboxState("Torre De Londres"))

        self.checkBoxPruebaMotivosDeportivos = QtWidgets.QCheckBox(
            self.centralwidget)
        self.checkBoxPruebaMotivosDeportivos.setGeometry(
            QtCore.QRect(20, 444, 250, 20))
        self.checkBoxPruebaMotivosDeportivos.setObjectName(
            "checkBoxPruebaMotivosDeportivos")
        # self.checkBoxPruebaMotivosDeportivos.stateChanged.connect(lambda:self.changeCheckboxState("Prueba Motivos Deportivos"))

        self.checkBoxPruebaDePittsburgh = QtWidgets.QCheckBox(
            self.centralwidget)
        self.checkBoxPruebaDePittsburgh.setGeometry(
            QtCore.QRect(20, 470, 250, 20))
        self.checkBoxPruebaDePittsburgh.setObjectName(
            "checkBoxPruebaDePittsburgh")
        # self.checkBoxPruebaDePittsburgh.stateChanged.connect(lambda:self.changeCheckboxState("Prueba De Pittsburgh"))

        self.checkBoxPruebaSCL90 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBoxPruebaSCL90.setGeometry(QtCore.QRect(20, 496, 250, 20))
        self.checkBoxPruebaSCL90.setObjectName("checkBoxPruebaSCL90")
        # self.checkBoxPruebaSCL90.stateChanged.connect(lambda:self.changeCheckboxState("Prueba SCL90"))

        self.checkBoxPruebaBSI18 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBoxPruebaBSI18.setGeometry(QtCore.QRect(20, 522, 250, 20))
        self.checkBoxPruebaBSI18.setObjectName("checkBoxPruebaBSI18")
        # self.checkBoxPruebaBSI18.stateChanged.connect(lambda:self.changeCheckboxState("Prueba BSI18"))

        self.labelPruebasSeleccionadas = QtWidgets.QLabel(self.centralwidget)
        self.labelPruebasSeleccionadas.setGeometry(
            QtCore.QRect(30, 545, 170, 25))
        self.labelPruebasSeleccionadas.setObjectName(
            "labelPruebasSeleccionadas")

        self.labelPruebasSeleccionadasDisplay = QtWidgets.QLabel(
            self.centralwidget)
        self.labelPruebasSeleccionadasDisplay.setGeometry(
            QtCore.QRect(10, 545, 16, 25))
        self.labelPruebasSeleccionadasDisplay.setObjectName(
            "labelPruebasSeleccionadasDisplay")

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
        # Form.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(Form)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 271, 18))
        self.menubar.setObjectName("menubar")
        # Form.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(Form)
        self.statusbar.setObjectName("statusbar")
        # Form.setStatusBar(self.statusbar)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Seleeccion de Pruebas"))
        self.checkBoxPruebaBussyPerry.setText(
            _translate("Form", "Prueba Buss y Perry"))
        self.checkBoxPruebaFluidezVerbal.setText(
            _translate("Form", "Prueba Fluidez Verbal"))
        self.checkBoxPruebaDenominacion.setText(
            _translate("Form", "Prueba Denominación"))
        self.checkBoxComprensionVerbal.setText(
            _translate("Form", "Prueba Comprensión Verbal"))
        self.checkBoxPruebaMemoriaVisoespacial.setText(
            _translate("Form", "Prueba Memoria Visoespacial"))
        self.checkBoxPruebaTMT.setText(_translate("Form", "Prueba TMT"))
        self.checkBoxPruebaAbstraccion.setText(
            _translate("Form", "Prueba Abstracción"))
        self.checkBoxPruebaDigitos.setText(
            _translate("Form", "Prueba Dígitos"))
        self.checkBoxPruebaSDMT.setText(_translate("Form", "Prueba SDMT"))
        self.checkBoxPruebaLNS.setText(_translate("Form", "Prueba LNS"))
        self.checkBoxPruebaD2.setText(_translate("Form", "Prueba D2"))
        self.checkBoxPruebaHopkins.setText(
            _translate("Form", "Prueba Hopkins"))
        self.checkBoxPruebaStroop.setText(_translate("Form", "Prueba Stroop"))
        self.checkBoxTorreDeLondres.setText(
            _translate("Form", "Prueba Torre de Londres"))
        self.checkBoxPruebaMotivosDeportivos.setText(
            _translate("Form", "Prueba Motivos Deportivos"))
        self.checkBoxPruebaDePittsburgh.setText(
            _translate("Form", "Prueba de Pittsburgh"))
        self.checkBoxPruebaSCL90.setText(_translate("Form", "Prueba SCL-90"))
        self.checkBoxPruebaBSI18.setText(_translate("Form", "Prueba BSI-18"))
        self.labelPruebasSeleccionadas.setText(
            _translate("Form", "prueba(s) seleccionadas"))
        self.labelPruebasSeleccionadasDisplay.setText(_translate("Form", "0"))
        self.pushButtonContinuar.setText(_translate("Form", "Continuar"))
        self.label.setText(_translate(
            "Form", "<html><head/><body><p><img src=\":/newPrefix/logoChico.png\"/></p></body></html>"))
        self.backButton.setText(_translate("Form", "Importar Reporte"))