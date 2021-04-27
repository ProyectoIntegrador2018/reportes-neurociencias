#Vista de la prueba de SDMT
from PyQt5 import QtCore, QtGui, QtWidgets
from AppCtxt import APPCTXT
from .mixins import WindowWidgetMixin

class SDMTWindowWidget(WindowWidgetMixin):
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

        self.sbSDMT = QtWidgets.QSpinBox(self.verticalLayoutWidget)
        self.sbSDMT.setObjectName("sbSDMT")
        #no estoy muy segura del rango, checar con Beatriz
        self.sbSDMT.setRange(1,100)
        self.sbSDMT.setSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Fixed)
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.sbSDMT)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        """
         Método empleado paraasignar el contenido de la Interfáz gráfica, es generado por pyuic5.
         Args:
          Form: Ventana en la que se deplegará la interfáz gráfica (es un tipo de dato QtWidget.QWidget) 
        """
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Prueba SDMT"))

        self.label_4.setText(_translate("Form", "Ingrese los puntajes de la prueba SDMT"))
        self.label_8.setText(_translate("Form", "SDMT: "))
        self.pbStart.setText(_translate("Form", "Registrar Prueba"))
        self.backButton.setText(_translate("Form", "Regresar al Menu"))