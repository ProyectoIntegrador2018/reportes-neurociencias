#Prueba de LNS
import pandas as pd
import PruebaModel
from AppCtxt import APPCTXT

class StroopPrueba(PruebaModel.PruebaModel):	
    def __init__(self, valores):
        nombre = "STROOP"
        baremos = [pd.read_csv(APPCTXT().get_resource('./Baremos/Baremo_Stroop.csv')),
                    pd.read_csv(APPCTXT().get_resource('./Baremos/Baremo_Stroop_50-56.csv')),
                    pd.read_csv(APPCTXT().get_resource('./Baremos/Baremo_Stroop_57-59.csv')),
                    pd.read_csv(APPCTXT().get_resource('./Baremos/Baremo_Stroop_60-62.csv')),
                    pd.read_csv(APPCTXT().get_resource('./Baremos/Baremo_Stroop_63-65.csv')),
                    pd.read_csv(APPCTXT().get_resource('./Baremos/Baremo_Stroop_66-68.csv')),
                    pd.read_csv(APPCTXT().get_resource('./Baremos/Baremo_Stroop_69-71.csv')),
                    pd.read_csv(APPCTXT().get_resource('./Baremos/Baremo_Stroop_72-74.csv')),
                    pd.read_csv(APPCTXT().get_resource('./Baremos/Baremo_Stroop_75-77.csv')),
                    pd.read_csv(APPCTXT().get_resource('./Baremos/Baremo_Stroop_78-80.csv')),
                    pd.read_csv(APPCTXT().get_resource('./Baremos/Baremo_Stroop_81-90.csv')),
                    pd.read_csv(APPCTXT().get_resource('./Baremos/Escolaridad_Stroop_p.csv')),
                    pd.read_csv(APPCTXT().get_resource('./Baremos/Escolaridad_Stroop_c.csv')),
                    pd.read_csv(APPCTXT().get_resource('./Baremos/Escolaridad_Stroop_pc.csv'))]
        campos = ("P", "C", "I")
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
                P = P

    def calcularPERP(self, datos):
        """
        Método que es empleado para calcular la Puntuación Escalar(PE), como la Percentil(RP)
        Args:
        datos: Lista de información relevante del reporte para calcular los valores de PE y RP (escolaridad, edad)
        """
        stroopData = self.baremos[0]
        edades = list()
        educa = list()
        for x in range(1,11):
            edades.append(self.baremos[x])
        for x in range(11,14):
            educa.append(self.baremos[x])
        P = self.valores[0]
        C = self.valores[1]
        PC = self.valores[2]
        escolaridad = datos[0]
        edad = datos[1]

        if edad >= 50:
            if 50 <= edad <= 56:
                ran = 0
            elif 57 <= edad <= 59:
                ran = 1
            elif 60 <= edad <= 62:
                ran = 2
            elif 63 <= edad <= 65:
                ran = 3
            elif 66 <= edad <= 68:
                ran = 4
            elif 69 <= edad <= 71:
                ran = 5
            elif 72 <= edad <= 74:
                ran = 6
            elif 75 <= edad <= 77:
                ran = 7
            elif 78 <= edad <= 80:
                ran = 8
            elif 81 <= edad <= 90:
                ran = 9
            
            #print(edades[ran]['Percentil Min'][(edades[ran]['Pmin'] <= P) & (P <= edades[ran]['Pmax'])].iloc[0])
            p_percentil = int(edades[ran]['Percentil Min'][(edades[ran]['Pmin'] <= P) & (P <= edades[ran]['Pmax'])].iloc[0])
            p_escalar = int(edades[ran]['Escalar'][(edades[ran]['Pmin'] <= P) & (P <= edades[ran]['Pmax'])].iloc[0])

            c_percentil = int(edades[ran]['Percentil Min'][(edades[ran]['Cmin'] <= C) & (C <= edades[ran]['Cmax'])].iloc[0])
            c_escalar = int(edades[ran]['Escalar'][(edades[ran]['Cmin'] <= C) & (C <= edades[ran]['Cmax'])].iloc[0])
            
            pc_percentil = int(edades[ran]['Percentil Min'][(edades[ran]['PCmin'] <= PC) & (PC <= edades[ran]['PCmax'])].iloc[0])
            pc_escalar = int(edades[ran]['Escalar'][(edades[ran]['PCmin'] <= PC) & (PC <= edades[ran]['PCmax'])].iloc[0])

            NSSa = p_escalar
            p_escalar = educa[0][str(escolaridad)][educa[0].NSSa == NSSa].iloc[0]
            NSSa = c_escalar
            c_escalar = educa[0][str(escolaridad)][educa[1].NSSa == NSSa].iloc[0]
            NSSa = pc_escalar
            pc_escalar = educa[0][str(escolaridad)][educa[2].NSSa == NSSa].iloc[0]
            
            '''
            escalares = list() 
            percentiles = list()
            labels = edades[ran].columns.values
            
            par = 1
            for x in range(5):
                par += 2
                #print(self.valores[x],edades[ran][labels[x][1]])
                escalares.append(int(edades[ran]['Escalar'][(edades[ran][labels[par]] <= self.valores[x]) & (self.valores[x] <= edades[ran][labels[par+1]])].iloc[0]))
                percentiles.append(int(edades[ran]['Percentil Min'][(edades[ran][labels[par]] <= self.valores[x]) & (self.valores[x] <= edades[ran][labels[par+1]])].iloc[0]))

                NSSa = escalares[-1]
                escalares[-1] = educa[x][str(escolaridad)][educa[x].NSSa == NSSa].iloc[0]

            p_escalar = escalares[0]
            c_escalar = escalares[1]
            pc_escalar = escalares[2]

            p_percentil = percentiles[0]
            c_percentil = percentiles[1]
            pc_percentil = percentiles[2]
            '''
        else:
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
