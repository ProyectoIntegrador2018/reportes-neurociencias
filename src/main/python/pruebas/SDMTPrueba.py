import pandas as pd
import PruebaModel
from AppCtxt import APPCTXT

class SDMTPrueba(PruebaModel.PruebaModel):
    def __init__(self, valores):
        nombre = "SDMT"
        baremos = (pd.read_csv(APPCTXT().get_resource('./Baremos/TablaSDMT.csv')),
                    pd.read_csv(APPCTXT().get_resource('./Baremos/EscolaridadSDMT.csv')))
        campos = ("C")

        super(SDMTPrueba,self).__init__(nombre, valores, baremos, campos)
    

    def calcularPERP(self, datos):
        tablaSDMT = self.baremos[0]
        tablaescolaridadSDMT = self.baremos[1]

        sdmtVal = self.valores
        escolaridad = datos[0]

        if escolaridad < 8:
            escolaridad = 8
        elif escolaridad > 20:
            escolaridad =20
        
        ajustes = tablaescolaridadSDMT[tablaescolaridadSDMT['Escolaridad'] == escolaridad].iloc[0]
        
        temp = tablaSDMT[(sdmtVal >= tablaSDMT['SDMTMIN']) & (sdmtVal <= tablaSDMT['SDMTMAX'])].iloc[0]
        puntuacionEscalar = temp['Escalar'] + ajustes['SDMT']
        rangoPercentil = (temp['PercentilMin'], temp['PercentilMax'])

        if puntuacionEscalar < 2:
            puntuacionEscalar = 2
        elif puntuacionEscalar > 18:
            puntuacionEscalar = 18


        # print("Puntuacion escalar: ", puntuacionEscalar)
        # print("Rango Percentil:", rangoPercentil)

        self.puntuacionEscalar = (puntuacionEscalar)
        self.rangoPercentil = (rangoPercentil)

        print(self.puntuacionEscalar)
        print(self.rangoPercentil)

