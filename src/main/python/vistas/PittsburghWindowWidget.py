#Vista de la prueba de Pittsburgh
from PyQt5 import QtCore, QtGui, QtWidgets
from AppCtxt import APPCTXT
from .mixins import WindowWidgetMixin

class PittsburghWindowWidget(WindowWidgetMixin):
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
        self.comp1 = QtWidgets.QDoubleSpinBox(self.verticalLayoutWidget)
        self.comp1.setObjectName("comp1")
        self.comp1.setRange(0.00,3.00)
        self.comp1.setSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Fixed)
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.comp1)
        

        self.label_9 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_9.setObjectName("label_9")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_9)
        self.comp2 = QtWidgets.QDoubleSpinBox(self.verticalLayoutWidget)
        self.comp2.setObjectName("comp2")
        self.comp2.setRange(0.00,3.00)
        self.comp2.setSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Fixed)
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.comp2)


        self.label_10 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_10.setObjectName("label_10")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_10)
        self.comp3 = QtWidgets.QDoubleSpinBox(self.verticalLayoutWidget)
        self.comp3.setObjectName("comp3")
        self.comp3.setRange(0.00,3.00)
        self.comp3.setSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Fixed)
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.comp3)


        self.label_11 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_11.setObjectName("label_11")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_11)
        self.comp4 = QtWidgets.QDoubleSpinBox(self.verticalLayoutWidget)
        self.comp4.setObjectName("comp4")
        self.comp4.setRange(0.00,3.00)
        self.comp4.setSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Fixed)
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.comp4)


        self.label_12 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_12.setObjectName("label_12")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.label_12)
        self.comp5 = QtWidgets.QDoubleSpinBox(self.verticalLayoutWidget)
        self.comp5.setObjectName("comp5")
        self.comp5.setRange(0.00,3.00)
        self.comp5.setSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Fixed)
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.comp5)


        self.label_13 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_13.setObjectName("label_13")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.label_13)
        self.comp6 = QtWidgets.QDoubleSpinBox(self.verticalLayoutWidget)
        self.comp6.setObjectName("comp6")
        self.comp6.setRange(0.00,3.00)
        self.comp6.setSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Fixed)
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.comp6)


        self.label_14 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_14.setObjectName("label_14")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.LabelRole, self.label_14)
        self.comp7 = QtWidgets.QDoubleSpinBox(self.verticalLayoutWidget)
        self.comp7.setObjectName("comp7")
        self.comp7.setRange(0.00,3.00)
        self.comp7.setSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Fixed)
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.FieldRole, self.comp7)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        """
         Método empleado paraasignar el contenido de la Interfáz gráfica, es generado por pyuic5.
         Args:
          Form: Ventana en la que se deplegará la interfáz gráfica (es un tipo de dato QtWidget.QWidget) 
        """
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Prueba de Pittsburgh"))

        self.label_4.setText(_translate("Form", "Ingrese los puntajes de la prueba de Pittsburgh"))
        self.label_8.setText(_translate("Form", "Componente 1: "))
        self.label_9.setText(_translate("Form", "Componente 2:"))
        self.label_10.setText(_translate("Form", "Componente 3:"))
        self.label_11.setText(_translate("Form", "Componente 4:"))
        self.label_12.setText(_translate("Form", "Componente 5:"))
        self.label_13.setText(_translate("Form", "Componente 6:"))
        self.label_14.setText(_translate("Form", "Componente 7:"))
        self.pbStart.setText(_translate("Form", "Registrar Prueba"))
        self.backButton.setText(_translate("Form", "Regresar al Menu"))
