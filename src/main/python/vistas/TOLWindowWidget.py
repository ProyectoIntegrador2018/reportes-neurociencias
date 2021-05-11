#Vista de la prueba de Torre de Londres
from PyQt5 import QtCore, QtGui, QtWidgets
from AppCtxt import APPCTXT
from .mixins import WindowWidgetMixin

class TOLWindowWidget(WindowWidgetMixin):
    def setupUi(self, Form):
        """
         Método empleado para especificar el contenido de la Interfáz gráfica, es generado por pyuic5.
         Args:
          Form: Ventana en la que se deplegará la interfáz gráfica (es un tipo de dato QtWidget.QWidget) 
        """
        super().setupUI(Form)
        
        self.label_4 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_4.setToolTip("")
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_2.addWidget(self.label_4)

        self.label_8 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_8.setObjectName("label_8")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_8)
        self.sbTotalCorrectos = QtWidgets.QSpinBox(self.verticalLayoutWidget)
        self.sbTotalCorrectos.setObjectName("sbTotalCorrectos")
        self.sbTotalCorrectos.setRange(0,10)
        self.sbTotalCorrectos.setSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Fixed)
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.sbTotalCorrectos)

        self.label_9 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_9.setObjectName("label_9")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_9)
        self.sbMovimientosTotales = QtWidgets.QSpinBox(self.verticalLayoutWidget)
        self.sbMovimientosTotales.setObjectName("sbMovimientosTotales")
        self.sbMovimientosTotales.setRange(0,1000)
        self.sbMovimientosTotales.setSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Fixed)
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.sbMovimientosTotales)

        self.label_10 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_10.setObjectName("label_10")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_10)
        self.sbTiempoLatencia = QtWidgets.QSpinBox(self.verticalLayoutWidget)
        self.sbTiempoLatencia.setObjectName("sbTiempoLatencia")
        self.sbTiempoLatencia.setRange(0,1000)
        self.sbTiempoLatencia.setSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Fixed)
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.sbTiempoLatencia)

        self.label_11 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_11.setObjectName("label_11")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_11)
        self.sbTiempoEjecucion = QtWidgets.QSpinBox(self.verticalLayoutWidget)
        self.sbTiempoEjecucion.setObjectName("sbTiempoEjecucion")
        self.sbTiempoEjecucion.setRange(0,1000)
        self.sbTiempoEjecucion.setSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Fixed)
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.sbTiempoEjecucion)

        self.label_12 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_12.setObjectName("label_12")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.label_12)
        self.sbTiempoResolucion = QtWidgets.QSpinBox(self.verticalLayoutWidget)
        self.sbTiempoResolucion.setObjectName("sbTiempoResolucion")
        self.sbTiempoResolucion.setRange(0,1000)
        self.sbTiempoResolucion.setSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Fixed)
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.sbTiempoResolucion)

        self.label_13 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_13.setObjectName("label_13")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.label_13)
        self.sbVT = QtWidgets.QSpinBox(self.verticalLayoutWidget)
        self.sbVT.setObjectName("sbVT")
        self.sbVT.setRange(0,100)
        self.sbVT.setSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Fixed)
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.sbVT)

        self.label_14 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_14.setObjectName("label_14")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.LabelRole, self.label_14)
        self.sbVR = QtWidgets.QSpinBox(self.verticalLayoutWidget)
        self.sbVR.setObjectName("sbVR")
        self.sbVR.setRange(0,100)
        self.sbVR.setSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Fixed)
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.FieldRole, self.sbVR)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)
        
    def retranslateUi(self, Form):
        """
         Método empleado paraasignar el contenido de la Interfáz gráfica, es generado por pyuic5.
         Args:
          Form: Ventana en la que se deplegará la interfáz gráfica (es un tipo de dato QtWidget.QWidget) 
        """
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Prueba Torre de Londres"))

        self.label_4.setText(_translate("Form", "Ingrese los puntajes de la prueba Torre de Londres"))
        self.label_8.setText(_translate("Form", "Total Correctos: "))
        self.label_9.setText(_translate("Form", "Movimimentos Totales:"))
        self.label_10.setText(_translate("Form", "Tiempo de Latencia:"))
        self.label_11.setText(_translate("Form", "Tiempo de Ejecución:"))
        self.label_12.setText(_translate("Form", "Tiempo de Resolución:"))
        self.label_13.setText(_translate("Form", "VT:"))
        self.label_14.setText(_translate("Form", "VR:"))
        self.pbStart.setText(_translate("Form", "Registrar Prueba"))
        self.backButton.setText(_translate("Form", "Regresar al Menu"))