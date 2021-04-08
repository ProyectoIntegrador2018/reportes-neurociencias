# Contolador de la vista de Torre de Londres
from PyQt5 import QtWidgets, QtCore
from vistas.TOLWindowWidget import *
from MainWindowController import *
from ReporteModel import *
from pruebas.TOLPrueba import *
from PruebaModel import *
from ControllerModel import *

class TOLController(QtWidgets.QWidget, ControllerModel):
    switch_window = QtCore.pyqtSignal(object, object, bool)

    def __init__(self, mainWindow, reporteModel = None):
        QtWidgets.QWidget.__init__(self)
        self.tolView = TOLWindowWidget(mainWindow)
        self.tolView.pbStart.clicked.connect(self.getDatos)
        self.tolView.backButton.clicked.connect(self.returnView)
        self.reporteModel = reporteModel
        self.invalidArgs = list()
    
    def returnView(self):
        """
		 Método encargado de notificar los elementos que serán pasados como parámetros a la siguiente vista
		"""
        self.switch_window.emit(self.invalidArgs, self.tolPrueba, True)

    def changeView(self):
        """
        Método encargado de notificar los elementos que serán pasados como parámetros a la siguiente vista
        """
        self.switch_window.emit(self.invalidArgs, self.tolPrueba, False)
    

    def getDatos(self):
        view = self.tolView

        totalCorrectos = view.sbTotalCorrectos.value()
        movimientosTotales = view.sbMovimientosTotales.value()
        tiempoLatencia = view.sbTiempoLatencia.value()
        tiempoEjecucion = view.sbTiempoEjecucion.value()
        tiempoResolucion = view.sbTiempoResolucion.value()
        vt = view.sbVT.value()
        vr = view.sbVR.value()

        valores = (totalCorrectos, movimientosTotales,
                tiempoLatencia, tiempoEjecucion, tiempoResolucion,
                vt, vr)

        # print("VALORES")
        # print(valores)
        
        self.tolPrueba = TOLPrueba(valores)

        datos = [self.reporteModel.reporte['educacion'], self.reporteModel.reporte['edad']]
        # datos = [19, 31]

        self.tolPrueba.calcularPERP(datos)
        self.changeView()
    

    def getListMenu(self):
        """
        Metodo que regresa el id del menu en la vista de Torre de Londres
        """
        return self.tolView.lWVistas
    

    def emptyInvalidArgs(self):
        """
        Metodo para vaciar la lista de elementos invalidos
        """
        self.invalidArgs = list()
    

    def getProgressBar(self):
        """
		 Método que se encarga de regresar el valor de la barra de progreso
		"""
        return self.tolView.progressBar

    def updateButtonText(self, text):
        """
         Método que se encarga de actulaizar el texto del botón de la vista
        """
        self.tolView.pbStart.setText(text)


# Pruebas unitarias
if __name__ == "__main__":
   import sys
   app = QtWidgets.QApplication(sys.argv)
   tolWindow = QtWidgets.QWidget()
   tolController = TOLController(tolWindow)
   tolWindow.show()
   sys.exit(app.exec_())