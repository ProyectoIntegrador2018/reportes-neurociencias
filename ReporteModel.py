# Modelo del Reporte a generar
class ReporteModel:
	def __init__(self, nombreExaminado, identificador, fecha, genero, edad, fechaNacimiento, lateralidad, nombreExaminador, carrera, semestre, educacion, equipo, prueba = None):
		self.reporte = { 
			"nombreExaminado" : nombreExaminado,
			"id" : identificador,
			"fecha" : fecha,
			"genero" : genero,
			"edad" : edad,
			"fechaNacimiento" : fechaNacimiento,
			"lateralidad" : lateralidad,
			"nombreExaminador" : nombreExaminador,
			"carrera" : carrera,
			"semestre" : semestre,
			"educacion" : educacion,
			"equipo" : equipo,
			"resultados" : list()
			}
	instance = None
	
	def __init__(self, nombreExaminado, identificador, fecha, genero, edad, fechaNacimiento, lateralidad, nombreExaminador, carrera, semestre, educacion, equipo, prueba = None):
		if not ReporteModel.instance:
			ReporteModel.instance = ReporteModel.__ReporteModel(nombreExaminado, identificador, fecha, genero, edad, fechaNacimiento, lateralidad, nombreExaminador, carrera, semestre, educacion, equipo)
		else:
			self.addPrueba(prueba)

	def addPrueba(self, prueba):
		"""
		 Adjunta la prueba especificada a la lista de resultados del Reporte
		 Args:
		  prueba: Elemento de la Clase Prueba
		"""
		tempReporte = self.reporte["resultados"]
		tempReporte[prueba.nombre] = prueba
		self.reporte["resultados"] = tempReporte

	def printReporte(self):
		"""
		 Despliega el contenido del reporte
		"""
		print("nombreExaminado: " + self.reporte["nombreExaminado"])
		print("id: " + self.reporte["id"])
		print("fecha: " + self.reporte["fecha"])
		print("genero: " + self.reporte["genero"])
		print("edad: " + str(self.reporte["edad"]))
		print("fechaNacimiento: " + self.reporte["fechaNacimiento"])
		print("lateralidad: " + self.reporte["lateralidad"])
		print("nombreExaminador: " + self.reporte["nombreExaminador"])
		print("carrera: " + self.reporte["carrera"])
		print("semestre: " + str(self.reporte["semestre"]))
		print("educacion: " + str(self.reporte["educacion"]))
		print("equipo: " + self.reporte["equipo"])
		for nombre, prueba in self.reporte["resultados"].items():
			prueba.printInfo()