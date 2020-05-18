#Controlador de la vista de ReporteWindow
from PyQt5 import QtWidgets, QtCore, Qt
from vistas.ReporteWindowWidget import *
from ReporteModel import *
from PruebaModel import *
from ControllerModel import *


class ReporteController(QtWidgets.QWidget, ControllerModel):
	#Atributo empleado para realizar el cambio de vista
	switch_window = QtCore.pyqtSignal()

	def __init__(self, mainWindow, url, reporteModel=None):
		QtWidgets.QWidget.__init__(self)
		self.reporteModel = reporteModel
		self.url = url
		self.mainWindow = mainWindow
		self.url = url

	def loadReporte(self):
		self.createReporte()
		self.reporteView = ReporteWindowWidget(self.mainWindow, self.url)
		self.reporteView.pbStart.clicked.connect(self.launchBrowser)
		self.reporteView.pbRestart.clicked.connect(self.changeView)

	def launchBrowser(self):
		Qt.QDesktopServices.openUrl(Qt.QUrl(self.url))

	def createReporte(self):
		reporte = self.reporteModel.reporte
		raw_html = '<!DOCTYPE html><html><head></head>'
		raw_html += '<link rel="stylesheet" href="w3-layout.css">'
		raw_html += '<link rel="stylesheet" href="reporte.css">'
		raw_html += '<link rel="stylesheet" media="print" href="reporte.css" />'
		raw_html += '<body>'
		raw_html += '<div class="w3-container">'
		raw_html += '<div class="w3-row">'
		raw_html += '<div class="w3-col">'
		raw_html += '<h1 class = "center-text">Evaluación Neurocognitiva del Deporte</h1>'
		raw_html += '<div class="new-table">'

		"""
		ESTA ES UNA ROW DE LA TABLA DE INFO GENERAL
		"""
		raw_html += '<table style="width:100%">' 	#Empieza una tabla

		raw_html += '<tr class="row-info top-row">'							#Empieza una row de la tabla
		raw_html += '<th>'
		raw_html += 'Nombre'
		raw_html += '</th>'
		raw_html += '<th>'
		raw_html += 'ID'
		raw_html += '</th>'
		raw_html += '<th>'
		raw_html += 'Fecha'
		raw_html += '</th>'
		raw_html += '<th>'
		raw_html += 'Género'
		raw_html += '</th>'
		raw_html += '</tr>'

		raw_html += '<tr class="row-info">'							#Empieza una row de la tabla 
		raw_html += '<td>'
		raw_html += reporte["nombreExaminado"]
		raw_html += '</td>'
		raw_html += '<td>'
		raw_html += reporte["id"]
		raw_html += '</td>'
		raw_html += '<td>'
		raw_html += reporte["fecha"]
		raw_html += '</td>'
		raw_html += '<td>'
		raw_html += reporte["genero"]
		raw_html += '</td>'
		raw_html += '</tr>'
		raw_html += '</table>'


		"""
		ESTA ES UNA ROW DE LA TABLA DE INFO GENERAL
		"""
		raw_html += '<table style="width:100%">' 	#Empieza una tabla
		raw_html += '<tr class="row-info">'							#Empieza una row de la tabla
		raw_html += '<th>'
		raw_html += 'Fecha de Nacimiento'
		raw_html += '</th>'
		raw_html += '<th>'
		raw_html += 'Edad'
		raw_html += '</th>'
		raw_html += '<th>'
		raw_html += 'Lateralidad'
		raw_html += '</th>'
		raw_html += '<th>'
		raw_html += 'Carrera'
		raw_html += '</th>'
		raw_html += '<th>'
		raw_html += 'Semestre'
		raw_html += '</th>'
		raw_html += '</tr>'

		raw_html += '<tr class="row-info">'							#Empieza una row de la tabla
		raw_html += '<td>'
		raw_html += reporte["fechaNacimiento"]
		raw_html += '</td>'
		raw_html += '<td>'
		raw_html += str(reporte["edad"])
		raw_html += '</td>'
		raw_html += '<td>'
		raw_html += reporte["lateralidad"]
		raw_html += '</td>'
		raw_html += '<td>'
		raw_html += reporte["carrera"]
		raw_html += '</td>'
		raw_html += '<td>'
		raw_html += str(reporte["semestre"])
		raw_html += '</td>'
		raw_html += '</tr>'
		raw_html += '</table>'


		"""
		ESTA ES UNA ROW DE LA TABLA DE INFO GENERAL
		"""
		raw_html += '<table style="width:100%">' 	#Empieza una tabla

		raw_html += '<tr class="row-info">'							#Empieza una row de la tabla
		raw_html += '<th>'
		raw_html += 'Educación'
		raw_html += '</th>'
		raw_html += '<th>'
		raw_html += 'Equipo'
		raw_html += '</th>'
		raw_html += '<th>'
		raw_html += 'Examinador'
		raw_html += '</th>'

		raw_html += '</tr>'

		raw_html += '<tr class="row-info">'							#Empieza una row de la tabla
		raw_html += '<td>'
		raw_html += str(reporte["educacion"])
		raw_html += '</td>'
		raw_html += '<td>'
		raw_html += reporte["equipo"]
		raw_html += '</td>'
		raw_html += '<td>'
		raw_html += reporte["nombreExaminador"]
		raw_html += '</td>'
		raw_html += '</tr>'
		raw_html += '</table>'
		raw_html += '</div>'

		################################################ AQUI ACABA LO DE LA INFO GENERAL ################################################


		"""
		Empieza lo de las pruebas, sus nombres y valores
		"""
		raw_html += '<div class="new-table">'

		# Aquí van los nombres de las pruebas y las variables que se ingresaron
		raw_html += '<table style="width:30%">' 	#Empieza una tabla
		raw_html += '<tr class="top-row">'							#Empieza una row de la tabla
		raw_html += '<th>'
		raw_html += 'Prueba'
		raw_html += '</th>'
		raw_html += '<th>'
		raw_html += 'Campo'
		raw_html += '</th>'
		raw_html += '<th>'
		raw_html += 'PD'
		raw_html += '</th>'
		raw_html += '<th>'
		raw_html += 'Pe'
		raw_html += '</th>'
		raw_html += '</tr>'

		iCantidadPruebas = -1

		pruebasRegistradas = reporte["resultados"]
		for pruebaName in pruebasRegistradas.keys():
			iCantidadPruebas += 1
			
			if pruebaName != 'SCL-90':
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
				print(pruebaName)

				raw_html += '<tr>'
				raw_html += '<th class="colored-background" rowspan="' + str(cantCampos) + '">'	
				raw_html += pruebaName
				raw_html += '</th>'

				raw_html += '<td>'
				if bFaltaActualizarPrueba:
					raw_html += 'TEMP'
				else:
					raw_html += infoPrueba.campos[0]
				raw_html += '</td>'
				raw_html += '<td>'
				#print(infoPrueba.valores)
				raw_html += str(infoPrueba.valores[0])
				raw_html += '</td>'
				raw_html += '<td>'
				try:
					raw_html += str(infoPrueba.puntuacionEscalar[0])
				except:
					raw_html += str(infoPrueba.puntuacionEscalar)
				raw_html += '</td>'

				#print("infoPrueba.puntuacionEscalar: ")
				#print(infoPrueba.puntuacionEscalar)

				if cantCampos > 1:
					for idx in range(1, cantCampos):
						raw_html += '<tr>'
						raw_html += '<td>'
						if bFaltaActualizarPrueba:
							raw_html += 'TEMP'
						else:
							raw_html += infoPrueba.campos[idx]
						raw_html += '</td>'
						raw_html += '<td>'
						raw_html += str(infoPrueba.valores[idx])
						raw_html += '</td>'
						raw_html += '<td>'
						raw_html += str(infoPrueba.puntuacionEscalar[idx])
						raw_html += '</td>'
						raw_html += '</tr>'
					raw_html += '</tr>'				
		raw_html += '</table>'


		raw_html += '<table style="width:70"%>'
		#Aquí va la gráfica
		raw_html += '</table>'
		raw_html += '</div>'

		#################################### AQUÍ ACABA LO DEL NOMBRE DE LAS PRUEBAS Y LA GRÁFICA ####################################

		raw_html += '<div class="new-table">'
		raw_html += '<table style="width:100%">' 	#Empieza una tabla
		raw_html += '<tr class="top-row">'							#Empieza una row de la tabla

		### Headers de la tabla
		raw_html += '<th>'
		raw_html += '</th>'
		raw_html += '<th>'
		raw_html += '</th>'


		raw_html += '<th>'
		raw_html += 'SO'
		raw_html += '</th>'

		raw_html += '<th>'
		raw_html += 'OB'
		raw_html += '</th>'

		raw_html += '<th>'
		raw_html += 'IN'
		raw_html += '</th>'

		raw_html += '<th>'
		raw_html += 'DE'
		raw_html += '</th>'

		raw_html += '<th>'
		raw_html += 'AN'
		raw_html += '</th>'

		raw_html += '<th>'
		raw_html += 'HO'
		raw_html += '</th>'

		raw_html += '<th>'
		raw_html += 'FO'
		raw_html += '</th>'

		raw_html += '<th>'
		raw_html += 'PA'
		raw_html += '</th>'

		raw_html += '<th>'
		raw_html += 'PSI'
		raw_html += '</th>'

		raw_html += '<th>'
		raw_html += 'GSI'
		raw_html += '</th>'

		raw_html += '<th>'
		raw_html += 'PST'
		raw_html += '</th>'

		raw_html += '<th>'
		raw_html += 'PSDI'
		raw_html += '</th>'

		raw_html += '</tr>'							#Cierra una row de la tabla



		raw_html += '<tr>'							#Empieza una row de la tabla
		raw_html += '<td>'
		raw_html += 'SCL-90'
		raw_html += '</td>'

		raw_html += '<td>'
		raw_html += 'PD'
		raw_html += '</td>'

		pruebaSCL90 = pruebasRegistradas['SCL-90']
		for puntuacionDir in pruebaSCL90.valores:
			raw_html += '<td>'
			raw_html += str(puntuacionDir)
			raw_html += '</td>'
		raw_html += '</tr>'							#Cierra una row de la tabla

		raw_html += '<tr>'							#Empieza una row de la tabla
		raw_html += '<td>'
		raw_html += 'P. Gral.'
		raw_html += '</td>'

		raw_html += '<td>'
		raw_html += 'Pc'
		raw_html += '</td>'

		for puntuacionPerc in pruebaSCL90.rangoPercentil[0]:
			raw_html += '<td>'
			raw_html += str(puntuacionPerc)
			raw_html += '</td>'
		raw_html += '</tr>'							#Cierra una row de la tabla

		raw_html += '<tr>'							#Empieza una row de la tabla
		raw_html += '<td>'
		raw_html += 'DTM'
		raw_html += '</td>'

		raw_html += '<td>'
		raw_html += 'Pc'
		raw_html += '</td>'

		if len(pruebaSCL90.rangoPercentil[1]) > 0:
			for puntuacionPerc in pruebaSCL90.rangoPercentil[1]:
				raw_html += '<td>'
				raw_html += str(puntuacionPerc)
				raw_html += '</td>'
		else:
			for puntuacionPerc in range(len(pruebaSCL90.rangoPercentil[0])):
				raw_html += '<td>'
				raw_html += '</td>'
		raw_html += '</tr>'							#Cierra una row de la tabla

		raw_html += '<tr>'							#Empieza una row de la tabla
		raw_html += '<td>'
		raw_html += 'M. Psiq.'
		raw_html += '</td>'

		raw_html += '<td>'
		raw_html += 'Pc'
		raw_html += '</td>'

		if len(pruebaSCL90.rangoPercentil[2]) > 0:
			for puntuacionPerc in pruebaSCL90.rangoPercentil[2]:
				raw_html += '<td>'
				raw_html += str(puntuacionPerc)
				raw_html += '</td>'
		else:
			for puntuacionPerc in range(len(pruebaSCL90.rangoPercentil[0])):
				raw_html += '<td>'
				raw_html += '</td>'
		raw_html += '</tr>'							#Cierra una row de la tabla
		raw_html += '</table>' 						#Cierra la tabla
		raw_html += '</div>'
		

		########################## AQUÍ EMPIEZA LAS OTRAS TRES PRUEBAS DE PSQI Y MOTIVOS BUTT ##########################

		raw_html += '<div class="new-table">'
		
		raw_html += '<table class = "table-BUTT">' 	#Empieza una tabla
		raw_html += '<tr class="top-row">'
		
		raw_html += '<th>'
		raw_html += '</th>'
		
		raw_html += '<th>'
		raw_html += '</th>'
		
		raw_html += '<th>'
		raw_html += 'PD'
		raw_html += '</th>'
		
		raw_html += '<th>'
		raw_html += 'V'
		raw_html += '</th>'
		
		raw_html += '<th>'
		raw_html += '</th>'
		
		raw_html += '<th>'
		raw_html += 'PD'
		raw_html += '</th>'
		
		raw_html += '<th>'
		raw_html += 'V'
		raw_html += '</th>'
		
		raw_html += '</tr>'

		raw_html += '<tr>'
		raw_html += '<td rowspan="3">'
		raw_html += 'Motivos BUTT'
		raw_html += '</td>'

		raw_html += '<td>'
		raw_html += 'C'
		raw_html += '</td>'

		########## AQUÍ VA EL PD DE C ##########
		raw_html += '<td>'
		raw_html += ''
		raw_html += '</td>'

		########## AQUÍ VA EL V DE C ##########
		raw_html += '<td>'
		raw_html += ''
		raw_html += '</td>'

		raw_html += '<td>'
		raw_html += 'Co'
		raw_html += '</td>'

		########## AQUÍ VA EL PD DE Co ##########
		raw_html += '<td>'
		raw_html += ''
		raw_html += '</td>'

		########## AQUÍ VA EL V DE Co ##########
		raw_html += '<td>'
		raw_html += ''
		raw_html += '</td>'

		raw_html += '<tr>'
		raw_html += '<td>'
		raw_html += 'R'
		raw_html += '</td>'

		########## AQUÍ VA EL PD DE R ##########
		raw_html += '<td>'
		raw_html += ''
		raw_html += '</td>'

		########## AQUÍ VA EL V DE R ##########
		raw_html += '<td>'
		raw_html += ''
		raw_html += '</td>'

		raw_html += '<td>'
		raw_html += 'A'
		raw_html += '</td>'

		########## AQUÍ VA EL PD DE A ##########
		raw_html += '<td>'
		raw_html += ''
		raw_html += '</td>'

		########## AQUÍ VA EL V DE A ##########
		raw_html += '<td>'
		raw_html += ''
		raw_html += '</td>'

		raw_html += '</tr>'
		
		raw_html += '<tr>'
		
		raw_html += '<td>'
		raw_html += 'S'
		raw_html += '</td>'

		########## AQUÍ VA EL PD DE S ##########
		raw_html += '<td>'
		raw_html += ''
		raw_html += '</td>'

		########## AQUÍ VA EL V DE S ##########
		raw_html += '<td>'
		raw_html += ''
		raw_html += '</td>'
		

		raw_html += '<td>'
		raw_html += 'T'
		raw_html += '</td>'

		########## AQUÍ VA EL PD DE T ##########
		raw_html += '<td>'
		raw_html += ''
		raw_html += '</td>'

		########## AQUÍ VA EL V DE T ##########
		raw_html += '<td>'
		raw_html += ''
		raw_html += '</td>'
		
		raw_html += '</tr>'
		
		
		raw_html += '</tr>'

		raw_html += '</table>' 						#Cierra la tabla
		
		raw_html += '<table class="table-PSQI">' 	#Empieza una tabla
		raw_html += '<tr class="top-row">'
		raw_html += '<th>'
		raw_html += 'PSQI'
		raw_html += '</th>'
		
		raw_html += '<th>'
		raw_html += 'P'
		raw_html += '</th>'
		
		raw_html += '<th>'
		raw_html += ''
		raw_html += '</th>'
		
		raw_html += '<th>'
		raw_html += 'P'
		raw_html += '</th>'
		raw_html += '</tr>'

		raw_html += '<tr>'
		
		raw_html += '<td>'
		raw_html += 'Cal.'
		raw_html += '</td>'
		
		################# Aquí va la P de Cal de PSQI #################
		raw_html += '<td>'
		raw_html += ''
		raw_html += '</td>'
		
		raw_html += '<td>'
		raw_html += 'Pert.'
		raw_html += '</td>'
		
		################# Aquí va la P de Pert de PSQI #################
		raw_html += '<td>'
		raw_html += ''
		raw_html += '</td>'
		
		raw_html += '</tr>'
		

		raw_html += '<tr>'
		
		raw_html += '<td>'
		raw_html += 'Lat.'
		raw_html += '</td>'
		
		################# Aquí va la P de Lat de PSQI #################
		raw_html += '<td>'
		raw_html += ''
		raw_html += '</td>'
		
		raw_html += '<td>'
		raw_html += 'Med.'
		raw_html += '</td>'
		
		################# Aquí va la P de Med de PSQI #################
		raw_html += '<td>'
		raw_html += ''
		raw_html += '</td>'
		
		raw_html += '</tr>'
		

		raw_html += '<tr>'
		
		raw_html += '<td>'
		raw_html += 'Dur.'
		raw_html += '</td>'
		
		################# Aquí va la P de Dar de PSQI #################
		raw_html += '<td>'
		raw_html += ''
		raw_html += '</td>'
		
		raw_html += '<td>'
		raw_html += 'Disf.'
		raw_html += '</td>'
		
		################# Aquí va la P de Disf de PSQI #################
		raw_html += '<td>'
		raw_html += ''
		raw_html += '</td>'
		
		raw_html += '</tr>'
		
		raw_html += '<tr>'
		
		raw_html += '<td>'
		raw_html += 'Efic.'
		raw_html += '</td>'
		
		################# Aquí va la P de Efic de PSQI #################
		raw_html += '<td>'
		raw_html += ''
		raw_html += '</td>'
		
		raw_html += '<td>'
		raw_html += 'Total'
		raw_html += '</td>'
		
		################# Aquí va la P de Total de PSQI #################
		raw_html += '<td>'
		raw_html += ''
		raw_html += '</td>'
		
		raw_html += '</tr>'
		
		raw_html += '</table>' 						#Cierra la tabla

		raw_html += '</div>'

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