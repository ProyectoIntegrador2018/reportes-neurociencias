# Vista de la Pantalla Principal
from PyQt5 import QtCore, QtGui, QtWidgets
from AppCtxt import APPCTXT


class MainWindowWithListWidget(object):
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
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.lblLogo.sizePolicy().hasHeightForWidth())
        self.lblLogo.setSizePolicy(sizePolicy)
        self.lblLogo.setMaximumSize(QtCore.QSize(1697/5, 312/5))
        self.lblLogo.setLineWidth(1)
        self.lblLogo.setText("")
        self.lblLogo.setPixmap(QtGui.QPixmap(APPCTXT().get_resource("logo3.png")))
        self.lblLogo.setScaledContents(True)
        self.lblLogo.setAlignment(QtCore.Qt.AlignCenter)
        self.lblLogo.setObjectName("lblLogo")
        self.horizontalLayout.addWidget(self.lblLogo)
        # self.label = QtWidgets.QLabel(self.verticalLayoutWidget)
        # self.label.setAlignment(QtCore.Qt.AlignCenter)
        # self.label.setObjectName("label")
        # self.horizontalLayout.addWidget(self.label)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_4 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_4.setToolTip("")
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_2.addWidget(self.label_4)
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setContentsMargins(7, -1, 7, -1)
        self.formLayout.setObjectName("formLayout")
        self.formLayout.setFieldGrowthPolicy(QtWidgets.QFormLayout.ExpandingFieldsGrow)
        self.label_10 = QtWidgets.QLabel(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.label_10.sizePolicy().hasHeightForWidth())
        self.label_10.setSizePolicy(sizePolicy)
        self.label_10.setObjectName("label_10")
        self.formLayout.setWidget(
            0, QtWidgets.QFormLayout.LabelRole, self.label_10)
        self.leName = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.leName.sizePolicy().hasHeightForWidth())
        self.leName.setSizePolicy(sizePolicy)
        self.leName.setObjectName("leName")
        self.formLayout.setWidget(
            0, QtWidgets.QFormLayout.FieldRole, self.leName)
        self.label_11 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_11.setObjectName("label_11")
        self.formLayout.setWidget(
            1, QtWidgets.QFormLayout.LabelRole, self.label_11)
        self.leId = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.leId.setObjectName("leId")
        self.formLayout.setWidget(
            1, QtWidgets.QFormLayout.FieldRole, self.leId)
        self.label_3 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(
            2, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.leExaminer = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.leExaminer.setObjectName("leExaminer")
        self.formLayout.setWidget(
            2, QtWidgets.QFormLayout.FieldRole, self.leExaminer)
        self.label_8 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_8.setObjectName("label_8")
        self.formLayout.setWidget(
            3, QtWidgets.QFormLayout.LabelRole, self.label_8)

        ageMin = 15
        ageMax = 90
        self.sbAge = QtWidgets.QSpinBox(self.verticalLayoutWidget)
        self.sbAge.setObjectName("sbAge")
        self.sbAge.setRange(ageMin, ageMax)
        self.sbAge.setSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Fixed)
        self.formLayout.setWidget(
            3, QtWidgets.QFormLayout.FieldRole, self.sbAge)
        self.label_9 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_9.setObjectName("label_9")
        self.formLayout.setWidget(
            4, QtWidgets.QFormLayout.LabelRole, self.label_9)
        self.sbEscolaridad = QtWidgets.QSpinBox(self.verticalLayoutWidget)
        self.sbEscolaridad.setObjectName("sbEscolaridad")
        self.sbEscolaridad.setSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Fixed)
        self.formLayout.setWidget(
            4, QtWidgets.QFormLayout.FieldRole, self.sbEscolaridad)
        self.label_12 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_12.setObjectName("label_12")
        self.formLayout.setWidget(
            5, QtWidgets.QFormLayout.LabelRole, self.label_12)
        self.cbSexo = QtWidgets.QComboBox(self.verticalLayoutWidget)
        self.cbSexo.setEnabled(True)
        self.cbSexo.setEditable(False)
        self.cbSexo.setObjectName("cbSexo")
        self.cbSexo.setSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Fixed)
        self.formLayout.setWidget(
            5, QtWidgets.QFormLayout.FieldRole, self.cbSexo)
        self.label_2 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(
            6, QtWidgets.QFormLayout.LabelRole, self.label_2)

        fechaActual = QtCore.QDate.currentDate()
        fechaMinYear = fechaActual.year() - ageMin
        fechaMinimaNacimiento = QtCore.QDate(fechaMinYear, 12, 31)

        fechaMaxYear = fechaActual.year() - ageMax
        fechaMaximaNacimiento = QtCore.QDate(fechaMaxYear, 1, 1)

        self.deFechaNacimiento = QtWidgets.QDateEdit(self.verticalLayoutWidget)
        self.deFechaNacimiento.setObjectName("deFechaNacimiento")
        self.deFechaNacimiento.setDisplayFormat("dd/MMMM/yyyy")
        self.deFechaNacimiento.setSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Fixed)
        self.deFechaNacimiento.setDateRange(
            fechaMaximaNacimiento, fechaMinimaNacimiento)

        dateToShow = QtCore.QDate(fechaMinYear, 1, 1)
        self.deFechaNacimiento.setDate(dateToShow)

        self.formLayout.setWidget(
            6, QtWidgets.QFormLayout.FieldRole, self.deFechaNacimiento)

        self.label_5 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_5.setObjectName("label_5")
        self.formLayout.setWidget(
            7, QtWidgets.QFormLayout.LabelRole, self.label_5)
        self.cbLateralidad = QtWidgets.QComboBox(self.verticalLayoutWidget)
        self.cbLateralidad.setEnabled(True)
        self.cbLateralidad.setEditable(False)
        self.cbLateralidad.setObjectName("cbLateralidad")
        self.cbLateralidad.setSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Fixed)
        self.formLayout.setWidget(
            7, QtWidgets.QFormLayout.FieldRole, self.cbLateralidad)
        self.label_6 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_6.setObjectName("label_6")
        self.formLayout.setWidget(
            8, QtWidgets.QFormLayout.LabelRole, self.label_6)

        self.deFecha = QtWidgets.QDateEdit(self.verticalLayoutWidget)
        self.deFecha.setObjectName("deFecha")
        self.deFecha.setDisplayFormat("dd/MMMM/yyyy")
        self.deFecha.setSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Fixed)
        self.formLayout.setWidget(
            8, QtWidgets.QFormLayout.FieldRole, self.deFecha)

        self.label_7 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_7.setObjectName("label_7")
        self.formLayout.setWidget(
            9, QtWidgets.QFormLayout.LabelRole, self.label_7)
        self.leCarrera = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.leCarrera.setObjectName("leCarrera")
        self.formLayout.setWidget(
            9, QtWidgets.QFormLayout.FieldRole, self.leCarrera)
        self.label_13 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_13.setObjectName("label_13")
        self.formLayout.setWidget(
            10, QtWidgets.QFormLayout.LabelRole, self.label_13)
        self.sbSemestre = QtWidgets.QSpinBox(self.verticalLayoutWidget)
        self.sbSemestre.setObjectName("sbSemestre")
        self.sbSemestre.setSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Fixed)
        self.formLayout.setWidget(
            10, QtWidgets.QFormLayout.FieldRole, self.sbSemestre)
        self.label_14 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_14.setObjectName("label_14")
        self.formLayout.setWidget(
            11, QtWidgets.QFormLayout.LabelRole, self.label_14)
        self.leEquipo = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.leEquipo.setObjectName("leEquipo")
        self.formLayout.setWidget(
            11, QtWidgets.QFormLayout.FieldRole, self.leEquipo)
        self.label_15 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_15.setObjectName("label_15")
        self.formLayout.setWidget(
            12, QtWidgets.QFormLayout.LabelRole, self.label_15)
        self.leDeporte = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.leDeporte.setObjectName("leDeporte")
        self.formLayout.setWidget(
            12, QtWidgets.QFormLayout.FieldRole, self.leDeporte)
        self.verticalLayout_2.addLayout(self.formLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setSizeConstraint(
            QtWidgets.QLayout.SetDefaultConstraint)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.pbStart = QtWidgets.QPushButton(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.pbStart.sizePolicy().hasHeightForWidth())
        self.pbStart.setSizePolicy(sizePolicy)
        self.pbStart.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.pbStart.setObjectName("pbStart")
        self.horizontalLayout_2.addWidget(self.pbStart)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.verticalLayout_2.setStretch(0, 1)
        self.verticalLayout_2.setStretch(1, 8)
        self.verticalLayout.addLayout(self.verticalLayout_2)
        self.verticalLayout.setStretch(0, 6)
        self.verticalLayout.setStretch(0, 0)

        self.backButton = QtWidgets.QPushButton(Form)
        self.backButton.setGeometry(QtCore.QRect(15, 50, 20, 30))
        self.backButton.setObjectName("returnButton")

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
        Form.setWindowTitle(_translate("Form", "Información de Sujeto"))
        # self.lblLogo.setText(_translate("Form", "Logo"))
        # self.label.setText(_translate("Form", "SYNAPPS"))
        self.label_4.setText(_translate(
            "Form", "Ingrese los datos del paciente"))
        self.label_10.setText(_translate("Form", "Nombre:"))
        self.label_11.setText(_translate("Form", "ID:"))
        self.label_3.setText(_translate("Form", "Examinador:"))
        self.label_8.setText(_translate("Form", "Edad:"))
        self.label_9.setText(_translate("Form", "Educación (Años):"))
        self.label_12.setText(_translate("Form", "Género:"))
        self.label_2.setText(_translate("Form", "Fecha de Nacimiento:"))
        self.label_5.setText(_translate("Form", "Lateralidad:"))
        self.label_6.setText(_translate("Form", "Fecha:"))
        self.label_7.setText(_translate("Form", "Carrera:"))
        self.label_13.setText(_translate("Form", "Semestre:"))
        self.label_14.setText(_translate("Form", "Equipo:"))
        self.label_15.setText(_translate("Form", "Deporte:"))
        self.pbStart.setText(_translate("Form", "Comenzar Captura"))
        self.backButton.setText(_translate("Form", "Regresar al Menu"))

