# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'memoria_visoespacial.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
import pandas as pd

baremoData = pd.read_excel(r"C:\Users\emi_l\OneDrive\Documents\TEC DE MONTERREY\9no Semestre\Proyecto Integrador\Baremos\Excel_Files\Baremo_BVMT-R-1.xlsx")
tablaDf = pd.read_excel(r"C:\Users\emi_l\OneDrive\Documents\TEC DE MONTERREY\9no Semestre\Proyecto Integrador\Baremos\Excel_Files\Tabla_Conversión_Psicométrica_Completa.xlsx")

class Ui_widget1(object):
    def setupUi(self, widget1):
        widget1.setObjectName("widget1")
        widget1.resize(451, 432)
        self.label = QtWidgets.QLabel(widget1)
        self.label.setGeometry(QtCore.QRect(190, 70, 211, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(widget1)
        self.label_2.setGeometry(QtCore.QRect(190, 140, 41, 20))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(widget1)
        self.label_3.setGeometry(QtCore.QRect(190, 180, 41, 20))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(widget1)
        self.label_4.setGeometry(QtCore.QRect(190, 220, 41, 20))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(widget1)
        self.label_5.setGeometry(QtCore.QRect(190, 260, 91, 20))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.spin_trial1 = QtWidgets.QSpinBox(widget1)
        self.spin_trial1.setGeometry(QtCore.QRect(340, 140, 42, 22))
        self.spin_trial1.setObjectName("spin_trial1")
        self.spin_trial2 = QtWidgets.QSpinBox(widget1)
        self.spin_trial2.setGeometry(QtCore.QRect(340, 180, 42, 22))
        self.spin_trial2.setObjectName("spin_trial2")
        self.spin_trial3 = QtWidgets.QSpinBox(widget1)
        self.spin_trial3.setGeometry(QtCore.QRect(340, 220, 42, 22))
        self.spin_trial3.setObjectName("spin_trial3")
        self.spin_delayed_recall = QtWidgets.QSpinBox(widget1)
        self.spin_delayed_recall.setGeometry(QtCore.QRect(340, 260, 42, 22))
        self.spin_delayed_recall.setObjectName("spin_delayed_recall")
        self.results_button = QtWidgets.QPushButton(widget1)
        self.results_button.setGeometry(QtCore.QRect(250, 340, 75, 23))
        self.results_button.setObjectName("results_button")
        self.results_button.clicked.connect(self.clicked)

        self.retranslateUi(widget1)
        QtCore.QMetaObject.connectSlotsByName(widget1)
    
    def clicked(self):
        print("RESULTADOS")
        trial1 = self.spin_trial1.value()
        trial2 = self.spin_trial2.value()
        trial3 = self.spin_trial3.value()
        delayed_recall = self.spin_delayed_recall.value()
        total_recall = trial1 + trial2 + trial3
        percentil_normal = baremoData.percentile[baremoData.total_recall == total_recall].item()
        escalar_normal  = tablaDf.puntuacion_escalar[tablaDf.puntuacion_percentil == percentil_normal].item()
        percentil_delayed = baremoData.percentile[baremoData.delayed_recall == delayed_recall].item()
        escalar_delayed = tablaDf.puntuacion_escalar[tablaDf.puntuacion_percentil == percentil_delayed].item()
        print ("Puntaje percentil (total recall): " + str(percentil_normal)+"%")
        print ("Puntaje escalar: (total recall): " + str(escalar_normal))
        print ("Puntaje percentil (delayed recall): " + str(percentil_delayed)+"%")
        print ("Puntaje escalar (delayed recall): " + str(escalar_delayed))
        

    def retranslateUi(self, widget1):
        _translate = QtCore.QCoreApplication.translate
        widget1.setWindowTitle(_translate("widget1", "Synapps"))
        self.label.setText(_translate("widget1", "Memoria Visoespacial"))
        self.label_2.setText(_translate("widget1", "Trial 1"))
        self.label_3.setText(_translate("widget1", "Trial 2"))
        self.label_4.setText(_translate("widget1", "Trial 3"))
        self.label_5.setText(_translate("widget1", "Delayed recall"))
        self.results_button.setText(_translate("widget1", "Resultados"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    widget1 = QtWidgets.QWidget()
    ui = Ui_widget1()
    ui.setupUi(widget1)
    widget1.show()
    sys.exit(app.exec_())
