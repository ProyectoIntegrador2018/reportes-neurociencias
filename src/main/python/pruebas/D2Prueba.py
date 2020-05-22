#Prueba de D2
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QUrl, QDir
import pandas as pd
import PruebaModel

class D2Prueba(PruebaModel.PruebaModel):	
	def __init__(self, valores):
		nombre = "D2"
		tablaD2_15_16 = QUrl(QDir.currentPath()+"/Baremos/TablaD2_15-16.csv").toString()
		tablaD2_17_18 = QUrl(QDir.currentPath()+"/Baremos/TablaD2_17-18.csv").toString()
		tablaD2_19_23 = QUrl(QDir.currentPath()+"/Baremos/TablaD2_19-23.csv").toString()
		tablaD2_24_29 = QUrl(QDir.currentPath()+"/Baremos/TablaD2_24-29.csv").toString()
		tablaD2_30_39 = QUrl(QDir.currentPath()+"/Baremos/TablaD2_30-39.csv").toString()
		baremos =	(pd.read_csv(tablaD2_15_16), 
					pd.read_csv(tablaD2_17_18),
					pd.read_csv(tablaD2_19_23),
					pd.read_csv(tablaD2_24_29),
					pd.read_csv(tablaD2_30_39))
		campos = ("TOT", "CON", "VAR")

		super(D2Prueba,self).__init__(nombre, valores, baremos, campos)

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

		tot = self.valores[0]
		con = self.valores[1]
		var = self.valores[2]
		
		if edad == 15 or edad == 16:
			auxTOT = b1[(tot >= b1['TOTmin']) & (b1['TOTmax'] >= tot)].iloc[0]
			peTOT = auxTOT['Escalar']
			ppTOT = auxTOT['Percentil']
			auxCON = b1[(con >= b1['CONmin']) & (b1['CONmax'] >= con)].iloc[0]
			peCON = auxCON['Escalar']
			ppCON = auxCON['Percentil']
			auxVAR = b1[(var >= b1['VARmin']) & (b1['VARmax'] >= var)].iloc[0]
			peVAR= auxVAR['Escalar']
			ppVAR= auxVAR['Percentil']

		elif edad == 17 or edad == 18:
			auxTOT = b2[(tot >= b2['TOTmin']) & (b2['TOTmax'] >= tot)].iloc[0]
			peTOT = auxTOT['Escalar']
			ppTOT = auxTOT['Percentil']
			auxCON = b2[(con >= b2['CONmin']) & (b2['CONmax'] >= con)].iloc[0]
			peCON = auxCON['Escalar']
			ppCON = auxCON['Percentil']
			auxVAR = b2[(var >= b2['VARmin']) & (b2['VARmax'] >= var)].iloc[0]
			peVAR= auxVAR['Escalar']
			ppVAR= auxVAR['Percentil']

		elif edad >= 19 and edad <= 23:
			auxTOT = b3[(tot >= b3['TOTmin']) & (b3['TOTmax'] >= tot)].iloc[0]
			peTOT = auxTOT['Escalar']
			ppTOT = auxTOT['Percentil']
			auxCON = b3[(con >= b3['CONmin']) & (b3['CONmax'] >= con)].iloc[0]
			peCON = auxCON['Escalar']
			ppCON = auxCON['Percentil']
			auxVAR = b3[(var >= b3['VARmin']) & (b3['VARmax'] >= var)].iloc[0]
			peVAR= auxVAR['Escalar']
			ppVAR= auxVAR['Percentil']

		elif edad >= 24 and edad <= 29:
			auxTOT = b4[(tot >= b4['TOTmin']) & (b4['TOTmax'] >= tot)].iloc[0]
			peTOT = auxTOT['Escalar']
			ppTOT = auxTOT['Percentil']
			auxCON = b4[(con >= b4['CONmin']) & (b4['CONmax'] >= con)].iloc[0]
			peCON = auxCON['Escalar']
			ppCON = auxCON['Percentil']
			auxVAR = b4[(var >= b4['VARmin']) & (b4['VARmax'] >= var)].iloc[0]
			peVAR= auxVAR['Escalar']
			ppVAR= auxVAR['Percentil']

		elif edad >= 30 and edad <= 39:
			auxTOT = b5[(tot >= b5['TOTmin']) & (b5['TOTmax'] >= tot)].iloc[0]
			peTOT = auxTOT['Escalar']
			ppTOT = auxTOT['Percentil']
			auxCON = b5[(con >= b5['CONmin']) & (b5['CONmax'] >= con)].iloc[0]
			peCON = auxCON['Escalar']
			ppCON = auxCON['Percentil']
			auxVAR = b5[(var >= b5['VARmin']) & (b5['VARmax'] >= var)].iloc[0]
			peVAR= auxVAR['Escalar']
			ppVAR= auxVAR['Percentil']

		self.puntuacionEscalar = (peTOT, peCON, peVAR)
		self.rangoPercentil = (ppTOT, ppCON, ppVAR)