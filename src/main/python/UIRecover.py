from PyQt5 import QtCore, QtGui, QtDesigner, QtWidgets

#import the widget you want to recover
from vistas.TMTWindowWidget import TMTWindowWidget

def dump_ui(widget, path):
    builder = QtDesigner.QFormBuilder()
    stream = QtCore.QFile(path)
    stream.open(QtCore.QIODevice.WriteOnly)
    builder.save(stream, widget)
    stream.close()

app = QtWidgets.QApplication([''])

dialog = QtWidgets.QDialog()

## instnatice your widget
TMTWindowWidget(dialog)

dialog.show()

dump_ui(dialog, 'ui/myui2.ui')