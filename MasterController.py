#Controlador principal de todo el programa
from MainWindowController import *
from MVCController import *
from ModalController import *

class MasterController:
	def __init__(self):
		self.mainWindow = QtWidgets.QWidget()
		self.modalController = ModalController()
		self.currentWindow = self.mainWindow
		self.nextWindow = self.mainWindow

	def loadView(self):
		"""
		 Método que se encarga de mostrar la siguiente vista y de esconder la previa
		"""
		self.currentWindow.close()
		self.nextWindow.show()

	def connectMenu(self, currentController):
		"""
		 Método que se encarga de conectar el menú con la vista del controlador actual
		"""
		self.listMenu = currentController.getListMenu()
		self.menuController = MenuController(self.listMenu)


	def showMainWindow(self):
		"""
		 Método que se encarga de cargar la vista de la pantalla a MainWindow, así como el controlador de la misma.
		"""
		self.mainWindowController = MainWindowController(self.mainWindow)
		self.currentWindow = self.mainWindow
		self.mainWindowController.switch_window.connect(self.showMVC)
		self.connectMenu(self.mainWindowController)
		self.loadView()

	#Actualizar para que la primera prueba a llenar sea la que reciba el reporte como paramatro
	def showMVC(self, listMissingElem, reporte):
		"""
		 Método que se encarga de cargar la vista de la pantalla Material Verbal Complejo, así como el controlador de la misma.
		 Args:
		  listMissingElem: Elementos del reporte que no han sido llenados
		  reporte: Tipo de dato ReporteModel que ha sido exitosamente creado
		"""

		self.reporteModel = reporte
		self.MVCWindow = QtWidgets.QWidget()
		self.MVCController = MVCController(self.MVCWindow)
		self.MVCController.switch_window.connect(self.tempEnd)
			
		
		if(len(listMissingElem) != 0):
			self.modalController.setWindowTitle("Elementos no válidos")
			self.modalController.setHeader("Elementos:")
			self.modalController.setContenido(listMissingElem)
			self.modalController.showModal()
			self.mainWindowController.emptyMissingArgs()

		else:
			print("Toda la info fue llenada")
			self.reporteModel.printReporte()
		
			self.nextWindow = self.MVCWindow
			self.connectMenu(self.MVCController)
			self.loadView()

	def tempEnd(self, invalidArgs, MVCPrueba):
		if len(invalidArgs) != 0:
			self.modalController.setHeader("Deben de ser mayor a 0:")
			self.modalController.setContenido(invalidArgs)
			self.modalController.showModal()
			self.MVCController.emptyInvalidArgs()
		else:
			self.reporteModel.addPrueba(MVCPrueba)
			self.reporteModel.printReporte()
			

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
