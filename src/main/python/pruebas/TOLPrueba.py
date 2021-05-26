import pandas as pd
import PruebaModel
from AppCtxt import APPCTXT

class TOLPrueba(PruebaModel.PruebaModel):
    def __init__(self, valores):
        nombre = "Torre de Londres"
        baremos = (pd.read_csv(APPCTXT().get_resource('./Baremos/Baremo_TOL.csv')),
                    pd.read_csv(APPCTXT().get_resource('./Baremos/Baremo_TOL_VT_VR_16-19a.csv')),
                    pd.read_csv(APPCTXT().get_resource('./Baremos/Baremo_TOL_VT_VR_20-29a.csv')),
                    pd.read_csv(APPCTXT().get_resource('./Baremos/Baremo_TOL_VT_VR_30-39a.csv')),
                    pd.read_csv(APPCTXT().get_resource('./Baremos/EscolaridadTOL.csv')),
                    pd.read_csv(APPCTXT().get_resource('./Baremos/Baremo_TOL_MovimientosTotales.csv')),
                    pd.read_csv(APPCTXT().get_resource('./Baremos/Baremo_TOL_50-56.csv')),
                    pd.read_csv(APPCTXT().get_resource('./Baremos/Baremo_TOL_57-59.csv')),
                    pd.read_csv(APPCTXT().get_resource('./Baremos/Baremo_TOL_60-62.csv')),
                    pd.read_csv(APPCTXT().get_resource('./Baremos/Baremo_TOL_63-65.csv')),
                    pd.read_csv(APPCTXT().get_resource('./Baremos/Baremo_TOL_66-68.csv')),
                    pd.read_csv(APPCTXT().get_resource('./Baremos/Baremo_TOL_69-71.csv')),
                    pd.read_csv(APPCTXT().get_resource('./Baremos/Baremo_TOL_72-74.csv')),
                    pd.read_csv(APPCTXT().get_resource('./Baremos/Baremo_TOL_75-77.csv')),
                    pd.read_csv(APPCTXT().get_resource('./Baremos/Baremo_TOL_78-80.csv')),
                    pd.read_csv(APPCTXT().get_resource('./Baremos/Baremo_TOL_81-90.csv')),
                    pd.read_csv(APPCTXT().get_resource('./Baremos/Escolaridad_TOL_correct.csv')),
                    pd.read_csv(APPCTXT().get_resource('./Baremos/Escolaridad_TOL_mov.csv')),
                    pd.read_csv(APPCTXT().get_resource('./Baremos/Escolaridad_TOL_time.csv')),
                    pd.read_csv(APPCTXT().get_resource('./Baremos/Escolaridad_TOL_exec.csv')),
                    pd.read_csv(APPCTXT().get_resource('./Baremos/Escolaridad_TOL_solve.csv')))
        campos = ("C", "M", "IT", "ET", "TT", "TV", "RV")
        super(TOLPrueba,self).__init__(nombre, valores, baremos, campos)
    
    def calcularPERP(self, datos):
        """
        Metodo usado para calcular la Puntuacion Escalar y Percentil de la Prueba de Londres

        Args:
            datos: Lista de datos del reporte (escolaridad)
        """
        tablaTOL = self.baremos[0]
        tablaTOL_VT_VR_16_19a = self.baremos[1]
        tablaTOL_VT_VR_20_29a = self.baremos[2]
        tablaTOL_VT_VR_30_39a = self.baremos[3]
        tablaescolaridadTOL = self.baremos[4]
        tablaTOLMovTotales = self.baremos[5]
        edades = list()
        educa = list()
        for x in range(6,16):
            edades.append(self.baremos[x])
        for x in range(16,21):
            educa.append(self.baremos[x])

        totalCorrectos = self.valores[0]
        movimientosTotales = self.valores[1]
        tiempoLatencia = self.valores[2]
        tiempoEjecucion = self.valores[3]
        tiempoResolucion = self.valores[4]
        vt = self.valores[5]
        vr = self.valores[6]

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
            
            escalares = list() 
            percentiles = list()
            labels = [('TotalCorrectoMax','TotalCorrectoMin'),
                    ('TotalMovMax','TotalMovMin'),
                    ('TotalInitTimeMax','TotalInitTimeMin'),
                    ('TotalExecMax','TotalExecMin'),
                    ('TotalTimeMax','TotalTimeMin')]
            for x in range(5):
                #print(self.valores[x],edades[ran][labels[x][1]])
                escalares.append(int(edades[ran]['Escalar'][(edades[ran][labels[x][1]] <= self.valores[x]) & (self.valores[x] <= edades[ran][labels[x][0]])].iloc[0]))
                percentiles.append(int(edades[ran]['Percentil Min'][(edades[ran][labels[x][1]] <= self.valores[x]) & (self.valores[x] <= edades[ran][labels[x][0]])].iloc[0]))

                NSSa = escalares[-1]
                escalares[-1] = educa[x][str(escolaridad)][educa[x].NSSa == NSSa].iloc[0]

            escalarTotalCorrectos = escalares[0]
            escalarMovTotales = escalares[1]
            escalarLatencia = escalares[2]
            escalarEjecucion = escalares[3]
            escalarResolucion = escalares[4]
            
            #escalarVT = escalares[]
            #escalarVR = escalares[]

            percentilTotalCorrectos = percentiles[0]
            percentilMovTotales = percentiles[1]
            percentilLatencia = percentiles[2]
            percentilEjecucion = percentiles[3]
            percentilResolucion = percentiles[4]
            #percentilVT = percentiles[]
            #percentilVR = percentiles[]

            escalarVT = escalarVR = percentilVT = percentilVR = 0
        else:

            if escolaridad < 8:
                escolaridad = 8
            elif escolaridad > 20:
                escolaridad = 20

            if edad < 18:
                edad = 18
            elif edad > 39:
                edad = 39
            
            ajustes = tablaescolaridadTOL[tablaescolaridadTOL['Escolaridad'] == escolaridad].iloc[0]

            tmpTotalCorrectos = tablaTOLMovTotales[tablaTOLMovTotales["Total Correctos"] == totalCorrectos].iloc[0]
            escalarTotalCorrectos = tmpTotalCorrectos['Escalar']
            percentilTotalCorrectos = (tmpTotalCorrectos["PercentilMin"], tmpTotalCorrectos["PercentilMax"])
            # print("escalar total correctos: ", escalarTotalCorrectos)
            # print("percentil total correctos:", percentilTotalCorrectos)

            tmpMovTotales = tablaTOL[(movimientosTotales >= tablaTOL["Mov Totales Min"]) & (movimientosTotales <= tablaTOL["Mov Totales Max"])].iloc[0]
            escalarMovTotales = tmpMovTotales['Escalar'] + ajustes["Movimientos Totales"]

            if escalarMovTotales> 18:
                escalarMovTotales = 18
            elif escalarMovTotales < 2:
                escalarMovTotales = 2

            percentilTotal = tablaTOL[tablaTOL['Escalar'] == escalarMovTotales].iloc[0]
            percentilMovTotales = (percentilTotal["Percentil Min"], percentilTotal["Percentil Max"])


            # print("escalar mov totales: ", escalarMovTotales)
            # print("percentil mov totales: ", percentilMovTotales)


            tmpLatencia = tablaTOL[(tiempoLatencia >= tablaTOL["T Latencia Min"]) & (tiempoLatencia <= tablaTOL["T Latencia Max"])].iloc[0]
            escalarLatencia = tmpLatencia["Escalar Invertido"] + ajustes["Tiempo de Latencia"]
            percentilLatencia = (tmpLatencia["Percentil Invertido Min"], tmpLatencia["Percentil Invertido Max"])

            if escalarLatencia > 18:
                escalarLatencia = 18
            elif escalarLatencia < 2:
                escalarLatencia = 2

            # print("escalar tiempo latencia:", escalarLatencia)
            # print("percentil tiempo latencia: ", percentilLatencia)

            tmpEjecucion = tablaTOL[(tiempoEjecucion >= tablaTOL["T Ejecucion Min"]) & (tiempoEjecucion <= tablaTOL["T Ejecucion Max"])].iloc[0]
            escalarEjecucion = tmpEjecucion['Escalar']
            percentilEjecucion = (tmpEjecucion["Percentil Min"], tmpEjecucion["Percentil Max"])
            # print("escalar ejecucion: ", escalarEjecucion)
            # print("percentil ejecucion: ", percentilEjecucion)

            tmpResolucion = tablaTOL[(tiempoResolucion >= tablaTOL["T Resolucion Min"]) & (tiempoResolucion <= tablaTOL["T Resolucion Max"])].iloc[0]
            escalarResolucion = tmpResolucion['Escalar']
            percentilResolucion = (tmpResolucion["Percentil Min"], tmpResolucion["Percentil Max"])
            # print("escalar resolucion: ", escalarResolucion)
            # print("percentil resolucion: ", percentilResolucion)


            escalarVT = None
            percentilVT = None
            escalarVR = None
            percentilVR = None
            # si la edad se encuentra entre 18 y 19 se usa este pedazo
            # para calcular el escalar y percentil de los campos VT y VR
            if edad >= 18: 
                if edad <= 19:
                    if vt > 3:
                        vt = 3
                    if vr > 3:
                        vr = 3
                    tmpVT = tablaTOL_VT_VR_16_19a[tablaTOL_VT_VR_16_19a["VT"] == vt].iloc[0]
                    escalarVT = tmpVT['Escalar']
                    percentilVT = tmpVT['Percentil']
                    tmpVR = tablaTOL_VT_VR_16_19a[tablaTOL_VT_VR_16_19a["VR"] == vr].iloc[0]
                    escalarVR = tmpVR['Escalar']
                    percentilVR = tmpVR['Percentil']
            
            # si la edad se encuentra entre 20 y 29 se usa este pedazo
            # para calcular el escalar y percentil de los campos VT y VR
            if edad >= 20:
                if edad <= 29:
                    if vt > 4:
                        vt = 4
                    if vr > 3:
                        vr = 3
                    tmpVT = tablaTOL_VT_VR_20_29a[tablaTOL_VT_VR_20_29a["VT"] == vt].iloc[0]
                    escalarVT = tmpVT['Escalar']
                    percentilVT = tmpVT['Percentil']
                    tmpVR = tablaTOL_VT_VR_20_29a[tablaTOL_VT_VR_20_29a["VR"] == vr].iloc[0]
                    escalarVR = tmpVR['Escalar']
                    percentilVR = tmpVR['Percentil']
            
            # si la edad se encuentra entre 30 y 39 se usa este pedazo
            # para calcular el escalar y percentil de los campos VT y VR
            if edad >= 30:
                if edad <= 39:
                    if vt > 3:
                        vt = 3
                    if vr > 4:
                        vr = 4
                    tmpVT = tablaTOL_VT_VR_30_39a[tablaTOL_VT_VR_30_39a['VT'] == vt].iloc[0]
                    escalarVT = tmpVT['Escalar']
                    percentilVT = tmpVT['Percentil']
                    tmpVR = tablaTOL_VT_VR_30_39a[tablaTOL_VT_VR_30_39a['VR'] == vr].iloc[0]
                    escalarVR = tmpVR['Escalar']
                    percentilVR = tmpVR['Percentil']

            
            # print("escalar VT: ", escalarVT)
            # print("percentil VT: ", percentilVT)
            # print("escalar VR: ", escalarVR)
            # print("percentill VR: ", percentilVR)

        self.puntuacionEscalar = (escalarTotalCorrectos, escalarMovTotales, escalarLatencia, escalarEjecucion, escalarResolucion, escalarVT, escalarVR)
        self.rangoPercentil = (percentilTotalCorrectos, percentilMovTotales, percentilLatencia, percentilEjecucion, percentilResolucion, percentilVT, percentilVR)
