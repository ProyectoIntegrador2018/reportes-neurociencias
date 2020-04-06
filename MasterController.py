#Controlador principal de todo el programa
from MainWindowController import *
from FluidezVerbalController import *
from ModalController import *

class MasterController:
	def __init__(self):
		self.mainWindow = QtWidgets.QWidget()
		self.modalController = ModalController()


	def showMainWindow(self):
		"""
		 Método que se encarga de cargar la vista de la pantalla a MainWindow, así como el controlador de la misma.
		"""
		self.mainWindowController = MainWindowController(self.mainWindow)
		self.mainWindowController.switch_window.connect(self.showFluidezVerbal)
		self.mainWindow.show()

	#Actualizar para que la primera prueba a llenar sea la que reciba el reporte como paramatro
	def showFluidezVerbal(self, listMissingElem, reporte):
		"""
		 Método que se encarga de cargar la vista de la pantalla Fluidez Verbal, así como el controlador de la misma.
		 Args:
		  listMissingElem: Elementos del reporte que no han sido llenados
		  reporte: Tipo de dato ReporteModel que ha sido exitosamente creado
		"""

		self.reporteModel = reporte
		self.fluidezWindow = QtWidgets.QWidget()
		#self.fluidezWindow.switch_window.connect()
		
		if(len(listMissingElem) != 0):
			self.modalController.setWindowTitle("Falta llenar elementos")
			self.modalController.setHeader("Hay elementos vacíos")
			self.modalController.setContenido(listMissingElem)
			self.modalController.showModal()
			self.mainWindowController.emptyMissingArgs()

		else:
			print("Toda la info fue llenada")
			self.fluidezVerbalController = FluidezVerbalController(self.fluidezWindow, self.reporteModel)
			self.reporteModel.printReporte()
		
			self.mainWindow.close()
			self.fluidezWindow.show()

def main():
	"""
	 Método principal en la ejecución del programa
	"""
    app = QtWidgets.QApplication(sys.argv)
    masterController = MasterController()
    masterController.showMainWindow()
    sys.exit(app.exec_())

if __name__ == '__main__':
	main()
