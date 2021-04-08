# controlador de la vista de Digitis
from PyQt5 import QtWidgets, QtCore
from vistas.DigitosWindowWidget import *
from MainWindowController import *
from ReporteModel import *
from pruebas.DigitosPrueba import *
from PruebaModel import *
from ControllerModel import *

class DigitosController(QtWidgets.QWidget, ControllerModel):
    # Atributo empleado para realizar el cambio de vista
    switch_window = QtCore.pyqtSignal(object, object, bool)

    def __init__(self, mainWindow, reporteModel=None):
        QtWidgets.QWidget.__init__(self)
        self.digitosView = DigitosWindowWidget(mainWindow)
        self.digitosView.pbStart.clicked.connect(self.getDatos)
        self.digitosView.backButton.clicked.connect(self.returnView)
        self.reporteModel = reporteModel
        self.invalidArgs = list()
    
    def returnView(self):
        """
		 Método encargado de notificar los elementos que serán pasados como parámetros a la siguiente vista
		"""
        self.switch_window.emit(self.invalidArgs, self.digitosPrueba, True)
	
    def changeView(self):
        self.switch_window.emit(self.invalidArgs, self.digitosPrueba, False)
    
    def getDatos(self):
        """
        Metodo para tomar los datos ingresados en la vista de Digitos
        """
        view = self.digitosView
        directos = view.sbDirectos.value()
        inversos = view.sbInversos.value()

        valores = (directos, inversos)

        self.digitosPrueba = DigitosPrueba(valores)

        datos = [self.reporteModel.reporte['educacion']]

        self.digitosPrueba.calcularPERP(datos)

        self.changeView()
    
    def emptyInvalidArgs(self):
        """
        Metodo para vaciar la lista de elementos invalidos
        """
        self.invalidArgs = list()
    
    def addInvalidArgs(self,arg):
        """
        Metodo para agregar elementos invalidos
        arg = el string a añadir
        """
        if len(self.invalidArgs) == 0:
            self.invalidArgs = [arg]
        else:
            tempList = self.invalidArgs
            tempList.append(arg)
            self.invalidArgs = tempList
    
    def getListMenu(self):
        """
		 Método que se regresa el id del menu en la vista de Digitos
		"""
        return self.digitosView.lWVistas

    def getProgressBar(self):
        """
         Método que se encarga de regresar el valor de la barra de progreso
        """
        return self.digitosView.progressBar

    def updateButtonText(self, text):
        """
         Método que se encarga de actulaizar el texto del botón de la vista
        """
        self.digitosView.pbStart.setText(text)


#Pruebas unitarias
#if __name__ == "__main__":
#    import sys
#    app = QtWidgets.QApplication(sys.argv)
#    digitosWindow = QtWidgets.QWidget()
#    digitosController = DigitosController(digitosWindow)
#    digitosWindow.show()
#    sys.exit(app.exec_())