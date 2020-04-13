#Controlador de la vista ModalWindow
from ModalWindow import *

class ModalController(QtWidgets.QWidget):
	def __init__(self):
		self.modalWindow = ModalWindow()
		
	def setContenido(self, displayText):
		"""
		 Método empleado para modificar el contenido del mensaje a desplegar.
		 Args:
		  displayText: Contenido del mensaje.
		"""
		tempText = ""
		if type(displayText) == type(list()):
			for elem in displayText:
				tempText = tempText + elem + '\n'	
		self.modalWindow.setInformativeText(tempText)

	def setWindowTitle(self, title):
		"""
		 Método empleado para asignar el valor del Título de la ventana en la que se despliega el mensaje.
		 Args: 
		  title: Título de la pantalla.
		"""
		self.modalWindow.setWindowTitle(title)

	def setHeader(self, header):
		"""
		 Método empleado para asignar el valor al encabezado de la ventana en la que se despliega el mensaje.
		 Args: 
		  header: Encabezado del mensaje. 
		"""
		self.modalWindow.setText(header)

	def showModal(self):
		"""
		 Método empleado para desplegar el mensaje y que este deba de ser cerrado antes de proseguir con la ejecución del programa.
		"""
		self.modalWindow.exec_()
