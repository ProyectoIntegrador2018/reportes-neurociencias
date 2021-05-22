#Prueba de TMT
import pandas as pd
import PruebaModel
from AppCtxt import APPCTXT

class EMDPrueba(PruebaModel.PruebaModel):	
	def __init__(self, valores):
		nombre = "EMD"
		baremos = (pd.read_csv(APPCTXT().get_resource('./Baremos/TablaTMT.csv')),
					pd.read_csv(APPCTXT().get_resource('./Baremos/EscolaridadTMTA.csv')),
					pd.read_csv(APPCTXT().get_resource('./Baremos/EscolaridadTMTB.csv')))
		campos = ("A", "B")

		super(EMDPrueba,self).__init__(nombre, valores, baremos, campos)

	def calcularPERP(self):
		"""
	 	 Método que es empleado para calcular la Puntuación Escalar(PE), como la Percentil(RP)
	 	 Args:
	 	  datos: Lista de información relevante del reporte para calcular los valores de PE y RP (escolaridad, edad)
		"""
		print(self.valores)

		(me,mico,mie,mia,micu,amed,mid) = self.valores

		if me == 1:
			print("hola aqui pasa algo")
			me = "Cambio"

		#self.puntuacionEscalar = (uno,dos,tres,cuatro,cinco,seis,siete)
        
        self.puntuacionEscalar = (me,mico,mie,mia,micu,amed,mid)
		# self.rangoPercentil = ((6,42),(4,28),(4,28),(4,28),(4,28),(5,35),(2,14))