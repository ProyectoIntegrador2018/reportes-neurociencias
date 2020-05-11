#Prueba de Abstraccion
import pandas as pd
import PruebaModel

class AbstraccionPrueba(PruebaModel.PruebaModel):	
	def __init__(self, valores):
		nombre = "Abs"
		baremos = (pd.read_csv('./Baremos/TablaAbstraccion.csv'))
		campos = ("Abs")

		super(AbstraccionPrueba,self).__init__(nombre, valores, baremos, campos)

	def calcularPERP(self, datos):
		"""
	 	 Método que es empleado para calcular la Puntuación Escalar(PE), como la Percentil(RP)
	 	 Args:
	 	  datos: Lista de información relevante del reporte para calcular los valores de PE y RP (edad)
		"""
		tablaAbstraccion = self.baremos
		
		valSemAbs = self.valores

		edad = datos[0]

		"""
		 ****REVISAR CON BEATRIZ****
		 LA PRUEBA DICE QUE SE DEBE DE TOMAR EN CUENTA LA EDAD PERO NO HAY NINGÚN REGISTRO DE CUÁLES AJUSTES SE DEBEN DE HACER
		"""
		if edad < 18:
			edad = 18
		elif edad > 50:
			edad = 50

		temp = tablaAbstraccion[tablaAbstraccion['Abstraccion'] == valSemAbs].iloc[0]
		puntuacionEscalar = temp['PuntuacionEscalar']
		puntuacionPercentil = temp['RangoPercentil']

		
		self.puntuacionEscalar = puntuacionEscalar
		self.rangoPercentil = puntuacionPercentil