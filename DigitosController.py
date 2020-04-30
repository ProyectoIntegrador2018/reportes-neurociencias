# controlador de la vista de Digitis
from PyQt5 import QtWidgets, QtCore
from DigitosWindowWidget import *
from MainWindowController import *
from ReporteModel import *
from DigitosPrueba import *
from PruebaModel import *
from ControllerModel import *

class DigitosController(QtWidgets.QWidget, ControllerModel):
    switch_window = QtCore.pyqtSignal(object, object)

    def __init__(self, mainWindow, reporteModel=None):
        QtWidgets.QWidget.__init__(self)
        self.digitosView = DigitosWindowWidget(mainWindow)
        self.digitosView.pbStart.clicked.connect(self.getDatos)
        self.reporteModel = reporteModel
        self.invalidArgs = list()
    
    def changeView(self):
        print("ando en changeView de Prueba Digitos")
        self.switch_window.emit(self.invalidArgs, self.digitosPrueba)
    
    def getDatos(self):
        """
        Metodo para tomar los datos ingresados en la vista de Digitos
        """
        view = self.digitosView
        directos = view.sbDirectos.value()
        inversos = view.sbInversos.value()

        valores = (directos, inversos)

        self.digitosPrueba = DigitosPrueba(valores)

        # datos = [self.reporteModel.reporte['educacion']]
        datos = 8

        self.digitosPrueba.calcularPERP(datos)

        self.changeView()
    
    def getListMenu(self):
        """
		 Método que se regresa el id del menu en la vista de Digitos
		"""
        return self.digitosView.lWVistas


#Pruebas unitarias
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    digitosWindow = QtWidgets.QWidget()
    digitosController = DigitosController(digitosWindow)
    digitosWindow.show()
    sys.exit(app.exec_())