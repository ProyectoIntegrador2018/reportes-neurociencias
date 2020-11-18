#Prueba de Pittsburgh
import pandas as pd
import PruebaModel
from AppCtxt import APPCTXT

class PittsburghPrueba(PruebaModel.PruebaModel):	
    def __init__(self, valores):
        nombre = "PSQI"
        baremos = pd.read_csv(APPCTXT().get_resource('./Baremos/Pittsburgh.csv'))
        campos = ("1.", "2.", "3.", "4.", "5.", "6.", "7.", "total")
        super(PittsburghPrueba,self).__init__(nombre, valores, baremos, campos)
    def calcularPERP(self, datos):
        """
        Método para obtener el feedback de la puntuación toal de la prueba de Pittsburgh
        datos: Lista de información relevante del reporte para calcular los valores de PE y RP (escolaridad, género, etc.)
        """
        psqiTabla = self.baremos
        comp1 = self.valores[0]
        comp2 = self.valores[1]
        comp3 = self.valores[2]
        comp4 = self.valores[3]
        comp5 = self.valores[4]
        comp6 = self.valores[5]
        comp7 = self.valores[6]
        puntuacion_total = comp1+comp2+comp3+comp4+comp5+comp6+comp7
        retro = psqiTabla.feedback[psqiTabla.puntuacion == puntuacion_total].iloc[0]
        
        #####################################################################################
        # # En los Baremos previstos, no se especifican los valores de la puntuación Escalar. #
        # #####################################################################################
        tempValores = self.valores
        self.valores = (tempValores[0], tempValores[1], tempValores[2], tempValores[3], tempValores[4], tempValores[5], tempValores[6], puntuacion_total)
        self.puntuacionEscalar = (comp1,comp2,comp3,comp4,comp5,comp6,comp7,puntuacion_total)
        self.rangoPercentil = (retro)