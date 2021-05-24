# Prueba Digitos
import pandas as pd
import PruebaModel
from AppCtxt import APPCTXT

class DigitosPrueba(PruebaModel.PruebaModel):
    def __init__(self, valores):
        nombre = "DIGITOS"
        baremos = (pd.read_csv(APPCTXT().get_resource('./Baremos/Digitos.csv')),
                    pd.read_csv(APPCTXT().get_resource('./Baremos/EscolaridadDigitos.csv')))
        campos = ("DD", "DI")

        super(DigitosPrueba,self).__init__(nombre, valores, baremos, campos)

    def calcularPERP(self, datos):
        """
        Metodo para calcular la puntuacion escalar (PE) y percentil (RP)
        de la prueba de Digitos
        Argumentos:
            datos: Lista de informacion relevante del reporte para calcular los valores PE y RP
        """
        print("Directos " + str(self.valores[0]))
        print("Inversos " + str(self.valores[1]))
        directos = self.valores[0]
        inversos = self.valores[1]

        tablaDigitos = self.baremos[0]
        tablaEscolaridadDigitos = self.baremos[1]
        escolaridad = datos[0]

        if escolaridad < 8:
            escolaridad = 8
        elif escolaridad > 20:
            escolaridad = 20
        

        ajustes = tablaEscolaridadDigitos[tablaEscolaridadDigitos["Escolaridad"] == escolaridad].iloc[0]

        tmpDirectos = tablaDigitos[tablaDigitos["Directos"] == directos].iloc[0]
        escalarDirectos = tmpDirectos['Escalar'] + ajustes['Directos']
        percentilDirectos = (tmpDirectos["Percentil Min"], tmpDirectos["Percentil Max"])
        print("Escalar directos: ", escalarDirectos)
        print("percentil directos:", percentilDirectos)

        tmpInversos = tablaDigitos[tablaDigitos["Inversos"] == inversos].iloc[0]
        escalarInversos = tmpInversos['Escalar'] + ajustes['Inversos']
        percentilInversos = (tmpInversos["Percentil Min"], tmpInversos["Percentil Max"])
        print("Escalar inversos", escalarInversos)
        print("percentil inversos:", percentilInversos)

        self.puntuacionEscalar = (escalarDirectos, escalarInversos)
        self.rangoPercentil = (percentilDirectos, percentilInversos)
        print( self.puntuacionEscalar)
        print(self.rangoPercentil)
