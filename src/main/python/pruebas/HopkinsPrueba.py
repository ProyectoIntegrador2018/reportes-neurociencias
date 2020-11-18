#Prueba de Hopkins
import pandas as pd
import PruebaModel
import math
from AppCtxt import APPCTXT

class HopkinsPrueba(PruebaModel.PruebaModel):	
	def __init__(self, valores):
		nombre = "HVLT-R"
		baremos = (pd.read_csv(APPCTXT().get_resource('./Baremos/Baremo_Hopkins_Normal.csv')), 
                    pd.read_csv(APPCTXT().get_resource('./Baremos/Baremo_Hopkins_Diferido.csv')),
                    pd.read_csv(APPCTXT().get_resource('./Baremos/Tabla_Conversión_Psicométrica_Completa.csv')))
		campos = ("M.I.", "M.D.")

		super(HopkinsPrueba,self).__init__(nombre, valores, baremos, campos)

	def calcularPERP(self, datos):
		"""
	 	 Método que es empleado para calcular la Puntuación Escalar(PE), como la Percentil(RP)
	 	 Args:
	 	  datos: Lista de información relevante del reporte para calcular los valores de PE y RP (escolaridad, edad)
		"""
		totalDf = self.baremos[0]
		delayedDf = self.baremos[1]
		conversionDf = self.baremos[2]

		total_recall = self.valores[0]
		delayed_recall = self.valores[1]
		edad = datos
		
		if edad < 18:
			edad = 18
		
		if edad >42:
			edad = 42
		
		if ((edad <= 22) and (edad >= 18)):
			if total_recall <= 18:
				total_recall = 18
			if delayed_recall <= 5:
				delayed_recall = 5
			percentile_normal = totalDf.percentile[totalDf.rango18_22 == total_recall].iloc[0]
			escalar_normal = conversionDf['puntuacion_escalar'][conversionDf.puntuacion_percentil == str(math.floor(int(percentile_normal)))].iloc[0]
			percentile_delayed = delayedDf['percentile'][delayedDf.rango18_22 == delayed_recall].iloc[0]
			escalar_delayed = conversionDf['puntuacion_escalar'][conversionDf.puntuacion_percentil == str(math.floor(int(percentile_delayed)))].iloc[0]
		elif ((edad <= 27) and (edad >= 23)):
			if total_recall <= 18:
				total_recall = 18
			if delayed_recall <= 5:
				delayed_recall = 5
			percentile_normal = totalDf.percentile[totalDf.rango23_27 == total_recall].iloc[0]
			escalar_normal = conversionDf['puntuacion_escalar'][conversionDf.puntuacion_percentil == str(math.floor(int(percentile_normal)))].iloc[0]
			percentile_delayed = delayedDf['percentile'][delayedDf.rango23_27 == delayed_recall].iloc[0]
			escalar_delayed = conversionDf['puntuacion_escalar'][conversionDf.puntuacion_percentil == str(math.floor(int(percentile_delayed)))].iloc[0]
		elif ((edad <= 32) and (edad >= 28)):
			if total_recall <= 17:
				total_recall = 17
			if delayed_recall <= 5:
				delayed_recall = 5
			percentile_normal = totalDf.percentile[totalDf.rango28_32 == total_recall].iloc[0]
			escalar_normal = conversionDf['puntuacion_escalar'][conversionDf.puntuacion_percentil == str(math.floor(int(percentile_normal)))].iloc[0]
			percentile_delayed = delayedDf['percentile'][delayedDf.rango28_32 == delayed_recall].iloc[0]
			escalar_delayed = conversionDf['puntuacion_escalar'][conversionDf.puntuacion_percentil == str(math.floor(int(percentile_delayed)))].iloc[0]
		elif ((edad <= 37) and (edad >= 33)):
			if total_recall <= 16:
				total_recall = 16
			if delayed_recall <= 5:
				delayed_recall = 5
			percentile_normal = totalDf.percentile[totalDf.rango33_37 == total_recall].iloc[0]
			escalar_normal = conversionDf['puntuacion_escalar'][conversionDf.puntuacion_percentil == str(math.floor(int(percentile_normal)))].iloc[0]
			percentile_delayed = delayedDf['percentile'][delayedDf.rango33_37 == delayed_recall].iloc[0]
			escalar_delayed = conversionDf['puntuacion_escalar'][conversionDf.puntuacion_percentil == str(math.floor(int(percentile_delayed)))].iloc[0]
		elif ((edad <= 42) and (edad >= 38)):
			if total_recall <= 16:
				total_recall = 16
			if delayed_recall <= 4:
				delayed_recall = 4
			percentile_normal = totalDf.percentile[totalDf.rango38_42 == total_recall].iloc[0]
			escalar_normal = conversionDf['puntuacion_escalar'][conversionDf.puntuacion_percentil == str(math.floor(int(percentile_normal)))].iloc[0]
			percentile_delayed = delayedDf['percentile'][delayedDf.rango38_42 == delayed_recall].iloc[0]
			escalar_delayed = conversionDf['puntuacion_escalar'][conversionDf.puntuacion_percentil == str(math.floor(int(percentile_delayed)))].iloc[0]
		

		self.puntuacionEscalar = (escalar_normal, escalar_delayed)
		self.rangoPercentil = (percentile_normal, percentile_delayed)