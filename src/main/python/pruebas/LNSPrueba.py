#Prueba de LNS
import pandas as pd
import PruebaModel
from AppCtxt import APPCTXT

class LNSPrueba(PruebaModel.PruebaModel):	
	def __init__(self, valores):
		nombre = "LNS"
		baremos = (pd.read_csv(APPCTXT().get_resource('./Baremos/TablaLNS.csv')),
					pd.read_csv(APPCTXT().get_resource('./Baremos/EscolaridadLNS.csv')),
					pd.read_csv(APPCTXT().get_resource('./Baremos/Baremo_LNS_50-56.csv')),
					pd.read_csv(APPCTXT().get_resource('./Baremos/Baremo_LNS_57-59.csv')),
					pd.read_csv(APPCTXT().get_resource('./Baremos/Baremo_LNS_60-62.csv')),
					pd.read_csv(APPCTXT().get_resource('./Baremos/Baremo_LNS_63-65.csv')),
					pd.read_csv(APPCTXT().get_resource('./Baremos/Baremo_LNS_66-68.csv')),
					pd.read_csv(APPCTXT().get_resource('./Baremos/Baremo_LNS_69-71.csv')),
					pd.read_csv(APPCTXT().get_resource('./Baremos/Baremo_LNS_72-74.csv')),
					pd.read_csv(APPCTXT().get_resource('./Baremos/Baremo_LNS_75-77.csv')),
					pd.read_csv(APPCTXT().get_resource('./Baremos/Baremo_LNS_78-80.csv')),
					pd.read_csv(APPCTXT().get_resource('./Baremos/Baremo_LNS_81-90.csv')),
					pd.read_csv(APPCTXT().get_resource('./Baremos/Escolaridad_LNS_li.csv')),
					pd.read_csv(APPCTXT().get_resource('./Baremos/Escolaridad_LNS_rs.csv')))
		campos = ("I", "T")

		super(LNSPrueba,self).__init__(nombre, valores, baremos, campos)

	def calcularPERP(self, datos):
		"""
	 	 Método que es empleado para calcular la Puntuación Escalar(PE), como la Percentil(RP)
	 	 Args:
	 	  datos: Lista de información relevante del reporte para calcular los valores de PE y RP (escolaridad, edad)
		"""
		tablaLNS = self.baremos[0]
		tablaEscolaridadLNS = self.baremos[1]

		edades = list()
		educa = list()
		ins = 3
		for x in range(2,12):
			edades.append(self.baremos[x])
		educa.append(self.baremos[12])
		educa.append(self.baremos[13])

		span = self.valores[0]
		total = self.valores[1]
		escolaridad = datos[0]
		edad = datos[1]

		if edad >= 50:
			if 50 <= edad <= 56:
				ran = 0
			elif 57 <= edad <= 59:
				ran = 1
			elif 60 <= edad <= 62:
				ran = 2
			elif 63 <= edad <= 65:
				ran = 3
			elif 66 <= edad <= 68:
				ran = 4
			elif 69 <= edad <= 71:
				ran = 5
			elif 72 <= edad <= 74:
				ran = 6
			elif 75 <= edad <= 77:
				ran = 7
			elif 78 <= edad <= 80:
				ran = 8
			elif 81 <= edad <= 90:
				ran = 9
			cols = edades[ran].columns.values
			#print(edades[ran]['Percentil Min'][(edades[ran]['Pmin'] <= P) & (P <= edades[ran]['Pmax'])].iloc[0])
			param = 3
			#print(edades[ran][cols[1]])
			#print(((edades[ran][cols[param]] <= sdmtVal ) & (sdmtVal  <= edades[ran][cols[param+1]])|((edades[ran][cols[param+1]] <= sdmtVal ) & (sdmtVal  <= edades[ran][cols[param]]))))
			valores = edades[ran][((edades[ran][cols[param]] <= total) & (total <= edades[ran][cols[param+1]])|((edades[ran][cols[param+1]] <= total ) & (total  <= edades[ran][cols[param]])))]
			puntuacionPercentilTotal = (int(valores[cols[1]].iloc[0]),int(valores[cols[2]].iloc[0]))
			puntuacionEscalarTotal = int(valores[cols[0]].iloc[0])

			NSSa = puntuacionEscalarTotal
			puntuacionEscalarTotal = educa[0][str(escolaridad)][educa[0].NSSa == NSSa].iloc[0]
			
			param += 2
			valores = edades[ran][((edades[ran][cols[param]] <= span) & (span <= edades[ran][cols[param+1]])|((edades[ran][cols[param+1]] <= span ) & (span  <= edades[ran][cols[param]])))]
			puntuacionPercentilSpan = (int(valores[cols[1]].iloc[0]),int(valores[cols[2]].iloc[0]))
			puntuacionEscalarSpan = int(valores[cols[0]].iloc[0])

			NSSa = puntuacionEscalarSpan
			puntuacionEscalarSpan = educa[1][str(escolaridad)][educa[1].NSSa == NSSa].iloc[0]
			

		else:

			'''
			La escolaridad tiene que estar forzada a un rango de 8 a 20 años
			'''
			if escolaridad < 8:
				escolaridad = 8
			elif escolaridad > 20:
				escolaridad = 20

			ajuste = tablaEscolaridadLNS[tablaEscolaridadLNS['Escolaridad'] == escolaridad].iloc[0]

			auxSpan = tablaLNS[tablaLNS['Span'] == span].iloc[0]
			puntuacionEscalarSpan = auxSpan['Escalar'] + ajuste['LNSspan']

			'''
			Se asegura que despues del ajuste por escolaridad, la puntuación exista y pasarse a percentil
			'''
			if puntuacionEscalarSpan < 2:
				puntuacionEscalarSpan = 2
			elif puntuacionEscalarSpan > 18:
				puntuacionEscalarSpan = 18

			auxSpan = tablaLNS[tablaLNS['Escalar'] == puntuacionEscalarSpan].iloc[0]
			puntuacionPercentilSpan = (auxSpan['PercentilMin'], auxSpan['PercentilMax'])


			auxTotal = tablaLNS[(total >= tablaLNS['TotalMin']) & (tablaLNS['TotalMax'] >= total)].iloc[0]
			puntuacionEscalarTotal = auxTotal['Escalar'] + ajuste['LNStotal']

			if puntuacionEscalarTotal < 2:
				puntuacionEscalarTotal = 2
			elif puntuacionEscalarTotal > 18:
				puntuacionEscalarTotal = 18

			auxTotal = tablaLNS[tablaLNS['Escalar'] == puntuacionEscalarTotal].iloc[0]
			puntuacionPercentilTotal = (auxTotal['PercentilMin'], auxTotal['PercentilMax'])

		self.puntuacionEscalar = (puntuacionEscalarSpan, puntuacionEscalarTotal)
		self.rangoPercentil = (puntuacionPercentilSpan, puntuacionPercentilTotal)
