#Vista de la prueba TMT
from PyQt5 import QtCore, QtGui, QtWidgets
from AppCtxt import APPCTXT
from .mixins import WindowWidgetMixin

class BussyPerryWindowWidget(WindowWidgetMixin):
    def setupUi(self, Form):
        """
         Método empleado para especificar el contenido de la Interfáz gráfica, es generado por pyuic5.
         Args:
          Form: Ventana en la que se deplegará la interfáz gráfica (es un tipo de dato QtWidget.QWidget) 
        """
        super().setupUI(Form)
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
        self.lblLogo.setMaximumSize(QtCore.QSize(1697/3.5, 312/3.5))
        self.lblLogo.setLineWidth(1)
        self.lblLogo.setText("")
        self.lblLogo.setPixmap(QtGui.QPixmap(APPCTXT().get_resource("logo3.png")))
        self.lblLogo.setScaledContents(True)
        self.lblLogo.setAlignment(QtCore.Qt.AlignCenter)
        self.lblLogo.setObjectName("lblLogo")
        self.horizontalLayout.addWidget(self.lblLogo)
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
        self.formLayout.setFieldGrowthPolicy(QtWidgets.QFormLayout.ExpandingFieldsGrow)

        self.label_8 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_8.setObjectName("label_8")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_8)
        self.sbTMTA = QtWidgets.QSpinBox(self.verticalLayoutWidget)
        self.sbTMTA.setObjectName("sbTMTA")
        self.sbTMTA.setRange(9,45)
        self.sbTMTA.setSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Fixed)
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.sbTMTA)
        self.label_9 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_9.setObjectName("label_9")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_9)
        self.sbTMTB = QtWidgets.QSpinBox(self.verticalLayoutWidget)
        self.sbTMTB.setObjectName("sbTMTB")
        self.sbTMTB.setRange(5,25)
        self.sbTMTB.setSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Fixed)
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.sbTMTB)

        self.label_10 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_10.setObjectName("label_10")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_10)
        self.sbTMTC = QtWidgets.QSpinBox(self.verticalLayoutWidget)
        self.sbTMTC.setObjectName("sbTMTC")
        self.sbTMTC.setRange(11,31)
        self.sbTMTC.setSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Fixed)
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.sbTMTC)

        self.label_11 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_11.setObjectName("label_11")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_11)
        self.sbTMTD = QtWidgets.QSpinBox(self.verticalLayoutWidget)
        self.sbTMTD.setObjectName("sbTMTD")
        self.sbTMTD.setRange(8,40)
        self.sbTMTD.setSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Fixed)
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.sbTMTD)

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
        self.verticalLayout.setStretch(0, 0)
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
        Form.setWindowTitle(_translate("Form", "Prueba Buss y Perry"))
        # self.lblLogo.setText(_translate("Form", "Logo"))
        # self.label.setText(_translate("Form", "SYNAPPS"))
        self.label_4.setText(_translate("Form", "Ingrese la suma de los puntajes de la prueba Buss y Perry"))
        self.label_8.setText(_translate("Form", "Puntuación en Agresión física: "))
        self.label_9.setText(_translate("Form", "Puntuación en Agresión verbal : "))
        self.label_10.setText(_translate("Form", "Puntuación en Ira : "))
        self.label_11.setText(_translate("Form", "Puntuación en Hostilidad : "))

        self.pbStart.setText(_translate("Form", "Registrar Prueba"))
        self.backButton.setText(_translate("Form", "Regresar al Menu"))


# if __name__ == "__main__":
#     import sys
#     app = QtWidgets.QApplication(sys.argv)
#     Form = QtWidgets.QWidget()
#     ui = TMTWindowWidget(Form)
#     ui.setupUi(Form)
#     Form.show()
#     sys.exit(app.exec_())
# 