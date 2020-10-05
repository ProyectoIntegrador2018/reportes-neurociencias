# Controlador principal de todo el programa
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
from ReporteModel import ReporteModel
from Routes import Router


class MasterController:
    def __init__(self):
        self.modalController = ModalController()

        self.pagesFunctions = {
            "informacionSujeto": self.asignaReporte,
            "fluidezVerbal": self.customShow("fluidezVerbal", FluidezVerbalController),
            "denominacion": self.customShow("denominacion",DenominacionController),
            "comprensionVerbal": self.customShow("comprensionVerbal", MVCController),
            "memoriaVisoespacial": self.customShow("memoriaVisoespacial",MemoriaVisoespaciaController),
            "tmt": self.customShow("tmt",TMTController),
            "abstraccion": self.customShow("abstraccion",AbstraccionController),
            "digitos": self.customShow("digitos",DigitosController),
            "sdmt": self.customShow("sdmt",SDMTController),
            "lns": self.customShow("lns",LNSController),
            "d2": self.customShow("d2",D2Controller),
            "hopkins": self.customShow("hopkins",HopkinsController),
            "stroop": self.customShow("stroop",StroopController),
            "torreLondres": self.customShow("torreLondres",TOLController),
            "motivoDeportivo": self.customShow("motivoDeportivo",ButtController),
            "pittsburgh": self.customShow("pittsburgh",PittsburghController),
            "scl90": self.customShow("scl90",SCL90Controller),
            "report": self.customShow("report",ReporteController),
            # do not remove used for reseting and initialize pruebas
            "dummyWindow": self.newReport
        }

        self.paginasVisitadas = ["informacionSujeto"]  # intial view
        self.paginasDisponibles = [
            "informacionSujeto",
            "fluidezVerbal",
            "denominacion",
            "comprensionVerbal",
            "memoriaVisoespacial",
            "tmt",
            "abstraccion",
            "digitos",
            "sdmt",
            "lns",
            "d2",
            "hopkins",
            "stroop",
            "torreLondres",
            "motivoDeportivo",
            "pittsburgh",
            "scl90",
            "report",
            # do not remove used for reseting and initialize pruebas
            "dummyWindow",
        ]

        self.paginasDisponibles = self.fillAvailablePages(
            self.paginasDisponibles)

        self.router = Router(self.paginasDisponibles)
        self.router.setController(
            "informacionSujeto", MainWindowController)
        self.router.getController(
            "informacionSujeto").newInfo()

        self.listMenu = self.router.getController(
            "informacionSujeto").getListMenu()

        self.menuController = MenuController(
            self.paginasVisitadas, self.router.getEntrieNames())
        self.menuController.switch_window.connect(self.showSpecificWindowMenu)

        self.progressBarController = ProgressBarController(
            len(self.router)-2) #1 intial view and 2 final view

        self.currentWindow = self.router.getView("dummyWindow")
        self.nextWindow = self.router.getView("informacionSujeto")
        self.reporteModel = None

    def fillAvailablePages(self, pages):
        return [[page, self.pagesFunctions[page]] for page in pages]

    def resetPaginasVisitadas(self):
        """
         Método que se encarga de restablecer las páginas visitadas
        """
        self.paginasVisitadas = ["informacionSujeto"]
        return self.paginasVisitadas

    def addPaginaVisitada(self, routePage):
        """
         Método que se encarga de marcar cuáles páginas han sido visitadas
         Args:
          routePage: Nombre de página que ha sido visitada
        """
        paginasDisponibles = [routePage for routePage,
                              _ in self.paginasDisponibles]
        if routePage not in paginasDisponibles:
            raise NameError("{} not a posible route".format(routePage))

        tempList = self.paginasVisitadas
        if routePage not in tempList:
            tempList.append(routePage)
        self.paginasVisitadas = tempList

    def updateButtonText(self, routePage, currentController):
        """
         Método emplado para saber qué mensaje desplegar en el botón
         Args:
          routePage: Nombre de página de interés
          currentController: Controlador que se usará para desplegar la vista correspondiente
        """
        if routePage in self.paginasVisitadas[:-1]:
            if routePage == "informacionSujeto":
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
        self.progressBarController.updateProgress(len(self.paginasVisitadas)-1)
        self.progressBarController.setProgressBar(
            currentController.getProgressBar())

    def getRouteProgress(self, routeName):
        for idx, key in enumerate(self.paginasVisitadas):
            if key == routeName:
                return idx

        return len(self.paginasVisitadas)-1

    def showSpecificWindowMenu(self, elemSelected):
        """
         Método que se encarga de manejar el doble click sobre un elemento del menú
         Args:
          elemSelected: Lista que contiene el elemento seleccionado
        """
        self.nextWindow, currentController = self.router.getRouteViewAndController(
            elemSelected)
        # print("hola", self.nextWindow, currentController)
        progress = self.getRouteProgress(elemSelected)
        self.menuController.updateCurrentWindow(progress)

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
        print("modal 1")
        self.modalController.setWindowTitle(modalTitle)
        self.modalController.setHeader(modalHeader)
        self.modalController.setContenido(listMissingElem)
        self.modalController.showModal()

    def showMainWindow(self):
        """
         Método que se encarga de cargar la vista de la pantalla a MainWindow, así como el controlador de la misma.
        """
        self.showSpecificWindowMenu(self.paginasVisitadas[0])

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
                    self.menuController.resetPagesVisited(
                        self.resetPaginasVisitadas())
                    resetMainWindow = False
                    self.resetReport(resetMainWindow)
                    self.reporteModel = reporte
            nextKey = self.router.getNextPageKey("informacionSujeto")
            func = self.pagesFunctions[nextKey]
            func([], self.reporteModel)

        self.router.getController("informacionSujeto").emptyMissingArgs()

    def customShow(self, nameKey, ClassRef):
        def F(invalidArgs, prevPrueba):
            if len(invalidArgs) != 0:
                self.displayModal(
                    invalidArgs, modalHeader="Deben de ser mayor a 0:")
                self.router.getController(self.paginasVisitadas[-1]).emptyInvalidArgs()
            else:
                if not isinstance(prevPrueba, ReporteModel):
                    self.reporteModel.addPrueba(prevPrueba)

                self.router.setController(
                    nameKey, ClassRef, self.reporteModel)

                self.addPaginaVisitada(nameKey)
                self.menuController.updatePagesVisited(self.paginasVisitadas)
                self.showSpecificWindowMenu(nameKey)

        return F

    # def showFluidezVerbal(self, invalidArgs, prevPrueba):
    #     """
    #      Método que se encarga de cargar la vista de la pantalla Fluidez Verbal, así como el controlador de la misma.
    #      Args:
    #       reporte: Tipo de dato ReporteModel que ha sido exitosamente creado
    #     """

    #     if len(invalidArgs) != 0:
    #         self.displayModal(
    #             invalidArgs, modalHeader="Deben de ser mayor a 0:")
    #         self.router.getController(self.paginasVisitadas[-1]).emptyInvalidArgs()
    #     else:
    #         if not isinstance(prevPrueba, ReporteModel):
    #             self.reporteModel.addPrueba(prevPrueba)

    #         self.router.setController(
    #             "fluidezVerbal", FluidezVerbalController, self.reporteModel)

    #         self.addPaginaVisitada("fluidezVerbal")
    #         self.menuController.updatePagesVisited(self.paginasVisitadas)
    #         self.showSpecificWindowMenu("fluidezVerbal")

    # def showDenominacion(self, invalidArgs, prevPrueba):
    #     """
    #      Metodo que se encarga de cargar la vista y el controlador de la prueba de Denominacion
    #      Args: 
    #       invalidArgs: Lista de elementos inválidos
    #       prevPrueba: Prueba previa a la de Denominación
    #     """
    #     if len(invalidArgs) != 0:
    #         self.displayModal(
    #             invalidArgs, modalHeader="Deben de ser mayor a 0:")
    #         self.router.getController(self.paginasVisitadas[-1]).emptyInvalidArgs()
    #     else:
    #         if not isinstance(prevPrueba, ReporteModel):
    #             self.reporteModel.addPrueba(prevPrueba)

    #         self.router.setController(
    #             "denominacion", DenominacionController, self.reporteModel)

    #         self.addPaginaVisitada("denominacion")
    #         self.menuController.updatePagesVisited(self.paginasVisitadas)
    #         self.showSpecificWindowMenu("denominacion")

    # def showMVC(self, invalidArgs, prevPrueba):
    #     """
    #      Metodo que se encarga de cargar la vista y el controlador de la prueba de MVC
    #      Args: 
    #       invalidArgs: Lista de elementos inválidos
    #       prevPrueba: Prueba previa a la de MVC
    #     """
    #     if len(invalidArgs) != 0:
    #         self.displayModal(invalidArgs)
    #         self.router.getController(self.paginasVisitadas[-1]).emptyInvalidArgs()
    #     else:
    #         if not isinstance(prevPrueba, ReporteModel):
    #             self.reporteModel.addPrueba(prevPrueba)

    #         self.router.setController(
    #             "comprensionVerbal", MVCController)

    #         self.addPaginaVisitada("comprensionVerbal")
    #         self.menuController.updatePagesVisited(self.paginasVisitadas)
    #         self.showSpecificWindowMenu("comprensionVerbal")

    # def showMemoriaVisoespacia(self, invalidArgs, prevPrueba):
    #     """
    #      Metodo que se encarga de cargar la vista y el controlador de la prueba de Memoria Visoespacial
    #      Args: 
    #       invalidArgs: Lista de elementos inválidos
    #       prevPrueba: Prueba previa a la de MEmoria Visoespacial
    #     """
        

    #     if len(invalidArgs) != 0:
    #         self.displayModal(invalidArgs)
    #         self.router.getController(self.paginasVisitadas[-1]).emptyInvalidArgs()
    #     else:
    #         if not isinstance(prevPrueba, ReporteModel):
    #             self.reporteModel.addPrueba(prevPrueba)

    #         self.router.setController(
    #             "memoriaVisoespacial", MemoriaVisoespaciaController, self.reporteModel)
            
    #         self.addPaginaVisitada("memoriaVisoespacial")
    #         self.menuController.updatePagesVisited(self.paginasVisitadas)
    #         self.showSpecificWindowMenu("memoriaVisoespacial")

    # def showTMT(self, invalidArgs, prevPrueba):
    #     """
    #      Metodo que se encarga de cargar la vista y el controlador de la prueba de TMT
    #      Args: 
    #       invalidArgs: Lista de elementos inválidos
    #       prevPrueba: Prueba previa a la de TMT
    #     """
    #     if len(invalidArgs) != 0:
    #         self.displayModal(invalidArgs)
    #         self.router.getController(self.paginasVisitadas[-1]).emptyInvalidArgs()
    #     else:
    #         if not isinstance(prevPrueba, ReporteModel):
    #             self.reporteModel.addPrueba(prevPrueba)

    #         self.router.setController(
    #             "tmt", TMTController, self.reporteModel)

    #         self.addPaginaVisitada("tmt")
    #         self.menuController.updatePagesVisited(self.paginasVisitadas)
    #         self.showSpecificWindowMenu("tmt")

    # def showAbstraccion(self, invalidArgs, prevPrueba):
    #     """
    #      Metodo que se encarga de cargar la vista y el controlador de la prueba de Abstraccion
    #      Args: 
    #       invalidArgs: Lista de elementos inválidos
    #       prevPrueba: Prueba previa a la de Abstraccion
    #     """
        

    #     if len(invalidArgs) != 0:
    #         self.displayModal(invalidArgs)
    #         self.router.getController(self.paginasVisitadas[-1]).emptyInvalidArgs()
    #     else:
    #         if not isinstance(prevPrueba, ReporteModel):
    #             self.reporteModel.addPrueba(prevPrueba)

    #         self.router.setController(
    #             "abstraccion", AbstraccionController, self.reporteModel)

    #         self.addPaginaVisitada("abstraccion")
    #         self.menuController.updatePagesVisited(self.paginasVisitadas)
    #         self.showSpecificWindowMenu("abstraccion")

    # def showDigitos(self, invalidArgs, prevPrueba):
    #     """
    #      Metodo que se encarga de cargar la vista y el controlador de la prueba de Digitos
    #      Args: 
    #       invalidArgs: Lista de elementos inválidos
    #       prevPrueba: Prueba previa a la de Digitos
    #     """
    #     if len(invalidArgs) != 0:
    #         self.displayModal(invalidArgs)
    #         self.router.getController(self.paginasVisitadas[-1]).emptyInvalidArgs()
    #     else:
    #         if not isinstance(prevPrueba, ReporteModel):
    #             self.reporteModel.addPrueba(prevPrueba)

    #         self.router.setController(
    #             "digitos", DigitosController, self.reporteModel)

    #         self.addPaginaVisitada("digitos")
    #         self.menuController.updatePagesVisited(self.paginasVisitadas)
    #         self.showSpecificWindowMenu("digitos")

    # def showSDMT(self, invalidArgs, prevPrueba):
    #     """
    #      Metodo que se encarga de cargar la vista y el controlador de la prueba de SDMT
    #      Args: 
    #       invalidArgs: Lista de elementos inválidos
    #       prevPrueba: Prueba previa a la de SDMT
    #     """
    #     if len(invalidArgs) != 0:
    #         self.displayModal(invalidArgs)
    #         self.router.getController(self.paginasVisitadas[-1]).emptyInvalidArgs()
    #     else:
    #         if not isinstance(prevPrueba, ReporteModel):
    #             self.reporteModel.addPrueba(prevPrueba)

    #         self.router.setController(
    #             "sdmt", SDMTController, self.reporteModel)

    #         self.addPaginaVisitada("sdmt")
    #         self.menuController.updatePagesVisited(self.paginasVisitadas)
    #         self.showSpecificWindowMenu("sdmt")

    # def showLNS(self, invalidArgs, prevPrueba):
    #     """
    #      Metodo que se encarga de cargar la vista y el controlador de la prueba de LNS
    #      Args: 
    #       invalidArgs: Lista de elementos inválidos
    #       prevPrueba: Prueba previa a la de LNS
    #     """
    #     if len(invalidArgs) != 0:
    #         self.displayModal(invalidArgs)
    #         self.router.getController(self.paginasVisitadas[-1]).emptyInvalidArgs()
    #     else:
    #         if not isinstance(prevPrueba, ReporteModel):
    #             self.reporteModel.addPrueba(prevPrueba)

    #         self.router.setController(
    #             "lns", LNSController, self.reporteModel)

    #         self.addPaginaVisitada("lns")
    #         self.menuController.updatePagesVisited(self.paginasVisitadas)
    #         self.showSpecificWindowMenu("lns")

    # def showD2(self, invalidArgs, prevPrueba):
    #     """
    #      Metodo que se encarga de cargar la vista y el controlador de la prueba de D2
    #      Args: 
    #       invalidArgs: Lista de elementos inválidos
    #       prevPrueba: Prueba previa a la de D2
    #     """
        

    #     if len(invalidArgs) != 0:
    #         self.displayModal(invalidArgs)
    #         self.router.getController(self.paginasVisitadas[-1]).emptyInvalidArgs()
    #     else:
    #         if not isinstance(prevPrueba, ReporteModel):
    #             self.reporteModel.addPrueba(prevPrueba)

    #         self.router.setController(
    #             "d2", D2Controller, self.reporteModel)

    #         self.addPaginaVisitada("d2")
    #         self.menuController.updatePagesVisited(self.paginasVisitadas)
    #         self.showSpecificWindowMenu("d2")

    # def showHopkins(self, invalidArgs, prevPrueba):
    #     """
    #      Metodo que se encarga de cargar la vista y el controlador de la prueba de Hopkins
    #      Args: 
    #       invalidArgs: Lista de elementos inválidos
    #       prevPrueba: Prueba previa a la de Hopkins
    #     """
        

    #     if len(invalidArgs) != 0:
    #         self.displayModal(invalidArgs)
    #         self.router.getController(self.paginasVisitadas[-1]).emptyInvalidArgs()
    #     else:
    #         if not isinstance(prevPrueba, ReporteModel):
    #             self.reporteModel.addPrueba(prevPrueba)

    #         self.router.setController(
    #             "hopkins", HopkinsController, self.reporteModel)

    #         self.addPaginaVisitada("hopkins")
    #         self.menuController.updatePagesVisited(self.paginasVisitadas)
    #         self.showSpecificWindowMenu("hopkins")

    # def showStroop(self, invalidArgs, prevPrueba):
    #     """
    #      Metodo que se encarga de cargar la vista y el controlador de la prueba de Stroop
    #      Args: 
    #       invalidArgs: Lista de elementos inválidos
    #       prevPrueba: Prueba previa a la de Stroop
    #     """
        

    #     if len(invalidArgs) != 0:
    #         self.displayModal(invalidArgs)
    #         self.router.getController(self.paginasVisitadas[-1]).emptyInvalidArgs()
    #     else:
    #         if not isinstance(prevPrueba, ReporteModel):
    #             self.reporteModel.addPrueba(prevPrueba)

    #         self.router.setController(
    #             "stroop", StroopController, self.reporteModel)

    #         self.addPaginaVisitada("stroop")
    #         self.menuController.updatePagesVisited(self.paginasVisitadas)
    #         self.showSpecificWindowMenu("stroop")

    # def showTOL(self, invalidArgs, prevPrueba):
    #     """
    #      Metodo que se encarga de cargar la vista y el controlador de la prueba de TOL
    #      Args: 
    #       invalidArgs: Lista de elementos inválidos
    #       prevPrueba: Prueba previa a la de TOL
    #     """
        

    #     if len(invalidArgs) != 0:
    #         self.displayModal(invalidArgs)
    #         self.router.getController(self.paginasVisitadas[-1]).emptyInvalidArgs()
    #     else:
    #         if not isinstance(prevPrueba, ReporteModel):
    #             self.reporteModel.addPrueba(prevPrueba)

    #         self.router.setController(
    #             "torreLondres", TOLController, self.reporteModel)

    #         self.addPaginaVisitada("torreLondres")
    #         self.menuController.updatePagesVisited(self.paginasVisitadas)
    #         self.showSpecificWindowMenu("torreLondres")

    # def showButt(self, invalidArgs, prevPrueba):
    #     """
    #      Metodo que se encarga de cargar la vista y el controlador de la prueba de TOL
    #      Args: 
    #       invalidArgs: Lista de elementos inválidos
    #       prevPrueba: Prueba previa a la de TOL
    #     """
    #     if len(invalidArgs) != 0:
    #         self.displayModal(invalidArgs)
    #         self.router.getController(self.paginasVisitadas[-1]).emptyInvalidArgs()
    #     else:
    #         if not isinstance(prevPrueba, ReporteModel):
    #             self.reporteModel.addPrueba(prevPrueba)

    #         self.router.setController(
    #             "motivoDeportivo", ButtController, self.reporteModel)

    #         self.addPaginaVisitada("motivoDeportivo")
    #         self.menuController.updatePagesVisited(self.paginasVisitadas)
    #         self.showSpecificWindowMenu("motivoDeportivo")

    # def showPittsburgh(self, invalidArgs, prevPrueba):
    #     """
    #      Metodo que se encarga de cargar la vista y el controlador de la prueba de TOL
    #      Args: 
    #       invalidArgs: Lista de elementos inválidos
    #       prevPrueba: Prueba previa a la de TOL
    #     """
    #     if len(invalidArgs) != 0:
    #         self.displayModal(invalidArgs)
    #         self.router.getController(self.paginasVisitadas[-1]).emptyInvalidArgs()
    #     else:
    #         if not isinstance(prevPrueba, ReporteModel):
    #             self.reporteModel.addPrueba(prevPrueba)

    #         self.router.setController(
    #             "pittsburgh", PittsburghController, self.reporteModel)

    #         self.addPaginaVisitada("pittsburgh")
    #         self.menuController.updatePagesVisited(self.paginasVisitadas)
    #         self.showSpecificWindowMenu("pittsburgh")

    # def showSCL90(self, invalidArgs, prevPrueba):
    #     """
    #      Metodo que se encarga de cargar la vista y el controlador de la prueba de SCL90
    #      Args: 
    #       invalidArgs: Lista de elementos inválidos
    #       prevPrueba: Prueba previa a la de SCL90
    #     """
    #     if len(invalidArgs) != 0:
    #         self.displayModal(invalidArgs)
    #         self.router.getController(self.paginasVisitadas[-1]).emptyInvalidArgs()
    #     else:
    #         if not isinstance(prevPrueba, ReporteModel):
    #             self.reporteModel.addPrueba(prevPrueba)

    #         self.router.setController(
    #             "scl90", SCL90Controller, self.reporteModel)

    #         self.addPaginaVisitada("scl90")
    #         self.menuController.updatePagesVisited(self.paginasVisitadas)
    #         self.showSpecificWindowMenu("scl90")

    # def showReporte(self, invalidArgs, prevPrueba):
    #     """
    #      Metodo que se encarga de cargar la vista y el controlador del Reporte
    #      Args: 
    #       invalidArgs: Lista de elementos inválidos
    #       prevPrueba: Prueba previa al Reporte
    #     """
    #     if len(invalidArgs) != 0:
    #         self.displayModal(invalidArgs)
    #         self.router.getController(self.paginasVisitadas[-1]).emptyInvalidArgs()
    #     else:
    #         if not isinstance(prevPrueba, ReporteModel):
    #             self.reporteModel.addPrueba(prevPrueba)

    #         self.router.setController(
    #             "report", ReporteController, self.reporteModel)

    #         self.addPaginaVisitada("report")
    #         self.menuController.updatePagesVisited(self.paginasVisitadas)
    #         self.showSpecificWindowMenu("report")
            

    def newReport(self):
        """
         Metodo que se encarga de crear un nuevo reporte y regresar a la pantalla principal
        """
        self.resetReport(False)
        self.router.getController("informacionSujeto").newInfo()
        self.showMainWindow()

    def resetReport(self, resetMainWindow):
        """
         Método que se encarga de eliminar todas las vistas y controladores de las mismas
         Args: 
          resetMainWindow: Booleano que se encarga de notificar si se debe de eliminar el controlador y vista de mainWindow
        """
        self.menuController.resetPagesVisited(self.resetPaginasVisitadas())

        self.reporteModel = None

        self.router.resetRouterViews(resetMainWindow)
        self.router.resetRouterControllers(resetMainWindow)


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
