# Prueba Denominacion
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QUrl, QDir
import pandas as pd
import PruebaModel

class DenominacionPrueba(PruebaModel.PruebaModel):
    def __init__(self,valores):
        nombre = "Denominacion"
        baremoDenominacion = QUrl(QDir.currentPath()+"/Baremos/DenominacionImagenes.csv").toString()
        baremos = (pd.read_csv(baremoDenominacion))

        super(DenominacionPrueba,self).__init__(nombre, valores, baremos)

    def calcularPERP(self):
        """
        Metodo que se encarga de calcular la puntiacion escalar y percentil de la prueba de 
        Denominacion
        Parametros: los valores necesarios para realizar los calculos
        """

        baremoDenomImg = self.baremos
        denomimgs = self.valores[0]
        denomimgT = self.valores[1]

        escalarDenomImg = None
        percentilDenomImg = None
        escalarDenomImgT = None
        percentilDenomImgT = None

        tmpDenominImg = baremoDenomImg[baremoDenomImg["Denominacion imagenes"] == denomimgs]
        if not tmpDenominImg.empty:
            escalarDenomImg = tmpDenominImg["DenomImgEscalar"].iloc[0]
            percentilDenomImg = tmpDenominImg["DenomImgPercentil"].iloc[0]

        
        tmpDenomImgT = baremoDenomImg[baremoDenomImg["Denominacion imagenes T"] == denomimgT]
        if not tmpDenomImgT.empty:
            escalarDenomImgT = tmpDenomImgT["DenomImgTEscalar"].iloc[0]
            percentilDenomImgT = tmpDenomImgT["DenomImgTPercentil"].iloc[0]

        self.puntuacionEscalar = (int(escalarDenomImg), int(escalarDenomImgT))
        self.rangoPercentil = (int(percentilDenomImg), int(percentilDenomImgT))


# # Pruebas unitarias
# if __name__ == "__main__":
#     denomimgs = 2
#     denomimgT = 22
#     DenominacionPrueba.calcularPERP(denomimgs, denomimgT)