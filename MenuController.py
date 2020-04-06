#Controlador del Menu De Pantallas Disponibles
class MenuController(object):
	def __init__(self, listView):
		self.listView = listView
		self.entries = ['Información de Sujeto', 'Prueba Fluidez Verbal']
	
	def poblarLista(self):
		"""
		 Método encargado de llenar la lista con los elementos especificados en eñ atributo entries.
		"""
		self.listView.addItems(self.entries)
	
