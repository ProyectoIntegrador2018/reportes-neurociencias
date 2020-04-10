# Modelo del Reporte a generar
class ReporteModel:
	class __ReporteModel:
		def __init__(self, nombreExaminado, identificador, fecha, genero, edad, fechaNacimiento, lateralidad, nombreExaminador, carrera, semestre, educacion, equipo):
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
			addPrueba(prueba)

	def addPrueba(self, prueba):
		"""
		 Adjunta la prueba especificada a la lista de resultados del Reporte
		 Args:
		  prueba: Elemento de la Clase Prueba
		"""
		tempReporte = self.instance.reporte["resultados"]
		if (len(tempReporte) == 0):
			self.instance.reporte["resultados"] = [prueba]
		else:
			tempReporte = tempReporte.append(prueba)
			self.instance.reporte["resultados"] = tempReporte

	def printReporte(self):
		"""
		 Despliega el contenido del reporte
		"""
		print("nombreExaminado: " + self.instance.reporte["nombreExaminado"])
		print("id: " + self.instance.reporte["id"])
		print("fecha: " + self.instance.reporte["fecha"])
		print("genero: " + self.instance.reporte["genero"])
		print("edad: " + str(self.instance.reporte["edad"]))
		print("fechaNacimiento: " + self.instance.reporte["fechaNacimiento"])
		print("lateralidad: " + self.instance.reporte["lateralidad"])
		print("nombreExaminador: " + self.instance.reporte["nombreExaminador"])
		print("carrera: " + self.instance.reporte["carrera"])
		print("semestre: " + str(self.instance.reporte["semestre"]))
		print("educacion: " + str(self.instance.reporte["educacion"]))
		print("equipo: " + self.instance.reporte["equipo"])
		for prueba in self.instance.reporte["resultados"]:
			prueba.printInfo()