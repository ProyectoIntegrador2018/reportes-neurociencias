import pandas as pd
import PruebaModel
from AppCtxt import APPCTXT

class TOLPrueba(PruebaModel.PruebaModel):
    def __init__(self, valores):
        nombre = "Denominación"
        baremos = (pd.read_csv(APPCTXT().get_resource('./Baremos/Baremo_TOL.csv')),
            pd.read_csv(APPCTXT().get_resource('./Baremos/Baremo_TOL_VT_VR_16-19a.csv')),
            pd.read_csv(APPCTXT().get_resource('./Baremos/Baremo_TOL_VT_VR_20-29a.csv')),
            pd.read_csv(APPCTXT().get_resource('./Baremos/Baremo_TOL_VT_VR_30-39a.csv')),
            pd.read_csv(APPCTXT().get_resource('./Baremos/EscolaridadTOL.csv')),
            pd.read_csv(APPCTXT().get_resource('./Baremos/Baremo_TOL_MovimientosTotales.csv')))
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

        totalCorrectos = self.valores[0]
        movimientosTotales = self.valores[1]
        tiempoLatencia = self.valores[2]
        tiempoEjecucion = self.valores[3]
        tiempoResolucion = self.valores[4]
        vt = self.valores[5]
        vr = self.valores[6]

        escolaridad = datos[0]
        edad = datos[1]

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
