#Prueba de Fluidez Verbal
import pandas as pd
import PruebaModel
from AppCtxt import APPCTXT


class FluidezVerbalPrueba(PruebaModel.PruebaModel):	
	def __init__(self, valores):
		nombre = "FLUIDEZ"
		baremos = (pd.read_csv(APPCTXT().get_resource('./Baremos/TablaFluidezVerbal.csv')),
					pd.read_csv(APPCTXT().get_resource('./Baremos/EscolaridadFluidezVerbal.csv')))
		campos = ("P", "A")

		super(FluidezVerbalPrueba,self).__init__(nombre, valores, baremos, campos)

	def calcularPERP(self, datos):
		"""
	 	 Método que es empleado para calcular la Puntuación Escalar(PE), como la Percentil(RP)
	 	 Args:
	 	  datos: Lista de información relevante del reporte para calcular los valores de PE y RP (escolaridad, género, etc.)
		"""
		tablaFV = self.baremos[0]
		tablaEscolaridad = self.baremos[1]

		palabrasConP = self.valores[0]
		animalesConP = self.valores[1]
		escolaridad = datos[0]

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