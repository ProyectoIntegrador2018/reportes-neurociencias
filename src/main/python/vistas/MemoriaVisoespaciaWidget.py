#Vista de la prueba de Memoria Visoespacia
from PyQt5 import QtCore, QtGui, QtWidgets
from AppCtxt import APPCTXT
from .mixins import WindowWidgetMixin

class MemoriaVisoespaciaWidget(WindowWidgetMixin):
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
        self.sbDenomImg = QtWidgets.QSpinBox(self.verticalLayoutWidget)
        self.sbDenomImg.setObjectName("sbDenomImg")
        self.sbDenomImg.setRange(0,36)
        self.sbDenomImg.setSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Fixed)
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.sbDenomImg)

        self.label_9 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_9.setObjectName("label_9")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_9)
        self.sbDenomImgT = QtWidgets.QSpinBox(self.verticalLayoutWidget)
        self.sbDenomImgT.setObjectName("sbDenomImgT")
        self.sbDenomImgT.setRange(0,12)
        self.sbDenomImgT.setSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Fixed)
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.sbDenomImgT)

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
        Form.setWindowTitle(_translate("Form", "Prueba Memoria Visoespacial"))
        # self.lblLogo.setText(_translate("Form", "Logo"))
        # self.label.setText(_translate("Form", "SYNAPPS"))
        self.label_4.setText(_translate("Form", "Ingrese los datos de la prueba de Memoria Visoespacia"))
        self.label_8.setText(_translate("Form", "Total recall: "))
        self.label_9.setText(_translate("Form", "Delayed recall:"))
        self.pbStart.setText(_translate("Form", "Registrar Prueba"))
        self.backButton.setText(_translate("Form", "Regresar al Menu"))


# if __name__ == "__main__":
#     import sys
#     app = QtWidgets.QApplication(sys.argv)
#     Form = QtWidgets.QWidget()
#     ui = MemoriaVisoespaciaWidget(Form)
#     ui.setupUi(Form)
#     Form.show()
#     sys.exit(app.exec_())


