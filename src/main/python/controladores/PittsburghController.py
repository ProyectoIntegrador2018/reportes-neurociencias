# Contolador de la vista de Torre de Londres
from PyQt5 import QtWidgets, QtCore
from vistas.PittsburghWindowWidget import *
from MainWindowController import *
from ReporteModel import *
from pruebas.PittsburghPrueba import *
from PruebaModel import *
from ControllerModel import *

class PittsburghController(QtWidgets.QWidget, ControllerModel):
    switch_window = QtCore.pyqtSignal(object, object, bool)

    def __init__(self, mainWindow, reporteModel = None):
        QtWidgets.QWidget.__init__(self)
        self.pittsburghView = PittsburghWindowWidget(mainWindow)
        self.pittsburghView.pbStart.clicked.connect(self.getDatos)
        self.pittsburghView.backButton.clicked.connect(self.returnView)
        self.reporteModel = reporteModel
        self.invalidArgs = list()

    def returnView(self):
        """
		 Método encargado de notificar los elementos que serán pasados como parámetros a la siguiente vista
		"""
        self.switch_window.emit(self.invalidArgs, self.pittsburghPrueba, True)
	
    def changeView(self):
        """
        Método encargado de notificar los elementos que serán pasados como parámetros a la siguiente vista
        """
        self.switch_window.emit(self.invalidArgs, self.pittsburghPrueba, False)
    

    def getDatos(self):
        view = self.pittsburghView

        comp1 = view.comp1.value()
        comp2 = view.comp2.value()
        comp3 = view.comp3.value()
        comp4 = view.comp4.value()
        comp5 = view.comp5.value()
        comp6 = view.comp6.value()
        comp7 = view.comp7.value()

        valores = (comp1,comp2,comp3,comp4,comp5,comp6,comp7)

        # print("VALORES")
        # print(valores)
        
        self.pittsburghPrueba = PittsburghPrueba(valores)

        datos = [self.reporteModel.reporte['educacion'], self.reporteModel.reporte['edad']]
        # datos = [19, 31]

        self.pittsburghPrueba.calcularPERP(datos)
        self.changeView()

    def emptyInvalidArgs(self):
        """
        Método que se encarga de vacíar la lista de elementos inválidos en la vista
        """
        self.invalidArgs = list()
    
    def addInvalidArg(self, arg):
        """
        Método que se encarga de añadir a la lista de elementos inválidos, aquel parámetro especificado
        Args:
        arg: String a añadir a la lista de elementos inválidos
        """
        
        if len(self.invalidArgs) == 0:
            self.invalidArgs = [arg]
        else:
            tempList = self.invalidArgs
            tempList.append(arg)
            self.invalidArgs = tempList
    
    def getListMenu(self):
        """
        Método que se regresa el id del menu en la vista de Butt
        """
        return self.pittsburghView.lWVistas
    
    def getProgressBar(self):
        """
        Método que se encarga de regresar el valor de la barra de progreso
        """
        return self.pittsburghView.progressBar
    
    def updateButtonText(self, text):
        """
        Método que se encarga de actulaizar el texto del botón de la vista
        """
        self.pittsburghView.pbStart.setText(text)

# Pruebas unitarias
#if __name__ == "__main__":
#    import sys
#    app = QtWidgets.QApplication(sys.argv)
#    buttWindow = QtWidgets.QWidget()
#    buttController = ButtController(buttWindow)
#    buttWindow.show()
#    sys.exit(app.exec_())