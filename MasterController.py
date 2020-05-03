#Controlador principal de todo el programa
from MainWindowController import *
from ModalController import *
from MenuController import *
from controladores.FluidezVerbalController import *
from controladores.DenominacionController import *
from controladores.MVCController import *
from controladores.MemoriaVisoespaciaController import *
from controladores.DigitosController import *
from controladores.TMTController import *
from controladores.AbstraccionController import *

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
		if elemSelected == 3:
			self.nextWindow = self.MVCWindow
			currentController = self.mvcController
			self.menuController.updateCurrentWindow(3)
		if elemSelected == 4:
			self.nextWindow = self.memoriaVisoespaciaWindow
			currentController = self.memoriaVisoespaciaController
			self.menuController.updateCurrentWindow(4)
		if elemSelected == 5:
			self.nextWindow = self.tmtWindow
			currentController = self.tmtController
			self.menuController.updateCurrentWindow(5)
		if elemSelected == 6:
			self.nextWindow = self.abstraccionWindow
			currentController = self.abstraccionController
			self.menuController.updateCurrentWindow(6)
		if elemSelected == 7:
			self.nextWindow = self.digitosView
			currentController = self.digitosController
			self.menuController.updateCurrentWindow(7)

			
		if self.windowsAreDifferent():
			self.connectMenu(currentController)
			self.loadView()


	def windowsAreDifferent(self):
		"""
		 Método que evalúa si las variables de currentWindow y nextWindow son diferentes
		"""
		return self.currentWindow != self.nextWindow

	def displayModal(self, listMissingElem, modalTitle="Elementos no válidos", modalHeader="Elementos: "):
		self.modalController.setWindowTitle(modalTitle)
		self.modalController.setHeader(modalHeader)
		self.modalController.setContenido(listMissingElem)
		self.modalController.showModal()

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
			self.displayModal(listMissingElem)
			self.mainWindowController.emptyMissingArgs()
		else:
			print("Toda la info fue llenada")
			self.reporteModel.printReporte()
			self.addPaginaVisitada(1)
			self.menuController.updatePagesVisited(self.paginasVisitadas)
			
			self.showSpecificWindowMenu(1)

	
	def showDenominacion(self, invalidArgs, fluidezVerbalPrueba):
		"""
		Metodo que se encarga de cargar la vista y el controlador de la prueba de Denominacion
		"""
		self.denominacionWindow = QtWidgets.QWidget()
		self.denominacionController = DenominacionController(self.denominacionWindow)
		self.denominacionController.switch_window.connect(self.showMVC)

		if len(invalidArgs) != 0:
			self.displayModal(invalidArgs, modalHeader="Deben de ser mayor a 0:")
			self.fluidezVerbalController.emptyInvalidArgs()
		else:
			self.reporteModel.addPrueba(fluidezVerbalPrueba)
			#self.reporteModel.printReporte()

			self.addPaginaVisitada(2)
			self.menuController.updatePagesVisited(self.paginasVisitadas)
			self.showSpecificWindowMenu(2)

	def showMVC(self, invalidArgs, denominacionPrueba):
		self.MVCWindow = QtWidgets.QWidget()
		self.mvcController = MVCController(self.MVCWindow)
		self.mvcController.switch_window.connect(self.showMemoriaVisoespacia)

		if len(invalidArgs) != 0:
			self.displayModal(invalidArgs)
			self.denominacionController.emptyInvalidArgs()
		else:
			denominacionPrueba.printInfo()
			self.reporteModel.addPrueba(denominacionPrueba)
			#self.reporteModel.printReporte()

			self.addPaginaVisitada(3)
			self.menuController.updatePagesVisited(self.paginasVisitadas)
			self.showSpecificWindowMenu(3)


	def showMemoriaVisoespacia(self, invalidArgs, MVCPrueba):
		self.memoriaVisoespaciaWindow = QtWidgets.QWidget()
		self.memoriaVisoespaciaController = MemoriaVisoespaciaController(self.memoriaVisoespaciaWindow)
		self.memoriaVisoespaciaController.switch_window.connect(self.showTMT)

		if len(invalidArgs) != 0:
			self.displayModal(invalidArgs)
			self.mvcController.emptyInvalidArgs()
		else:
			MVCPrueba.printInfo()
			self.reporteModel.addPrueba(MVCPrueba)
			#self.reporteModel.printReporte()

			self.addPaginaVisitada(4)
			self.menuController.updatePagesVisited(self.paginasVisitadas)
			self.showSpecificWindowMenu(4)

	def showTMT(self, invalidArgs, memoriaVisoespaciaPrueba):
		self.tmtWindow = QtWidgets.QWidget()
		self.tmtController = TMTController(self.tmtWindow, self.reporteModel)
		self.tmtController.switch_window.connect(self.showAbstraccion)

		if len(invalidArgs) != 0:
			self.displayModal(invalidArgs)
			self.memoriaVisoespaciaController.emptyInvalidArgs()
		else:
			memoriaVisoespaciaPrueba.printInfo()
			self.reporteModel.addPrueba(memoriaVisoespaciaPrueba)
			#self.reporteModel.printReporte()

			self.addPaginaVisitada(5)
			self.menuController.updatePagesVisited(self.paginasVisitadas)
			self.showSpecificWindowMenu(5)

	def showAbstraccion(self, invalidArgs, tmtPrueba):
		self.abstraccionWindow = QtWidgets.QWidget()
		self.abstraccionController = AbstraccionController(self.abstraccionWindow, self.reporteModel)
		self.abstraccionController.switch_window.connect(self.showDigitos)

		if len(invalidArgs) != 0:
			self.displayModal(invalidArgs)
			self.tmtController.emptyInvalidArgs()
		else:
			tmtPrueba.printInfo()
			self.reporteModel.addPrueba(tmtPrueba)
			#self.reporteModel.printReporte()

			self.addPaginaVisitada(6)
			self.menuController.updatePagesVisited(self.paginasVisitadas)
			self.showSpecificWindowMenu(6)


	def showDigitos(self, invalidArgs, pruebaAbstraccion):
		self.digitosView = QtWidgets.QWidget()
		self.digitosController = DigitosController(self.digitosView, self.reporteModel)
		self.digitosController.switch_window.connect(self.tempEnd)

		if len(invalidArgs) != 0:
			self.modalController.setHeader("Deben ser mayor a 0:")
			self.modalController.setContenido(invalidArgs)
			self.modalController.showModal()
			self.fluidezVerbalController.emptyInvalidArgs()
		else:
			self.reporteModel.addPrueba(pruebaAbstraccion)
			self.reporteModel.printReporte()

			self.addPaginaVisitada(7)
			self.menuController.updatePagesVisited(self.paginasVisitadas)
			self.showSpecificWindowMenu(7)


	# def tempEnd(self, invalidArgs, pruebaDigitos):
	# 	if len(invalidArgs) != 0:
	# 		self.displayModal(invalidArgs)
	# 		self.tmtPrueba.emptyInvalidArgs()
	# 	else:
	# 		self.reporteModel.addPrueba(pruebaDigitos)
	# 		self.reporteModel.printReporte()

	# 		self.addPaginaVisitada(7)
	# 		self.menuController.updatePagesVisited(self.paginasVisitadas)
	# 		self.showSpecificWindowMenu(7)


	def tempEnd(self, invalidArgs, digitosPrueba):
		if len(invalidArgs) != 0:
			self.modalController.setHeader("Elementos no válidos:")
			self.modalController.setContenido(invalidArgs)
			self.modalController.showModal()
			self.digitosController.emptyInvalidArgs()
		else:
			self.reporteModel.addPrueba(digitosPrueba)
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