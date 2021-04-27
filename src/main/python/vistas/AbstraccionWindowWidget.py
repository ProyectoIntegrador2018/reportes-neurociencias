# Vista de la prueba de Abstraccion
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QLabel, QWidget
from .mixins import WindowWidgetMixin

class AbstraccionWindowWidget(WindowWidgetMixin):
    def setupUi(self, Form):
        """
         Método empleado para especificar el contenido de la Interfáz gráfica, es generado por pyuic5.
         Args:
          Form: Ventana en la que se deplegará la interfáz gráfica (es un tipo de dato QtWidget.QWidget) 
        """
        super().setupUI(Form)

        self.horizontalLayout.setStretch(0,1)
        self.horizontalLayout.setStretch(1,3)

        self.label_4 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_4.setToolTip("")
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_2.addWidget(self.label_4)

        self.label_8 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_8.setObjectName("label_8")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_8)
        self.sbAbstraccion = QtWidgets.QSpinBox(self.verticalLayoutWidget)
        self.sbAbstraccion.setObjectName("sbAbstraccion")
        self.sbAbstraccion.setRange(0,12)
        self.sbAbstraccion.setSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Fixed)
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.sbAbstraccion)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)
    def retranslateUi(self, Form):
        """
         Método empleado paraasignar el contenido de la Interfáz gráfica, es generado por pyuic5.
         Args:
          Form: Ventana en la que se deplegará la interfáz gráfica (es un tipo de dato QtWidget.QWidget) 
        """
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Prueba Abstracción"))

        self.label_4.setText(_translate("Form", "Ingrese los datos de la prueba Abstracción"))
        self.label_8.setText(_translate("Form", "Puntuación en semejanza-abstracción: "))
        self.pbStart.setText(_translate("Form", "Registrar Prueba"))
        self.backButton.setText(_translate("Form", "Regresar al Menu"))