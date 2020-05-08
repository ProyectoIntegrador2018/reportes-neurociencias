from PyQt5 import QtWidgets, QtCore
from vistas.MemoriaVisoespaciaWidget import *
from MainWindowController import *
from ReporteModel import *
from pruebas.MemoriaVisoespaciaPrueba import *
from PruebaModel import *
from ControllerModel import *


class MemoriaVisoespaciaController(QtWidgets.QWidget,ControllerModel):
    switch_window = QtCore.pyqtSignal(object, object)

    def __init__(self, mainWindow, reporteModel=None):
        QtWidgets.QWidget.__init__(self)
        self.memoriaVisoespaciaView = MemoriaVisoespaciaWidget(mainWindow)
        self.memoriaVisoespaciaView.pbStart.clicked.connect(self.getDatos)
        self.reporteModel = reporteModel
        self.invalidArgs = list()
    
    def changeView(self):
        """
        Metodo de notificar los elementos que seran pasados a la siguiene vista como parametros
        """
        self.switch_window.emit(self.invalidArgs, self.memoriaVisoespaciaPrueba)
    
    def getDatos(self):
        """
        Metodo para tomar los datos ingresados en la prueba de memoria visoespacia
        """
        view = self.memoriaVisoespaciaView
        total = view.sbDenomImg.value()
        delayed = view.sbDenomImgT.value()
        

        valores = [total, delayed]

        self.memoriaVisoespaciaPrueba = MemoriaVisoespaciaPrueba(valores)

        datos = self.reporteModel.reporte['edad']

        self.memoriaVisoespaciaPrueba.calcularPERP(datos)

        self.changeView()
    
    def getListMenu(self):
        """
        Regresa el id del menu en la vista Memoria visoespacia
        """
        return self.memoriaVisoespaciaView.lWVistas

    def getProgressBar(self):
        """
         Método que se encarga de regresar el valor de la barra de progreso
        """
        return self.memoriaVisoespaciaView.progressBar




#Pruebas unitarias
# if __name__ == "__main__":
#     import sys
#     app = QtWidgets.QApplication(sys.argv)
#     memoriaVisoespaciaWindow = QtWidgets.QWidget()
#     memoriaVisoespaciaController = MemoriaVisoespaciaController(memoriaVisoespaciaWindow)
#     memoriaVisoespaciaWindow.show()
#     sys.exit(app.exec_())


