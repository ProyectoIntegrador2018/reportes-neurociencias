# Prueba Memoria Visoespacia
import pandas as pd

class MemoriaVisoespaciaPrueba():
    def __init__(self):
        nombre = "MemoriaVisoespacia"

        # super(DenominacionPrueba,self).__init__(nombre, valores)

    def calcularPERP(totalRecall, delayedRecall):
        """
        Metodo que se encarga de calcular la puntiacion escalar y percentil de la prueba de 
        Denominacion
        Parametros: los valores necesarios para realizar los calculos
        """

        baremoData = pd.read_csv('./Baremos/Baremo_BVMT-R-1.csv')
        tablaDf = pd.read_csv('./Baremos/Tabla_Conversión_Psicométrica_Completa.csv')

        totalRecall = str(totalRecall)
        delayedRecall = str(delayedRecall)
        percentil_normal = baremoData.percentile[baremoData.total_recall == totalRecall].item()
        escalar_normal  = tablaDf.puntuacion_escalar[tablaDf.puntuacion_percentil == percentil_normal].iloc[0]
        percentil_delayed = baremoData.percentile[baremoData.delayed_recall == delayedRecall].item()
        escalar_delayed = tablaDf.puntuacion_escalar[tablaDf.puntuacion_percentil == percentil_delayed].iloc[0]
        print("\nRESULTADOS\n")
        print ("Puntaje percentil (total recall): " + str(percentil_normal)+"%")
        print ("Puntaje escalar: (total recall): " + str(escalar_normal))
        print ("Puntaje percentil (delayed recall): " + str(percentil_delayed)+"%")
        print ("Puntaje escalar (delayed recall): " + str(escalar_delayed))

"""
if __name__ == "__main__":
    totalRecall = 36
    delayedRecall = 10
    MemoriaVisoespaciaPrueba.calcularPERP(totalRecall, delayedRecall)
"""