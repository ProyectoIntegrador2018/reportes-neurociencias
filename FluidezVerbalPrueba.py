#Prueba de Fluidez Verbal
import pandas as pd
import PruebaModel

class FluidezVerbalPrueba(PruebaModel.PruebaModel):	
	def __init__(self, valores):
		nombre = "FluidezVerbal"
		baremos = (pd.read_csv('./Baremos/TablaFluidezVerbal.csv'), pd.read_csv('./Baremos/EscolaridadFluidezVerbal.csv'))

		super(FluidezVerbalPrueba,self).__init__(nombre, valores, baremos)

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
		ajustes = tablaEscolaridad[tablaEscolaridad['Escolaridad']==escolaridad].iloc[0]

		temp = tablaFV[tablaFV['AnimalesMin']>=animalesConP].iloc[0]
		puntuacionEscalarAnim = temp['PuntuacionEscalar'] + ajustes['Animales']
		puntuacionPercentilAnim = (temp['RangoDePercentilMin'], temp['RangoDePercentilMax'])

		tempPal = tablaFV[tablaFV['PalabrasMin']>=palabrasConP].iloc[0]
		puntuacionEscalarPal = tempPal['PuntuacionEscalar'] + ajustes['Palabras']
		puntuacionPercentilPal = (tempPal['RangoDePercentilMin'], tempPal['RangoDePercentilMax'])

		self.puntuacionEscalar = (puntuacionEscalarAnim, puntuacionEscalarPal)
		self.rangoPercentil = (puntuacionPercentilAnim, puntuacionPercentilPal)