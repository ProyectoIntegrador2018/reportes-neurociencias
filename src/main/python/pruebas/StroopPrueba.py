#Prueba de Stroop
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QUrl, QDir
import pandas as pd
import PruebaModel

class StroopPrueba(PruebaModel.PruebaModel):	
    def __init__(self, valores):
        nombre = "Stroop"
        baremoStroop = QUrl(QDir.currentPath()+"/Baremos/Baremo_Stroop.csv").toString()
        baremos = (pd.read_csv(baremoStroop))
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

    def calcularPERP(self, datos):
        """
        Método que es empleado para calcular la Puntuación Escalar(PE), como la Percentil(RP)
        Args:
        datos: Lista de información relevante del reporte para calcular los valores de PE y RP (escolaridad, edad)
        """
        stroopData = self.baremos
        P = self.valores[0]
        C = self.valores[1]
        PC = self.valores[2]
        escolaridad = datos



        p_percentil = ((stroopData.percentile_inf[stroopData.P == P].iloc[0]),(stroopData.percentile_sup[stroopData.P == P].iloc[0]))
        c_percentil = ((stroopData.percentile_inf[stroopData.C == C].iloc[0]),(stroopData.percentile_sup[stroopData.C == C].iloc[0]))
        pc_percentil = ((stroopData.percentile_inf[stroopData.PC == PC].iloc[0]),(stroopData.percentile_sup[stroopData.PC == PC].iloc[0]))
        
        p_escalar = int(stroopData.escalar[stroopData.percentile_inf == p_percentil[0]].iloc[0])
        c_escalar = int(stroopData.escalar[stroopData.percentile_inf == c_percentil[0]].iloc[0])
        pc_escalar = int(stroopData.escalar[stroopData.percentile_inf == pc_percentil[0]].iloc[0])

        '''
        La escolaridad tiene que estar forzada a un rango de 8 a 20 años
        '''
        self.puntuacionEscalar = (p_escalar, c_escalar,pc_escalar)
        self.rangoPercentil = (p_percentil, c_percentil,pc_percentil)
