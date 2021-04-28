# Controlador del Menu De Pantallas Disponibles
from PyQt5 import QtCore, QtWidgets, QtGui


class MenuController(QtWidgets.QWidget):
    # Atributo empleado para realizar el cambio de vista
    switch_window = QtCore.pyqtSignal(str)

    def __init__(self, pagesVisited, entriesList):
        QtWidgets.QWidget.__init__(self)
        # self.entries = ['Información de Sujeto',
        #                 'Prueba Fluidez Verbal',
        #                 'Prueba Denominación',
        #                 'Prueba Comprensión Verbal',
        #                 'Prueba Memoria Visoespacial',
        #                 'Prueba TMT',
        #                 'Prueba Abstracción',
        #                 'Prueba Dígitos',
        #                 'Prueba SDMT',
        #                 'Prueba LNS',
        #                 'Prueba D2',
        #                 'Prueba Hopkins',
        #                 'Prueba Stroop',
        #                 'Prueba Torre de Londres',
        #                 'Prueba Motivos Deportivos',
        #                 'Prueba de Pittsburgh',
        #                 'Prueba SCL-90',
        #                 'Prueba BSI-18',
        #                 'Reporte']

        self.pagesVisited = pagesVisited
        self.entriesList = entriesList
        self.qListItems = QtWidgets.QListWidget(self)
        self.qListItems.addItems(entriesList)
        self.listView = QtWidgets.QListWidget(self)
        self.listView.setSelectionRectVisible(True)

        self.currentWindow = pagesVisited[0]

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

        flag_disable = QtCore.Qt.NoItemFlags
        flag_enable = QtCore.Qt.ItemIsEnabled

        for index in range(model.count()):
            item = model.item(index)

            if index > len(self.pagesVisited)-1:
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
            # Cuando el elemento está disabled
            if chooseCSS == 0:
                bckColor = QtGui.QColor("#585858")
                fontColor = QtGui.QColor("#FFFFFF")
            # Cuando el elemento es el que se está mostrando
            elif chooseCSS == 1:
                bckColor = QtGui.QColor("#f28b00")
                fontColor = QtGui.QColor("#000000")
            # Cuando el elemento está enabled pero no está actualmente mostrándose
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
        if "seleccionarPruebas" in pagesVisited and \
            "informacionSujeto" in  pagesVisited:
            pagesVisited.remove("seleccionarPruebas")
        self.pagesVisited = pagesVisited

    def updateListView(self, listView):
        """
         Método encargado de reasignar el valor de listView de la clase
          Args:
          listView: Argunmento que contiene el identificador del menú en la vista actual 
        """
        self.listView = listView
        self.listView.itemClicked.connect(self.selectionChanged)

    def selectionChanged(self, item):
        """
         Método el cuál es llamado cuando se selecciona algún elemento de la lista
        """
        if int(item.flags()) == QtCore.Qt.NoItemFlags:
            return

        selectedIdx = self.listView.currentRow()
        if selectedIdx < 0 or selectedIdx > len(self.pagesVisited):
            # early skip becasuse -1 and out of len of current possible pages
            return

        if selectedIdx == self.currentWindow:
            return


        nextRoute = self.pagesVisited[selectedIdx]
        self.switch_window.emit(nextRoute)

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
