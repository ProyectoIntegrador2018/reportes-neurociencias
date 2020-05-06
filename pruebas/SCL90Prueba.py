#Prueba de SCL90
import pandas as pd
import PruebaModel

class SCL90Prueba(PruebaModel.PruebaModel):	
	def __init__(self, valores):
		nombre = "SCL-90"
		baremos = (pd.read_csv('./Baremos/SCL90R_MUJERES_NC_TABLA.csv'), pd.read_csv('./Baremos/SCL90R_VARONES_NC_TABLA.csv'), 
			pd.read_csv('./Baremos/SCL90R_MUJERES_PSIQUIATRICA_TABLA.csv'), pd.read_csv('./Baremos/SCL90R_VARONES_PSIQUIATRICA_TABLA.csv'),
			pd.read_csv('./Baremos/SCL90R_PSICOSOMATICA_TABLA.csv'))
		campos = ("SO", "OB", "IN", "DE", "AN", "HO", "FO", "PA", "PSI", "GSI", "PST", "PSDI")

		super(SCL90Prueba,self).__init__(nombre, valores, baremos, campos)

	def getPuntuacionPercentil(self, tablaPrincipal, columnName, inputVal):
		"""
		 Método que es empleado para obtener la puntuación percentil de la tablaPrincipal especificada
		 Args:
		  tablaPrincipal: dataframe donde se buscará el rango percentil adecuado
		  columnName: string con el que se buscará realizar el filtro
		  inputVal: float que se usa para saber cuál será el valor a comparar para obtener el valor percentil de interés

		"""
		tablaPrincipal = tablaPrincipal.replace({'---': None})
		tempTabla = tablaPrincipal[['RangoPercentil', columnName]].dropna()
		tempTabla[columnName] = tempTabla[columnName].astype(float)
		puntPercentil = tempTabla[tempTabla[columnName] <= inputVal]
		#print(puntPercentil.head())
		if puntPercentil.empty:
			puntPercentil = tempTabla.tail(1).iloc[0]
		else:
			puntPercentil = puntPercentil.iloc[0]
		return puntPercentil['RangoPercentil']

	def calcularPERP(self, datos):
		"""
	 	 Método que es empleado para calcular la Puntuación Escalar(PE), como la Percentil(RP)
	 	 Args:
	 	  datos: Lista de información relevante del reporte para calcular los valores de PE y RP (escolaridad, género, etc.)
		"""
		tablaNoClinicaMujeres = self.baremos[0]
		tablaNoClinicaVarones =  self.baremos[1]
		tablaPsiquiatricaMujeres = self.baremos[2]
		tablaPsiquiatricaVarones = self.baremos[3]
		tablaPsico = self.baremos[4]
		valoresList = self.valores
		sexo = datos

		colNames = ['SOM','OBS','INT','DEP','ANS','HOS','FOB','PAR','PSI','GSI','PST','PSDI']
		bDTM = False
		bMPsiq = False
		puntuacionPercentilGeneral = []
		puntuacionPercentilDTM = []
		puntuacionPercentilMPsiq = []
		
		# Define cuáles tablas serán las empleadas
		if sexo == "Femenino":
			tablaNoClinica = tablaNoClinicaMujeres
			tablaPsiquiatrica = tablaPsiquiatricaMujeres
		else:
			tablaNoClinica = tablaNoClinicaVarones
			tablaPsiquiatrica = tablaPsiquiatricaVarones

		# Obtiene las puntuaciones percentiles generales
		for idx in range(len(self.valores)):
			puntuacionPercentilGeneral.append(self.getPuntuacionPercentil(tablaNoClinica, colNames[idx], valoresList[idx]))

		print("PuntPercGeneral: ")
		print(puntuacionPercentilGeneral)
		pstIndex = colNames.index('GSI')

		# Valor de GSI
		gsiValue = puntuacionPercentilGeneral[pstIndex]
		
		# Cuenta los elementos que de puntuacionPercentilGeneral que sean mayores a 0.80
		dimGT80 = sum(list(map(lambda puntPerc: 1 if puntPerc >= 80.0 else 0, puntuacionPercentilGeneral)))
		
		# Cuenta los elementos que de puntuacionPercentilGeneral que sean mayores a 0.90
		dimGT90 = sum(list(map(lambda puntPerc: 1 if puntPerc >= 90.0 else 0, puntuacionPercentilGeneral)))

		if gsiValue >= 80.0 or dimGT80 >= 2:
			print("gsiValue: " + str(gsiValue))
			print("dimGT80: " + str(dimGT80))
			print("bDTM es True")
			bDTM = True
		if gsiValue >= 90.0 or dimGT90 >= 2:
			print("gsiValue: " + str(gsiValue))
			print("dimGT90: " + str(dimGT90))
			print("gsiValue es True")
			bMPsiq = True
		
		# Para que bMPsiq sea True, bDTM debe de ser True
		if bDTM and bMPsiq:
			for idx in range(len(self.valores)):
				puntuacionPercentilMPsiq.append(self.getPuntuacionPercentil(tablaPsiquiatrica, colNames[idx], valoresList[idx]))
			# Ya se calculó lo de Puntuacion Percentil Mpsiq
			bMPsiq = False
			bDTM = False
		elif bDTM:
			for idx in range(len(self.valores)):
				puntuacionPercentilDTM.append(self.getPuntuacionPercentil(tablaPsico, colNames[idx], valoresList[idx]))
			
			gsiValue = puntuacionPercentilDTM[pstIndex]
			dimDTM = 0
			valLimit = 0.0
			
			if sexo == 'Femenino':
				dimDTM = sum(list(map(lambda puntPerc: 1 if puntPerc >= 80.0 else 0, puntuacionPercentilDTM)))
				gsiLimit = 80.0
			else:
				dimDTM = sum(list(map(lambda puntPerc: 1 if puntPerc >= 70.0 else 0, puntuacionPercentilDTM)))
				gsiLimit = 70.0

			if gsiValue >= gsiLimit or dimDTM >= 2:
				bMPsiq = True

		if bMPsiq:
			for idx in range(len(self.valores)):
				puntuacionPercentilMPsiq.append(self.getPuntuacionPercentil(tablaPsiquiatrica, colNames[idx], valoresList[idx]))


		self.puntuacionEscalar = (0, 0, 0)
		self.rangoPercentil = (puntuacionPercentilGeneral, puntuacionPercentilDTM, puntuacionPercentilMPsiq)