from PyQt5 import QtWidgets, QtCore
from vistas.MemoriaVisoespaciaWidget import *
from MainWindowController import *
from ReporteModel import *
from pruebas.MemoriaVisoespaciaPrueba import *
# from PruebaModel import *

class MemoriaVisoespaciaController(QtWidgets.QWidget):
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
        print("Ando en changeView de MemoriaVisoespacia")
        self.switch_window.emit(self.invalidArgs, self.memoriaVisoespaciaPrueba)
    
    def getDatos(self):
        """
        Metodo para tomar los datos ingresados en la prueba de memoria visoespacia
        """
        view = self.memoriaVisoespaciaView
        total_recall = view.sbDenomImg.value()
        print("Valor total recall: ", total_recall)
        delayed_recall = view.sbDenomImgT.value()
        print("Valor delayed recall: ", delayed_recall)

        valores = (total_recall, delayed_recall)

        self.memoriaVisoespaciaPrueba = MemoriaVisoespaciaPrueba(valores)

        self.memoriaVisoespaciaPrueba.calcularPERP()

        self.changeView()
    
    def getListMenu(self):
        """
        Regresa el id del menu en la vista Memoria visoespacia
        """
        return self.memoriaVisoespaciaView.lWVistas




#Pruebas unitarias
# if __name__ == "__main__":
#     import sys
#     app = QtWidgets.QApplication(sys.argv)
#     memoriaVisoespaciaWindow = QtWidgets.QWidget()
#     memoriaVisoespaciaController = MemoriaVisoespaciaController(memoriaVisoespaciaWindow)
#     memoriaVisoespaciaWindow.show()
#     sys.exit(app.exec_())


