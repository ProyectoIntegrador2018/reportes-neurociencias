#Prueba de Material Verbal Complejo
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QUrl, QDir
import pandas as pd
import PruebaModel

class MVCPrueba(PruebaModel.PruebaModel):	
	def __init__(self, valores):
		nombre = "MVC"
		baremoMVC = QUrl(QDir.currentPath()+"/Baremos/MaterialVerbalComplejo.csv").toString()
		baremos = (pd.read_csv(baremoMVC))
		campos = ("MVC", "MVCt")

		super(MVCPrueba,self).__init__(nombre, valores, baremos, campos)

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
		puntuacionEscalarMVC = auxMVC['MVC_Escalar']
		puntuacionPercentilMVC = auxMVC['MVC_Percentil']

		auxMVCT = tablaMVC.loc[tablaMVC['MVCT'] == MVCT]
		puntuacionEscalarMVCT = auxMVCT['MVCT_Escalar']
		puntuacionPercentilMVCT = auxMVCT['MVCT_Percentil']

		self.puntuacionEscalar = (int(puntuacionEscalarMVC), int(puntuacionEscalarMVCT))
		self.rangoPercentil = (int(puntuacionPercentilMVC), int(puntuacionPercentilMVCT))
