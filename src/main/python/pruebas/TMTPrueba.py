#Prueba de TMT
import pandas as pd
import PruebaModel
from AppCtxt import APPCTXT

class TMTPrueba(PruebaModel.PruebaModel):	
	def __init__(self, valores):
		nombre = "TMT"
		baremos = (pd.read_csv(APPCTXT().get_resource('./Baremos/TablaTMT.csv')),
					pd.read_csv(APPCTXT().get_resource('./Baremos/EscolaridadTMTA.csv')),
					pd.read_csv(APPCTXT().get_resource('./Baremos/EscolaridadTMTB.csv')),
					pd.read_csv(APPCTXT().get_resource('./Baremos/Baremo_TMT_50-56.csv')),
					pd.read_csv(APPCTXT().get_resource('./Baremos/Baremo_TMT_57-59.csv')),
					pd.read_csv(APPCTXT().get_resource('./Baremos/Baremo_TMT_60-62.csv')),
					pd.read_csv(APPCTXT().get_resource('./Baremos/Baremo_TMT_63-65.csv')),
					pd.read_csv(APPCTXT().get_resource('./Baremos/Baremo_TMT_66-68.csv')),
					pd.read_csv(APPCTXT().get_resource('./Baremos/Baremo_TMT_69-71.csv')),
					pd.read_csv(APPCTXT().get_resource('./Baremos/Baremo_TMT_72-74.csv')),
					pd.read_csv(APPCTXT().get_resource('./Baremos/Baremo_TMT_75-77.csv')),
					pd.read_csv(APPCTXT().get_resource('./Baremos/Baremo_TMT_78-80.csv')),
					pd.read_csv(APPCTXT().get_resource('./Baremos/Baremo_TMT_81-90.csv')),
					pd.read_csv(APPCTXT().get_resource('./Baremos/Escolaridad_TMT_pa.csv')),
					pd.read_csv(APPCTXT().get_resource('./Baremos/Escolaridad_TMT_pb.csv')))
		campos = ("A", "B")

		super(TMTPrueba,self).__init__(nombre, valores, baremos, campos)

	def calcularPERP(self, datos):
		"""
	 	 Método que es empleado para calcular la Puntuación Escalar(PE), como la Percentil(RP)
	 	 Args:
	 	  datos: Lista de información relevante del reporte para calcular los valores de PE y RP (escolaridad, edad)
		"""
		tablaTMT = self.baremos[0]
		tablaEscolaridadTMTA = self.baremos[1]
		tablaEscolaridadTMTB = self.baremos[2]
		edades = list()
		educa = list()
		ins = 3
		for x in range(3,13):
			edades.append(self.baremos[x])
		for x in range(13,15):
			educa.append(self.baremos[x])

		tmtA = self.valores[0]
		tmtB = self.valores[1]
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
			print(edades[ran][cols[1]])
			print(((edades[ran][cols[param]] <= tmtA) & (tmtA <= edades[ran][cols[param+1]])|((edades[ran][cols[param+1]] <= tmtA) & (tmtA <= edades[ran][cols[param]]))))
			puntuacionPercentilA = int(edades[ran][cols[1]][((edades[ran][cols[param]] <= tmtA) & (tmtA <= edades[ran][cols[param+1]])|((edades[ran][cols[param+1]] <= tmtA) & (tmtA <= edades[ran][cols[param]])))].iloc[0])
			puntuacionEscalarA = int(edades[ran][cols[0]][((edades[ran][cols[param]] <= tmtA) & (tmtA <= edades[ran][cols[param+1]])|((edades[ran][cols[param+1]] <= tmtA) & (tmtA <= edades[ran][cols[param]])))].iloc[0])

			param += 2
			puntuacionPercentilB =  int(edades[ran][cols[1]][((edades[ran][cols[param]] <= tmtB) & (tmtB <= edades[ran][cols[param+1]])|((edades[ran][cols[param+1]] <= tmtB) & (tmtB <= edades[ran][cols[param]])))].iloc[0])
			puntuacionEscalarB = int(edades[ran][cols[0]][((edades[ran][cols[param]] <= tmtB) & (tmtB <= edades[ran][cols[param+1]])|((edades[ran][cols[param+1]] <= tmtB) & (tmtB <= edades[ran][cols[param]])))].iloc[0])

			NSSa = puntuacionEscalarA
			puntuacionEscalarA = educa[0][str(escolaridad)][educa[0].NSSa == NSSa].iloc[0]
			NSSa = puntuacionEscalarB
			puntuacionEscalarB = educa[1][str(escolaridad)][educa[1].NSSa == NSSa].iloc[0]


		else:

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
			
			if puntuacionEscalarA < 2:
				puntuacionEscalarA = 2
			elif puntuacionEscalarA > 18:
				puntuacionEscalarA = 18

			tempA = tablaTMT[tablaTMT['PuntuacionEscalar'] == puntuacionEscalarA].iloc[0]
			puntuacionPercentilA = (tempA['RangoDePercentilMin'], tempA['RangoDePercentilMax'])


			ajustesTMTB = tablaEscolaridadTMTB[tablaEscolaridadTMTB['Escolaridad'] == escolaridad].iloc[0]
			temp = tablaTMT[tablaTMT['TMTBMIN'] <= tmtB].iloc[0]
			puntuacionEscalarB = temp['PuntuacionEscalar'] + ajustesTMTB['TMTB']
			
			if puntuacionEscalarB < 2:
				puntuacionEscalarB = 2
			elif puntuacionEscalarB > 18:
				puntuacionEscalarB = 18


			temp = tablaTMT[tablaTMT['PuntuacionEscalar'] == puntuacionEscalarB].iloc[0]
			puntuacionPercentilB = (temp['RangoDePercentilMin'], temp['RangoDePercentilMax'])

		
		self.puntuacionEscalar = (puntuacionEscalarA, puntuacionEscalarB)
		self.rangoPercentil = (puntuacionPercentilA, puntuacionPercentilB)