import unittest
from PyQt5 import QtWidgets, QtCore

from PyQt5.QtTest import QTest
from test.UsesQApplication import UsesQApplication
# from test.UsersQApplication import UsesQApplication
from MasterController import MasterController

class TestMainWindow(UsesQApplication):

    def setUp(self):
        self.app = QtWidgets.QApplication([])
        self.app.setStyleSheet(open('app.css').read())
        self.ui = MasterController()

    def tearDown(self):
        self.app.deleteLater()

    def fillInfo(self, form, info):
        field = form.findChild(QtWidgets.QLineEdit, "leName")
        field.clear()
        QTest.keyClicks(field, info["nombre"])
        self.assertEqual(field.text(), info["nombre"])

        field = form.findChild(QtWidgets.QLineEdit, "leId")
        field.clear()
        QTest.keyClicks(field, info["id"])
        self.assertEqual(field.text(), info["id"])

        field = form.findChild(QtWidgets.QLineEdit, "leExaminer")
        field.clear()
        QTest.keyClicks(field, info["examinador"])
        self.assertEqual(field.text(), info["examinador"])
        
        field = form.findChild(QtWidgets.QSpinBox, "sbAge")
        field.setValue(int(info["edad"]))
        self.assertEqual(field.value(), int(info["edad"]))
        
        field = form.findChild(QtWidgets.QSpinBox, "sbEscolaridad")
        field.setValue(int(info["educacion"]))
        self.assertEqual(field.value(), int(info["educacion"]))

        field = form.findChild(QtWidgets.QComboBox, "cbSexo")
        itemIdx = field.findText(info["genero"])
        self.assertNotEqual(itemIdx, -1)
        field.setCurrentIndex(itemIdx)
        self.assertEqual(field.currentText(), info["genero"])

        field = form.findChild(QtWidgets.QDateEdit, "deFechaNacimiento")
        date = QtCore.QDate(*info["fechaNacimiento"])
        field.setDate(date)
        self.assertEqual(field.date(), date)

        field = form.findChild(QtWidgets.QComboBox, "cbLateralidad")
        itemIdx = field.findText(info["lateralidad"])
        self.assertNotEqual(itemIdx, -1)
        field.setCurrentIndex(itemIdx)
        self.assertEqual(field.currentText(), info["lateralidad"])

        field = form.findChild(QtWidgets.QDateEdit, "deFecha")
        date = QtCore.QDate(*info["fecha"])
        field.setDate(date)
        self.assertEqual(field.date(), date)

        field = form.findChild(QtWidgets.QLineEdit, "leCarrera")
        field.clear()
        QTest.keyClicks(field, info["carrera"])
        self.assertEqual(field.text(), info["carrera"])

        field = form.findChild(QtWidgets.QSpinBox, "sbSemestre")
        field.setValue(int(info["semestre"]))
        self.assertEqual(field.value(), int(info["semestre"]))

        field = form.findChild(QtWidgets.QLineEdit, "leEquipo")
        field.clear()
        QTest.keyClicks(field, info["equipo"])
        self.assertEqual(field.text(), info["equipo"])

        field = form.findChild(QtWidgets.QLineEdit, "leDeporte")
        field.clear()
        QTest.keyClicks(field, info["deporte"])
        self.assertEqual(field.text(), info["deporte"])

    def test_select_all(self):
        ## test menu selection automatic
        view = self.ui.nextWindow

        checkbox = view.findChild(QtWidgets.QCheckBox, "checkBoxPruebaFluidezVerbal")
        self.assertEqual(checkbox.checkState(), QtCore.Qt.Unchecked)
        QTest.mouseClick(checkbox, QtCore.Qt.LeftButton)
        self.assertEqual(checkbox.checkState(), QtCore.Qt.Checked)

        checkbox = view.findChild(QtWidgets.QCheckBox, "checkBoxPruebaDenominacion")
        self.assertEqual(checkbox.checkState(), QtCore.Qt.Unchecked)
        QTest.mouseClick(checkbox, QtCore.Qt.LeftButton)
        self.assertEqual(checkbox.checkState(), QtCore.Qt.Checked)

        checkbox = view.findChild(QtWidgets.QCheckBox, "checkBoxComprensionVerbal")
        self.assertEqual(checkbox.checkState(), QtCore.Qt.Unchecked)
        QTest.mouseClick(checkbox, QtCore.Qt.LeftButton)
        self.assertEqual(checkbox.checkState(), QtCore.Qt.Checked)

        checkbox = view.findChild(QtWidgets.QCheckBox, "checkBoxPruebaMemoriaVisoespacial")
        self.assertEqual(checkbox.checkState(), QtCore.Qt.Unchecked)
        QTest.mouseClick(checkbox, QtCore.Qt.LeftButton)
        self.assertEqual(checkbox.checkState(), QtCore.Qt.Checked)

        checkbox = view.findChild(QtWidgets.QCheckBox, "checkBoxPruebaTMT")
        self.assertEqual(checkbox.checkState(), QtCore.Qt.Unchecked)
        checkbox.click()
        # QTest.mouseClick(checkbox, QtCore.Qt.LeftButton)
        self.assertEqual(checkbox.checkState(), QtCore.Qt.Checked)

        checkbox = view.findChild(QtWidgets.QCheckBox, "checkBoxPruebaAbstraccion")
        self.assertEqual(checkbox.checkState(), QtCore.Qt.Unchecked)
        checkbox.click()
        # QTest.mouseClick(checkbox, QtCore.Qt.LeftButton)
        self.assertEqual(checkbox.checkState(), QtCore.Qt.Checked)

        checkbox = view.findChild(QtWidgets.QCheckBox, "checkBoxPruebaDigitos")
        self.assertEqual(checkbox.checkState(), QtCore.Qt.Unchecked)
        checkbox.click()
        # QTest.mouseClick(checkbox, QtCore.Qt.LeftButton)
        self.assertEqual(checkbox.checkState(), QtCore.Qt.Checked)

        checkbox = view.findChild(QtWidgets.QCheckBox, "checkBoxPruebaSDMT")
        self.assertEqual(checkbox.checkState(), QtCore.Qt.Unchecked)
        checkbox.click()
        # QTest.mouseClick(checkbox, QtCore.Qt.LeftButton)
        self.assertEqual(checkbox.checkState(), QtCore.Qt.Checked)

        checkbox = view.findChild(QtWidgets.QCheckBox, "checkBoxPruebaLNS")
        self.assertEqual(checkbox.checkState(), QtCore.Qt.Unchecked)
        checkbox.click()
        # QTest.mouseClick(checkbox, QtCore.Qt.LeftButton)
        self.assertEqual(checkbox.checkState(), QtCore.Qt.Checked)

        checkbox = view.findChild(QtWidgets.QCheckBox, "checkBoxPruebaD2")
        self.assertEqual(checkbox.checkState(), QtCore.Qt.Unchecked)
        checkbox.click()
        # QTest.mouseClick(checkbox, QtCore.Qt.LeftButton)
        self.assertEqual(checkbox.checkState(), QtCore.Qt.Checked)

        checkbox = view.findChild(QtWidgets.QCheckBox, "checkBoxPruebaHopkins")
        self.assertEqual(checkbox.checkState(), QtCore.Qt.Unchecked)
        checkbox.click()
        # QTest.mouseClick(checkbox, QtCore.Qt.LeftButton)
        self.assertEqual(checkbox.checkState(), QtCore.Qt.Checked)

        checkbox = view.findChild(QtWidgets.QCheckBox, "checkBoxPruebaStroop")
        self.assertEqual(checkbox.checkState(), QtCore.Qt.Unchecked)
        checkbox.click()
        # QTest.mouseClick(checkbox, QtCore.Qt.LeftButton)
        self.assertEqual(checkbox.checkState(), QtCore.Qt.Checked)

        checkbox = view.findChild(QtWidgets.QCheckBox, "checkBoxTorreDeLondres")
        self.assertEqual(checkbox.checkState(), QtCore.Qt.Unchecked)
        checkbox.click()
        # QTest.mouseClick(checkbox, QtCore.Qt.LeftButton)
        self.assertEqual(checkbox.checkState(), QtCore.Qt.Checked)

        checkbox = view.findChild(QtWidgets.QCheckBox, "checkBoxPruebaMotivosDeportivos")
        self.assertEqual(checkbox.checkState(), QtCore.Qt.Unchecked)
        checkbox.click()
        # QTest.mouseClick(checkbox, QtCore.Qt.LeftButton)
        self.assertEqual(checkbox.checkState(), QtCore.Qt.Checked)

        checkbox = view.findChild(QtWidgets.QCheckBox, "checkBoxPruebaDePittsburgh")
        self.assertEqual(checkbox.checkState(), QtCore.Qt.Unchecked)
        checkbox.click()
        # QTest.mouseClick(checkbox, QtCore.Qt.LeftButton)
        self.assertEqual(checkbox.checkState(), QtCore.Qt.Checked)

        checkbox = view.findChild(QtWidgets.QCheckBox, "checkBoxPruebaSCL90")
        self.assertEqual(checkbox.checkState(), QtCore.Qt.Unchecked)
        checkbox.click()
        # QTest.mouseClick(checkbox, QtCore.Qt.LeftButton)
        self.assertEqual(checkbox.checkState(), QtCore.Qt.Checked)

        label = view.findChild(QtWidgets.QLabel, "labelPruebasSeleccionadasDisplay")
        self.assertEqual(label.text(), "16")

        button = view.findChild(QtWidgets.QPushButton, "pushButtonContinuar")
        QTest.mouseClick(button, QtCore.Qt.LeftButton)

        ## test main window
        view = self.ui.nextWindow
        user_info = {
            "nombre": 'Bernardo',
            "id": '123',
            "examinador": 'Juan',
            "edad": '24',
            "educacion": '15',
            "genero": 'Masculino',
            "fechaNacimiento": [1996,6,1], #year, month, day
            "lateralidad": 'Diestro',
            "fecha": [2020,11,1],
            "carrera": 'ITC',
            "semestre": '9',
            "equipo": "No Aplica",
            "deporte": "No Aplica"
        }
        self.fillInfo(view, user_info)
        button = view.findChild(QtWidgets.QPushButton, "pbStart")
        QTest.mouseClick(button, QtCore.Qt.LeftButton)

        ## click next multiple times
        # PruebaFluidezVerbal
        view = self.ui.nextWindow
        button = view.findChild(QtWidgets.QPushButton, "pbStart")
        QTest.mouseClick(button, QtCore.Qt.LeftButton)

        # PruebaDenominacion
        view = self.ui.nextWindow
        button = view.findChild(QtWidgets.QPushButton, "pbStart")
        QTest.mouseClick(button, QtCore.Qt.LeftButton)

        # ComprensionVerbal
        view = self.ui.nextWindow
        button = view.findChild(QtWidgets.QPushButton, "pbStart")
        QTest.mouseClick(button, QtCore.Qt.LeftButton)
        
        # PruebaMemoriaVisoespacial
        view = self.ui.nextWindow
        button = view.findChild(QtWidgets.QPushButton, "pbStart")
        QTest.mouseClick(button, QtCore.Qt.LeftButton)

        # PruebaTMT
        view = self.ui.nextWindow
        button = view.findChild(QtWidgets.QPushButton, "pbStart")
        QTest.mouseClick(button, QtCore.Qt.LeftButton)

        # PruebaAbstraccion
        view = self.ui.nextWindow
        button = view.findChild(QtWidgets.QPushButton, "pbStart")
        QTest.mouseClick(button, QtCore.Qt.LeftButton)

        # PruebaDigitos
        view = self.ui.nextWindow
        button = view.findChild(QtWidgets.QPushButton, "pbStart")
        QTest.mouseClick(button, QtCore.Qt.LeftButton)

        # PruebaSDMT
        view = self.ui.nextWindow
        button = view.findChild(QtWidgets.QPushButton, "pbStart")
        QTest.mouseClick(button, QtCore.Qt.LeftButton)

        # PruebaLNS
        view = self.ui.nextWindow
        button = view.findChild(QtWidgets.QPushButton, "pbStart")
        QTest.mouseClick(button, QtCore.Qt.LeftButton)

        # PruebaD2
        view = self.ui.nextWindow
        button = view.findChild(QtWidgets.QPushButton, "pbStart")
        QTest.mouseClick(button, QtCore.Qt.LeftButton)

        # PruebaHopkins
        view = self.ui.nextWindow
        button = view.findChild(QtWidgets.QPushButton, "pbStart")
        QTest.mouseClick(button, QtCore.Qt.LeftButton)

        # PruebaStroop
        view = self.ui.nextWindow
        button = view.findChild(QtWidgets.QPushButton, "pbStart")
        QTest.mouseClick(button, QtCore.Qt.LeftButton)

        # TorreDeLondres
        view = self.ui.nextWindow
        button = view.findChild(QtWidgets.QPushButton, "pbStart")
        QTest.mouseClick(button, QtCore.Qt.LeftButton)

        # PruebaMotivosDeportivos
        view = self.ui.nextWindow
        button = view.findChild(QtWidgets.QPushButton, "pbStart")
        QTest.mouseClick(button, QtCore.Qt.LeftButton)

        # PruebaDePittsburgh
        view = self.ui.nextWindow
        button = view.findChild(QtWidgets.QPushButton, "pbStart")
        QTest.mouseClick(button, QtCore.Qt.LeftButton)

        # PruebaSCL90
        view = self.ui.nextWindow
        button = view.findChild(QtWidgets.QPushButton, "pbStart")
        QTest.mouseClick(button, QtCore.Qt.LeftButton)



if __name__ == '__main__':
    unittest.main()