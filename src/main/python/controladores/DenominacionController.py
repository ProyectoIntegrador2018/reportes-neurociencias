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

    def getDatos(self):
        """
        Metodo para tomar los datos ingresados en la prueba de denominacion
        """
        view = self.view
        denomimgs = view.sbDenomImg.value()
        # print("Valor denominacion imagenes: ", denomimgs)
        denomimgT = view.sbDenomImgT.value()
        # print("Valor denominacion imagenes T: ", denomimgT)

        valores = (denomimgs, denomimgT)

        self.test = DenominacionPrueba(valores)

        self.test.calcularPERP()
        self.changeView()