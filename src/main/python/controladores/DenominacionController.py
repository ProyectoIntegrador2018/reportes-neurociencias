from PyQt5 import QtWidgets, QtCore
from vistas.DenominacionWidget import DenominacionWidget
# from MainWindowController import *
# from ReporteModel import *
from pruebas.DenominacionPrueba import DenominacionPrueba
# from PruebaModel import *
from ControllerModel import * 

class DenominacionController(QtWidgets.QWidget, ControllerModel):
    # Atributo empleado para realizar el cambio de vista
    switch_window = QtCore.pyqtSignal(object, object, bool)

    def __init__(self, mainWindow, reporteModel=None):
        QtWidgets.QWidget.__init__(self)
        self.denominacionView = DenominacionWidget(mainWindow)
        self.denominacionView.pbStart.clicked.connect(self.getDatos)
        self.denominacionView.backButton.clicked.connect(self.returnView)
        self.reporteModel = reporteModel
        self.invalidArgs = list()
    
    def returnView(self):
        """
		 Método encargado de notificar los elementos que serán pasados como parámetros a la siguiente vista
		"""
        self.switch_window.emit(self.invalidArgs, self.denominacionPrueba, True)
	
    def changeView(self):
        """
        Metodo de notificar los elementos que seran pasados a la siguiene vista como parametros
        """
        # print("Ando en changeView de Denominacion")
        self.switch_window.emit(self.invalidArgs, self.denominacionPrueba, False)
    
    def getDatos(self):
        """
        Metodo para tomar los datos ingresados en la prueba de denominacion
        """
        view = self.denominacionView
        denomimgs = view.sbDenomImg.value()
        # print("Valor denominacion imagenes: ", denomimgs)
        denomimgT = view.sbDenomImgT.value()
        # print("Valor denominacion imagenes T: ", denomimgT)

        valores = (denomimgs, denomimgT) 

        self.denominacionPrueba = DenominacionPrueba(valores)

        self.denominacionPrueba.calcularPERP()


        self.changeView()

    
    def getListMenu(self):
        """
        Regresa el id del meni en la vista Denominacion
        """
        return self.denominacionView.lWVistas

    def getProgressBar(self):
        """
         Método que se encarga de regresar el valor de la barra de progreso
        """
        return self.denominacionView.progressBar

    def updateButtonText(self, text):
        """
         Método que se encarga de actulaizar el texto del botón de la vista
         Args:
          text: Objeto de tipo str que contiene el nuevo valor a asignar al botón presente en las pruebas
        """
        self.denominacionView.pbStart.setText(text)


# Pruebas unitarias
#if __name__ == "__main__":
#    import sys
#    app = QtWidgets.QApplication(sys.argv)
#    denominacionWindow = QtWidgets.QWidget()
#    denominacionController = DenominacionController(denominacionWindow)
#    denominacionWindow.show()
#    sys.exit(app.exec_())
