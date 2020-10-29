#Prueba de Motivos Deportivos de Butt
import pandas as pd
import PruebaModel

class ButtPrueba(PruebaModel.PruebaModel):	
	def __init__(self, valores):
		nombre = "Motivos Deportivos de Butt"
		baremos = [] #en esta prueba no se utilizan baremos
		campos = ("CONFLICTO", "RIVALIDAD", "SUFICIENCIA", "COOPERACION", "AGRESIVIDAD", "TOTAL") #el total se calcula en este script

		super(ButtPrueba,self).__init__(nombre, valores, baremos, campos)

	def calcularPERP(self):
		"""
	 	 Método que es empleado para calcular el valor total de la prueba de Motivos de Butt y otorgar una interpretacion
	 	 Args:
	 	  para esta prueba no se necesitan datos del reporte, solo los valores de los campos ingresados por el usuario
		"""
		conflicto = self.valores[0]
		rivalidad = self.valores[1]
		suficiencia = self.valores[2]
		cooperacion = self.valores[3]
		agresividad =  self.valores[4]

		if conflicto >= 2:
			sConflicto = 'Conflicto'
		else:
			sConflicto = 'Sin conflicto'

		if rivalidad >= 3 or suficiencia >= 3 or agresividad >= 3:
			sRivalidad = 'Le falta motivación'
			sSuficiencia = 'Insuficiente'
			sAgresividad = 'Sin fuerza'
		else:
			sRivalidad = 'Está motivado'
			sSuficiencia = 'Suficiente'
			sAgresividad = 'Con fuerza'
			

		if cooperacion >= 4:
			sCooperacion = 'Cooperativo'
		else:
			sCooperacion = 'No cooperativo'

		total = (rivalidad + suficiencia + cooperacion + agresividad) - conflicto

		tempValores = self.valores
		self.valores = (tempValores[0], tempValores[1], tempValores[2], tempValores[3], tempValores[4], total)

		if total <= 11:
			sTotal = 'Baja motivación'
		if total >= 12 and total <= 14:
			sTotal = 'Media motivación'
		if total >= 15:
			sTotal = 'Alta motivación'

		self.puntuacionEscalar = (conflicto, rivalidad, suficiencia, cooperacion, agresividad, total)
		self.rangoPercentil = (sConflicto, sRivalidad, sSuficiencia, sCooperacion, sAgresividad, sTotal)