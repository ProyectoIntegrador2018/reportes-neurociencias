#Prueba de D2
import pandas as pd
import PruebaModel

class D2Prueba(PruebaModel.PruebaModel):	
	def __init__(self, valores):
		nombre = "D2"
		baremos =	(pd.read_csv('./Baremos/TablaD2_15-16.csv'), 
					pd.read_csv('./Baremos/TablaD2_17-18.csv'),
					pd.read_csv('./Baremos/TablaD2_19-23.csv'),
					pd.read_csv('./Baremos/TablaD2_24-29.csv'),
					pd.read_csv('./Baremos/TablaD2_30-39.csv'))
		campos = ("TR", "TA", "O", "C", "TOT", "CON", "VAR") #TOT y CON son campos que se calculan en este script

		super(D2Prueba,self).__init__(nombre, valores, baremos, campos)

	def scores(self, bar, tr, ta, o, c, var):
		'''
		Método interno que se usa para calcular los 7 distintos punntajes directos de acuerdo al baremo de edad
		Args:
			bar: baremo que usara
		'''
		auxTR = bar[(tr >= bar['TRmin']) & (bar['TRmax'] >= tr)].iloc[0]
		peTR = auxTR['Escalar']
		ppTR = auxTR['Percentil']
		auxTA = bar[(ta >= bar['TAmin']) & (bar['TAmax'] >= ta)].iloc[0]
		peTA = auxTA['Escalar']
		ppTA = auxTA['Percentil']
		auxO = bar[(o >= bar['Omin']) & (bar['Omax'] >= o)].iloc[0]
		peO = auxO['Escalar']
		ppO = auxO['Percentil']
		auxC = bar[(c >= bar['Cmin']) & (bar['Cmax'] >= c)].iloc[0]
		peC = auxC['Escalar']
		ppC = auxC['Percentil']

		tot = tr - (o + c)
		con = ta - c 

		auxTOT = bar[(tot >= bar['TOTmin']) & (bar['TOTmax'] >= tot)].iloc[0]
		peTOT = auxTOT['Escalar']
		ppTOT = auxTOT['Percentil']
		auxCON = bar[(con >= bar['CONmin']) & (bar['CONmax'] >= con)].iloc[0]
		peCON = auxCON['Escalar']
		ppCON = auxCON['Percentil']
		auxVAR = bar[(var >= bar['VARmin']) & (bar['VARmax'] >= var)].iloc[0]
		peVAR= auxVAR['Escalar']
		ppVAR= auxVAR['Percentil']

		self.puntuacionEscalar = (peTR, peTA, peO, peC, peTOT, peCON, peVAR)
		self.rangoPercentil = (ppTR, ppTA, ppO, ppC, ppTOT, ppCON, ppVAR)


	def calcularPERP(self, datos):
		"""
	 	 Método que es empleado para calcular la Puntuación Escalar(PE), como la Percentil(RP)
	 	 Args:
	 	  datos: Lista de información relevante del reporte para calcular los valores de PE y RP (escolaridad, edad)
		"""
		edad = datos
		'''
		La edad tiene que estar forzada a un rango de 15 a 39 años
		'''
		if edad < 15:
			edad = 15
		elif edad > 39:
			edad = 39

		b1 = self.baremos[0]
		b2 = self.baremos[1]
		b3 = self.baremos[2]
		b4 = self.baremos[3]
		b5 = self.baremos[4]

		tr = self.valores[0]
		ta = self.valores[1]
		o = self.valores[2]
		c = self.valores[3]
		var = self.valores[4]
		
		if edad == 15 or edad == 16:
			self.scores(b1, tr, ta, o, c, var)

		elif edad == 17 or edad == 18:
			self.scores(b2, tr, ta, o, c, var)


		elif edad >= 19 and edad <= 23:
			self.scores(b3, tr, ta, o, c, var)


		elif edad >= 24 and edad <= 29:
			self.scores(b4, tr, ta, o, c, var)


		elif edad >= 30 and edad <= 39:
			self.scores(b5, tr, ta, o, c, var)
