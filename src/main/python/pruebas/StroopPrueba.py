#Prueba de Stroop
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QUrl, QDir
import pandas as pd
import PruebaModel

class StroopPrueba(PruebaModel.PruebaModel):
    def __init__(self, valores):
        nombre = "Stroop"
        baremoStroop = QUrl(QDir.currentPath()+"/src/main/python/Baremos/Baremo_Stroop.csv").toString()

        baremos =	(pd.read_csv(baremoStroop))
        campos = ("P", "C", "PC")
        
        super(StroopPrueba,self).__init__(nombre, valores, baremos, campos)
        
        def calcularPERP(self, datos):
            """
            Método que es empleado para calcular la Puntuación Escalar(PE), como la Percentil(RP)
            Args:
            datos: Lista de información relevante del reporte para calcular los valores de PE y RP (escolaridad, edad)
            """
            edad = datos
            stroopData = self.baremos[0]
            
            P = self.valores[0]
            C = self.valores[1]
            PC = self.valores[2]

            if P<=71:
                P = '71'
            else:
                P = str(P)

            if C<=48:
                C = '48'
            else:
                C = str(C)

            if PC<=24:
                PC='24'
            else:
                PC = str(PC)
            
            print(P)
            print(C)
            print(PC)

            p_puntuacion_percentil = stroopData['percentile'][stroopData.P == P].iloc[0]
            c_puntuacion_percentil = stroopData['percentile'][stroopData.C == C].iloc[0]
            pc_puntuacion_percentil = stroopData['percentile'][stroopData.PC == PC].iloc[0]
            p_puntunacion_escalar = stroopData['escalar'][stroopData.P == P].iloc[0]
            c_puntunacion_escalar = stroopData['escalar'][stroopData.C == C].iloc[0]
            pc_puntuacion_escalar = stroopData['escalar'][stroopData.PC == PC].iloc[0]

            self.puntuacionEscalar = (p_puntunacion_escalar, c_puntunacion_escalar, pc_puntuacion_escalar)
            self.rangoPercentil = (p_puntuacion_percentil, c_puntuacion_percentil, pc_puntuacion_percentil)

