#Controlador principal de todo el programa
from MainWindowController import *
from ModalController import *
from MenuController import *
from ProgressBarController import *
from controladores.FluidezVerbalController import *
from controladores.DenominacionController import *
from controladores.MVCController import *
from controladores.MemoriaVisoespaciaController import *
from controladores.DigitosController import *
from controladores.TMTController import *
from controladores.AbstraccionController import *
from controladores.SDMTController import *
from controladores.LNSController import *
from controladores.D2Controller import *
from controladores.SCL90Controller import *
from controladores.HopkinsController import *
from controladores.StroopController import *
from controladores.ReporteController import *


class MasterController:
	def __init__(self):
		self.modalController = ModalController()

		#Lista de todas las vistas
		self.dummyWindow = QtWidgets.QWidget()
		self.mainWindow = QtWidgets.QWidget()
		self.fluidezWindow = QtWidgets.QWidget()
		self.abstraccionWindow = QtWidgets.QWidget()
		self.d2View = QtWidgets.QWidget()
		self.denominacionWindow = QtWidgets.QWidget()
		self.digitosView = QtWidgets.QWidget()
		self.hopkinsView = QtWidgets.QWidget()
		self.lnsView = QtWidgets.QWidget()
		self.memoriaVisoespaciaWindow = QtWidgets.QWidget()
		self.MVCWindow = QtWidgets.QWidget()
		self.reporteView = QtWidgets.QWidget()
		self.scl90View = QtWidgets.QWidget()
		self.sdmtView = QtWidgets.QWidget()
		self.stroopView = QtWidgets.QWidget()
		self.tmtWindow = QtWidgets.QWidget()
		
		#self.mainWindow.setStyleSheet(open('app.css').read())
	
		#Lista de todos los controllers
		self.mainWindowController = MainWindowController(self.mainWindow)
		self.abstraccionController = None
		self.d2Controller = None
		self.denominacionController = None
		self.fluidezVerbalController = None
		self.hopkinsController = None
		self.lnsController = None
		self.memoriaVisoespaciaController = None
		self.mvcController = None
		self.reporteController = None
		self.scl90Controller = None
		self.sdmtController = None
		self.stroopController = None
		self.tmtController = None
		self.digitosController = None
		
		self.paginasVisitadas = [0]
		self.listMenu = self.mainWindowController.getListMenu()
		
		self.menuController = MenuController(self.paginasVisitadas)
		self.menuController.switch_window.connect(self.showSpecificWindowMenu)

		self.progressBarController = ProgressBarController(len(self.menuController.entries)-1)

		self.currentWindow = self.dummyWindow
		self.nextWindow = self.mainWindow
		self.ventanaMostrada = 0
		self.reporteModel = None

	def resetPaginasVisitadas(self):
		"""
		 Método que se encarga de restablecer las páginas visitadas
		"""
		self.paginasVisitadas = [0]
		return self.paginasVisitadas

	def addPaginaVisitada(self, numPag):
		"""
		 Método que se encarga de marcar cuáles páginas han sido visitadas
		 Args:
		  numPag: Número de página que ha sido visitada
		"""
		tempList = self.paginasVisitadas
		if numPag not in tempList:
			tempList.append(numPag)
		self.paginasVisitadas = tempList

	def updateButtonText(self, numPag, currentController):
		"""
		 Método emplado para saber qué mensaje desplegar en el botón
		 Args:
		  numPag: Número de página de interés
		  currentController: Controlador que se usará para desplegar la vista correspondiente
		"""
		if numPag in self.paginasVisitadas[:-1]:
			if numPag == 0:
				currentController.updateButtonText("Actualizar Información")
			else:
				currentController.updateButtonText("Actualizar Datos")

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

	def connectProgressBar(self, currentController):
		"""
		 Método que se encarga de conectar el menú con la vista del controlador actual
		"""
		self.progressBarController.updateProgress(max(self.paginasVisitadas))
		self.progressBarController.setProgressBar(currentController.getProgressBar())


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
		if elemSelected == 8:
			self.nextWindow = self.sdmtView
			currentController = self.sdmtController
			self.menuController.updateCurrentWindow(8)
		if elemSelected == 9:
			self.nextWindow = self.lnsView
			currentController = self.lnsController
			self.menuController.updateCurrentWindow(9)
		if elemSelected == 10:
			self.nextWindow = self.d2View
			currentController = self.d2Controller
			self.menuController.updateCurrentWindow(10)
		if elemSelected == 11:
			self.nextWindow = self.hopkinsView
			currentController = self.hopkinsController
			self.menuController.updateCurrentWindow(11)
		if elemSelected == 12:
			self.nextWindow = self.stroopView
			currentController = self.stroopController
			self.menuController.updateCurrentWindow(12)
		if elemSelected == 13:
			self.nextWindow = self.scl90View
			currentController = self.scl90Controller
			self.menuController.updateCurrentWindow(13)
		if elemSelected == 14:
			self.nextWindow = self.reporteView
			currentController = self.reporteController
			currentController.loadReporte()
			self.menuController.updateCurrentWindow(14)
			
		if self.windowsAreDifferent():
			self.connectMenu(currentController)
			self.connectProgressBar(currentController)
			self.updateButtonText(elemSelected, currentController)
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

	def asignaReporte(self, reporte):
		listMissingElem = list()
		if isinstance(self.reporteModel, type(None)):
			self.reporteModel = reporte
		else:
			if self.reporteModel.reporte['educacion'] != reporte.reporte['educacion']:
				listMissingElem.append("Escolaridad")
			if self.reporteModel.reporte['edad'] != reporte.reporte['edad']:
				listMissingElem.append("Edad")
			if self.reporteModel.reporte['genero'] != reporte.reporte['genero']:
				listMissingElem.append("Género")
		
			if len(listMissingElem) == 0:
				tempResultados = self.reporteModel.updateReporte(reporte)
				self.reporteModel.updateResultados(tempResultados)
			else:
				modalTitle = "Favor de volver a ingresar las pruebas"
				modalHeader = "Los cambios realizados a los siguientes elementos modifican el valor de algunas pruebas: "
				self.displayModal(listMissingElem, modalTitle, modalHeader)
				self.menuController.resetPagesVisited(self.resetPaginasVisitadas())

				self.reporteModel = reporte		


	###Actualizar para que la primera prueba a llenar sea la que reciba el reporte como paramatro
	def showFluidezVerbal(self, listMissingElem, reporte):
		"""
		 Método que se encarga de cargar la vista de la pantalla Fluidez Verbal, así como el controlador de la misma.
		 Args:
		  listMissingElem: Elementos del reporte que no han sido llenados
		  reporte: Tipo de dato ReporteModel que ha sido exitosamente creado
		"""
		self.asignaReporte(reporte)
		
		if isinstance(self.fluidezVerbalController, type(None)):
			self.fluidezVerbalController = FluidezVerbalController(self.fluidezWindow, self.reporteModel)
		
		self.fluidezVerbalController.switch_window.connect(self.showDenominacion)
				
			
		if(len(listMissingElem) != 0):
			self.displayModal(listMissingElem)
			self.mainWindowController.emptyMissingArgs()
		else:
			print("Toda la info fue llenada")
			#self.reporteModel.printReporte()
			self.addPaginaVisitada(1)
			self.menuController.updatePagesVisited(self.paginasVisitadas)
			
			self.showSpecificWindowMenu(1)

	
	def showDenominacion(self, invalidArgs, fluidezVerbalPrueba):
		"""
		Metodo que se encarga de cargar la vista y el controlador de la prueba de Denominacion
		"""
		if isinstance(self.denominacionController, type(None)):
			self.denominacionController = DenominacionController(self.denominacionWindow)
		self.denominacionController.switch_window.connect(self.showMVC)

		if len(invalidArgs) != 0:
			self.modalController.setHeader("Deben de ser mayor a 0:")
			self.modalController.setContenido(invalidArgs)
			self.modalController.showModal()
			self.displayModal(invalidArgs, modalHeader="Deben de ser mayor a 0:")
			self.fluidezVerbalController.emptyInvalidArgs()
		else:
			self.reporteModel.addPrueba(fluidezVerbalPrueba)
			#self.reporteModel.printReporte()

			self.addPaginaVisitada(2)
			self.menuController.updatePagesVisited(self.paginasVisitadas)
			self.showSpecificWindowMenu(2)

	def showMVC(self, invalidArgs, denominacionPrueba):
		if isinstance(self.mvcController, type(None)):
			self.mvcController = MVCController(self.MVCWindow)
		self.mvcController.switch_window.connect(self.showMemoriaVisoespacia)

		if len(invalidArgs) != 0:
			self.modalController.setHeader("Elementos no validos:")
			self.modalController.setContenido(invalidArgs)
			self.modalController.showModal()
			self.displayModal(invalidArgs)
			self.denominacionController.emptyInvalidArgs()
		else:
			#denominacionPrueba.printInfo()
			self.reporteModel.addPrueba(denominacionPrueba)
			#self.reporteModel.printReporte()

			self.addPaginaVisitada(3)
			self.menuController.updatePagesVisited(self.paginasVisitadas)
			self.showSpecificWindowMenu(3)


	def showMemoriaVisoespacia(self, invalidArgs, MVCPrueba):
		if isinstance(self.memoriaVisoespaciaController, type(None)):
			self.memoriaVisoespaciaController = MemoriaVisoespaciaController(self.memoriaVisoespaciaWindow,self.reporteModel)
		self.memoriaVisoespaciaController.switch_window.connect(self.showTMT)

		if len(invalidArgs) != 0:
			self.modalController.setHeader("Elementos no validos:")
			self.modalController.setContenido(invalidArgs)
			self.modalController.showModal()
			self.displayModal(invalidArgs)
			self.memoriaVisoespaciaController.emptyInvalidArgs()
		else:
			self.reporteModel.addPrueba(MVCPrueba)
			#self.reporteModel.printReporte()
			self.addPaginaVisitada(4)
			self.menuController.updatePagesVisited(self.paginasVisitadas)
			self.showSpecificWindowMenu(4)

	def showTMT(self, invalidArgs, memoriaVisoespaciaPrueba):
		if isinstance(self.tmtController, type(None)):
			self.tmtController = TMTController(self.tmtWindow, self.reporteModel)
		self.tmtController.switch_window.connect(self.showAbstraccion)

		if len(invalidArgs) != 0:
			self.modalController.setHeader("Elementos no validos:")
			self.modalController.setContenido(invalidArgs)
			self.modalController.showModal()
			self.displayModal(invalidArgs)
			self.memoriaVisoespaciaController.emptyInvalidArgs()
		else:
			#memoriaVisoespaciaPrueba.printInfo()
			self.reporteModel.addPrueba(memoriaVisoespaciaPrueba)
			#self.reporteModel.printReporte()

			self.addPaginaVisitada(5)
			self.menuController.updatePagesVisited(self.paginasVisitadas)
			self.showSpecificWindowMenu(5)

	def showAbstraccion(self, invalidArgs, tmtPrueba):
		if isinstance(self.abstraccionController, type(None)):
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
		if isinstance(self.digitosController, type(None)):
			self.digitosController = DigitosController(self.digitosView, self.reporteModel)
		self.digitosController.switch_window.connect(self.showSDMT)

		if len(invalidArgs) != 0:
			self.modalController.setHeader("Deben de ser mayor a 0:")
			self.modalController.setContenido(invalidArgs)
			self.modalController.showModal()
			self.tmtPrueba.emptyInvalidArgs()
			self.displayModal(invalidArgs)
			self.abstraccionController.emptyInvalidArgs()
		else:
			self.reporteModel.addPrueba(pruebaAbstraccion)
			#self.reporteModel.printReporte()

			self.addPaginaVisitada(7)
			self.menuController.updatePagesVisited(self.paginasVisitadas)
			self.showSpecificWindowMenu(7)
	
	def showSDMT(self, invalidArgs, digitosPrueba):
		if isinstance(self.sdmtController, type(None)):
			self.sdmtController = SDMTController(self.sdmtView, self.reporteModel)
		self.sdmtController.switch_window.connect(self.showLNS)

		if len(invalidArgs) != 0:
			self.displayModal(invalidArgs)
			self.digitosController.emptyInvalidArgs()
		else:
			self.reporteModel.addPrueba(digitosPrueba)
			#self.reporteModel.printReporte()

			self.addPaginaVisitada(8)
			self.menuController.updatePagesVisited(self.paginasVisitadas)
			self.showSpecificWindowMenu(8)

	def showLNS(self, invalidArgs, sdmtPrueba):
		if isinstance(self.lnsController, type(None)):
			self.lnsController = LNSController(self.lnsView, self.reporteModel)
		self.lnsController.switch_window.connect(self.showD2) 

		if len(invalidArgs) != 0:
			self.displayModal(invalidArgs)
			self.sdmtController.emptyInvalidArgs()
		else:
			self.reporteModel.addPrueba(sdmtPrueba)
			#self.reporteModel.printReporte()

			self.addPaginaVisitada(9)
			self.menuController.updatePagesVisited(self.paginasVisitadas)
			self.showSpecificWindowMenu(9)

	def showD2(self, invalidArgs, lnsPrueba):
		if isinstance(self.d2Controller, type(None)):
			self.d2Controller = D2Controller(self.d2View, self.reporteModel)
		self.d2Controller.switch_window.connect(self.showHopkins) 

		if len(invalidArgs) != 0:
			self.displayModal(invalidArgs)
			self.lnsController.emptyInvalidArgs()
		else:
			self.reporteModel.addPrueba(lnsPrueba)
			#self.reporteModel.printReporte()

			self.addPaginaVisitada(10)
			self.menuController.updatePagesVisited(self.paginasVisitadas)
			self.showSpecificWindowMenu(10)

	def showHopkins(self, invalidArgs, d2Prueba):
		if isinstance(self.hopkinsController, type(None)):
			self.hopkinsController = HopkinsController(self.hopkinsView, self.reporteModel)
		self.hopkinsController.switch_window.connect(self.showStroop) 

		if len(invalidArgs) != 0:
			self.displayModal(invalidArgs)
			self.d2Controller.emptyInvalidArgs()
		else:
			self.reporteModel.addPrueba(d2Prueba)
			#self.reporteModel.printReporte()

			self.addPaginaVisitada(11)
			self.menuController.updatePagesVisited(self.paginasVisitadas)
			self.showSpecificWindowMenu(11)

	def showStroop(self, invalidArgs, hopkinsPrueba):
		if isinstance(self.stroopController, type(None)):
			self.stroopController = StroopController(self.stroopView, self.reporteModel)
		self.stroopController.switch_window.connect(self.showSCL90) 

		if len(invalidArgs) != 0:
			self.displayModal(invalidArgs)
			self.hopkinsController.emptyInvalidArgs()
		else:
			self.reporteModel.addPrueba(hopkinsPrueba)
			#self.reporteModel.printReporte()

			self.addPaginaVisitada(12)
			self.menuController.updatePagesVisited(self.paginasVisitadas)
			self.showSpecificWindowMenu(12)

	def showSCL90(self, invalidArgs, prevPrueba):
		if isinstance(self.scl90Controller, type(None)):
			self.scl90Controller = SCL90Controller(self.scl90View, self.reporteModel)
		self.scl90Controller.switch_window.connect(self.showReporte)

		if len(invalidArgs) != 0:
			self.displayModal(invalidArgs)
			self.stroopController.emptyInvalidArgs()
		else:
			#self.reporteModel.addPrueba(prevPrueba)
			self.reporteModel.printReporte()

			self.addPaginaVisitada(13)
			self.menuController.updatePagesVisited(self.paginasVisitadas)
			self.showSpecificWindowMenu(13)


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

	def showReporte(self, invalidArgs, prevPrueba):
		if len(invalidArgs) != 0:
			self.modalController.showModal(invalidArgs)
			self.scl90Controller.emptyInvalidArgs()
		else:
			self.reporteModel.addPrueba(prevPrueba)
			self.reporteModel.printReporte()

			tempUrl = QUrl(QDir.currentPath()+"/vistas/Reporte/reporte.html")
			tempUrl = tempUrl.toString()
			if isinstance(self.reporteController, type(None)):
				self.reporteController = ReporteController(self.reporteView, tempUrl, self.reporteModel)
			self.reporteController.switch_window.connect(self.newReport)

			self.addPaginaVisitada(14)
			self.menuController.updatePagesVisited(self.paginasVisitadas)
			self.showSpecificWindowMenu(14)	

	def newReport(self):
		self.menuController.resetPagesVisited(self.resetPaginasVisitadas())
		self.showMainWindow()



	def tempEnd(self, invalidArgs, scl90Prueba):
		if len(invalidArgs) != 0:
			self.modalController.setHeader("Elementos no válidos para sexo " + str(self.reporteModel.reporte['genero']) + ":")
			self.modalController.setContenido(invalidArgs)
			self.modalController.showModal()
			self.scl90Controller.emptyInvalidArgs()
		else:
			self.reporteModel.addPrueba(scl90Prueba)
			self.reporteModel.printReporte()

def main():
	"""
	 Método principal en la ejecución del programa
	"""
	app = QtWidgets.QApplication(sys.argv)
	#app.setStyleSheet(open('app.css').read())
	masterController = MasterController()
	masterController.showMainWindow()
	sys.exit(app.exec_())

if __name__ == '__main__':
	main()