# Contolador de la vista de Torre de Londres
from PyQt5 import QtWidgets, QtCore
from vistas.PittsburghWindowWidget import *
from MainWindowController import *
from ReporteModel import *
from pruebas.PittsburghPrueba import *
from PruebaModel import *
from ControllerModel import *
from .mixins import WindowControllerMixin

class PittsburghController(WindowControllerMixin):
    switch_window = QtCore.pyqtSignal(object, object, bool)

    def getWidgetClass(self):
        return PittsburghWindowWidget

    def getDatos(self):
        """
        Metodo para tomar los datos ingresados en la prueba de memoria visoespacia
        """
        view = self.view

        comp1 = view.comp1.value()
        comp2 = view.comp2.value()
        comp3 = view.comp3.value()
        comp4 = view.comp4.value()
        comp5 = view.comp5.value()
        comp6 = view.comp6.value()
        comp7 = view.comp7.value()

        valores = (comp1,comp2,comp3,comp4,comp5,comp6,comp7)
        
        self.test = PittsburghPrueba(valores)

        datos = [self.reporteModel.reporte['educacion'], self.reporteModel.reporte['edad']]

        self.test.calcularPERP(datos)
        self.changeView()