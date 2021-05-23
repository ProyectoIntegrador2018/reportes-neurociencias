from PyQt5 import QtCore
from vistas.DenominacionWidget import DenominacionWidget
from pruebas.DenominacionPrueba import DenominacionPrueba
from .mixins import WindowControllerMixin

class DenominacionController(WindowControllerMixin):
    # Atributo empleado para realizar el cambio de vista
    switch_window = QtCore.pyqtSignal(object, object, bool)
    
    def getWidgetClass(self):
	    return DenominacionWidget

    def getTestClass(self):
        return DenominacionPrueba

    def setField(self, data):
        view = self.view
        view.sbDenomImg.setValue(data['sbDenomImg'])
        view.sbDenomImgT.setValue(data['sbDenomImgT'])

    def getDatos(self):
        """
        Metodo para tomar los datos ingresados en la prueba de denominacion
        """
        view = self.view
        denomimgs = view.sbDenomImg.value()
        denomimgT = view.sbDenomImgT.value()

        valores = (denomimgs, denomimgT)

        self.test = DenominacionPrueba(valores)

        self.test.calcularPERP()
        self.changeView()