# Prueba Memoria Visoespacia
import pandas as pd
import PruebaModel

class MemoriaVisoespaciaPrueba(PruebaModel.PruebaModel):
    def __init__(self, valores):
        nombre = "MemoriaVisoespacia"
        baremos = (pd.read_csv('./Baremos/Baremo_BVMT-R-1.csv'), pd.read_csv('./Baremos/Tabla_Conversión_Psicométrica_Completa.csv'))

        super(MemoriaVisoespaciaPrueba,self).__init__(nombre, valores, baremos)

    def calcularPERP(self):
        """
        Metodo que se encarga de calcular la puntiacion escalar y percentil de la prueba de 
        Memoria Visoespacia
        Parametros: total recall y delayed recall, que arrojan dos resultados diferentes
        """

        baremoData = self.baremos[0]
        tablaDf = self.baremos[1]

        totalRecall = self.valores[0]
        delayedRecall = self.valores[1]

        totalRecall = str(totalRecall)
        delayedRecall = str(delayedRecall)
        percentil_normal = baremoData.percentile[baremoData.total_recall == totalRecall].item()
        escalar_normal  = tablaDf.puntuacion_escalar[tablaDf.puntuacion_percentil == percentil_normal].iloc[0]
        percentil_delayed = baremoData.percentile[baremoData.delayed_recall == delayedRecall].item()
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