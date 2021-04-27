#Vista de la prueba Motivos de Butt
from PyQt5 import QtCore, QtWidgets
from .mixins import WindowWidgetMixin

class ButtWindowWidget(WindowWidgetMixin):
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
        self.sbConflicto = QtWidgets.QSpinBox(self.verticalLayoutWidget)
        self.sbConflicto.setObjectName("sbConflicto")
        self.sbConflicto.setRange(0,5)
        self.sbConflicto.setSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Fixed)
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.sbConflicto)
        self.label_9 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_9.setObjectName("label_9")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_9)
        self.sbRivalidad = QtWidgets.QSpinBox(self.verticalLayoutWidget)
        self.sbRivalidad.setObjectName("sbRivalidad")
        self.sbRivalidad.setRange(0,5)
        self.sbRivalidad.setSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Fixed)
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.sbRivalidad)
        self.label_10 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_10.setObjectName("label_10")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_10)
        self.sbSuficiencia = QtWidgets.QSpinBox(self.verticalLayoutWidget)
        self.sbSuficiencia.setObjectName("sbSuficiencia")
        self.sbSuficiencia.setRange(0,5)
        self.sbSuficiencia.setSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Fixed)
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.sbSuficiencia)
        self.label_11 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_11.setObjectName("label_11")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_11)
        self.sbCooperacion = QtWidgets.QSpinBox(self.verticalLayoutWidget)
        self.sbCooperacion.setObjectName("sbCooperacion")
        self.sbCooperacion.setRange(0,5)
        self.sbCooperacion.setSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Fixed)
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.sbCooperacion)
        self.label_12 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_12.setObjectName("label_12")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.label_12)
        self.sbAgresividad = QtWidgets.QSpinBox(self.verticalLayoutWidget)
        self.sbAgresividad.setObjectName("sbAgresividada")
        self.sbAgresividad.setRange(0,5)
        self.sbAgresividad.setSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Fixed)
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.sbAgresividad)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)
        
    def retranslateUi(self, Form):
        """
         Método empleado paraasignar el contenido de la Interfáz gráfica, es generado por pyuic5.
         Args:
          Form: Ventana en la que se deplegará la interfáz gráfica (es un tipo de dato QtWidget.QWidget) 
        """
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Prueba Motivos Deportivos de Butt"))

        self.label_4.setText(_translate("Form", "Ingrese los puntajes de la prueba Butt"))
        self.label_8.setText(_translate("Form", "Conflicto: "))
        self.label_9.setText(_translate("Form", "Rivalidad: "))
        self.label_10.setText(_translate("Form", "Suficiencia: "))
        self.label_11.setText(_translate("Form", "Cooperacion: "))
        self.label_12.setText(_translate("Form", "Agresividad: "))

        self.pbStart.setText(_translate("Form", "Registrar Prueba"))
        self.backButton.setText(_translate("Form", "Regresar al Menu"))