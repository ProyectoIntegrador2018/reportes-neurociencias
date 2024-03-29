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
		
		if edad > 78:
			edad = 78
		
		if ((edad <= 22) and (edad >= 18)):
			if total_recall <= 18:
				total_recall = 18
			if delayed_recall <= 5:
				delayed_recall = 5
			delayedDf.rango18_22 = delayedDf.rango18_22.fillna(0)
			totalDf.rango18_22 = [math.floor(x) for x in totalDf.rango18_22]
			delayedDf.rango18_22 = [math.floor(x) for x in delayedDf.rango18_22]
			
			percentile_normal = totalDf.percentile[totalDf.rango18_22 == total_recall].iloc[0]
			escalar_normal = conversionDf['puntuacion_escalar'][conversionDf.puntuacion_percentil == str(math.floor(int(percentile_normal)))].iloc[0]
			percentile_delayed = delayedDf['percentile'][delayedDf.rango18_22 == delayed_recall].iloc[0]
			escalar_delayed = conversionDf['puntuacion_escalar'][conversionDf.puntuacion_percentil == str(math.floor(int(percentile_delayed)))].iloc[0]
		elif ((edad <= 27) and (edad >= 23)):
			if total_recall <= 18:
				total_recall = 18
			if delayed_recall <= 5:
				delayed_recall = 5
			delayedDf.rango18_22 = delayedDf.rango18_22.fillna(0)
			totalDf.rango18_22 = [math.floor(x) for x in totalDf.rango18_22]
			delayedDf.rango18_22 = [math.floor(x) for x in delayedDf.rango18_22]

			percentile_normal = totalDf.percentile[totalDf.rango23_27 == total_recall].iloc[0]
			escalar_normal = conversionDf['puntuacion_escalar'][conversionDf.puntuacion_percentil == str(math.floor(int(percentile_normal)))].iloc[0]
			percentile_delayed = delayedDf['percentile'][delayedDf.rango23_27 == delayed_recall].iloc[0]
			escalar_delayed = conversionDf['puntuacion_escalar'][conversionDf.puntuacion_percentil == str(math.floor(int(percentile_delayed)))].iloc[0]
		elif ((edad <= 32) and (edad >= 28)):
			if total_recall <= 17:
				total_recall = 17
			if delayed_recall <= 5:
				delayed_recall = 5
			delayedDf.rango28_32 = delayedDf.rango28_32.fillna(0)
			totalDf.rango28_32 = [math.floor(x) for x in totalDf.rango28_32]
			delayedDf.rango28_32 = [math.floor(x) for x in delayedDf.rango28_32]

			percentile_normal = totalDf.percentile[totalDf.rango28_32 == total_recall].iloc[0]
			escalar_normal = conversionDf['puntuacion_escalar'][conversionDf.puntuacion_percentil == str(math.floor(int(percentile_normal)))].iloc[0]
			percentile_delayed = delayedDf['percentile'][delayedDf.rango28_32 == delayed_recall].iloc[0]
			escalar_delayed = conversionDf['puntuacion_escalar'][conversionDf.puntuacion_percentil == str(math.floor(int(percentile_delayed)))].iloc[0]
		elif ((edad <= 37) and (edad >= 33)):
			if total_recall <= 16:
				total_recall = 16
			if delayed_recall <= 5:
				delayed_recall = 5
			delayedDf.rango33_37 = delayedDf.rango33_37.fillna(0)
			totalDf.rango33_37 = [math.floor(x) for x in totalDf.rango33_37]
			delayedDf.rango33_37 = [math.floor(x) for x in delayedDf.rango33_37]

			percentile_normal = totalDf.percentile[totalDf.rango33_37 == total_recall].iloc[0]
			escalar_normal = conversionDf['puntuacion_escalar'][conversionDf.puntuacion_percentil == str(math.floor(int(percentile_normal)))].iloc[0]
			percentile_delayed = delayedDf['percentile'][delayedDf.rango33_37 == delayed_recall].iloc[0]
			escalar_delayed = conversionDf['puntuacion_escalar'][conversionDf.puntuacion_percentil == str(math.floor(int(percentile_delayed)))].iloc[0]
		elif ((edad <= 42) and (edad >= 38)):
			if total_recall <= 16:
				total_recall = 16
			if delayed_recall <= 4:
				delayed_recall = 4
			delayedDf.rango38_42 = delayedDf.rango38_42.fillna(0)
			totalDf.rango38_42 = [math.floor(x) for x in totalDf.rango38_42]
			delayedDf.rango38_42 = [math.floor(x) for x in delayedDf.rango38_42]

			percentile_normal = totalDf.percentile[totalDf.rango38_42 == total_recall].iloc[0]
			escalar_normal = conversionDf['puntuacion_escalar'][conversionDf.puntuacion_percentil == str(math.floor(int(percentile_normal)))].iloc[0]
			percentile_delayed = delayedDf['percentile'][delayedDf.rango38_42 == delayed_recall].iloc[0]
			escalar_delayed = conversionDf['puntuacion_escalar'][conversionDf.puntuacion_percentil == str(math.floor(int(percentile_delayed)))].iloc[0]
		elif ((edad <= 47) and (edad >= 43)):
			if total_recall <= 15:
				total_recall = 15
			if delayed_recall <= 4:
				delayed_recall = 4
			delayedDf.rango43_47 = delayedDf.rango43_47.fillna(0)
			totalDf.rango43_47 = [math.floor(x) for x in totalDf.rango43_47]
			delayedDf.rango43_47 = [math.floor(x) for x in delayedDf.rango43_47]

			percentile_normal = totalDf.percentile[totalDf.rango43_47 == total_recall].iloc[0]
			escalar_normal = conversionDf['puntuacion_escalar'][conversionDf.puntuacion_percentil == str(math.floor(int(percentile_normal)))].iloc[0]
			percentile_delayed = delayedDf['percentile'][delayedDf.rango43_47 == delayed_recall].iloc[0]
			escalar_delayed = conversionDf['puntuacion_escalar'][conversionDf.puntuacion_percentil == str(math.floor(int(percentile_delayed)))].iloc[0]
		elif ((edad <= 52) and (edad >= 48)):
			if total_recall <= 15:
				total_recall = 15
			if delayed_recall <= 4:
				delayed_recall = 4
			delayedDf.rango48_52 = delayedDf.rango48_52.fillna(0)
			totalDf.rango48_52 = [math.floor(x) for x in totalDf.rango48_52]
			delayedDf.rango48_52 = [math.floor(x) for x in delayedDf.rango48_52]

			percentile_normal = totalDf.percentile[totalDf.rango48_52 == total_recall].iloc[0]
			escalar_normal = conversionDf['puntuacion_escalar'][conversionDf.puntuacion_percentil == str(math.floor(int(percentile_normal)))].iloc[0]
			percentile_delayed = delayedDf['percentile'][delayedDf.rango48_52 == delayed_recall].iloc[0]
			escalar_delayed = conversionDf['puntuacion_escalar'][conversionDf.puntuacion_percentil == str(math.floor(int(percentile_delayed)))].iloc[0]
		elif ((edad <= 57) and (edad >= 53)):
			if total_recall <= 14:
				total_recall = 14
			if delayed_recall <= 3:
				delayed_recall = 3
			delayedDf.rango53_57 = delayedDf.rango53_57.fillna(0)
			totalDf.rango53_57 = [math.floor(x) for x in totalDf.rango53_57]
			delayedDf.rango53_57 = [math.floor(x) for x in delayedDf.rango53_57]

			percentile_normal = totalDf.percentile[totalDf.rango53_57 == total_recall].iloc[0]
			escalar_normal = conversionDf['puntuacion_escalar'][conversionDf.puntuacion_percentil == str(math.floor(int(percentile_normal)))].iloc[0]
			percentile_delayed = delayedDf['percentile'][delayedDf.rango53_57 == delayed_recall].iloc[0]
			escalar_delayed = conversionDf['puntuacion_escalar'][conversionDf.puntuacion_percentil == str(math.floor(int(percentile_delayed)))].iloc[0]
		elif ((edad <= 62) and (edad >= 58)):
			if total_recall <= 14:
				total_recall = 14
			if delayed_recall <= 3:
				delayed_recall = 3
			delayedDf.rango58_62 = delayedDf.rango58_62.fillna(0)
			totalDf.rango58_62 = [math.floor(x) for x in totalDf.rango58_62]
			delayedDf.rango58_62 = [math.floor(x) for x in delayedDf.rango58_62]

			percentile_normal = totalDf.percentile[totalDf.rango58_62 == total_recall].iloc[0]
			escalar_normal = conversionDf['puntuacion_escalar'][conversionDf.puntuacion_percentil == str(math.floor(int(percentile_normal)))].iloc[0]
			percentile_delayed = delayedDf['percentile'][delayedDf.rango58_62 == delayed_recall].iloc[0]
			escalar_delayed = conversionDf['puntuacion_escalar'][conversionDf.puntuacion_percentil == str(math.floor(int(percentile_delayed)))].iloc[0]
		elif ((edad <= 67) and (edad >= 63)):
			if total_recall <= 13:
				total_recall = 13
			if delayed_recall <= 3:
				delayed_recall = 3
			delayedDf.rango63_67 = delayedDf.rango63_67.fillna(0)
			totalDf.rango63_67 = [math.floor(x) for x in totalDf.rango63_67]
			delayedDf.rango63_67 = [math.floor(x) for x in delayedDf.rango63_67]

			percentile_normal = totalDf.percentile[totalDf.rango63_67 == total_recall].iloc[0]
			escalar_normal = conversionDf['puntuacion_escalar'][conversionDf.puntuacion_percentil == str(math.floor(int(percentile_normal)))].iloc[0]
			percentile_delayed = delayedDf['percentile'][delayedDf.rango63_67 == delayed_recall].iloc[0]
			escalar_delayed = conversionDf['puntuacion_escalar'][conversionDf.puntuacion_percentil == str(math.floor(int(percentile_delayed)))].iloc[0]
		elif ((edad <= 72) and (edad >= 68)):
			if total_recall <= 13:
				total_recall = 13
			if delayed_recall <= 3:
				delayed_recall = 3
			delayedDf.rango68_72 = delayedDf.rango68_72.fillna(0)
			totalDf.rango68_72 = [math.floor(x) for x in totalDf.rango68_72]
			delayedDf.rango68_72 = [math.floor(x) for x in delayedDf.rango68_72]

			percentile_normal = totalDf.percentile[totalDf.rango68_72 == total_recall].iloc[0]
			escalar_normal = conversionDf['puntuacion_escalar'][conversionDf.puntuacion_percentil == str(math.floor(int(percentile_normal)))].iloc[0]
			percentile_delayed = delayedDf['percentile'][delayedDf.rango68_72 == delayed_recall].iloc[0]
			escalar_delayed = conversionDf['puntuacion_escalar'][conversionDf.puntuacion_percentil == str(math.floor(int(percentile_delayed)))].iloc[0]
		elif ((edad <= 77) and (edad >= 73)):
			if total_recall <= 12:
				total_recall = 12
			if delayed_recall <= 2:
				delayed_recall = 2
			delayedDf.rango73_77 = delayedDf.rango73_77.fillna(0)
			totalDf.rango73_77 = [math.floor(x) for x in totalDf.rango73_77]
			delayedDf.rango73_77 = [math.floor(x) for x in delayedDf.rango73_77]

			percentile_normal = totalDf.percentile[totalDf.rango73_77 == total_recall].iloc[0]
			escalar_normal = conversionDf['puntuacion_escalar'][conversionDf.puntuacion_percentil == str(math.floor(int(percentile_normal)))].iloc[0]
			percentile_delayed = delayedDf['percentile'][delayedDf.rango73_77 == delayed_recall].iloc[0]
			escalar_delayed = conversionDf['puntuacion_escalar'][conversionDf.puntuacion_percentil == str(math.floor(int(percentile_delayed)))].iloc[0]
		else:
			if total_recall <= 11:
				total_recall = 11
			if delayed_recall <= 2:
				delayed_recall = 2
			delayedDf.rango78_ = delayedDf.rango78_.fillna(0)
			totalDf.rango78_ = [math.floor(x) for x in totalDf.rango78_]
			delayedDf.rango78_ = [math.floor(x) for x in delayedDf.rango78_]

			percentile_normal = totalDf.percentile[totalDf.rango78_ == total_recall].iloc[0]
			escalar_normal = conversionDf['puntuacion_escalar'][conversionDf.puntuacion_percentil == str(math.floor(int(percentile_normal)))].iloc[0]
			percentile_delayed = delayedDf['percentile'][delayedDf.rango78_ == delayed_recall].iloc[0]
			escalar_delayed = conversionDf['puntuacion_escalar'][conversionDf.puntuacion_percentil == str(math.floor(int(percentile_delayed)))].iloc[0]

		self.puntuacionEscalar = (escalar_normal, escalar_delayed)
		self.rangoPercentil = (percentile_normal, percentile_delayed)
