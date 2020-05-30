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
from controladores.TOLController import *
from controladores.ButtController import*
from controladores.PittsburghController import *


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
		self.tolView = QtWidgets.QWidget()
		self.buttView = QtWidgets.QWidget()
		self.pittsburghView = QtWidgets.QWidget()

	
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
		self.tolController = None
		self.buttController = None
		self.pittsburghController = None

		
		
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
		 Args:
		  currentController: Valor que contiene el controlador de la prueba actual
		"""
		self.menuController.clearMenu()
		self.listMenu = currentController.getListMenu()
		self.menuController.updateListView(self.listMenu)
		self.menuController.poblarLista()

	def connectProgressBar(self, currentController):
		"""
		 Método que se encarga de conectar el menú con la vista del controlador actual
		 Args:
		  currentController: Valor que contiene el controlador de la prueba actual
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
			self.nextWindow = self.tolView
			currentController = self.tolController
			self.menuController.updateCurrentWindow(13)
		if elemSelected == 14:
			self.nextWindow = self.buttView
			currentController = self.buttController
			self.menuController.updateCurrentWindow(14)
		if elemSelected == 15:
			self.nextWindow = self.pittsburghView
			currentController = self.pittsburghController
			self.menuController.updateCurrentWindow(15)
		if elemSelected == 16:
			self.nextWindow = self.scl90View
			currentController = self.scl90Controller
			self.menuController.updateCurrentWindow(16)
		if elemSelected == 17:
			self.nextWindow = self.reporteView
			currentController = self.reporteController
			currentController.loadReporte()
			self.menuController.updateCurrentWindow(17)

		
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
		"""
		 Método que despliega la ventana de elementos faltantes o inválidos
		 Args:
		  listMissingElem: Lista que tiene los elementos faltantes de la prueba
		  modalTitle: Título de la ventana
		  modalHeader: Encabezado de la ventana
		"""
		self.modalController.setWindowTitle(modalTitle)
		self.modalController.setHeader(modalHeader)
		self.modalController.setContenido(listMissingElem)
		self.modalController.showModal()
        
	def showMainWindow(self):
		"""
		 Método que se encarga de cargar la vista de la pantalla a MainWindow, así como el controlador de la misma.
        """
		self.mainWindowController.switch_window.connect(self.asignaReporte)
		self.showSpecificWindowMenu(0)
        
	def asignaReporte(self, listMissingElem, reporte):
		"""
		 Método que se encarga de asignar los valores agregados al reporte
		 Args:
		  listMissingElem: Lista de elementos inválidos
		  reporte: Objeto de tipo reporte que será asignado al reporte de todas las pruebas
		"""
		listModElem = list()
		if len(listMissingElem) != 0:
			self.displayModal(listMissingElem)
			self.mainWindowController.emptyMissingArgs()
		else:
			if isinstance(self.reporteModel, type(None)):
				self.reporteModel = reporte
			else:
				if self.reporteModel.reporte['educacion'] != reporte.reporte['educacion']:
					listModElem.append("Escolaridad")
				if self.reporteModel.reporte['edad'] != reporte.reporte['edad']:
					listModElem.append("Edad")
				if self.reporteModel.reporte['genero'] != reporte.reporte['genero']:
					listModElem.append("Género")
			
				if len(listModElem) == 0:
					tempResultados = self.reporteModel.updateReporte(reporte)
					self.reporteModel.updateResultados(tempResultados)
				else:
					modalTitle = "Favor de volver a ingresar las pruebas"
					modalHeader = "Los cambios realizados a los siguientes elementos modifican el valor de algunas pruebas: "
					self.displayModal(listModElem, modalTitle, modalHeader)
					self.menuController.resetPagesVisited(self.resetPaginasVisitadas())
					resetMainWindow = False
					self.resetReport(resetMainWindow)
					self.reporteModel = reporte
			self.showFluidezVerbal(self.reporteModel)
			

	def showFluidezVerbal(self, reporte):
		"""
		 Método que se encarga de cargar la vista de la pantalla Fluidez Verbal, así como el controlador de la misma.
		 Args:
		  reporte: Tipo de dato ReporteModel que ha sido exitosamente creado
		"""
		print("FluidezVerbal")
		if isinstance(self.fluidezVerbalController, type(None)):
			self.fluidezVerbalController = FluidezVerbalController(self.fluidezWindow, self.reporteModel)
			self.fluidezVerbalController.switch_window.connect(self.showDenominacion)
		
			
		self.addPaginaVisitada(1)
		self.menuController.updatePagesVisited(self.paginasVisitadas)
		self.showSpecificWindowMenu(1)

	
	def showDenominacion(self, invalidArgs, fluidezVerbalPrueba):
		"""
		 Metodo que se encarga de cargar la vista y el controlador de la prueba de Denominacion
		 Args: 
		  invalidArgs: Lista de elementos inválidos
		  fluidezVerbalPrueba: Prueba previa a la de Denominación
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
		"""
		 Metodo que se encarga de cargar la vista y el controlador de la prueba de MVC
		 Args: 
		  invalidArgs: Lista de elementos inválidos
		  denominacionPrueba: Prueba previa a la de MVC
		"""
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
		"""
		 Metodo que se encarga de cargar la vista y el controlador de la prueba de Memoria Visoespacial
		 Args: 
		  invalidArgs: Lista de elementos inválidos
		  MVCPrueba: Prueba previa a la de MEmoria Visoespacial
		"""
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
		"""
		 Metodo que se encarga de cargar la vista y el controlador de la prueba de TMT
		 Args: 
		  invalidArgs: Lista de elementos inválidos
		  memoriaVisoespacialPrueba: Prueba previa a la de TMT
		"""
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
		"""
		 Metodo que se encarga de cargar la vista y el controlador de la prueba de Abstraccion
		 Args: 
		  invalidArgs: Lista de elementos inválidos
		  tmtPrueba: Prueba previa a la de Abstraccion
		"""
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
		"""
		 Metodo que se encarga de cargar la vista y el controlador de la prueba de Digitos
		 Args: 
		  invalidArgs: Lista de elementos inválidos
		  pruebaAbstraccion: Prueba previa a la de Digitos
		"""
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
		"""
		 Metodo que se encarga de cargar la vista y el controlador de la prueba de SDMT
		 Args: 
		  invalidArgs: Lista de elementos inválidos
		  digitosPrueba: Prueba previa a la de SDMT
		"""
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
		"""
		 Metodo que se encarga de cargar la vista y el controlador de la prueba de LNS
		 Args: 
		  invalidArgs: Lista de elementos inválidos
		  sdmtPrueba: Prueba previa a la de LNS
		"""
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
		"""
		 Metodo que se encarga de cargar la vista y el controlador de la prueba de D2
		 Args: 
		  invalidArgs: Lista de elementos inválidos
		  lnsPrueba: Prueba previa a la de D2
		"""
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
		"""
		 Metodo que se encarga de cargar la vista y el controlador de la prueba de Hopkins
		 Args: 
		  invalidArgs: Lista de elementos inválidos
		  d2Prueba: Prueba previa a la de Hopkins
		"""
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
		"""
		 Metodo que se encarga de cargar la vista y el controlador de la prueba de Stroop
		 Args: 
		  invalidArgs: Lista de elementos inválidos
		  hopkinsPrueba: Prueba previa a la de Stroop
		"""
		if isinstance(self.stroopController, type(None)):
			self.stroopController = StroopController(self.stroopView, self.reporteModel)
			self.stroopController.switch_window.connect(self.showTOL) 

		if len(invalidArgs) != 0:
			self.displayModal(invalidArgs)
			self.hopkinsController.emptyInvalidArgs()
		else:
			self.reporteModel.addPrueba(hopkinsPrueba)
			#self.reporteModel.printReporte()

			self.addPaginaVisitada(12)
			self.menuController.updatePagesVisited(self.paginasVisitadas)
			self.showSpecificWindowMenu(12)

	def showTOL(self, invalidArgs, stroopPrueba):
		"""
		 Metodo que se encarga de cargar la vista y el controlador de la prueba de TOL
		 Args: 
		  invalidArgs: Lista de elementos inválidos
		  scl90Prueba: Prueba previa a la de TOL
		"""
		if isinstance(self.tolController, type(None)):
			self.tolController = TOLController(self.tolView, self.reporteModel)
			self.tolController.switch_window.connect(self.showButt)

		if len(invalidArgs) != 0:
			self.displayModal(invalidArgs)
			self.stroopController.emptyInvalidArgs()
		else:
			self.reporteModel.addPrueba(stroopPrueba)
			#self.reporteModel.printReporte()

			self.addPaginaVisitada(13)
			self.menuController.updatePagesVisited(self.paginasVisitadas)
			self.showSpecificWindowMenu(13)

	def showButt(self, invalidArgs, tolPrueba):
		"""
		 Metodo que se encarga de cargar la vista y el controlador de la prueba de TOL
		 Args: 
		  invalidArgs: Lista de elementos inválidos
		  scl90Prueba: Prueba previa a la de TOL
		"""
		if isinstance(self.buttController, type(None)):
			self.buttController = ButtController(self.buttView, self.reporteModel)
			self.buttController.switch_window.connect(self.showPittsburgh)


		if len(invalidArgs) != 0:
			self.displayModal(invalidArgs)
			self.tolController.emptyInvalidArgs()
		else:
			self.reporteModel.addPrueba(tolPrueba)
			#self.reporteModel.printReporte()

			self.addPaginaVisitada(14)
			self.menuController.updatePagesVisited(self.paginasVisitadas)
			self.showSpecificWindowMenu(14)


	def showPittsburgh(self, invalidArgs, buttPrueba):
		"""
		 Metodo que se encarga de cargar la vista y el controlador de la prueba de TOL
		 Args: 
		  invalidArgs: Lista de elementos inválidos
		  scl90Prueba: Prueba previa a la de TOL
		"""
		if isinstance(self.pittsburghController, type(None)):
			self.pittsburghController = PittsburghController(self.pittsburghView, self.reporteModel)
			self.pittsburghController.switch_window.connect(self.showSCL90)

		if len(invalidArgs) != 0:
			self.displayModal(invalidArgs)
			self.buttController.emptyInvalidArgs()
		else:
			self.reporteModel.addPrueba(buttPrueba)
			#self.reporteModel.printReporte()

			self.addPaginaVisitada(15)
			self.menuController.updatePagesVisited(self.paginasVisitadas)
			self.showSpecificWindowMenu(15)


	def showSCL90(self, invalidArgs, prevPrueba):
		"""
		 Metodo que se encarga de cargar la vista y el controlador de la prueba de SCL90
		 Args: 
		  invalidArgs: Lista de elementos inválidos
		  prevPrueba: Prueba previa a la de SCL90
		"""
		if isinstance(self.scl90Controller, type(None)):
			self.scl90Controller = SCL90Controller(self.scl90View, self.reporteModel)
			self.scl90Controller.switch_window.connect(self.showReporte)

		if len(invalidArgs) != 0:
			self.displayModal(invalidArgs)
			self.pittsburghController.emptyInvalidArgs()
		else:
			self.reporteModel.addPrueba(prevPrueba)
			#self.reporteModel.printReporte()

			self.addPaginaVisitada(16)
			self.menuController.updatePagesVisited(self.paginasVisitadas)
			self.showSpecificWindowMenu(16)

	def showReporte(self, invalidArgs, prevPrueba):

		"""
		 Metodo que se encarga de cargar la vista y el controlador del Reporte
		 Args: 
		  invalidArgs: Lista de elementos inválidos
		  prevPrueba: Prueba previa al Reporte
		"""

		print("Llamé a showReporte")

		if len(invalidArgs) != 0:
			modalHeaderStr = "Elementos no válidos para género " + self.reporteModel.reporte["genero"] + ":"
			self.displayModal(invalidArgs, modalHeader=modalHeaderStr)
			self.scl90Controller.emptyInvalidArgs()
		else:
			self.reporteModel.addPrueba(prevPrueba)

			#self.reporteModel.printReporte()

			tempUrl = QUrl(QDir.currentPath()+"/vistas/Reporte/reporte.html")
			tempUrl = tempUrl.toString()
			imageUrl = QUrl(QDir.currentPath()+"/vistas/Reporte/reporte.png")
			imageUrl = imageUrl.toString()

			if isinstance(self.reporteController, type(None)):
				print("reporteController es None")
				self.reporteController = ReporteController(self.reporteView, tempUrl, imageUrl, self.reporteModel)
				self.reporteController.switch_window.connect(self.newReport)


			self.addPaginaVisitada(17)
			self.menuController.updatePagesVisited(self.paginasVisitadas)
			self.showSpecificWindowMenu(17)	


	def newReport(self):
		"""
		 Metodo que se encarga de crear un nuevo reporte y regresar a la pantalla principal
		"""
		self.resetReport(True)
		self.showMainWindow()

	def resetReport(self, resetMainWindow):
		"""
		 Método que se encarga de eliminar todas las vistas y controladores de las mismas
		 Args: 
		  resetMainWindow: Booleano que se encarga de notificar si se debe de eliminar el controlador y vista de mainWindow
		"""
		self.menuController.resetPagesVisited(self.resetPaginasVisitadas())

		self.reporteModel = None
		
		del self.dummyWindow
		del self.fluidezWindow
		del self.abstraccionWindow
		del self.d2View
		del self.denominacionWindow
		del self.digitosView
		del self.hopkinsView
		del self.lnsView
		del self.memoriaVisoespaciaWindow
		del self.MVCWindow
		del self.reporteView
		del self.scl90View
		del self.sdmtView
		del self.stroopView
		del self.tmtWindow
		del self.tolView
		del self.buttView
		del self.pittsburghView
	

		del self.abstraccionController
		del self.d2Controller
		del self.denominacionController
		del self.fluidezVerbalController
		del self.hopkinsController
		del self.lnsController
		del self.memoriaVisoespaciaController
		del self.mvcController
		del self.reporteController
		del self.scl90Controller
		del self.sdmtController
		del self.stroopController
		del self.tmtController
		del self.digitosController
		del self.tolController
		del self.buttController
		del self.pittsburghController


		if (resetMainWindow):
			del self.mainWindow
			del self.mainWindowController
			self.mainWindow = QtWidgets.QWidget()
			self.mainWindowController = MainWindowController(self.mainWindow)
			

		self.dummyWindow = QtWidgets.QWidget()
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
		self.tolView = QtWidgets.QWidget()
		self.buttView = QtWidgets.QWidget()
		self.pittsburghView = QtWidgets.QWidget()


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
		self.tolController = None
		self.buttController = None
		self.pittsburghController = None


def main():
	"""
	 Método principal en la ejecución del programa
	"""
	app = QtWidgets.QApplication(sys.argv)
	app.setStyleSheet(open('app.css').read())
	masterController = MasterController()
	masterController.showMainWindow()
	sys.exit(app.exec_())

if __name__ == '__main__':
	main()