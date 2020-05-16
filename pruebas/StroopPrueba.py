#Prueba de LNS
import pandas as pd
import PruebaModel

class StroopPrueba(PruebaModel.PruebaModel):	
    def __init__(self, valores):
        nombre = "Stroop"
        baremos = (pd.read_csv('./Baremos/Baremo_Stroop.csv'))
        campos = ("P", "C", "PC")
        super(StroopPrueba,self).__init__(nombre, valores, baremos, campos)
        
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
