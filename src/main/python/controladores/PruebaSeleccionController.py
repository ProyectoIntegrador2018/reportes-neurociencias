# Contolador de la vista seleccion de pruebas
from PyQt5 import QtWidgets, QtCore
from vistas.PruebaSeleccionWindowWidget import PruebaSeleccionWindowWidget
from ControllerModel import *


class PruebaSeleccionController(QtWidgets.QWidget, ControllerModel):
    switch_window = QtCore.pyqtSignal(object, object)

    def __init__(self, mainWindow, reporteModel=None):
        QtWidgets.QWidget.__init__(self)
        self.seleccionView = PruebaSeleccionWindowWidget(mainWindow)
        self.reporteModel = reporteModel
        self.invalidArgs = list()
        self.initialRoutes = ["seleccionarPruebas",
                              "informacionSujeto", ]
        self.endRoutes = ["report",
                          # do not remove used for reseting and initialize pruebas
                          "dummyWindow", ]
        self.pruebasSeleccionadas = []

        self.seleccionView.checkBoxPruebaFluidezVerbal.stateChanged.connect(
            lambda: self.addSelectedPrueba("fluidezVerbal", self.seleccionView.checkBoxPruebaFluidezVerbal))
        self.seleccionView.checkBoxPruebaDenominacion.stateChanged.connect(
            lambda: self.addSelectedPrueba("denominacion", self.seleccionView.checkBoxPruebaDenominacion))
        self.seleccionView.checkBoxComprensionVerbal.stateChanged.connect(
            lambda: self.addSelectedPrueba("comprensionVerbal", self.seleccionView.checkBoxComprensionVerbal))
        self.seleccionView.checkBoxPruebaMemoriaVisoespacial.stateChanged.connect(
            lambda: self.addSelectedPrueba("memoriaVisoespacial", self.seleccionView.checkBoxPruebaMemoriaVisoespacial))
        self.seleccionView.checkBoxPruebaTMT.stateChanged.connect(
            lambda: self.addSelectedPrueba("tmt", self.seleccionView.checkBoxPruebaTMT))
        self.seleccionView.checkBoxPruebaAbstraccion.stateChanged.connect(
            lambda: self.addSelectedPrueba("abstraccion", self.seleccionView.checkBoxPruebaAbstraccion))
        self.seleccionView.checkBoxPruebaDigitos.stateChanged.connect(
            lambda: self.addSelectedPrueba("digitos", self.seleccionView.checkBoxPruebaDigitos))
        self.seleccionView.checkBoxPruebaSDMT.stateChanged.connect(
            lambda: self.addSelectedPrueba("sdmt", self.seleccionView.checkBoxPruebaSDMT))
        self.seleccionView.checkBoxPruebaLNS.stateChanged.connect(
            lambda: self.addSelectedPrueba("lns", self.seleccionView.checkBoxPruebaLNS))
        self.seleccionView.checkBoxPruebaD2.stateChanged.connect(
            lambda: self.addSelectedPrueba("d2", self.seleccionView.checkBoxPruebaD2))
        self.seleccionView.checkBoxPruebaHopkins.stateChanged.connect(
            lambda: self.addSelectedPrueba("hopkins", self.seleccionView.checkBoxPruebaHopkins))
        self.seleccionView.checkBoxPruebaStroop.stateChanged.connect(
            lambda: self.addSelectedPrueba("stroop", self.seleccionView.checkBoxPruebaStroop))
        self.seleccionView.checkBoxTorreDeLondres.stateChanged.connect(
            lambda: self.addSelectedPrueba("torreLondres", self.seleccionView.checkBoxTorreDeLondres))
        self.seleccionView.checkBoxPruebaMotivosDeportivos.stateChanged.connect(
            lambda: self.addSelectedPrueba("motivoDeportivo", self.seleccionView.checkBoxPruebaMotivosDeportivos))
        self.seleccionView.checkBoxPruebaDePittsburgh.stateChanged.connect(
            lambda: self.addSelectedPrueba("pittsburgh", self.seleccionView.checkBoxPruebaDePittsburgh))
        self.seleccionView.checkBoxPruebaSCL90.stateChanged.connect(
            lambda: self.addSelectedPrueba("scl90", self.seleccionView.checkBoxPruebaSCL90))

        self.seleccionView.pushButtonContinuar.clicked.connect(self.getData)

    def changeView(self):
        """
        Método encargado de notificar los elementos que serán pasados como parámetros a la siguiente vista
        """
        totalRoutes = self.initialRoutes + self.pruebasSeleccionadas + self.endRoutes
        self.switch_window.emit(self.invalidArgs, totalRoutes)

    def getData(self):
        if len(self.pruebasSeleccionadas) == 0:
            self.invalidArgs = ["ALMENOS SELECCIONAR UNA PRUEBA"]

        self.changeView()

    def emptyInvalidArgs(self):
        """
        Metodo para vaciar la lista de elementos invalidos
        """
        self.invalidArgs = list()

    def getListMenu(self):
        return None

    def getProgressBar(self):
        return None

    def newInfo(self):
        self.resetPruebas()
        self.seleccionView.checkBoxPruebaFluidezVerbal.setChecked(False)
        self.seleccionView.checkBoxPruebaDenominacion.setChecked(False)
        self.seleccionView.checkBoxComprensionVerbal.setChecked(False)
        self.seleccionView.checkBoxPruebaMemoriaVisoespacial.setChecked(False)
        self.seleccionView.checkBoxPruebaTMT.setChecked(False)
        self.seleccionView.checkBoxPruebaAbstraccion.setChecked(False)
        self.seleccionView.checkBoxPruebaDigitos.setChecked(False)
        self.seleccionView.checkBoxPruebaSDMT.setChecked(False)
        self.seleccionView.checkBoxPruebaLNS.setChecked(False)
        self.seleccionView.checkBoxPruebaD2.setChecked(False)
        self.seleccionView.checkBoxPruebaHopkins.setChecked(False)
        self.seleccionView.checkBoxPruebaStroop.setChecked(False)
        self.seleccionView.checkBoxTorreDeLondres.setChecked(False)
        self.seleccionView.checkBoxPruebaMotivosDeportivos.setChecked(False)
        self.seleccionView.checkBoxPruebaDePittsburgh.setChecked(False)
        self.seleccionView.checkBoxPruebaSCL90.setChecked(False)
        self.seleccionView.labelPruebasSeleccionadasDisplay.setText("0")

    def addSelectedPrueba(self, checkboxName, checkboxItem):
        if checkboxName not in self.pruebasSeleccionadas and checkboxItem.isChecked():
            self.pruebasSeleccionadas.append(checkboxName)
        elif checkboxName in self.pruebasSeleccionadas:
            self.pruebasSeleccionadas.remove(checkboxName)
        self.seleccionView.labelPruebasSeleccionadasDisplay.setText(
            str(len(self.pruebasSeleccionadas)))

    def resetPruebas(self):
        self.pruebasSeleccionadas = []
