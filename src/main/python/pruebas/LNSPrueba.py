#Prueba de LNS
import pandas as pd
import PruebaModel
from AppCtxt import APPCTXT

class LNSPrueba(PruebaModel.PruebaModel):	
	def __init__(self, valores):
		nombre = "LNS"
		baremos = (pd.read_csv(APPCTXT().get_resource('./Baremos/TablaLNS.csv')),
					pd.read_csv(APPCTXT().get_resource('./Baremos/EscolaridadLNS.csv')))
		campos = ("I", "T")

		super(LNSPrueba,self).__init__(nombre, valores, baremos, campos)

	def calcularPERP(self, datos):
		"""
	 	 Método que es empleado para calcular la Puntuación Escalar(PE), como la Percentil(RP)
	 	 Args:
	 	  datos: Lista de información relevante del reporte para calcular los valores de PE y RP (escolaridad, edad)
		"""
		tablaLNS = self.baremos[0]
		tablaEscolaridadLNS = self.baremos[1]

		span = self.valores[0]
		total = self.valores[1]
		escolaridad = datos

		'''
		La escolaridad tiene que estar forzada a un rango de 8 a 20 años
		'''
		if escolaridad < 8:
			escolaridad = 8
		elif escolaridad > 20:
			escolaridad = 20

		ajuste = tablaEscolaridadLNS[tablaEscolaridadLNS['Escolaridad'] == escolaridad].iloc[0]

		auxSpan = tablaLNS[tablaLNS['Span'] == span].iloc[0]
		puntuacionEscalarSpan = auxSpan['Escalar'] + ajuste['LNSspan']

		'''
		Se asegura que despues del ajuste por escolaridad, la puntuación exista y pasarse a percentil
		'''
		if puntuacionEscalarSpan < 2:
			puntuacionEscalarSpan = 2
		elif puntuacionEscalarSpan > 18:
			puntuacionEscalarSpan = 18

		auxSpan = tablaLNS[tablaLNS['Escalar'] == puntuacionEscalarSpan].iloc[0]
		puntuacionPercentilSpan = (auxSpan['PercentilMin'], auxSpan['PercentilMax'])


		auxTotal = tablaLNS[(total >= tablaLNS['TotalMin']) & (tablaLNS['TotalMax'] >= total)].iloc[0]
		puntuacionEscalarTotal = auxTotal['Escalar'] + ajuste['LNStotal']

		if puntuacionEscalarTotal < 2:
			puntuacionEscalarTotal = 2
		elif puntuacionEscalarTotal > 18:
			puntuacionEscalarTotal = 18

		auxTotal = tablaLNS[tablaLNS['Escalar'] == puntuacionEscalarTotal].iloc[0]
		puntuacionPercentilTotal = (auxTotal['PercentilMin'], auxTotal['PercentilMax'])

		self.puntuacionEscalar = (puntuacionEscalarSpan, puntuacionEscalarTotal)
		self.rangoPercentil = (puntuacionPercentilSpan, puntuacionPercentilTotal)
