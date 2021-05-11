#Prueba de BSI18
import pandas as pd
import PruebaModel
from AppCtxt import APPCTXT

class BSI18Prueba(PruebaModel.PruebaModel):	
	def __init__(self, valores):
		nombre = "BSI-18"
		baremos = (pd.read_csv(APPCTXT().get_resource('./Baremos/BSI18_VARONES_TRABAJADORES_ACTIVO.csv')),
					pd.read_csv(APPCTXT().get_resource('./Baremos/BSI18_MUJERES_TRABAJADORES_ACTIVO.csv')),
					pd.read_csv(APPCTXT().get_resource('./Baremos/BSI18_MUJERES_Y_VARONES_TRABAJADORES_ACTIVO.csv')),
					pd.read_csv(APPCTXT().get_resource('./Baremos/BSI18_VARONES_PACIENTES_CON_CANCER.csv')),
					pd.read_csv(APPCTXT().get_resource('./Baremos/BSI18_MUJERES_PACIENTES_CON_CANCER.csv')),
					pd.read_csv(APPCTXT().get_resource('./Baremos/BSI18_MUJERES_Y_VARONES_PACIENTES_CON_CANCER.csv')),
					pd.read_csv(APPCTXT().get_resource('./Baremos/BSI18_PRERCENTILES_EQUIVALENTES_PUNTUACIONES_T.csv')),
					pd.read_csv(APPCTXT().get_resource('./Baremos/Tabla_Conversión_Psicométrica_Completa.csv')))
		campos = ("DIRECTA", "SOM", "DEP", "ANS", "IGS")

		super(BSI18Prueba,self).__init__(nombre, valores, baremos, campos)

	def calcularPERP(self, datos):
		"""
	 	 Método que es empleado para calcular la Puntuación Escalar(PE), como la Percentil(RP)
	 	 Args:
	 	  datos: Lista de información relevante del reporte para calcular los valores de PE y RP (escolaridad, género, etc.)
		"""
		# Extrar las distintas tablas de baremos
		varonesActivos = self.baremos[0]
		mujeresActivos =  self.baremos[1]
		mujeresVaronesActivos = self.baremos[2]
		varonesCancer = self.baremos[3]
		mujeresCancer =  self.baremos[4]
		mujeresVaronesCancer = self.baremos[5]
		percentiles = self.baremos[6]
		conversion = self.baremos[7]
		
		# Extrae los datos que recibe del controlador
		valoresList = self.valores
		sexo = datos[0]
		# Si el paciente padece cancer
		t_C = datos[1]		

		colNames = ["DIRECTA", "SOM", "DEP", "ANS", "IGS"]

		# Extrae los valores de las dimensiones
		SOM = valoresList[0]
		DEP = valoresList[1]
		ANS = valoresList[2]

		# Suma todas las dimensiones para obtener la general
		IGS = SOM + DEP + ANS
		self.valores.append(IGS)
		
		# Define cuáles tablas serán las empleadas
		if sexo == "Femenino":
			if t_C:
				baremos = mujeresCancer
			else:
				baremos = mujeresActivos
		elif sexo == "Masculino":
			if t_C:
				baremos = varonesCancer
			else:
				baremos = varonesActivos
		else:
			if t_C:
				baremos = mujeresVaronesCancer
			else:
				baremos = mujeresVaronesActivos

		# Obtiene los baremos de cada dimensión y la general
		SOM = baremos.SOM[baremos.directa == SOM].iloc[0]
		DEP = baremos.DEP[baremos.directa == DEP].iloc[0]
		ANS = baremos.ANS[baremos.directa == ANS].iloc[0]
		IGS = baremos.IGS[baremos.directa == IGS].iloc[0]

		# Obtiene los baremos de cada dimensión y la general
		SOMp = percentiles.Percentil[percentiles.Puntuacion_T == SOM].iloc[0]
		DEPp = percentiles.Percentil[percentiles.Puntuacion_T == DEP].iloc[0]
		ANSp = percentiles.Percentil[percentiles.Puntuacion_T == ANS].iloc[0]
		IGSp = percentiles.Percentil[percentiles.Puntuacion_T == IGS].iloc[0]

		SOMe = conversion.puntuacion_escalar[conversion.puntuacion_percentil == str(SOMp)].iloc[0]
		DEPe = conversion.puntuacion_escalar[conversion.puntuacion_percentil == str(DEPp)].iloc[0]
		ANSe = conversion.puntuacion_escalar[conversion.puntuacion_percentil == str(ANSp)].iloc[0]
		IGSe = conversion.puntuacion_escalar[conversion.puntuacion_percentil == str(IGSp)].iloc[0]

		self.puntuacionEscalar = (SOMe, DEPe, ANSe, IGSe)
		self.rangoPercentil = (SOMp, DEPp, ANSp, IGSp)