# Prueba Memoria Visoespacia
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QUrl, QDir
import pandas as pd
import PruebaModel

class MemoriaVisoespaciaPrueba(PruebaModel.PruebaModel):
    def __init__(self, valores):
        nombre = "MemoriaVisoespacia"
        baremoR1 = QUrl(QDir.currentPath()+"/Baremos/Baremo_BVMT-R-1.csv").toString()
        baremoR2 = QUrl(QDir.currentPath()+"/Baremos/Baremo_BVMT-R-2.csv").toString()
        baremoR3 = QUrl(QDir.currentPath()+"/Baremos/Baremo_BVMT-R-3.csv").toString()
        baremoR4 = QUrl(QDir.currentPath()+"/Baremos/Baremo_BVMT-R-4.csv").toString()
        baremoR5 = QUrl(QDir.currentPath()+"/Baremos/Baremo_BVMT-R-5.csv").toString()
        tablaConversion = QUrl(QDir.currentPath()+"/Baremos/Tabla_Conversión_Psicométrica_Completa.csv").toString()


        baremos = (pd.read_csv(baremoR1),
                    pd.read_csv(baremoR2),
                    pd.read_csv(baremoR3), 
                    pd.read_csv(baremoR4),
                    pd.read_csv(baremoR5),
                    pd.read_csv(tablaConversion))
        campos = ("T", "Dif")

        super(MemoriaVisoespaciaPrueba,self).__init__(nombre, valores, baremos, campos)

    def calcularPERP(self, datos):
        """
        Metodo que se encarga de calcular la puntiacion escalar y percentil de la prueba de 
        Memoria Visoespacia
        Parametros: total recall y delayed recall, que arrojan dos resultados diferentes
        """
        edad = datos

        baremoData1 = self.baremos[0]
        baremoData2 = self.baremos[1]
        baremoData3 = self.baremos[2]
        baremoData4 = self.baremos[3]
        baremoData5 = self.baremos[4]
        tablaDf = self.baremos[5]

        totalRecall = self.valores[0]
        delayedRecall = self.valores[1]

        if (edad<18):
            edad = 18
        elif (edad>49):
            edad = 38

        if (edad>=18 and edad<=22):
            if totalRecall <= 18:
                totalRecall = 18
            
            if delayedRecall <= 7:
                delayedRecall = 7

            totalRecall = str(totalRecall)
            delayedRecall = str(delayedRecall)
            percentil_normal = baremoData1.percentile[baremoData1.total_recall == totalRecall].iloc[0]
            escalar_normal  = tablaDf.puntuacion_escalar[tablaDf.puntuacion_percentil == percentil_normal].iloc[0]
            percentil_delayed = baremoData1.percentile[baremoData1.delayed_recall == delayedRecall].iloc[0]
            escalar_delayed = tablaDf.puntuacion_escalar[tablaDf.puntuacion_percentil == percentil_delayed].iloc[0]

        elif (edad>22 and edad<=26):
            if totalRecall <= 17:
                totalRecall = 17
            
            if delayedRecall <= 7:
                delayedRecall = 7
            totalRecall = str(totalRecall)
            delayedRecall = str(delayedRecall)
            percentil_normal = baremoData2.percentile[baremoData2.total_recall == totalRecall].iloc[0]
            escalar_normal  = tablaDf.puntuacion_escalar[tablaDf.puntuacion_percentil == percentil_normal].iloc[0]
            percentil_delayed = baremoData2.percentile[baremoData2.delayed_recall == delayedRecall].iloc[0]
            escalar_delayed = tablaDf.puntuacion_escalar[tablaDf.puntuacion_percentil == percentil_delayed].iloc[0]
        
        elif (edad>26 and edad<=30):
            if totalRecall <= 16:
                totalRecall = 16

            if delayedRecall <= 7:
                delayedRecall = 7
            totalRecall = str(totalRecall)
            delayedRecall = str(delayedRecall)
            percentil_normal = baremoData3.percentile[baremoData3.total_recall == totalRecall].iloc[0]
            escalar_normal  = tablaDf.puntuacion_escalar[tablaDf.puntuacion_percentil == percentil_normal].iloc[0]
            percentil_delayed = baremoData3.percentile[baremoData3.delayed_recall == delayedRecall].iloc[0]
            escalar_delayed = tablaDf.puntuacion_escalar[tablaDf.puntuacion_percentil == percentil_delayed].iloc[0]

        elif (edad>30 and edad<=34):
            if totalRecall <= 16:
                totalRecall = 16
            
            if delayedRecall <= 7:
                delayedRecall = 7
            totalRecall = str(totalRecall)
            delayedRecall = str(delayedRecall)
            percentil_normal = baremoData4.percentile[baremoData4.total_recall == totalRecall].iloc[0]
            escalar_normal  = tablaDf.puntuacion_escalar[tablaDf.puntuacion_percentil == percentil_normal].iloc[0]
            percentil_delayed = baremoData4.percentile[baremoData4.delayed_recall == delayedRecall].iloc[0]
            escalar_delayed = tablaDf.puntuacion_escalar[tablaDf.puntuacion_percentil == percentil_delayed].iloc[0]
        
        elif (edad>34 and edad<=38):
            if totalRecall <= 15:
                totalRecall = 15
            
            if delayedRecall <= 6:
                delayedRecall = 6
            totalRecall = str(totalRecall)
            delayedRecall = str(delayedRecall)
            percentil_normal = baremoData5.percentile[baremoData5.total_recall == totalRecall].iloc[0]
            escalar_normal  = tablaDf.puntuacion_escalar[tablaDf.puntuacion_percentil == percentil_normal].iloc[0]
            percentil_delayed = baremoData5.percentile[baremoData5.delayed_recall == delayedRecall].iloc[0]
            escalar_delayed = tablaDf.puntuacion_escalar[tablaDf.puntuacion_percentil == percentil_delayed].iloc[0]
        
        #print("\nRESULTADOS\n")
        #print ("Puntaje percentil (total recall): " + str(percentil_normal)+"%")
        #print ("Puntaje escalar: (total recall): " + str(escalar_normal))
        #print ("Puntaje percentil (delayed recall): " + str(percentil_delayed)+"%")
        #print ("Puntaje escalar (delayed recall): " + str(escalar_delayed))

        self.puntuacionEscalar = (int(escalar_normal), int(escalar_delayed))
        self.rangoPercentil = (int(percentil_normal), int(percentil_delayed))

"""
if __name__ == "__main__":
    totalRecall = 36
    delayedRecall = 10
    MemoriaVisoespaciaPrueba.calcularPERP(totalRecall, delayedRecall)
"""