# Prueba Denominacion
import pandas as pd

class DenominacionPrueba():
    def __init__(self):
        nombre = "Denominacion"

    def calcularPERP(denomimgs, denomimgT, verbalComplejo, verbalComplejoT, semejanza):
        """
        Metodo que se encarga de calcular la puntiacion escalar y percentil de la prueba de 
        Denominacion
        Parametros: los valores necesarios para realizar los calculos
        """

        baremoDenomImg = pd.read_csv('./Baremos/DenominacionImagenes.csv')
        baremoVerbalComplejo = pd.read_csv('./Baremos/MaterialVerbalComplejo.csv')
        baremoSemejanza = pd.read_csv('./Baremos/SemejanzaAbstraccion.csv')

        escalarDenomImg = None
        percentilDenomImg = None
        escalarDenomImgT = None
        percentilDenomImgT = None
        escalarVerbalComlejo = None
        percentilVerbalComplejo = None
        escalarVerbalComlejoT = None
        percentilVerbalComplejoT = None
        escalarSemejanza = None
        percentilSemejanza = None

        tmpDenominImg = baremoDenomImg[baremoDenomImg["Denominacion imagenes"] == denomimgs]
        if not tmpDenominImg.empty:
            print(tmpDenominImg)
            escalarDenomImg = tmpDenominImg["Puntuacion Escalar"].iloc[0]
            percentilDenomImg = tmpDenominImg["Percentil"].iloc[0]
            print("Resultados denominacion imagenes")
            print("escalar:", escalarDenomImg)
            print("percentil:",percentilDenomImg)
        
        tmpDenomImgT = baremoDenomImg[baremoDenomImg["Denominacion imagenes T"] == denomimgT]
        if not tmpDenomImgT.empty:
            print(tmpDenomImgT)
            escalarDenomImgT = tmpDenomImgT["Puntuacion Escalar"].iloc[0]
            percentilDenomImgT = tmpDenomImgT["Percentil"].iloc[0]
            print("Resultados denominacion imagenes T")
            print("escalar:", escalarDenomImgT)
            print("percentil:",percentilDenomImgT)
        
        tmpVerbalComplejo = baremoVerbalComplejo[baremoVerbalComplejo["Material verbal complejo"] == verbalComplejo]
        if not tmpVerbalComplejo.empty:
            print(tmpVerbalComplejo)
            escalarVerbalComlejo = tmpVerbalComplejo["Puntuacion Escalar"].iloc[0]
            percentilVerbalComplejo = tmpVerbalComplejo["Percentil"].iloc[0]
            print("Resultados material verbal complejo")
            print("Escalar: ", escalarVerbalComlejo)
            print("Percentil:", percentilVerbalComplejo)
        
        tmpVerbalComplejoT = baremoVerbalComplejo[baremoVerbalComplejo["Material verbal complejo T"] == verbalComplejoT]
        if not tmpVerbalComplejoT.empty:
            print(tmpVerbalComplejoT)
            escalarVerbalComlejoT = tmpVerbalComplejoT["Puntuacion Escalar"].iloc[0]
            percentilVerbalComplejoT = tmpVerbalComplejoT["Percentil"].iloc[0]
            print("Resultados material verbal complejo T")
            print("Escalar: ", escalarVerbalComlejoT)
            print("Percentil:", percentilVerbalComplejoT)
        
        tmpSemejanza = baremoSemejanza[baremoSemejanza["SemejanzasAbstraccion"] == semejanza]
        if not tmpSemejanza.empty:
            print(tmpSemejanza)
            escalarSemejanza = tmpSemejanza["Puntuacion Escalar"].iloc[0]
            percentilSemejanza = tmpSemejanza["Percentil"].iloc[0]
            print("Resultados semejanzas-abstraccion")
            print("Escalar: ", escalarSemejanza)
            print("Percentil: ", percentilSemejanza)

# if __name__ == "__main__":
#     denomimgs = 0
#     denomimgT = 41
#     verbalComplejo = 8
#     verbalComplejoT = 26
#     semejanza = 5
#     DenominacionPrueba.calcularPERP(denomimgs, denomimgT, verbalComplejo, verbalComplejoT, semejanza)