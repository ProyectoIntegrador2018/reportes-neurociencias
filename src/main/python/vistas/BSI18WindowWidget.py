#Vista de la prueba de BSI-18
from PyQt5 import QtCore, QtGui, QtWidgets
from AppCtxt import APPCTXT
from .mixins import WindowWidgetMixin

# Definición de los parámetros
preguntas = ['1. Sensación de desmayo o mareo: ',
              '2. No sentir interés por las cosas:',
              '3. Nerviosismo o temblor:',
              '4. Dolores en el corazón o en el pecho:',
              '5. Sentirse solo:',
              '6. Sentirse tenso o alterado:'
              '7. Náuseas o malestar de estómago:',
              '8. Sentimientos de tristeza:',
              '9. Sustos repentinos sin razón:',
              '10. Falta de aire:',
              '11. Sentir que usted no vale nada:',
              '12. Ataques de terror o pánico',
              '13. Adormecimiento u hormigueo en ciertas partes del cuerpo',
              '14. Sentirse sin esperanza frente al futuro',
              '15. Sentirse tan inquieto que no puede permanecer sentado',
              '16. Sentirse débil en partes del cuerpo',
              '17. Pensamientos de poner fin a su vida',
              '18. Sentirse con miedo'
            ]
        

class BSI18WindowWidget(WindowWidgetMixin):
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

        # Crear los labels de cada parámetro y su entrada
        # Agregarlos a los layouts
        self.labels = []
        for x, _ in enumerate(preguntas):
            self.labels.append(QtWidgets.QLabel(self.verticalLayoutWidget))
            self.labels[-1].setObjectName("label_"+str(x+1))
            self.formLayout.setWidget(x,QtWidgets.QFormLayout.LabelRole, self.labels[-1])
            self.questions = []
            self.questions.append(QtWidgets.QSpinBox(self.verticalLayoutWidget))
            self.questions[-1].setObjectName("Q"+str(x+1))
            self.questions[-1].setRange(0,4)
            self.questions[-1].setSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Fixed)
            self.formLayout.setWidget(x, QtWidgets.QFormLayout.FieldRole, self.questions[-1])
        
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
        Form.setWindowTitle(_translate("Form", "Prueba BSI-18"))
        # self.lblLogo.setText(_translate("Form", "Logo"))
        # self.label.setText(_translate("Form", "SYNAPPS"))
        self.label_4.setText(_translate("Form", "Ingrese los puntajes de la prueba de BSI-18"))

        '''preguntas = ['1. Sensación de desmayo o mareo: ', 
                      '2. No sentir interés por las cosas:',
                      '3. Nerviosismo o temblor:',
                      '4. Dolores en el corazón o en el pecho:',
                      '5. Sentirse solo:',
                      '6. Sentirse tenso o alterado:',
                      '7. Náuseas o malestar de estómago:',
                      '8. Sentimientos de tristeza:',
                      '9. Sustos repentinos sin razón:',
                      '10. Falta de aire:',
                      '11. Sentir que usted no vale nada:',
                      '12. Ataques de terror o pánico',
                      '13. Adormecimiento u hormigueo en ciertas partes del cuerpo',
                      '14. Sentirse sin esperanza frente al futuro',
                      '15. Sentirse tan inquieto que no puede permanecer sentado',
                      '16. Sentirse débil en partes del cuerpo',
                      '17. Pensamientos de poner fin a su vida',
                      '18. Sentirse con miedo'
                      ]
        '''
        # Agregar los textos a los labels de la información
        print(len(preguntas), len(self.labels))
        for x, label in enumerate(preguntas):
          self.labels[x].setText(_translate("Form", label))

        self.pbStart.setText(_translate("Form", "Registrar Prueba"))
        self.backButton.setText(_translate("Form", "Regresar al Menu"))


#if __name__ == "__main__":
#    import sys
#    app = QtWidgets.QApplication(sys.argv)
#    Form = QtWidgets.QWidget()
#    ui = BSI18WindowWidget(Form)
#    ui.setupUi(Form)
#    Form.show()
#    sys.exit(app.exec_())
