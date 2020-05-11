#Vista de la prueba de Fluidez Verbal
from PyQt5 import QtCore, QtGui, QtWidgets


class DenominacionWidget(object):
    def __init__(self, Form):
        self.setupUi(Form)

    def setupUi(self, Form):
        """
         Método empleado para especificar el contenido de la Interfáz gráfica, es generado por pyuic5.
         Args:
          Form: Ventana en la que se deplegará la interfáz gráfica (es un tipo de dato QtWidget.QWidget) 
        """
        Form.setObjectName("Form")
        Form.resize(800, 598)
        self.verticalLayoutWidget = QtWidgets.QWidget(Form)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(220, 0, 581, 541))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.lblLogo = QtWidgets.QLabel(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lblLogo.sizePolicy().hasHeightForWidth())
        self.lblLogo.setSizePolicy(sizePolicy)
        self.lblLogo.setLineWidth(1)
        self.lblLogo.setAlignment(QtCore.Qt.AlignCenter)
        self.lblLogo.setObjectName("lblLogo")
        self.horizontalLayout.addWidget(self.lblLogo)
        self.label = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_4 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_4.setToolTip("")
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_2.addWidget(self.label_4)
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setFormAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.formLayout.setContentsMargins(7, -1, 7, -1)
        self.formLayout.setObjectName("formLayout")

        self.label_8 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_8.setObjectName("label_8")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_8)
        self.sbTotalCorrectos = QtWidgets.QSpinBox(self.verticalLayoutWidget)
        self.sbTotalCorrectos.setObjectName("sbTotalCorrectos")
        self.sbTotalCorrectos.setRange(0,10)
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.sbTotalCorrectos)

        self.label_9 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_9.setObjectName("label_9")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_9)
        self.sbMovimientosTotales = QtWidgets.QSpinBox(self.verticalLayoutWidget)
        self.sbMovimientosTotales.setObjectName("sbMovimientosTotales")
        self.sbMovimientosTotales.setRange(0,1000)
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.sbMovimientosTotales)

        self.label_10 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_10.setObjectName("label_10")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_10)
        self.sbTiempoLatencia = QtWidgets.QSpinBox(self.verticalLayoutWidget)
        self.sbTiempoLatencia.setObjectName("sbTiempoLatencia")
        self.sbTiempoLatencia.setRange(0,1000)
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.sbTiempoLatencia)

        self.label_11 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_11.setObjectName("label_11")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_11)
        self.sbTiempoEjecucion = QtWidgets.QSpinBox(self.verticalLayoutWidget)
        self.sbTiempoEjecucion.setObjectName("sbTiempoEjecucion")
        self.sbTiempoEjecucion.setRange(0,1000)
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.sbTiempoEjecucion)

        self.label_12 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_12.setObjectName("label_12")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.label_12)
        self.sbTiempoResolucion = QtWidgets.QSpinBox(self.verticalLayoutWidget)
        self.sbTiempoResolucion.setObjectName("sbTiempoResolucion")
        self.sbTiempoResolucion.setRange(0,1000)
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.sbTiempoResolucion)

        self.label_13 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_13.setObjectName("label_13")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.label_13)
        self.sbVT = QtWidgets.QSpinBox(self.verticalLayoutWidget)
        self.sbVT.setObjectName("sbVT")
        self.sbVT.setRange(0,100)
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.sbVT)

        self.label_14 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_14.setObjectName("label_14")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.LabelRole, self.label_14)
        self.sbVR = QtWidgets.QSpinBox(self.verticalLayoutWidget)
        self.sbVR.setObjectName("sbVR")
        self.sbVR.setRange(0,100)
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.FieldRole, self.sbVR)

        self.verticalLayout_2.addLayout(self.formLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.pbStart = QtWidgets.QPushButton(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pbStart.sizePolicy().hasHeightForWidth())
        self.pbStart.setSizePolicy(sizePolicy)
        self.pbStart.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.pbStart.setObjectName("pbStart")
        self.horizontalLayout_2.addWidget(self.pbStart)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.verticalLayout_2.setStretch(0, 1)
        self.verticalLayout_2.setStretch(1, 5)
        self.verticalLayout.addLayout(self.verticalLayout_2)
        self.verticalLayout.setStretch(0, 1)
        self.verticalLayout.setStretch(1, 6)
        self.lWVistas = QtWidgets.QListWidget(Form)
        self.lWVistas.setGeometry(QtCore.QRect(0, 90, 221, 451))
        self.lWVistas.setObjectName("lWVistas")

        self.progressBar = QtWidgets.QProgressBar(Form)
        self.progressBar.setGeometry(QtCore.QRect(127, 560, 601, 23))
        self.progressBar.setProperty("value", 24)
        self.progressBar.setObjectName("progressBar")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        """
         Método empleado paraasignar el contenido de la Interfáz gráfica, es generado por pyuic5.
         Args:
          Form: Ventana en la que se deplegará la interfáz gráfica (es un tipo de dato QtWidget.QWidget) 
        """
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.lblLogo.setText(_translate("Form", "Logo"))
        self.label.setText(_translate("Form", "SYNAPPS"))
        self.label_4.setText(_translate("Form", "Ingrese los puntajes de la prueba Denominación"))
        self.label_8.setText(_translate("Form", "Total Correctos: "))
        self.label_9.setText(_translate("Form", "Movimimentos Totales:"))
        self.label_10.setText(_translate("Form", "Tiempo de Latencia:"))
        self.label_11.setText(_translate("Form", "Tiempo de Ejecución:"))
        self.label_12.setText(_translate("Form", "Tiempo de Resolución:"))
        self.label_13.setText(_translate("Form", "VT:"))
        self.label_14.setText(_translate("Form", "VR:"))
        self.pbStart.setText(_translate("Form", "Registrar Prueba"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = DenominacionWidget(Form)
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
