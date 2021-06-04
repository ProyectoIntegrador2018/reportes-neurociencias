# Contolador de la vista seleccion de pruebas
from PyQt5 import QtWidgets, QtCore, QtGui
from vistas.PruebaSeleccionWindowWidget import PruebaSeleccionWindowWidget
from ControllerModel import *
from Routes import Router
import pandas as pd
import csv

class PruebaSeleccionController(QtWidgets.QWidget, ControllerModel):
    switch_window = QtCore.pyqtSignal(object, object, object)

    atributosMapper = {
        "DIGITOS": {
            "DD": 'sbDirectos', 
            "DI": 'sbInversos',
        },
        "Datos":{
            "nombreExaminado": 'leName',
            "id": 'leId',
            "nombreExaminador": 'leExaminer',
            "edad": 'sbAge',
            "educacion": 'sbEscolaridad',
            "genero": 'cbSexo',
            "fechaNacimiento": 'deFechaNacimiento',
            "lateralidad": 'cbLateralidad',
            "fecha": 'deFecha',
            "carrera": 'leCarrera',
            "semestre": 'sbSemestre',
            "equipo": 'leEquipo',
            "deporte": 'leDeporte',
        },
        "ABS": {
            "ABS": 'sbAbstraccion',
        },
        "Motivos Deportivos de Butt": {
            "CONFLICTO": 'sbConflicto',
            "RIVALIDAD": 'sbRivalidad',
            "SUFICIENCIA": 'sbSuficiencia',
            "COOPERACION": 'sbCooperacion',
            "AGRESIVIDAD": 'sbAgresividad'
        },
        "Torre de Londres": {
            "C" : 'sbTotalCorrectos',
            "M" : 'sbMovimientosTotales',
            "IT" : 'sbTiempoLatencia',
            "ET" : 'sbTiempoEjecucion',
            "TT" : 'sbTiempoResolucion',
            "TV" : 'sbVT',
            "RV" : 'sbVR',
        },
        "D2": {
            "TR": 'sbTR',
            "TA": 'sbTA',
            "O": 'sbO',
            "C": 'sbC',
            "VAR": 'sbVAR',
        },
        "DENOM": {
            "DV": 'sbDenomImg',
            "DVt": 'sbDenomImgT',
        },
        "FLUIDEZ": {
            "P": 'sbWords',
            "A": 'sbAnimals',
        },
        "HVLT-R": {
            "M.I.": 'sbSpan',
            "M.D.": 'sbTotal',
        },
        "LNS": {
            "I": 'sbSpan',
            "T": 'sbTotal',
        },
        "BVMT-R": {
            "T": 'sbDenomImg',
            "Dif": 'sbDenomImgT',
        },
        "COMP V": {
            "MVC": 'sbMVC',
            "MVCt": 'sbMVCT',
        },
        "PSQI": {
            "1.": 'comp1',
            "2.": 'comp2',
            "3.": 'comp3',
            "4.": 'comp4',
            "5.": 'comp5',
            "6.": 'comp6',
            "7.": 'comp7',
        },
        "SCL-90": {
            "SO": 'dsbSOM',
            "OB": 'dsbOBS',
            "IN": 'dsbINT',
            "DE": 'dsbDEP',
            "AN": 'dsbANS',
            "HO": 'dsbHOS',
            "FO": 'dsbFOB',
            "PA": 'dsbPAR',
            "PSI": 'dsbPSI',
            "GSI": 'dsbGSI',
            "PST": 'dsbPST',
            "PSDI": 'dsbPSDI',
        },
        "SDMT": {
            "C": 'sbSDMT',
        },
        "STROOP": {
            "P": 'sbTR',
            "C": 'sbTA',
            "I": 'sbO',
        },
        "TMT": {
            "A": 'sbTMTA',
            "B": 'sbTMTB',
        },
        "BSI-18": {
            "DIRECTA": 'Q1',
            "SOM": 'Q2',
            "DEP": 'Q3',
        },
        "BussYPerry": {
            'agFis': 'sbTMTA',
            'agVer': 'sbTMTB',
            'ira': 'sbTMTC',
            'hos': 'sbTMTD',
        },
        "EMD": {
            'ME': 'sbTMTA',
            'MICO': 'sbTMTB',
            'MIE': 'sbTMTC',
            'MIA': 'sbTMTD',
            'MICU': 'sbTMTE',
            'Amotivacion': 'sbTMTF',
            'MID': 'sbTMTG',
        }
    }

    # Mapper para mapear el nombre visual (excel) de una prueba con su nombre (variable) para el codigo
    pruebasMapper = {
        "ABS": "abstraccion",
        "DIGITOS": "digitos",
        "Motivos Deportivos de Butt": "motivoDeportivo",
        "Torre de Londres": 'torreLondres',
        "D2": "d2",
        "FLUIDEZ": "fluidezVerbal",
        "DENOM": "denominacion",
        "COMP V": "comprensionVerbal",
        "BVMT-R": "memoriaVisoespacial",
        "TMT": "tmt",
        "BussYPerry": "bussyPerry",
        "SDMT": "sdmt",
        "LNS": "lns",
        "HVLT-R": "hopkins",
        "STROOP": "stroop",
        "BSI-18": "bsi18",
        "Datos": 'info_personal',
        "PSQI": 'pittsburgh',
        "SCL-90": 'scl90',
        "EMD": 'emd'
    }

    data = {}
    pruebasViewsMapper = {}

    def __init__(self, mainWindow, reporteModel=None):
        QtWidgets.QWidget.__init__(self)
        self.seleccionView = PruebaSeleccionWindowWidget(mainWindow)
        self.seleccionView.backButton.clicked.connect(self.file_open)
        self.reporteModel = reporteModel
        self.invalidArgs = list()
        self.initialRoutes = ["seleccionarPruebas",
                              "informacionSujeto", ]
        self.endRoutes = ["report",
                          # do not remove used for reseting and initialize pruebas
                          "dummyWindow", ]
        self.pruebasSeleccionadas = []

        self.seleccionView.checkBoxPruebaEMD.stateChanged.connect( 
            lambda: self.addSelectedPrueba("emd", self.seleccionView.checkBoxPruebaEMD))
        self.seleccionView.checkBoxPruebaBussyPerry.stateChanged.connect(
            lambda: self.addSelectedPrueba("bussyPerry", self.seleccionView.checkBoxPruebaBussyPerry))
        self.seleccionView.checkBoxPruebaFluidezVerbal.stateChanged.connect(
            lambda: self.addSelectedPrueba("fluidezVerbal", self.seleccionView.checkBoxPruebaFluidezVerbal))
        self.seleccionView.checkBoxPruebaDenominacion.stateChanged.connect(
            lambda: self.addSelectedPrueba("denominacion", self.seleccionView.checkBoxPruebaDenominacion))
        self.seleccionView.checkBoxComprensionVerbal.stateChanged.connect(
            lambda: self.addSelectedPrueba("comprensionVerbal", self.seleccionView.checkBoxComprensionVerbal))
        self.seleccionView.checkBoxPruebaMemoriaVisoespacial.stateChanged.connect(
            lambda: self.addSelectedPrueba("memoriaVisoespacial", self.seleccionView.checkBoxPruebaMemoriaVisoespacial))
        self.seleccionView.checkBoxPruebaTMT.stateChanged.connect(
            lambda: self.addSelectedPrueba("tmt", self.seleccionView.checkBoxPruebaTMT))
        self.seleccionView.checkBoxPruebaAbstraccion.stateChanged.connect(
            lambda: self.addSelectedPrueba("abstraccion", self.seleccionView.checkBoxPruebaAbstraccion))
        self.seleccionView.checkBoxPruebaDigitos.stateChanged.connect(
            lambda: self.addSelectedPrueba("digitos", self.seleccionView.checkBoxPruebaDigitos))
        self.seleccionView.checkBoxPruebaSDMT.stateChanged.connect(
            lambda: self.addSelectedPrueba("sdmt", self.seleccionView.checkBoxPruebaSDMT))
        self.seleccionView.checkBoxPruebaLNS.stateChanged.connect(
            lambda: self.addSelectedPrueba("lns", self.seleccionView.checkBoxPruebaLNS))
        self.seleccionView.checkBoxPruebaD2.stateChanged.connect(
            lambda: self.addSelectedPrueba("d2", self.seleccionView.checkBoxPruebaD2))
        self.seleccionView.checkBoxPruebaHopkins.stateChanged.connect(
            lambda: self.addSelectedPrueba("hopkins", self.seleccionView.checkBoxPruebaHopkins))
        self.seleccionView.checkBoxPruebaStroop.stateChanged.connect(
            lambda: self.addSelectedPrueba("stroop", self.seleccionView.checkBoxPruebaStroop))
        self.seleccionView.checkBoxTorreDeLondres.stateChanged.connect(
            lambda: self.addSelectedPrueba("torreLondres", self.seleccionView.checkBoxTorreDeLondres))
        self.seleccionView.checkBoxPruebaMotivosDeportivos.stateChanged.connect(
            lambda: self.addSelectedPrueba("motivoDeportivo", self.seleccionView.checkBoxPruebaMotivosDeportivos))
        self.seleccionView.checkBoxPruebaDePittsburgh.stateChanged.connect(
            lambda: self.addSelectedPrueba("pittsburgh", self.seleccionView.checkBoxPruebaDePittsburgh))
        self.seleccionView.checkBoxPruebaSCL90.stateChanged.connect(
            lambda: self.addSelectedPrueba("scl90", self.seleccionView.checkBoxPruebaSCL90))
        self.seleccionView.checkBoxPruebaBSI18.stateChanged.connect(
            lambda: self.addSelectedPrueba("bsi18", self.seleccionView.checkBoxPruebaBSI18))

        self.seleccionView.pushButtonContinuar.clicked.connect(self.getData)

        self.pruebasViewsMapper = {
            "FLUIDEZ": self.seleccionView.checkBoxPruebaFluidezVerbal,
            "DENOM": self.seleccionView.checkBoxPruebaDenominacion,
            "COMP V": self.seleccionView.checkBoxComprensionVerbal,
            "BVMT-R": self.seleccionView.checkBoxPruebaMemoriaVisoespacial,
            "TMT": self.seleccionView.checkBoxPruebaTMT,
            "BussYPerry": self.seleccionView.checkBoxPruebaBussyPerry,
            "ABS": self.seleccionView.checkBoxPruebaAbstraccion,
            "DIGITOS": self.seleccionView.checkBoxPruebaDigitos,
            "Motivos Deportivos de Butt": self.seleccionView.checkBoxPruebaMotivosDeportivos,
            "Torre de Londres": self.seleccionView.checkBoxTorreDeLondres,
            "D2": self.seleccionView.checkBoxPruebaD2,
            "SDMT": self.seleccionView.checkBoxPruebaSDMT,
            "LNS": self.seleccionView.checkBoxPruebaLNS,
            "HVLT-R": self.seleccionView.checkBoxPruebaHopkins,
            "PSQI": self.seleccionView.checkBoxPruebaDePittsburgh,
            "STROOP": self.seleccionView.checkBoxPruebaStroop,
            "BSI-18": self.seleccionView.checkBoxPruebaBSI18,
            "SCL-90": self.seleccionView.checkBoxPruebaSCL90,
            "EMD": self.seleccionView.checkBoxPruebaEMD,
        }

    def changeView(self):
        """
        Método encargado de notificar los elementos que serán pasados como parámetros a la siguiente vista
        """
        totalRoutes = self.initialRoutes + self.pruebasSeleccionadas + self.endRoutes
        self.switch_window.emit(self.invalidArgs, totalRoutes, self.data)

    def getData(self):
        if len(self.pruebasSeleccionadas) == 0:
            self.invalidArgs = ["ALMENOS SELECCIONAR UNA PRUEBA"]

        self.changeView()

    def emptyInvalidArgs(self):
        """
        Metodo para vaciar la lista de elementos invalidos
        """
        self.invalidArgs = list()

    def getListMenu(self):
        return None

    def getProgressBar(self):
        return None

    def newInfo(self):
        self.resetPruebas()
        self.seleccionView.checkBoxPruebaBussyPerry.setChecked(False)
        self.seleccionView.checkBoxPruebaEMD.setChecked(False)
        self.seleccionView.checkBoxPruebaFluidezVerbal.setChecked(False)
        self.seleccionView.checkBoxPruebaDenominacion.setChecked(False)
        self.seleccionView.checkBoxComprensionVerbal.setChecked(False)
        self.seleccionView.checkBoxPruebaMemoriaVisoespacial.setChecked(False)
        self.seleccionView.checkBoxPruebaTMT.setChecked(False)
        self.seleccionView.checkBoxPruebaAbstraccion.setChecked(False)
        self.seleccionView.checkBoxPruebaDigitos.setChecked(False)
        self.seleccionView.checkBoxPruebaSDMT.setChecked(False)
        self.seleccionView.checkBoxPruebaLNS.setChecked(False)
        self.seleccionView.checkBoxPruebaD2.setChecked(False)
        self.seleccionView.checkBoxPruebaHopkins.setChecked(False)
        self.seleccionView.checkBoxPruebaStroop.setChecked(False)
        self.seleccionView.checkBoxTorreDeLondres.setChecked(False)
        self.seleccionView.checkBoxPruebaMotivosDeportivos.setChecked(False)
        self.seleccionView.checkBoxPruebaDePittsburgh.setChecked(False)
        self.seleccionView.checkBoxPruebaSCL90.setChecked(False)
        self.seleccionView.checkBoxPruebaBSI18.setChecked(False)
        self.seleccionView.labelPruebasSeleccionadasDisplay.setText("0")
        self.data = {}

    def addSelectedPrueba(self, checkboxName, checkboxItem):
        if checkboxName not in self.pruebasSeleccionadas and checkboxItem.isChecked():
            self.pruebasSeleccionadas.append(checkboxName)
        elif checkboxName in self.pruebasSeleccionadas:
            self.pruebasSeleccionadas.remove(checkboxName)
        self.seleccionView.labelPruebasSeleccionadasDisplay.setText(
            str(len(self.pruebasSeleccionadas)))

    def resetPruebas(self):
        self.pruebasSeleccionadas = []

    def file_open(self):
        fileName =  QtWidgets.QFileDialog.getOpenFileName(self, 'Open file', 'c:\\',"Image files (*.xlsx)")

        df = pd.read_excel(fileName[0], sheet_name=None, index_col=0, engine='openpyxl')
        for name, sheet in df.items():
            pruebaName = self.pruebasMapper[name]
            pruebaData = {}
            for i, value in sheet.to_dict()['Valor'].items():
                try:
                    pruebaData[self.atributosMapper[name][i]] = value
                except:
                    print("Variable en la pestaña" + name + " no es parte de los inputs de la prueba")

            self.data[pruebaName] = pruebaData
            if(name != 'Datos'):
                self.pruebasViewsMapper[name].setChecked(True)
                self.addSelectedPrueba(pruebaName, self.pruebasViewsMapper[name])
                self.pruebasSeleccionadas.append(pruebaName)