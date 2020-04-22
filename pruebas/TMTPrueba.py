#Prueba de TMT
import pandas as pd
import PruebaModel

class TMTPrueba(PruebaModel.PruebaModel):	
	def __init__(self, valores):
		nombre = "TMT"
		baremos = (pd.read_csv('./Baremos/TablaTMT.csv'), pd.read_csv('./Baremos/EscolaridadTMTA.csv'), pd.read_csv('./Baremos/EscolaridadTMTB.csv'))
		campos = ("TMT A", "TMT B")

		super(TMTPrueba,self).__init__(nombre, valores, baremos, campos)

	def calcularPERP(self, datos):
		"""
	 	 Método que es empleado para calcular la Puntuación Escalar(PE), como la Percentil(RP)
	 	 Args:
	 	  datos: Lista de información relevante del reporte para calcular los valores de PE y RP (escolaridad, edad)
		"""
		tablaTMT = self.baremos[0]
		tablaEscolaridadTMTA = self.baremos[1]
		tablaEscolaridadTMTB = self.baremos[1]

		tmtA = self.valores[0]
		tmtB = self.valores[1]
		escolaridad = datos[0]
		edad = datos[1]

		if escolaridad < 8:
			escolaridad = 8
		elif escolaridad > 20:
			escolaridad = 20

		if edad < 18:
			edad = 18
		elif edad > 49:
			edad = 49

		ajustesTMTA = tablaEscolaridadTMTA[['Escolaridad', str(edad)]]
		ajustesTMTA = ajustesTMTA[ajustesTMTA['Escolaridad'] == escolaridad][str(edad)].iloc[0]

		tempA = tablaTMT[tablaTMT['TMTAMIN'] <= tmtA].iloc[0]
		puntuacionEscalarA = tempA['PuntuacionEscalar'] + ajustesTMTA
		tempA = tablaTMT[tablaTMT['PuntuacionEscalar'] == puntuacionEscalarA].iloc[0]
		puntuacionPercentilA = (tempA['RangoDePercentilMin'], tempA['RangoDePercentilMax'])


		ajustesTMTB = tablaEscolaridadTMTB[tablaEscolaridadTMTB['Escolaridad']==escolaridad].iloc[0]

		temp = tablaTMT[tablaTMT['TMTBMIN'] <= tmtB].iloc[0]
		puntuacionEscalarB = temp['PuntuacionEscalar'] + ajustesTMTB
		temp = tablaTMT[tablaTMT['PuntuacionEscalar'] == puntuacionEscalarB].iloc[0]
		puntuacionPercentilB = (temp['RangoDePercentilMin'], temp['RangoDePercentilMax'])

		
		self.puntuacionEscalar = (puntuacionEscalarA, puntuacionEscalarB)
		self.rangoPercentil = (puntuacionPercentilA, puntuacionPercentilB)