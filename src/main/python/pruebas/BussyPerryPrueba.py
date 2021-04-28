#Prueba de TMT
import pandas as pd
import PruebaModel
from AppCtxt import APPCTXT

class BussyPerryPrueba(PruebaModel.PruebaModel):	
	def __init__(self, valores):
		nombre = "BussYPerry"
		baremos = (pd.read_csv(APPCTXT().get_resource('./Baremos/TablaTMT.csv')),
					pd.read_csv(APPCTXT().get_resource('./Baremos/EscolaridadTMTA.csv')),
					pd.read_csv(APPCTXT().get_resource('./Baremos/EscolaridadTMTB.csv')))
		campos = ("A", "B")

		super(BussyPerryPrueba,self).__init__(nombre, valores, baremos, campos)

	def calcularPERP(self, datos):
		"""
	 	 Método que es empleado para calcular la Puntuación Escalar(PE), como la Percentil(RP)
	 	 Args:
	 	  datos: Lista de información relevante del reporte para calcular los valores de PE y RP (escolaridad, edad)
		"""

		agFis = self.valores[0]
		agVer = self.valores[1]
		ira = self.valores[2]
		hos = self.valores[3]

		self.puntuacionEscalar = (agFis, agVer,ira,hos)
		self.rangoPercentil = ((0,45),(0,25),(0,35), (0,40))