# Prueba Digitos
import pandas as pd
import PruebaModel
from AppCtxt import APPCTXT

class DigitosPrueba(PruebaModel.PruebaModel):
    def __init__(self, valores):
        nombre = "DIGITOS"
        baremos = (pd.read_csv(APPCTXT().get_resource('./Baremos/Digitos.csv')),
                    pd.read_csv(APPCTXT().get_resource('./Baremos/EscolaridadDigitos.csv')),
                    pd.read_csv(APPCTXT().get_resource('./Baremos/Baremo_Digit_50-56.csv')),
                    pd.read_csv(APPCTXT().get_resource('./Baremos/Baremo_Digit_57-59.csv')),
                    pd.read_csv(APPCTXT().get_resource('./Baremos/Baremo_Digit_60-62.csv')),
                    pd.read_csv(APPCTXT().get_resource('./Baremos/Baremo_Digit_63-65.csv')),
                    pd.read_csv(APPCTXT().get_resource('./Baremos/Baremo_Digit_66-68.csv')),
                    pd.read_csv(APPCTXT().get_resource('./Baremos/Baremo_Digit_69-71.csv')),
                    pd.read_csv(APPCTXT().get_resource('./Baremos/Baremo_Digit_72-74.csv')),
                    pd.read_csv(APPCTXT().get_resource('./Baremos/Baremo_Digit_75-77.csv')),
                    pd.read_csv(APPCTXT().get_resource('./Baremos/Baremo_Digit_78-80.csv')),
                    pd.read_csv(APPCTXT().get_resource('./Baremos/Baremo_Digit_81-90.csv')),
                    pd.read_csv(APPCTXT().get_resource('./Baremos/Escolaridad_Digits_f.csv')),
                    pd.read_csv(APPCTXT().get_resource('./Baremos/Escolaridad_Digits_b.csv')))
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

        edades = list()
        educa = list()
        ins = 3
        for x in range(2,12):
            edades.append(self.baremos[x])
        educa.append(self.baremos[12])
        educa.append(self.baremos[13])

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
            cols = edades[ran].columns.values
            #print(edades[ran]['Percentil Min'][(edades[ran]['Pmin'] <= P) & (P <= edades[ran]['Pmax'])].iloc[0])
            param = 3
            #print(edades[ran][cols[1]])
            #print(((edades[ran][cols[param]] <= sdmtVal ) & (sdmtVal  <= edades[ran][cols[param+1]])|((edades[ran][cols[param+1]] <= sdmtVal ) & (sdmtVal  <= edades[ran][cols[param]]))))
            valores = edades[ran][((edades[ran][cols[param]] <= directos) & (directos <= edades[ran][cols[param+1]])|((edades[ran][cols[param+1]] <= directos ) & (directos  <= edades[ran][cols[param]])))]
            percentilDirectos = (int(valores[cols[1]].iloc[0]),int(valores[cols[2]].iloc[0]))
            escalarDirectos = int(valores[cols[0]].iloc[0])

            NSSa = escalarDirectos
            escalarDirectos = educa[0][str(escolaridad)][educa[0].NSSa == NSSa].iloc[0]
            
            param += 2
            valores = edades[ran][((edades[ran][cols[param]] <= inversos) & (inversos <= edades[ran][cols[param+1]])|((edades[ran][cols[param+1]] <= inversos ) & (inversos  <= edades[ran][cols[param]])))]
            percentilInversos = (int(valores[cols[1]].iloc[0]),int(valores[cols[2]].iloc[0]))
            escalarInversos = int(valores[cols[0]].iloc[0])

            NSSa = escalarDirectos
            escalarDirectos = educa[1][str(escolaridad)][educa[1].NSSa == NSSa].iloc[0]
            

        else:

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
