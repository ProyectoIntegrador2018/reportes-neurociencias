# Modelo de Prueba
class PruebaModel:
	def __init__(self, nombre, valores, baremos, puntuacionEscalar=0, rangoPercentil=0):
		self.nombre = nombre
		self.valores = valores
		self.puntuacionEscalar = puntuacionEscalar
		self.rangoPercentil = rangoPercentil
		self.baremos = baremos
		#self.campos = campos AGREGAR LISTA DE NOMBRES DE CAMPOS SIGUIENTE SPRINT

	def printInfo(self):
		"""
		 Método que se encarga de imprimir el contenido de la prueba.
		"""
		print("Info de Prueba")
		print("Nombre: " + self.nombre)
		print("puntuacionEscalar: " + str(self.puntuacionEscalar))
		print("rangoPercentil: " + str(self.rangoPercentil))

	def calcularPERP(self, datos=None):
		"""
		 Método virtual que tiene que ser detallado por los hijos de PruebaModel, 
		 se encarga de calcular la Puntuación Escalar y la Puntuación Percentil.
		"""
		pass