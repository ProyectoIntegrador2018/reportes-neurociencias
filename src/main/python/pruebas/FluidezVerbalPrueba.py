#Prueba de Fluidez Verbal
import pandas as pd
import PruebaModel
from AppCtxt import APPCTXT


class FluidezVerbalPrueba(PruebaModel.PruebaModel):	
	def __init__(self, valores):
		nombre = "FLUIDEZ"
		baremos = (pd.read_csv(APPCTXT().get_resource('./Baremos/TablaFluidezVerbal.csv')),
					pd.read_csv(APPCTXT().get_resource('./Baremos/TablaFluidezVerbal50-56.csv')),
					pd.read_csv(APPCTXT().get_resource('./Baremos/TablaFluidezVerbal57-59.csv')),
					pd.read_csv(APPCTXT().get_resource('./Baremos/TablaFluidezVerbal60-62.csv')),
					pd.read_csv(APPCTXT().get_resource('./Baremos/TablaFluidezVerbal63-65.csv')),
					pd.read_csv(APPCTXT().get_resource('./Baremos/TablaFluidezVerbal66-68.csv')),
					pd.read_csv(APPCTXT().get_resource('./Baremos/TablaFluidezVerbal69-71.csv')),
					pd.read_csv(APPCTXT().get_resource('./Baremos/TablaFluidezVerbal72-74.csv')),
					pd.read_csv(APPCTXT().get_resource('./Baremos/TablaFluidezVerbal75-77.csv')),
					pd.read_csv(APPCTXT().get_resource('./Baremos/TablaFluidezVerbal78-80.csv')),
					pd.read_csv(APPCTXT().get_resource('./Baremos/TablaFluidezVerbal81-90.csv')),
					pd.read_csv(APPCTXT().get_resource('./Baremos/EscolaridadFluidezVerbal.csv')))
		campos = ("P", "A")

		super(FluidezVerbalPrueba,self).__init__(nombre, valores, baremos, campos)

	def calcularPERP(self, datos):
		"""
	 	 Método que es empleado para calcular la Puntuación Escalar(PE), como la Percentil(RP)
	 	 Args:
	 	  datos: Lista de información relevante del reporte para calcular los valores de PE y RP (escolaridad, género, etc.)
		"""
		tablaEscolaridad = self.baremos[-1]

		palabrasConP = self.valores[0]
		animalesConP = self.valores[1]
		escolaridad = datos[0]
		edad = datos[1]
		tablaFV_0_49 = self.baremos[0]
		tablaFV_50_56 = self.baremos[1]
		tablaFV_57_59 = self.baremos[2]
		tablaFV_60_62 = self.baremos[3]
		tablaFV_63_65 = self.baremos[4]
		tablaFV_66_68 = self.baremos[5]
		tablaFV_69_71 = self.baremos[6]
		tablaFV_72_74 = self.baremos[7]
		tablaFV_75_77 = self.baremos[8]
		tablaFV_78_80 = self.baremos[9]
		tablaFV_81_90 = self.baremos[10]

		if edad <= 49:
			tablaFV = tablaFV_0_49
		elif 50 <= edad <= 56:
			tablaFV = tablaFV_50_56
		elif 57 <= edad <= 59:
			tablaFV = tablaFV_57_59
		elif 60 <= edad <= 62:
			tablaFV = tablaFV_60_62
		elif 63 <= edad <= 65:
			tablaFV = tablaFV_63_65
		elif 66 <= edad <= 68:
			tablaFV = tablaFV_66_68
		elif 69 <= edad <= 71:
			tablaFV = tablaFV_69_71
		elif 72 <= edad <= 74:
			tablaFV = tablaFV_72_74
		elif 75 <= edad <= 77:
			tablaFV = tablaFV_75_77
		elif 78 <= edad <= 80:
			tablaFV = tablaFV_78_80
		else:
			tablaFV = tablaFV_81_90


		if escolaridad < 8:
			escolaridad = 8
		elif escolaridad > 20:
			escolaridad = 20

		ajustes = tablaEscolaridad[tablaEscolaridad['Escolaridad']==escolaridad].iloc[0]

		temp = tablaFV[(animalesConP >= tablaFV['AnimalesMin']) & (tablaFV['AnimalesMax']>=animalesConP)].iloc[0]
		puntuacionEscalarAnim = temp['PuntuacionEscalar'] + ajustes['Animales']
		
		if puntuacionEscalarAnim < 2:
			puntuacionEscalarAnim = 2
		elif puntuacionEscalarAnim > 18:
			puntuacionEscalarAnim = 18

		temp = tablaFV[tablaFV['PuntuacionEscalar'] == puntuacionEscalarAnim].iloc[0]
		puntuacionPercentilAnim = (temp['RangoDePercentilMin'], temp['RangoDePercentilMax'])


		tempPal = tablaFV[(palabrasConP >= tablaFV['PalabrasMin']) & (tablaFV['PalabrasMax']>=palabrasConP)].iloc[0]
		puntuacionEscalarPal = tempPal['PuntuacionEscalar'] + ajustes['Palabras']
		
		if puntuacionEscalarPal < 2:
			puntuacionEscalarPal = 2
		elif puntuacionEscalarPal > 18:
			puntuacionEscalarPal = 18

		tempPal = tablaFV[tablaFV['PuntuacionEscalar'] == puntuacionEscalarPal].iloc[0]
		puntuacionPercentilPal = (tempPal['RangoDePercentilMin'], tempPal['RangoDePercentilMax'])

		self.puntuacionEscalar = (int(puntuacionEscalarPal), int(puntuacionEscalarAnim))
		self.rangoPercentil = (puntuacionPercentilPal, puntuacionPercentilAnim)