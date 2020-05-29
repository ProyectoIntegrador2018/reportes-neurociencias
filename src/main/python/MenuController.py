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
						'Prueba Comprensión Verbal', 
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
						'Prueba Motivos Deportivos',
						'Prueba de Pittsburgh', 
						'Reporte' ]

		self.pagesVisited = pagesVisited
		self.qListItems = QtWidgets.QListWidget(self)
		self.qListItems.addItems(self.entries)
		self.listView = QtWidgets.QListWidget(self)
		self.listView.setSelectionRectVisible(True)
					
		self.currentWindow = 0
	
	def styleEnabled(self, listItem):
		pass

	def poblarLista(self):
		"""
		 Método encargado de llenar la lista con los elementos especificados en el atributo entries.
		"""
		chooseCSS = None
		bckColor = None
		fontColor = None
		model = self.qListItems

		flag_select = QtCore.Qt.ItemIsSelectable
		flag_disable = QtCore.Qt.NoItemFlags
		flag_enable = QtCore.Qt.ItemIsEnabled

		for index in range(model.count()):
			item = model.item(index)
			
			if (index not in self.pagesVisited):
				item.setFlags(flag_disable)
				chooseCSS = 0
			else:
				if index == self.currentWindow:
					item.setFlags(flag_enable)
					chooseCSS = 1
				else:
					item.setFlags(flag_enable)
					chooseCSS = 2
			
			tempItem = QtWidgets.QListWidgetItem(item)
			#Cuando el elemento está disabled
			if chooseCSS == 0:
				bckColor = QtGui.QColor("#585858")
				fontColor = QtGui.QColor("#FFFFFF")
			#Cuando el elemento es el que se está mostrando
			elif chooseCSS == 1:
				bckColor = QtGui.QColor("#f28b00")
				fontColor = QtGui.QColor("#000000")
			#Cuando el elemento está enabled pero no está actualmente mostrándose
			else:
				bckColor = QtGui.QColor("#FFFFFF")
				fontColor = QtGui.QColor("#000000")
			tempItem.setBackground(bckColor)
			tempItem.setForeground(fontColor)

			self.listView.addItem(tempItem)

	def updateCurrentWindow(self, currentWindow):
		"""
		 Método empleado para actualizar la ventana actual en la que se encuentra la ListView de las pruebas
		 Args:
		  currentWindow: Vista de qt actualmente desplegada.
		"""
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