#Controlador del Menu De Pantallas Disponibles
class MenuController(object):
	def __init__(self, listView):
		self.updateListView(listView)
		self.entries = ['Información de Sujeto', 'Prueba Fluidez Verbal']
		self.poblarLista()
	
	def poblarLista(self):
		"""
		 Método encargado de llenar la lista con los elementos especificados en el atributo entries.
		"""
		self.listView.addItems(self.entries)

	def updateListView(self, listView):
		"""
		 Método encargado de reasignar el valor de listView de la clase
		  Args:
		  listView: Argunmento que contiene el identificador del menú en la vista actual 
		"""
		self.listView = listView
