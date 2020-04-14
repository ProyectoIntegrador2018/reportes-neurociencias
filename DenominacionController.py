from PyQt5 import QtWidgets, QtCore
from DenominacionWidget import *
from MainWindowController import *
from ReporteModel import *
from DenominacionPrueba import *
from PruebaModel import *
from ControllerModel import * 

class DenominacionController(QtWidgets.QWidget, ControllerModel):
    switch_window = QtCore.pyqtSignal(object, object)

    def __init__(self, mainWindow, reporteModel=None):
        QtWidgets.QWidget.__init__(self)
        self.denominacionView = DenominacionWidget(mainWindow)
        self.denominacionView.pbStart.clicked.connect(self.getDatos)
        self.reporteModel = reporteModel
        self.invalidArgs = list()
    
    def changeView(self):
        """
        Metodo de notificar los elementos que seran pasados a la siguiene vista como parametros
        """
        print("Ando en changeView de Denominacion")
        self.switch_window.emit(self.invalidArgs, self.denominacionPrueba)
    
    def getDatos(self):
        """
        Metodo para tomar los datos ingresados en la prueba de denominacion
        """
        view = self.denominacionView
        denomimgs = view.sbDenomImg.value()
        print("Valor denominacion imagenes: ", denomimgs)
        denomimgT = view.sbDenomImgT.value()
        print("Valor denominacion imagenes T: ", denomimgT)

        valores = (denomimgs, denomimgT) 

        self.denominacionPrueba = DenominacionPrueba(valores)

        self.denominacionPrueba.calcularPERP()


        self.changeView()
    
    def getListMenu(self):
        """
        Regresa el id del meni en la vista Denominacion
        """
        return self.denominacionView.lWVistas




# Pruebas unitarias
# if __name__ == "__main__":
#     import sys
#     app = QtWidgets.QApplication(sys.argv)
#     denominacionWindow = QtWidgets.QWidget()
#     denominacionController = DenominacionController(denominacionWindow)
#     denominacionWindow.show()
#     sys.exit(app.exec_())
