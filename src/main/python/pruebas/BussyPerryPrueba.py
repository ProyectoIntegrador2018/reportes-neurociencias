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
		(agFis, agVer,ira,hos) = self.valores
		
		#agFis
		if agFis >= 9 and agFis <= 21:
			agFis = "Baja"
		elif agFis >= 22 and agFis <= 33:
			agFis = "Media"
		elif agFis >= 34 and agFis <= 45:
			agFis = "Alta"

		#agVer
		if agVer >= 5 and agVer <= 11:
			agVer = "Baja"
		elif agVer >= 12 and agVer <= 18:
			agVer = "Media"
		elif agVer >= 19 and agVer <= 25:
			agVer = "Alta"

		#ira
		if ira >= 11 and ira <= 17:
			ira = "Baja"
		elif ira >= 18 and ira <= 24:
			ira = "Media"
		elif ira >= 25 and ira <= 31:
			ira = "Alta"
			
		#hos
		if hos >= 8 and hos <= 18:
			hos = "Baja"
		elif hos >= 19 and hos <= 29:
			hos = "Media"
		elif hos >= 30 and hos <= 40:
			hos = "Alta"
		self.puntuacionEscalar = (agFis, agVer,ira,hos)
		#self.rangoPercentil = ((0,45),(0,25),(0,35), (0,40))