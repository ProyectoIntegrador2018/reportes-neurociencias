#Prueba de Hopkins
import pandas as pd
import PruebaModel

class HopkinsPrueba(PruebaModel.PruebaModel):	
	def __init__(self, valores):
		nombre = "Hopkins"
		baremos = (pd.read_csv('./Baremos/Baremo_Hopkins_Normal.csv'), 
                    pd.read_csv('./Baremos/Baremo_Hopkins_Diferido.csv'),
                    pd.read_csv('./Baremos/Tabla_Conversión_Psicométrica_Completa.csv'))
		campos = ("total_recall", "delayed_recall")

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

		
		
		percentile_normal = totalDf.percentile[totalDf.rango18_22 == total_recall].iloc[0]
		escalar_normal = conversionDf['puntuacion_escalar'][conversionDf.puntuacion_percentil == str(int(percentile_normal))].item()
		percentile_delayed = delayedDf['percentile'][delayedDf.rango18_22 == delayed_recall].iloc[0]
		escalar_delayed = conversionDf['puntuacion_escalar'][conversionDf.puntuacion_percentil == str(int(percentile_delayed))].item()
		

		self.puntuacionEscalar = (escalar_normal, escalar_delayed)
		self.rangoPercentil = (percentile_normal, percentile_delayed)