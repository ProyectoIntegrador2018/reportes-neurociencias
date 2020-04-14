#Controlador principal de todo el programa
from MainWindowController import *
from FluidezVerbalController import *
from ModalController import *
from MenuController import *
from DenominacionController import *

class MasterController:
	def __init__(self):
		self.modalController = ModalController()

		self.dummyWindow = QtWidgets.QWidget()
		self.mainWindow = QtWidgets.QWidget()
		self.fluidezWindow = QtWidgets.QWidget()
		
		self.mainWindowController = MainWindowController(self.mainWindow)
		
		self.paginasVisitadas = [0]
		self.listMenu = self.mainWindowController.getListMenu()
		
		self.menuController = MenuController(self.paginasVisitadas)
		self.menuController.switch_window.connect(self.showSpecificWindowMenu)

		self.currentWindow = self.dummyWindow
		self.nextWindow = self.mainWindow
		self.ventanaMostrada = 0

	def addPaginaVisitada(self, numPag):
		"""
		 Método que se encarga de marcar cuáles páginas han sido visitadas
		 Args:
		  numPag: Número de página que ha sido visitada
		"""
		tempList = self.paginasVisitadas
		tempList.append(numPag)
		self.paginasVisitadas = tempList


	def loadView(self):
		"""
		 Método que se encarga de mostrar la siguiente vista y de esconder la previa
		"""
		self.currentWindow.close()
		self.nextWindow.show()
		self.currentWindow = self.nextWindow

	def connectMenu(self, currentController):
		"""
		 Método que se encarga de conectar el menú con la vista del controlador actual
		"""
		self.menuController.clearMenu()
		self.listMenu = currentController.getListMenu()
		self.menuController = MenuController(self.listMenu)
		self.menuController.updateListView(self.listMenu)
		self.menuController.poblarLista()


	def showSpecificWindowMenu(self, elemSelected):
		"""
		 Método que se encarga de manejar el doble click sobre un elemento del menú
		 Args:
		  elemSelected: Lista que contiene el elemento seleccionado
		"""
		if elemSelected == 0:
			self.nextWindow = self.mainWindow
			currentController = self.mainWindowController
			self.menuController.updateCurrentWindow(0)
		if elemSelected == 1:
			self.nextWindow = self.fluidezWindow
			currentController = self.fluidezVerbalController
			self.menuController.updateCurrentWindow(1)
		if elemSelected == 2:
			self.nextWindow = self.denominacionWindow
			currentController = self.denominacionController
			self.menuController.updateCurrentWindow(2)
			
		if self.windowsAreDifferent():
			self.connectMenu(currentController)
			self.loadView()


	def windowsAreDifferent(self):
		"""
		 Método que evalúa si las variables de currentWindow y nextWindow son diferentes
		"""
		return self.currentWindow != self.nextWindow

	def showMainWindow(self):
		"""
		 Método que se encarga de cargar la vista de la pantalla a MainWindow, así como el controlador de la misma.
		"""
		self.mainWindowController.switch_window.connect(self.showFluidezVerbal)
		self.showSpecificWindowMenu(0)

	###Actualizar para que la primera prueba a llenar sea la que reciba el reporte como paramatro
	def showFluidezVerbal(self, listMissingElem, reporte):
		"""
		 Método que se encarga de cargar la vista de la pantalla Fluidez Verbal, así como el controlador de la misma.
		 Args:
		  listMissingElem: Elementos del reporte que no han sido llenados
		  reporte: Tipo de dato ReporteModel que ha sido exitosamente creado
		"""
		self.reporteModel = reporte
		
		self.fluidezVerbalController = FluidezVerbalController(self.fluidezWindow, self.reporteModel)
		self.fluidezVerbalController.switch_window.connect(self.showDenominacion)
				
			
		if(len(listMissingElem) != 0):
			self.modalController.setWindowTitle("Elementos no válidos")
			self.modalController.setHeader("Elementos:")
			self.modalController.setContenido(listMissingElem)
			self.modalController.showModal()
			self.mainWindowController.emptyMissingArgs()
		else:
			print("Toda la info fue llenada")
			self.reporteModel.printReporte()
			self.addPaginaVisitada(1)
			self.menuController.updatePagesVisited(self.paginasVisitadas)
			
			self.showSpecificWindowMenu(1)
	
	def showDenominacion(self, invalidArgs, fluidezVerbalPrueba):
		self.denominacionWindow = QtWidgets.QWidget()
		self.denominacionController = DenominacionController(self.denominacionWindow)
		self.denominacionController.switch_window.connect(self.tempEnd)

		if len(invalidArgs) != 0:
			self.modalController.setHeader("Deben de ser mayor a 0:")
			self.modalController.setContenido(invalidArgs)
			self.modalController.showModal()
			self.fluidezVerbalController.emptyInvalidArgs()
		else:
			self.reporteModel.addPrueba(fluidezVerbalPrueba)
			self.reporteModel.printReporte()
		# self.nextWindow = self.denominacionWindow
		# self.connectMenu(self.denominacionController)
		# self.loadView()
		self.addPaginaVisitada(2)
		self.menuController.updatePagesVisited(self.paginasVisitadas)
		self.showSpecificWindowMenu(2)

	def tempEnd(self, invalidArgs, denominacionPrueba):
		if len(invalidArgs) != 0:
			self.modalController.setHeader("Deben de ser mayor a 0:")
			self.modalController.setContenido(invalidArgs)
			self.modalController.showModal()
			self.fluidezVerbalController.emptyInvalidArgs()
		else:
			self.reporteModel.addPrueba(denominacionPrueba)
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