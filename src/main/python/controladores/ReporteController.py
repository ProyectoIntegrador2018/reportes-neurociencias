#Controlador de la vista de ReporteWindow
from PyQt5 import QtWidgets, QtCore, Qt
from vistas.ReporteWindowWidget import *
from ReporteModel import *
from PruebaModel import *
from ControllerModel import *
import matplotlib.pyplot as plt
import numpy as np
import os
import csv
import pdfkit
#from weasyprint import HTML, CSS
from AppCtxt import APPCTXT
# from MasterController import appctxt
import tempfile
from shutil import copyfile


class ReporteController(QtWidgets.QWidget, ControllerModel):
	#Atributo empleado para realizar el cambio de vista
	switch_window = QtCore.pyqtSignal()

	def __init__(self, mainWindow, reporteModel=None):
		QtWidgets.QWidget.__init__(self)
		self.reporteModel = reporteModel
		self.mainWindow = mainWindow

		self.hasSaveCSV = False
		self.hasSavePDF = False
		self.csvDialogHasShown = False

		tmpdir = os.path.join(tempfile.gettempdir(), "synapps")
		if not os.path.exists(tmpdir):
			os.makedirs(tmpdir)
		# tempUrl = QUrl(QDir.currentPath()+"/vistas/Reporte/reporte.html")
		# tempUrl = tempUrl.toString()
		# imageUrl = QUrl(QDir.currentPath()+"/vistas/Reporte/reporte.png")
		# imageUrl = imageUrl.toString()
		# logoUrl = QUrl(QDir.currentPath()+"/vistas/Reporte/logoReporte.png")
		tempUrl = os.path.join(tmpdir, "reporte.html")
		cssUrl = APPCTXT().get_resource("./vistas/Reporte/reporte.css")
		copyfile(cssUrl, os.path.join(tmpdir, 'reporte.css'))
		imageUrl = os.path.join(tmpdir, 'reporte.png')
		# imageUrl = APPCTXT().get_resource("./vistas/Reporte/reporte.png")
		# copyfile(imageUrl, os.path.join(tmpdir, 'reporte.png'))
		logoUrl = APPCTXT().get_resource("./vistas/Reporte/logoReporte.png")
		copyfile(logoUrl, os.path.join(tmpdir, 'logoReporte.png'))
		print(tmpdir)

		self.url = tempUrl
		self.cssUrl = cssUrl
		self.image = imageUrl
		self.logo = logoUrl
		self.reporteView = None
		self.pruebayLabels = {
			"FLUIDEZ":[('RV', 'TV')],
			"DENOM":[('TT', 'ET')],
			"COMP V":[('IT', 'M')],
			"BVMT-R":[('C', 'I')],
			"TMT":[('C', 'P')],
			"BussYPerry": [('AgFis','AgVer','Ira','Hos')],
			"ABS":['M.D.'],
			"DIGITOS":[('M.I.', 'VAR')],
			"SDMT":['CON'],
			"LNS":[('TOT', 'C')],
			"D2":[('O', 'TA', 'TR', 'T', 'I', 'C', 'DI')],
			"HVLT-R":[('DD', 'ABS')],
			"STROOP":[('B', 'A', 'Dif')],
			"Denominación":[('T', 'MVCt', 'MVC', 'DVt', 'DV', 'A', 'P')],
			"BSI-18":[('SOM', 'DEP', 'ANS', 'IGS')]
		}
		self.csvHeaders = ["nombreExaminado","id","fecha","genero","edad","fechaNacimiento",
			"lateralidad","nombreExaminador","carrera","semestre","educacion","equipo","deporte",
			'RV', 'TV', 'TT', 'ET', 'IT', 'M', 'C', 'I', 'C', 'P', 'M.D.', 'M.I.', 'VAR', 'CON', 'TOT', 'C', 'O',
			'TA', 'TR', 'T', 'I', 'C', 'DI', 'DD', 'ABS', 'B', 'A', 'Dif', 'T', 'MVCt', 'MVC', 'DVt', 'DV', 'A', 'P','SOM', 'DEP', 'ANS', 'IGS','Ira','AgFis','AgVer','Hos']
		self.escalares = []
		self.escalaresLabel = []
		self.loadReporte()

	def loadReporte(self):
		"""
		 Método encargado de cargar la vista del reporte
		"""
		self.createReporte()
		if isinstance(self.reporteView, type(None)):
			self.reporteView = ReporteWindowWidget(self.mainWindow, self.url)
		else:
			del self.reporteView
			self.reporteView = ReporteWindowWidget(self.mainWindow, self.url)
			
		self.reporteView.pbStart.clicked.connect(self.launchBrowser)
		self.reporteView.pbRestart.clicked.connect(self.changeView)
		self.reporteView.pdSaveCsv.clicked.connect(self.exportCsvClick)

	def launchBrowser(self):
		"""
		 Método encargado de abrir el reporte en el navegador predefinido para abrir los HTML
		"""
		#Qt.QDesktopServices.openUrl(Qt.QUrl.fromLocalFile(self.url))
		options = QtWidgets.QFileDialog.Options()
		options |= QtWidgets.QFileDialog.DontUseNativeDialog
		options |= QtWidgets.QFileDialog.DontConfirmOverwrite
		fileName, _ = QtWidgets.QFileDialog.getSaveFileName(self,"QFileDialog.getSaveFileName()","","PDF (*.pdf)", options=options)
		if not fileName:
			return

		if not self.hasSavePDF:
			self.saveToPdf(fileName)
			self.hasSavePDF = True

	def saveToPdf(self, fileName):
		options = {
			'disable-smart-shrinking': '',
			"enable-local-file-access": None,
  			"print-media-type": None,
		}

		pdfkit.from_file(self.url, fileName + '.pdf',options=options)
		#HTML(self.url).write_pdf(fileName)
		# reporte = self.reporteModel.reporte

		# append_write = ""
		# if os.path.exists(fileName):
		# 	append_write = 'a' # append if already exists
		# else:
		# 	append_write = 'w' # make a new file if not

		# data = self.getRowData()
		# with open(fileName,append_write, newline='', encoding='utf-8') as f:
		# 	w = csv.DictWriter(f, self.csvHeaders)
		# 	if append_write == 'w':
		# 		w.writeheader()
			
		# 	w.writerow(data)
		

	def createTableImg(self, escalares, escalaresLabel):
		"""
		 Método encargado de crear la gráfica del reporte
		"""
		yPos = np.arange(len(escalaresLabel)-1,-1,-1)
		escalaresLabel.reverse()
		yLabels = escalaresLabel
		
		x = np.arange(0,21)
		xi = list(range(len(x)))
		yi = np.arange(0,len(escalaresLabel))
		a = (0,0)
		b = (6.5, len(escalaresLabel)-1)

		xcoords = [10]
		colors = ['White']

		for xc,c in zip(xcoords,colors):
		    plt.axvline(x=xc, linewidth = 12, c=c, linestyle = '-')

		ax = plt.gca()
		rojo_lower = 0
		rojo_upper = 7.5
		amarillo_lower = rojo_upper
		amarillo_upper = 12.5
		verde_lower = amarillo_upper
		verde_upper = 20
		ax.axvspan(rojo_lower, rojo_upper, facecolor='Tomato', alpha=0.7)
		ax.axvspan(amarillo_lower, amarillo_upper, facecolor='Yellow', alpha=0.7)
		ax.axvspan(verde_lower, verde_upper, facecolor='Chartreuse', alpha=0.7)

		# Hide the right and top spines
		ax.spines['right'].set_visible(False)
		ax.spines['top'].set_visible(False)

		fig = plt.gcf()
		graphWidth = 10.5
		graphHeight = 15
		fig.set_size_inches(graphWidth, graphHeight)
		plt.grid(b=True, which='major', color='white',  linestyle='-')
		plt.xticks(xi, x)
		plt.yticks(yi, yLabels)
		plt.tick_params(axis='x', colors= '#b0aba5', direction='out', length=4, width=12)
		plt.tick_params(axis='y', colors='#b0aba5', direction='out', length=4, width=8)
		plt.xlim(-0.1, 20.1)
		plt.ylim(-1,len(escalaresLabel)-0.5)
		plt.plot(escalares, yPos, marker = 'o', color = 'Red', linewidth=1)
		if os.path.isfile(self.image):
			os.remove(self.image)
		plt.savefig(self.image, bbox_inches='tight')
		plt.clf() #con esta linea no se sobreescriben puntos en la grafica al actualizar los datos de las pruebas
		plt.close(fig)

	
	def createTableHeaders(self, encabezados):
		"""
		 Método encargado de generar las etiquetas HTML de encabezados de una tabla
		 Args:
		  encabezados: lista de elementos que serán encabezados en alguna tabla
		"""
		raw_html = ""
		for elem in encabezados:
			raw_html += '<th>'
			raw_html += elem
			raw_html += '</th>'
		return raw_html

	def createTableElements(self, elementos):
		"""
		 Método encargado de generar las etiquetas HTML de elementos de una tabla
		 Args:
		  elementos: lista de elementos que serán elementos en alguna tabla
		"""
		raw_html = ""
		for elem in elementos:
			raw_html += '<td>'
			raw_html += elem
			raw_html += '</td>'
		return raw_html


	def createReporte(self):
		"""
		 Método encargado de crear el HMTL del reporte
		"""
		reporte = self.reporteModel.reporte
		raw_html = '<!DOCTYPE html><html><head><meta charset="utf-8"></head>'
		raw_html += '<link rel="stylesheet" href="w3-layout.css">'
		raw_html += '<link rel="stylesheet" href="reporte.css">'
		raw_html += '<link rel="stylesheet" media="print" href="reporte.css" />'
		raw_html += '<link rel="stylesheet" media="screen" href="reporte.css" />'
		raw_html += '<body>'
		raw_html += '<div class="w3-container">'
		raw_html += '<div class="w3-row">'
		raw_html += '<div class="w3-col">'
		raw_html += '<div class="reporte-header">'
		raw_html += '<div class="div-foto">'
		raw_html += '<img src="logoReporte.png" class="logo-reporte">'
		raw_html += '</div>'
		raw_html += '<div class="div-titulo">'
		raw_html += '<h1 class = "center-text">Evaluación Neurocognitiva de ' + reporte["deporte"] + '</h1>'
		raw_html += '</div>'
		raw_html += '</div>'
		
		raw_html += '<div class="new-table">'

		"""
		ESTA ES UNA ROW DE LA TABLA DE INFO GENERAL
		"""
		raw_html += '<table style="width:100%">' 	#Empieza una tabla

		raw_html += '<tr class="row-info top-row">'							#Empieza una row de la tabla
		headerElements = ['Nombre', 'ID', 'Fecha', 'Género']
		raw_html += self.createTableHeaders(headerElements)
		raw_html += '</tr>'

		raw_html += '<tr class="row-info">'							#Empieza una row de la tabla 
		tableElements = [reporte["nombreExaminado"], reporte["id"], reporte["fecha"], reporte["genero"]]
		raw_html += self.createTableElements(tableElements)
		raw_html += '</tr>'
		raw_html += '</table>'


		"""
		ESTA ES UNA ROW DE LA TABLA DE INFO GENERAL
		"""
		raw_html += '<table style="width:100%">' 	#Empieza una tabla
		raw_html += '<tr class="row-info">'							#Empieza una row de la tabla
		headerElements = ['Fecha de Nacimiento', 'Edad', 'Lateralidad', 'Carrera', 'Semestre']
		raw_html += self.createTableHeaders(headerElements)
		raw_html += '</tr>'

		raw_html += '<tr class="row-info">'							#Empieza una row de la tabla
		tableElements = [reporte["fechaNacimiento"], str(reporte["edad"]), reporte["lateralidad"], reporte["carrera"], str(reporte["semestre"])]
		raw_html += self.createTableElements(tableElements)
		raw_html += '</tr>'
		raw_html += '</table>'


		"""
		ESTA ES UNA ROW DE LA TABLA DE INFO GENERAL
		"""
		raw_html += '<table style="width:100%">' 	#Empieza una tabla

		raw_html += '<tr class="row-info">'							#Empieza una row de la tabla
		headerElements = ['Educación', 'Equipo', 'Examinador']
		raw_html += self.createTableHeaders(headerElements)
		raw_html += '</tr>'

		raw_html += '<tr class="row-info">'							#Empieza una row de la tabla
		tableElements = [str(reporte["educacion"]), reporte["equipo"], reporte["nombreExaminador"]]
		raw_html += self.createTableElements(tableElements)
		raw_html += '</tr>'
		raw_html += '</table>'
		raw_html += '</div>'

		################################################ AQUI ACABA LO DE LA INFO GENERAL ################################################


		"""
		Empieza lo de las pruebas, sus nombres y valores
		"""
		raw_html += '<div class="new-table">'

		# Aquí van los nombres de las pruebas y las variables que se ingresaron
		raw_html += '<table class="table-pruebas">' 	#Empieza una tabla
		raw_html += '<tr class="top-row">'							#Empieza una row de la tabla
		headerElements = ['Prueba', 'Campo', 'PD', 'Pe']
		raw_html += self.createTableHeaders(headerElements)
		raw_html += '</tr>'

		iCantidadPruebas = -1


		pruebasRegistradas = reporte["resultados"]
		pe = [] #lista vacia de puntuaciones escalares
		peLabel = [] # lista vacia para yLabel en imagen
		for pruebaName in pruebasRegistradas.keys():
			iCantidadPruebas += 1
			
			if pruebaName != 'BSI-18' and pruebaName != 'BussYPerry' and pruebaName != 'SCL-90' and pruebaName != 'Motivos Deportivos de Butt' and pruebaName != 'PSQI':
				#print(pruebaName)
				infoPrueba = pruebasRegistradas[pruebaName]
				bFaltaActualizarPrueba = False

				cantCampos = 0

				if isinstance(infoPrueba.campos, str):
					#print("ip-campos no es str")
					infoPrueba.campos = tuple([infoPrueba.campos])

				if not isinstance(infoPrueba.valores, tuple):
					if not isinstance(infoPrueba.valores, list):
						#print("ip.valores no es tuple ni list")
						infoPrueba.valores = list([infoPrueba.valores])
				
				if isinstance(infoPrueba.campos, tuple):
					cantCampos = len(infoPrueba.campos)

				if cantCampos == 0:
					bFaltaActualizarPrueba = True
					cantCampos = len(infoPrueba.valores)

				#print("cantCampos: " + str(cantCampos))
				# print(pruebaName)
				sublista = list([infoPrueba.puntuacionEscalar])
				pe.append(sublista)
				peLabel.append(self.pruebayLabels[pruebaName])

				raw_html += '<tr>'
				raw_html += '<th class="colored-background" rowspan="' + str(cantCampos) + '">'	
				raw_html += pruebaName
				raw_html += '</th>'

				raw_html += '<td>'
				# Si aún no actualizaban los campos...
				if bFaltaActualizarPrueba:
					raw_html += 'TEMP'
				else:
					raw_html += infoPrueba.campos[0]
				raw_html += '</td>'
				raw_html += '<td>'
				raw_html += str(infoPrueba.valores[0])
				raw_html += '</td>'
				raw_html += '<td>'
				try:
					raw_html += str(infoPrueba.puntuacionEscalar[0])
				except:
					raw_html += str(infoPrueba.puntuacionEscalar)
				raw_html += '</td>'

				if cantCampos > 1:
					for idx in range(1, cantCampos):
						raw_html += '<tr>'
						raw_html += '<td>'
						if bFaltaActualizarPrueba:
							raw_html += 'TEMP'
						else:
							raw_html += infoPrueba.campos[idx]
						raw_html += '</td>'
						print(idx, infoPrueba.valores, infoPrueba.puntuacionEscalar)
						tableElements = [str(infoPrueba.valores[idx]), str(infoPrueba.puntuacionEscalar[idx])]
						raw_html += self.createTableElements(tableElements)
						raw_html += '</tr>'
					raw_html += '</tr>'	
		raw_html += '</table>'

		#aplanar lista de listas
		# print(pruebasRegistradas.keys())
		# print(peLabel)
		# print(pe)
		# print(['RV', 'TV', 'TT', 'ET', 'IT', 'M', 'C', 'I', 'C', 'P', 'M.D.', 'M.I.', 'VAR', 'CON', 'TOT', 'C', 'O',
		# 	'TA', 'TR', 'T', 'I', 'C', 'DI', 'DD', 'ABS', 'B', 'A', 'Dif', 'T', 'MVCt', 'MVC', 'DVt', 'DV', 'A', 'P'])
		flattened = [item for sublist in pe for item in sublist]
		#aplanar lista de tuplas
		def reemovNestings(l, arr): 
			for i in l: 
				if type(i) ==  tuple: 
					reemovNestings(i, arr) 
				else: 
					arr.append(i) 
			return arr
		
		escalares = reemovNestings(flattened, [])
		flattened = [item for sublist in peLabel for item in sublist]
		escalaresLabel = reemovNestings(flattened, [])
		self.escalares = escalares
		self.escalaresLabel = escalaresLabel
		'''
		ESCALARES es la lista de todas las puntuaciones escalares de todas las pruebas
		'''

		### uncomment for image
		escalares = [int(x) for x in escalares]
		print(escalaresLabel, escalares)
		#Se crean las imagenes a mostrar
		self.createTableImg(escalares, escalaresLabel)
		
		raw_html += '<div class="fill">'
		raw_html += '<img src="reporte.png" class="grafica">'
		raw_html += '</div>'
		raw_html += '</div>'

		raw_html += '<div class="pagebreak"></div>'

		#################################### AQUÍ ACABA LO DEL NOMBRE DE LAS PRUEBAS Y LA GRÁFICA ####################################

		if "BussYPerry" in pruebasRegistradas:
			raw_html += '<div class="new-table">'
			raw_html += '<table style="width:100%">' 	#Empieza una tabla
			raw_html += '<tr class="top-row">'							#Empieza una row de la tabla

			### Headers de la tabla
			raw_html += '<th>'
			raw_html += '</th>'
			raw_html += '<th>'
			raw_html += '</th>'

			headerElements = ['AgFis','AgVer','Ira','Hos']
			
			raw_html += self.createTableHeaders(headerElements)
			raw_html += '</tr>'							#Cierra una row de la tabla

			raw_html += '<tr>'							#Empieza una row de la tabla
			tableElements = ['Buss y Perry', 'PD']
			

			pruebaBP = pruebasRegistradas['BussYPerry']

			self.escalaresLabel = reemovNestings(headerElements, escalaresLabel)			
			self.escalares = reemovNestings(pruebaBP.puntuacionEscalar, escalares)
    
			for puntuacionDir in self.escalares:
				tableElements.append(str(puntuacionDir))
			raw_html += self.createTableElements(tableElements)
			raw_html += '</tr>'							#Cierra una row de la tabla					#Cierra una row de la tabla


			raw_html += '<tr>'							#Empieza una row de la tabla
			tableElements = ['DTM', 'Pc']

		if "SCL-90" in pruebasRegistradas:
			raw_html += '<div class="new-table">'
			raw_html += '<table style="width:100%">' 	#Empieza una tabla
			raw_html += '<tr class="top-row">'							#Empieza una row de la tabla

			### Headers de la tabla
			raw_html += '<th>'
			raw_html += '</th>'
			raw_html += '<th>'
			raw_html += '</th>'

			headerElements = ['SO','OB', 'IN', 'DE', 'AN', 'HO', 'FO', 'PA', 'PSI', 'GSI', 'PST', 'PSDI']
			raw_html += self.createTableHeaders(headerElements)
			raw_html += '</tr>'							#Cierra una row de la tabla



			raw_html += '<tr>'							#Empieza una row de la tabla
			tableElements = ['SCL-90', 'PD']
			

			pruebaSCL90 = pruebasRegistradas['SCL-90']
			for puntuacionDir in pruebaSCL90.valores:
				tableElements.append(str(puntuacionDir))
			raw_html += self.createTableElements(tableElements)
			raw_html += '</tr>'							#Cierra una row de la tabla


			raw_html += '<tr>'							#Empieza una row de la tabla
			tableElements = ['P. Gral.', 'Pc']
			# Se añaden cada uno de los valores percentiles obtenidos
			for puntuacionPerc in pruebaSCL90.rangoPercentil[0]:
				tableElements.append(str(puntuacionPerc))
			raw_html += self.createTableElements(tableElements)
			raw_html += '</tr>'							#Cierra una row de la tabla


			raw_html += '<tr>'							#Empieza una row de la tabla
			tableElements = ['DTM', 'Pc']

			#En caso de ameritarlo, se añaden los valores correspondientes a la segunda row
			if len(pruebaSCL90.rangoPercentil[1]) > 0:
				for puntuacionPerc in pruebaSCL90.rangoPercentil[1]:
					tableElements.append(str(puntuacionPerc))
			else:
				for puntuacionPerc in range(len(pruebaSCL90.rangoPercentil[0])):
					tableElements.append('')
			raw_html += self.createTableElements(tableElements)
			raw_html += '</tr>'							#Cierra una row de la tabla

			
			raw_html += '<tr>'							#Empieza una row de la tabla
			tableElements = ['M. Psiq.', 'Pc']
			
			#En caso de que haya pasado a la tercera row
			if len(pruebaSCL90.rangoPercentil[2]) > 0:
				for puntuacionPerc in pruebaSCL90.rangoPercentil[2]:
					tableElements.append(str(puntuacionPerc))
			else:
				for puntuacionPerc in range(len(pruebaSCL90.rangoPercentil[0])):
					tableElements.append('')

			raw_html += self.createTableElements(tableElements)
			raw_html += '</tr>'							#Cierra una row de la tabla
			
			raw_html += '</table>' 						#Cierra la tabla
			raw_html += '</div>'
		
		if "BSI-18" in pruebasRegistradas:
			raw_html += '<div class="new-table">'
			raw_html += '<table style="width:100%">' 	#Empieza una tabla
			raw_html += '<tr class="top-row">'							#Empieza una row de la tabla

			### Headers de la tabla
			raw_html += '<th>'
			raw_html += '</th>'
			raw_html += '<th>'
			raw_html += '</th>'

			headerElements = ["SOM", "DEP", "ANS", "IGS"]
			raw_html += self.createTableHeaders(headerElements)
			raw_html += '</tr>'							#Cierra una row de la tabla



			raw_html += '<tr>'							#Empieza una row de la tabla
			tableElements = ['BSI-18', 'PD']
			

			pruebaBSI18 = pruebasRegistradas['BSI-18']
			for puntuacionDir in pruebaBSI18.valores:
				tableElements.append(str(puntuacionDir))
			raw_html += self.createTableElements(tableElements)
			raw_html += '</tr>'							#Cierra una row de la tabla


			raw_html += '<tr>'							#Empieza una row de la tabla
			tableElements = ['P. Gral.', 'Pc']
			# Se añaden cada uno de los valores percentiles obtenidos
			for puntuacionPerc in pruebaBSI18.rangoPercentil:
				tableElements.append(str(puntuacionPerc))
			raw_html += self.createTableElements(tableElements)
			raw_html += '</tr>'							#Cierra una row de la tabla


			raw_html += '<tr>'							#Empieza una row de la tabla
			tableElements = ['DTM', 'Pc']
		

		########################## AQUÍ EMPIEZA LAS OTRAS TRES PRUEBAS DE PSQI Y MOTIVOS BUTT ##########################

		if "Motivos Deportivos de Butt" in pruebasRegistradas:
			raw_html += '<div class="new-table">'
			
			raw_html += '<table class = "table-BUTT">' 	#Empieza una tabla
			raw_html += '<tr class="top-row">'
			
			raw_html += '<th>'
			raw_html += '</th>'
			
			headerElements = ['Motivos', 'PD', 'V']
			raw_html += self.createTableHeaders(headerElements)
			raw_html += self.createTableHeaders(headerElements)
			raw_html += '</tr>'

			raw_html += '<tr>'
			raw_html += '<td rowspan="3">'
			raw_html += 'Motivos BUTT'
			raw_html += '</td>'

			pruebaButt = pruebasRegistradas['Motivos Deportivos de Butt']
			dirC = pruebaButt.valores[0]
			dirR = pruebaButt.valores[1]
			dirS = pruebaButt.valores[2]
			dirCo = pruebaButt.valores[3]
			dirA = pruebaButt.valores[4]
			dirT = pruebaButt.valores[5]

			intC = pruebaButt.rangoPercentil[0]
			intR = pruebaButt.rangoPercentil[1]
			intS = pruebaButt.rangoPercentil[2]
			intCo = pruebaButt.rangoPercentil[3]
			intA = pruebaButt.rangoPercentil[4]
			intT = pruebaButt.rangoPercentil[5]

			tableElements = ['C', str(dirC), str(intC)]
			raw_html += self.createTableElements(tableElements)

			tableElements = ['Co', str(dirCo), str(intCo)]
			raw_html += self.createTableElements(tableElements)
			
			raw_html += '<tr>'
			tableElements = ['R', str(dirR), str(intR)]
			raw_html += self.createTableElements(tableElements)

			tableElements = ['A', str(dirA), str(intA)]
			raw_html += self.createTableElements(tableElements)
			raw_html += '</tr>'
			


			raw_html += '<tr>'
			tableElements = ['S', str(dirS), str(intS)]
			raw_html += self.createTableElements(tableElements)
			
			tableElements = ['T', str(dirT), str(intT)]
			raw_html += self.createTableElements(tableElements)
			raw_html += '</tr>'
			


			raw_html += '</tr>' #Se cierra la row de Butt
			raw_html += '</table>' 						#Cierra la tabla
		
		##### start PSQI table
		if "PSQI" in pruebasRegistradas:
			raw_html += '<table class="table-PSQI">' 	#Empieza una tabla
			
			raw_html += '<tr class="top-row">'

			headerElements = ['PSQI', 'P']
			raw_html += self.createTableHeaders(headerElements)
			raw_html += self.createTableHeaders(headerElements)
			raw_html += '</tr>'

			raw_html += '<tr>'
			
			
			pruebaPittsburgh = pruebasRegistradas['PSQI']
			cal = pruebaPittsburgh.valores[0]
			lat = pruebaPittsburgh.valores[1]
			dur = pruebaPittsburgh.valores[2]
			efic = pruebaPittsburgh.valores[3]
			pert = pruebaPittsburgh.valores[4]
			med = pruebaPittsburgh.valores[5]
			disf = pruebaPittsburgh.valores[6]
			total = pruebaPittsburgh.puntuacionEscalar[7]
			inter = pruebaPittsburgh.rangoPercentil
			

			tableElements = ['Cal.', str(cal), 'Pert.', str(pert)]
			raw_html += self.createTableElements(tableElements)
			raw_html += '</tr>'
			

			raw_html += '<tr>'
			tableElements = ['Lat.', str(lat), 'Med.', str(med)]
			raw_html += self.createTableElements(tableElements)
			raw_html += '</tr>'
			

			raw_html += '<tr>'
			tableElements = ['Dur.', str(dur), 'Disf.', str(disf)]
			raw_html += self.createTableElements(tableElements)
			raw_html += '</tr>'
			
			
			raw_html += '<tr>'
			tableElements = ['Efic.', str(efic), 'Total', str(total)]
			raw_html += self.createTableElements(tableElements)
			raw_html += '</tr>'


			############### Renglón creado para la interpretación #############
			raw_html += '<tr>'
			
			raw_html += '<td>'
			raw_html += ''
			raw_html += '</td>'
			
			raw_html += '<td>'
			raw_html += ''
			raw_html += '</td>'
			
			tableElements = ['Interpretación', inter]
			raw_html += self.createTableElements(tableElements)
			raw_html += '</tr>'
			
			raw_html += '</table>' 						#Cierra la tabla

		raw_html += '</div>'
		raw_html += '</div>'
		raw_html += '</div>'
		raw_html += '</body></html>'


		with open(self.url,'w') as file:
			file.write(raw_html)

		
	def changeView(self):
		"""
		 Método encargado de notificar los elementos que serán pasados como parámetros a la siguiente vista
		"""
		self.switch_window.emit()

	def exportCsvClick(self):
		options = QtWidgets.QFileDialog.Options()
		options |= QtWidgets.QFileDialog.DontUseNativeDialog
		options |= QtWidgets.QFileDialog.DontConfirmOverwrite
		fileName, _ = QtWidgets.QFileDialog.getSaveFileName(self,"QFileDialog.getSaveFileName()","","CSV (*.csv)", options=options)
		if not fileName:
			return

		if not self.hasSaveCSV:
			self.saveToCsv(fileName)
			self.hasSaveCSV = True


	def saveToCsv(self, fileName):
		reporte = self.reporteModel.reporte
		fileName = fileName + '.csv'
		append_write = ""
		if os.path.exists(fileName):
			append_write = 'a' # append if already exists
		else:
			append_write = 'w' # make a new file if not

		data = self.getRowData()
		with open(fileName,append_write, newline='', encoding='utf-8') as f:
			w = csv.DictWriter(f, self.csvHeaders)
			if append_write == 'w':
				w.writeheader()
			
			w.writerow(data)

	def getRowData(self):
		dicInfo = {}
		
		for key, value in zip(self.escalaresLabel, self.escalares):
			dicInfo[key] = value
		for key in self.csvHeaders:
			if key not in dicInfo:
				dicInfo[key] = "nan"
		
		# append user info
		tmp = dict(self.reporteModel.reporte)
		del tmp["resultados"]
		dicInfo.update(tmp)

		return dicInfo

	def getDatos(self):
		pass

	def emptyInvalidArgs(self):
		pass

	def addInvalidArg(self, arg):
		pass

	def getListMenu(self):
		"""
		 Método que se regresa el id del menu en la vista de TMT
		"""
		return self.reporteView.lWVistas

	def getProgressBar(self):
		"""
		 Método que se encarga de regresar el valor de la barra de progreso
		"""
		return self.reporteView.progressBar


# Pruebas unitarias
#if __name__ == "__main__":
#    import sys
#    app = QtWidgets.QApplication(sys.argv)
#    fluidezWindow = QtWidgets.QWidget()
#    fluidezVerbalController = TMTController(fluidezWindow)
#    fluidezWindow.show()
#    sys.exit(app.exec_())