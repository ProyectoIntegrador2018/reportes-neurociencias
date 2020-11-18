from PyQt5 import QtWidgets, QtCore
from pruebas.SDMTPrueba import *
from vistas.SDMTWindowWidget import *
from ReporteModel import *
from ControllerModel import *

class SDMTController(QtWidgets.QWidget, ControllerModel):
    switch_window = QtCore.pyqtSignal(object, object)

    def __init__(self, mainWindow, ReporteModel = None):
        QtWidgets.QWidget.__init__(self)
        self.sdmtView = SDMTWindowWidget(mainWindow)
        self.sdmtView.pbStart.clicked.connect(self.getDatos)
        self.reporteModel = ReporteModel
        self.invalidArgs = list()
    

    def changeView(self):
        self.switch_window.emit(self.invalidArgs, self.sdmtPrueba)
    

    def getDatos(self):
        view = self.sdmtView
        sdmtVal = view.sbSDMT.value()

        valores = (sdmtVal)

        self.sdmtPrueba = SDMTPrueba(valores)

        datos = [self.reporteModel.reporte['educacion']]

       
        self.sdmtPrueba.calcularPERP(datos)
        
        self.changeView()
    

    def emptyInvalidArgs(self):
        self.invalidArgs = list()
    

    def addInvalidArgs(self, arg):
        if len(self.invalidArgs) == 0:
            self.invalidArgs = [arg]
        else:
            tempList = self.invalidArgs
            tempList.append(arg)
            self.invalidArgs = tempList
    

    def getListMenu(self):
        return self.sdmtView.lWVistas

    def getProgressBar(self):
        """
         Método que se encarga de regresar el valor de la barra de progreso
        """
        return self.sdmtView.progressBar

    def updateButtonText(self, text):
        """
         Método que se encarga de actulaizar el texto del botón de la vista
        """
        self.sdmtView.pbStart.setText(text)
    
# Pruebas unitarias
# if __name__ == "__main__":
#    import sys
#    app = QtWidgets.QApplication(sys.argv)
#    sdmtWindow = QtWidgets.QWidget()
#    fluidezVerbalController = SDMTController(sdmtWindow)
#    sdmtWindow.show()
#    sys.exit(app.exec_())
