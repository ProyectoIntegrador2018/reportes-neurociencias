#Prueba de Abstraccion
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QUrl, QDir
import pandas as pd
import PruebaModel

class AbstraccionPrueba(PruebaModel.PruebaModel):	
	def __init__(self, valores):
		baremoAbstraccion = QUrl(QDir.currentPath()+"/Baremos/TablaAbstraccion.csv").toString()
		baremos = (pd.read_csv(baremoAbstraccion))

		# baremos = (pd.read_csv("c:/users/usuario/desktop/reportes-neurociencias/src/main/python/Baremos/TablaAbstraccion.csv"))
		# baremos = (pd.read_csv("c:\\users\\usuario\\desktop\\reportes-neurociencias\\src\\main\\python\\Baremos\\TablaAbstraccion.csv"))
		nombre = "Abs"
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

		if edad < 18:
			edad = 18
		elif edad > 50:
			edad = 50

		temp = tablaAbstraccion[tablaAbstraccion['Abstraccion'] == valSemAbs].iloc[0]
		puntuacionEscalar = temp['PuntuacionEscalar']
		puntuacionPercentil = temp['RangoPercentil']

		
		self.puntuacionEscalar = puntuacionEscalar
		self.rangoPercentil = puntuacionPercentil