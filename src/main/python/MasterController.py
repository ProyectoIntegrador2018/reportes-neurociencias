# Controlador principal de todo el programa
# recursion error
# https://github.com/pyinstaller/pyinstaller/issues/2919#issuecomment-710716978
import sys
if getattr(sys, 'frozen', False) and sys.platform == 'darwin':
    os.environ['QTWEBENGINEPROCESS_PATH'] = os.path.normpath(os.path.join(
        sys._MEIPASS, 'PyQt5', 'Qt', 'lib',
        'QtWebEngineCore.framework', 'Helpers', 'QtWebEngineProcess.app',
        'Contents', 'MacOS', 'QtWebEngineProcess'
    ))

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
from controladores.ReporteController import ReporteController
from controladores.TOLController import *
from controladores.ButtController import *
from controladores.PittsburghController import *
from controladores.PruebaSeleccionController import *
from ReporteModel import ReporteModel
from Routes import Router
from AppCtxt import APPCTXT
import resources


class MasterController:
    def __init__(self):
        self.modalController = ModalController()

        self.pagesFunctions = {
            "seleccionarPruebas": self.pruebasSeleccionadas,
            "informacionSujeto": self.asignaReporte,
            "fluidezVerbal": self.customShow("fluidezVerbal", FluidezVerbalController),
            "denominacion": self.customShow("denominacion", DenominacionController),
            "comprensionVerbal": self.customShow("comprensionVerbal", MVCController),
            "memoriaVisoespacial": self.customShow("memoriaVisoespacial", MemoriaVisoespaciaController),
            "tmt": self.customShow("tmt", TMTController),
            "abstraccion": self.customShow("abstraccion", AbstraccionController),
            "digitos": self.customShow("digitos", DigitosController),
            "sdmt": self.customShow("sdmt", SDMTController),
            "lns": self.customShow("lns", LNSController),
            "d2": self.customShow("d2", D2Controller),
            "hopkins": self.customShow("hopkins", HopkinsController),
            "stroop": self.customShow("stroop", StroopController),
            "torreLondres": self.customShow("torreLondres", TOLController),
            "motivoDeportivo": self.customShow("motivoDeportivo", ButtController),
            "pittsburgh": self.customShow("pittsburgh", PittsburghController),
            "scl90": self.customShow("scl90", SCL90Controller),
            "report": self.customShow("report", ReporteController),
            # do not remove used for reseting and initialize pruebas
            "dummyWindow": self.newReport
        }

        self.router = None  # early init
        self.paginasVisitadas = ["seleccionarPruebas"]  # intial view
        self.initPossibleRoutes([
            "seleccionarPruebas",
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
        ])

        self.router = Router(self.paginasDisponibles)
        self.router.setController(
            "seleccionarPruebas", PruebaSeleccionController)

        self.router.setController(
            "informacionSujeto", MainWindowController)

        self.listMenu = self.router.getController(
            "informacionSujeto").getListMenu()

        self.menuController = MenuController(
            self.paginasVisitadas, self.router.getEntrieNames())
        self.menuController.switch_window.connect(
            self.showSpecificWindowMenu)

        # we substract 3 (
        # 1 - selected pruebas
        # 2 - informacion sujeto
        # 3 - reporte view
        # )
        self.progressBarController = ProgressBarController(
            len(self.router)-2)

        self.currentWindow = self.router.getView("dummyWindow")
        self.nextWindow = self.router.getView("seleccionarPruebas")
        self.nextController = None
        self.reporteModel = None

    def initPossibleRoutes(self, possibleRoutes):
        self.paginasDisponibles = possibleRoutes
        self.paginasDisponibles = self.fillAvailablePages(
            self.paginasDisponibles)

        if isinstance(self.router, Router):
            self.router.updatePossibleRoutes(self.paginasDisponibles)

    def fillAvailablePages(self, pages):
        return [[page, self.pagesFunctions[page]] for page in pages]

    def resetPaginasVisitadas(self):
        """
         Método que se encarga de restablecer las páginas visitadas
        """
        self.paginasVisitadas = ["seleccionarPruebas"]
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
                fun_update = getattr(currentController, "updateButtonText", None)
                if callable(fun_update):
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
        tmpMenu = currentController.getListMenu()
        if tmpMenu is None:
            return

        self.listMenu = tmpMenu
        self.menuController.updateListView(self.listMenu)
        self.menuController.poblarLista()

    def connectProgressBar(self, currentController):
        """
         Método que se encarga de conectar el menú con la vista del controlador actual
         Args:
          currentController: Valor que contiene el controlador de la prueba actual
        """
        self.progressBarController.updateProgress(len(self.paginasVisitadas)-1)

        tmpProgress = currentController.getProgressBar()
        if tmpProgress is None:
            return

        self.progressBarController.setProgressBar(tmpProgress)

    def getRouteProgress(self, routeName):
        for idx, key in enumerate(self.paginasVisitadas):
            if key == routeName:
                return idx

        return 0

    def showSpecificWindowMenu(self, elemSelected):
        """
         Método que se encarga de manejar el doble click sobre un elemento del menú
         Args:
          elemSelected: Lista que contiene el elemento seleccionado
        """
        self.nextWindow, self.nextController = self.router.getRouteViewAndController(
            elemSelected)
        # print("hola", self.nextWindow, self.nextController, elemSelected)
        progress = self.getRouteProgress(elemSelected)
        self.menuController.updateCurrentWindow(progress)

        if self.windowsAreDifferent():
            self.connectMenu(self.nextController)
            self.connectProgressBar(self.nextController)
            self.updateButtonText(elemSelected, self.nextController)
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
        # print("modal 1")
        self.modalController.setWindowTitle(modalTitle)
        self.modalController.setHeader(modalHeader)
        self.modalController.setContenido(listMissingElem)
        self.modalController.showModal()

    def showMainWindow(self):
        """
         Método que se encarga de cargar la vista de la pantalla a MainWindow, así como el controlador de la misma.
        """
        self.showSpecificWindowMenu(self.paginasVisitadas[0])

    def pruebasSeleccionadas(self, listMissingElem, selectedPruebas):
        """
         Metodo para inicializar las pruebas seleccionadas
         Args:
          listMissingElem: Lista de elementos inválidos
          selectedPruebas: Arreglo de string posibles
        """
        if len(listMissingElem) != 0:
            self.displayModal(listMissingElem)
            self.router.getController(
                self.paginasVisitadas[-1]).emptyInvalidArgs()
        else:
            self.initPossibleRoutes(selectedPruebas)
            entriNames = self.router.getEntrieNames()
            entriNames.remove("Seleccionar pruebas")
            self.menuController = MenuController(
                self.paginasVisitadas, entriNames)
            self.menuController.switch_window.connect(
                self.showSpecificWindowMenu)
            self.progressBarController = ProgressBarController(
                len(self.router)-3)

            self.addPaginaVisitada("seleccionarPruebas")
            self.menuController.updatePagesVisited(self.paginasVisitadas)
            self.showSpecificWindowMenu("informacionSujeto")

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
            self.addPaginaVisitada("informacionSujeto")
            self.menuController.updatePagesVisited(self.paginasVisitadas)
            func([], self.reporteModel)

        self.router.getController("informacionSujeto").emptyMissingArgs()

    def customShow(self, nameKey, ClassRef):
        def F(invalidArgs, prevPrueba):
            if len(invalidArgs) != 0:
                self.displayModal(
                    invalidArgs, modalHeader="Deben de ser mayor a 0:")
                self.router.getController(
                    self.paginasVisitadas[-1]).emptyInvalidArgs()
            else:
                if not isinstance(prevPrueba, ReporteModel):
                    self.reporteModel.addPrueba(prevPrueba)

                self.router.setController(
                    nameKey, ClassRef, self.reporteModel)

                self.addPaginaVisitada(nameKey)
                self.menuController.updatePagesVisited(self.paginasVisitadas)
                self.showSpecificWindowMenu(nameKey)

        return F

    def newReport(self):
        """
         Metodo que se encarga de crear un nuevo reporte y regresar a la pantalla principal
        """
        reporteController = self.router.getController("report")
        if not reporteController.hasSaveCSV and not reporteController.csvDialogHasShown:
            self.displayModal([], 
                    modalTitle="Guarda los datos",
                    modalHeader="No has guardado el reporte en CSV, tus datos se perderan \nSi planeas guardar tus datos da click en Guardar CSV")
            reporteController.csvDialogHasShown = True
            return

        self.resetReport(False)
        self.router.getController("seleccionarPruebas").newInfo()
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
    # app = QtWidgets.QApplication(sys.argv)
    
    # cssUrl = QUrl(QDir.currentPath()+"/app.css").toString()
    cssUrl = APPCTXT().get_resource("app.css")
    with open(cssUrl, 'r') as f:
        APPCTXT().app.setStyleSheet(f.read())
        # app.setStyleSheet(f.read())
    # cssUrl = QUrl(QDir.currentPath()+"/app.css").toString()
    # app.setStyleSheet(open('C:\\Users\\usuario\\Desktop\\reportes-neurociencias\\src\\main\\python\\app.css').read())
    # app.setStyleSheet(open(cssUrl).read())
    # app = QtWidgets.QApplication(sys.argv)
    # APPCTXT.setStyleSheet(open('app.css').read())
    masterController = MasterController()
    masterController.showMainWindow()
    sys.exit(APPCTXT().app.exec_())
    # sys.exit(app.exec_())


if __name__ == '__main__':
    main()
    