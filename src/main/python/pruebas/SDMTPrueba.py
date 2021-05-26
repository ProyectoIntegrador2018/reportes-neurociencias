import pandas as pd
import PruebaModel
from AppCtxt import APPCTXT

class SDMTPrueba(PruebaModel.PruebaModel):
    def __init__(self, valores):
        nombre = "SDMT"
        baremos = (pd.read_csv(APPCTXT().get_resource('./Baremos/TablaSDMT.csv')),
                    pd.read_csv(APPCTXT().get_resource('./Baremos/EscolaridadSDMT.csv')),
                    pd.read_csv(APPCTXT().get_resource('./Baremos/Baremo_SDMT_50-56.csv')),
                    pd.read_csv(APPCTXT().get_resource('./Baremos/Baremo_SDMT_57-59.csv')),
                    pd.read_csv(APPCTXT().get_resource('./Baremos/Baremo_SDMT_60-62.csv')),
                    pd.read_csv(APPCTXT().get_resource('./Baremos/Baremo_SDMT_63-65.csv')),
                    pd.read_csv(APPCTXT().get_resource('./Baremos/Baremo_SDMT_66-68.csv')),
                    pd.read_csv(APPCTXT().get_resource('./Baremos/Baremo_SDMT_69-71.csv')),
                    pd.read_csv(APPCTXT().get_resource('./Baremos/Baremo_SDMT_72-74.csv')),
                    pd.read_csv(APPCTXT().get_resource('./Baremos/Baremo_SDMT_75-77.csv')),
                    pd.read_csv(APPCTXT().get_resource('./Baremos/Baremo_SDMT_78-80.csv')),
                    pd.read_csv(APPCTXT().get_resource('./Baremos/Baremo_SDMT_81-90.csv')),
                    pd.read_csv(APPCTXT().get_resource('./Baremos/Escolaridad_SDMT.csv')))
        campos = ("C")

        super(SDMTPrueba,self).__init__(nombre, valores, baremos, campos)
    

    def calcularPERP(self, datos):
        tablaSDMT = self.baremos[0]
        tablaescolaridadSDMT = self.baremos[1]

        edades = list()
        educa = list()
        ins = 3
        for x in range(2,12):
            edades.append(self.baremos[x])
        educa.append(self.baremos[12])

        sdmtVal = self.valores
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
            valores = edades[ran][((edades[ran][cols[param]] <= sdmtVal) & (sdmtVal <= edades[ran][cols[param+1]])|((edades[ran][cols[param+1]] <= sdmtVal ) & (sdmtVal  <= edades[ran][cols[param]])))]
            print(valores)
            rangoPercentil = (int(valores[cols[1]].iloc[0]),int(valores[cols[2]].iloc[0]))
            puntuacionEscalar = int(valores[cols[0]].iloc[0])

            NSSa = puntuacionEscalar
            print(educa[0])
            print(educa[0][str(escolaridad)])
            #print[[educa[0].NSSa == str(NSSa)]]
            puntuacionEscalar = educa[0][str(escolaridad)][educa[0].NSSa == NSSa].iloc[0]

        else:

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

