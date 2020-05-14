#Controlador del Menu De Pantallas Disponibles
from PyQt5 import QtCore, QtWidgets, QtGui

class MenuController(QtWidgets.QWidget):
	#Atributo empleado para realizar el cambio de vista
	switch_window = QtCore.pyqtSignal(int)

	def __init__(self, pagesVisited):
		QtWidgets.QWidget.__init__(self)
		self.entries = ['Información de Sujeto', 
						'Prueba Fluidez Verbal', 
						'Prueba Denominación', 
						'Prueba Material Verbal Complejo', 
						'Prueba Memoria Visoespacial',
						'Prueba TMT',
						'Prueba Abstracción',
						'Prueba Dígitos',
						'Prueba SDMT',
						'Prueba LNS', 
						'Prueba D2',
						'Prueba Hopkins',
						'Prueba Stroop',
						'Prueba SCL-90',
						'Prueba Torre de Londres',
						'Reporte']


		self.pagesVisited = pagesVisited
		self.qListItems = QtWidgets.QListWidget(self)
		self.qListItems.addItems(self.entries)
		self.listView = QtWidgets.QListWidget(self)
		self.currentWindow = 0
		
	def poblarLista(self):
		"""
		 Método encargado de llenar la lista con los elementos especificados en el atributo entries.
		"""
		model = self.qListItems
		for index in range(model.count()):
			item = model.item(index)
			
			if (index not in self.pagesVisited):
				item.setFlags(QtCore.Qt.NoItemFlags)
			else:
				item.setFlags(QtCore.Qt.ItemIsEnabled)

			
			if index == self.currentWindow:
				item.setBackground(QtGui.QColor('#85C1E9'))
			else:
				item.setBackground(QtGui.QColor('#dcd7d1'))
			tempItem = QtWidgets.QListWidgetItem(item)
			self.listView.addItem(tempItem)
		
	def updateCurrentWindow(self, currentWindow):
		self.currentWindow = currentWindow

	def updatePagesVisited(self, pagesVisited):
		"""
		 Método que actualiza la lista de páginas que han sido visitadas
		 Args:
		  pagesVisited: Lista de enteros que representan las páginas ya visitadas. 
		"""
		self.pagesVisited = pagesVisited

	def updateListView(self, listView):
		"""
		 Método encargado de reasignar el valor de listView de la clase
		  Args:
		  listView: Argunmento que contiene el identificador del menú en la vista actual 
		"""
		self.listView = listView
		self.listView.itemActivated.connect(self.selectionChanged)

	def selectionChanged(self):
		"""
		 Método el cuál es llamado cuando se selecciona algún elemento de la lista
		"""
		self.switch_window.emit(self.listView.currentRow())

	def clearMenu(self):
		"""
		 Método que se encarga de vaciar el contenido del menú
		"""
		self.listView.clear()

	def resetPagesVisited(self, pagesVisited):
		"""
		 Método que se encarga de restablecer el contenido de la variable Pages Visited
		 Args:
		  pagesVisited: Lista que contiene las páginas ya visitadas
		"""
		self.pagesVisited = pagesVisited