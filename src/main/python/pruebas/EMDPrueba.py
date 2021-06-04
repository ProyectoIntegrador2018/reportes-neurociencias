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
		campos = ("ME", "MICO", "MIE", "MIA", "MICU", "Amotivacion", "MID")

		super(EMDPrueba,self).__init__(nombre, valores, baremos, campos)

	def calcularPERP(self):
		"""
	 	 Método que es empleado para calcular la Puntuación Escalar(PE), como la Percentil(RP)
	 	 Args:
	 	  datos: Lista de información relevante del reporte para calcular los valores de PE y RP (escolaridad, edad)
		"""
		print(self.valores)

		(me,mico,mie,mia,micu,amed,mid) = self.valores

		#ME
		if me >= 6 and me <= 19:
			me = "Baja"
		elif me >= 19 and me <= 30:
			me = "Media"
		elif me >= 31 and me <= 42:
			me = "Alta"

		#MICO
		if mico >= 4 and mico <= 12:
			mico = "Baja"
		elif mico >= 13 and mico <= 20:
			mico = "Media"
		elif mico >= 21 and mico <= 28:
			mico = "Alta"
		
		#MIE
		if mie >= 4 and mie <= 12:
			mie = "Baja"
		elif mie >= 13 and mie <= 20:
			mie = "Media"
		elif mie >= 21 and mie <= 28:
			mie = "Alta"

		#MIA
		if mia >= 4 and mia <= 12:
			mia = "Baja"
		elif mia >= 13 and mia <= 20:
			mia = "Media"
		elif mia >= 21 and mia <= 28:
			mia = "Alta"

		#MICU
		if micu >= 4 and micu <= 12:
			micu = "Baja"
		elif micu >= 13 and micu <= 20:
			micu = "Media"
		elif micu >= 21 and micu <= 28:
			micu = "Alta"

		#AMED
		if amed >= 26 and amed <= 35:
			amed = "Baja"
		elif amed >= 16 and amed <= 25:
			amed = "Media"
		elif amed >= 5 and amed <= 15:
			amed = "Alta"

		#MID
		if mid >= 2 and mid <= 6:
			mid = "Baja"
		elif mid >= 7 and mid <= 10:
			mid = "Media"
		elif mid >= 11 and mid <= 14:
			mid = "Alta"

		print(me,mico,mie,mia,micu,amed,mid)
		self.puntuacionEscalar = (me,mico,mie,mia,micu,amed,mid)
        #self.puntuacionEscalar = (me,mico,mie,mia,micu,amed,mid)
		# self.rangoPercentil = ((6,42),(4,28),(4,28),(4,28),(4,28),(5,35),(2,14))