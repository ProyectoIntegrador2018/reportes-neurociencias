import pandas as pd
import PruebaModel

class MVCPrueba(PruebaModel.PruebaModel):	
	def __init__(self, valores):
		nombre = "MVC"
		baremos = (pd.read_csv('./Baremos/MaterialVerbalComplejo.csv'))

		super(MVCPrueba,self).__init__(nombre, valores, baremos)

	def calcularPERP(self):
		"""
	 	 Método que es empleado para calcular la Puntuación Escalar(PE), como la Percentil(RP)
	 	 Args:
	 	  datos: Lista de información relevante del reporte para calcular los valores de PE y RP (escolaridad, género, etc.)
		"""
		tablaMVC = self.baremos

		print("MVC: " + str(self.valores[0]))
		print("MVCT: " + str(self.valores[1]))
		
		MVC = self.valores[0]
		MVCT = self.valores[1]

		auxMVC = tablaMVC.loc[tablaMVC['MVC'] == MVC]
		puntuacionEscalarMVC = auxMVC['Escalar']
		puntuacionPercentilMVC = auxMVC['Percentil']

		auxMVCT = tablaMVC.loc[tablaMVC['MVCT'] == MVCT]
		puntuacionEscalarMCVT = auxMVCT['Escalar']
		puntuacionPercentilMVCT = auxMVCT['Percentil']

		self.puntuacionEscalar = (int(puntuacionEscalarMVC), int(puntuacionEscalarMCVT))
		self.rangoPercentil = (int(puntuacionPercentilMVC), int(puntuacionPercentilMVCT))
