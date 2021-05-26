from PyQt5 import QtCore
from vistas.DigitosWindowWidget import DigitosWindowWidget
from pruebas.DigitosPrueba import DigitosPrueba
from .mixins import WindowControllerMixin

class DigitosController(WindowControllerMixin):
    # Atributo empleado para realizar el cambio de vista
    switch_window = QtCore.pyqtSignal(object, object, bool)

    def getWidgetClass(self):
       return DigitosWindowWidget

    def getTestClass(self):
        return DigitosPrueba

    def setField(self, data):
        view = self.view
        view.sbDirectos.setValue(data['sbDirectos'])
        view.sbInversos.setValue(data['sbInversos'])

    def getDatos(self):
        """
        Metodo para tomar los datos ingresados en la vista de Digitos
        """
        view = self.view
        directos = view.sbDirectos.value()
        inversos = view.sbInversos.value()

        valores = (directos, inversos)

        self.test = DigitosPrueba(valores)

        datos = [self.reporteModel.reporte['educacion'],self.reporteModel.reporte['edad']]

        self.test.calcularPERP(datos)

        self.changeView()