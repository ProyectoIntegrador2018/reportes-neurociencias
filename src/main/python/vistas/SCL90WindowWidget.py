#Vista de la prueba de SCL-90
from PyQt5 import QtCore, QtGui, QtWidgets
from AppCtxt import APPCTXT
from .mixins import WindowWidgetMixin

class SCL90WindowWidget(WindowWidgetMixin):
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
        self.dsbSOM = QtWidgets.QDoubleSpinBox(self.verticalLayoutWidget)
        self.dsbSOM.setObjectName("dsbSOM")
        self.dsbSOM.setRange(0.00,4.00)
        self.dsbSOM.setSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Fixed)
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.dsbSOM)
        

        self.label_9 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_9.setObjectName("label_9")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_9)
        self.dsbOBS = QtWidgets.QDoubleSpinBox(self.verticalLayoutWidget)
        self.dsbOBS.setObjectName("dsbOBS")
        self.dsbOBS.setRange(0.00,4.00)
        self.dsbOBS.setSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Fixed)
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.dsbOBS)


        self.label_10 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_10.setObjectName("label_10")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_10)
        self.dsbINT = QtWidgets.QDoubleSpinBox(self.verticalLayoutWidget)
        self.dsbINT.setObjectName("dsbINT")
        self.dsbINT.setRange(0.00,4.00)
        self.dsbINT.setSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Fixed)
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.dsbINT)


        self.label_11 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_11.setObjectName("label_11")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_11)
        self.dsbDEP = QtWidgets.QDoubleSpinBox(self.verticalLayoutWidget)
        self.dsbDEP.setObjectName("dsbDEP")
        self.dsbDEP.setRange(0.00,4.00)
        self.dsbDEP.setSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Fixed)
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.dsbDEP)


        self.label_12 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_12.setObjectName("label_12")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.label_12)
        self.dsbANS = QtWidgets.QDoubleSpinBox(self.verticalLayoutWidget)
        self.dsbANS.setObjectName("dsbANS")
        self.dsbANS.setRange(0.00,4.00)
        self.dsbANS.setSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Fixed)
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.dsbANS)


        self.label_13 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_13.setObjectName("label_13")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.label_13)
        self.dsbHOS = QtWidgets.QDoubleSpinBox(self.verticalLayoutWidget)
        self.dsbHOS.setObjectName("dsbHOS")
        self.dsbHOS.setRange(0.00,4.00)
        self.dsbHOS.setSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Fixed)
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.dsbHOS)


        self.label_14 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_14.setObjectName("label_14")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.LabelRole, self.label_14)
        self.dsbFOB = QtWidgets.QDoubleSpinBox(self.verticalLayoutWidget)
        self.dsbFOB.setObjectName("dsbFOB")
        self.dsbFOB.setRange(0.00,3.95)
        self.dsbFOB.setSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Fixed)
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.FieldRole, self.dsbFOB)


        self.label_15 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_15.setObjectName("label_15")
        self.formLayout.setWidget(7, QtWidgets.QFormLayout.LabelRole, self.label_15)
        self.dsbPAR = QtWidgets.QDoubleSpinBox(self.verticalLayoutWidget)
        self.dsbPAR.setObjectName("dsbPAR")
        self.dsbPAR.setRange(0.00,4.00)
        self.dsbPAR.setSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Fixed)
        self.formLayout.setWidget(7, QtWidgets.QFormLayout.FieldRole, self.dsbPAR)


        self.label_16 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_16.setObjectName("label_16")
        self.formLayout.setWidget(8, QtWidgets.QFormLayout.LabelRole, self.label_16)
        self.dsbPSI = QtWidgets.QDoubleSpinBox(self.verticalLayoutWidget)
        self.dsbPSI.setObjectName("dsbPSI")
        self.dsbPSI.setRange(0.00,3.89)
        self.dsbPSI.setSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Fixed)
        self.formLayout.setWidget(8, QtWidgets.QFormLayout.FieldRole, self.dsbPSI)


        self.label_17 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_17.setObjectName("label_17")
        self.formLayout.setWidget(9, QtWidgets.QFormLayout.LabelRole, self.label_17)
        self.dsbGSI = QtWidgets.QDoubleSpinBox(self.verticalLayoutWidget)
        self.dsbGSI.setObjectName("dsbGSI")
        self.dsbGSI.setRange(0.08,3.86)
        self.dsbGSI.setSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Fixed)
        self.formLayout.setWidget(9, QtWidgets.QFormLayout.FieldRole, self.dsbGSI)


        self.label_18 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_18.setObjectName("label_18")
        self.formLayout.setWidget(10, QtWidgets.QFormLayout.LabelRole, self.label_18)
        self.dsbPST = QtWidgets.QDoubleSpinBox(self.verticalLayoutWidget)
        self.dsbPST.setObjectName("dsbPST")
        self.dsbPST.setRange(5,90.0)
        self.dsbPST.setSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Fixed)
        self.formLayout.setWidget(10, QtWidgets.QFormLayout.FieldRole, self.dsbPST)


        self.label_19 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_19.setObjectName("label_19")
        self.formLayout.setWidget(11, QtWidgets.QFormLayout.LabelRole, self.label_19)
        self.dsbPSDI = QtWidgets.QDoubleSpinBox(self.verticalLayoutWidget)
        self.dsbPSDI.setObjectName("dsbPSDI")
        self.dsbPSDI.setRange(1.03,4.00)
        self.dsbPSDI.setSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Fixed)
        self.formLayout.setWidget(11, QtWidgets.QFormLayout.FieldRole, self.dsbPSDI)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        """
         Método empleado paraasignar el contenido de la Interfáz gráfica, es generado por pyuic5.
         Args:
          Form: Ventana en la que se deplegará la interfáz gráfica (es un tipo de dato QtWidget.QWidget) 
        """
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Prueba SCL-90"))

        self.label_4.setText(_translate("Form", "Ingrese los puntajes de la prueba de SCL-90"))
        self.label_8.setText(_translate("Form", "SOM: "))
        self.label_9.setText(_translate("Form", "OBS:"))
        self.label_10.setText(_translate("Form", "INT:"))
        self.label_11.setText(_translate("Form", "DEP:"))
        self.label_12.setText(_translate("Form", "ANS:"))
        self.label_13.setText(_translate("Form", "HOS:"))
        self.label_14.setText(_translate("Form", "FOB:"))
        self.label_15.setText(_translate("Form", "PAR:"))
        self.label_16.setText(_translate("Form", "PSI:"))
        self.label_17.setText(_translate("Form", "GSI:"))
        self.label_18.setText(_translate("Form", "PST:"))
        self.label_19.setText(_translate("Form", "PSDI:"))
        self.pbStart.setText(_translate("Form", "Registrar Prueba"))
        self.backButton.setText(_translate("Form", "Regresar al Menu"))