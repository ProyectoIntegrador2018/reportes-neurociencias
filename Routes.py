from PyQt5 import QtWidgets
from MainWindowController import MainWindowController


class Router:
    def __init__(self, routingOrder):
        """
        Método para tener las rutas seleccionadas al principio 
        Args:
            routingOrder: Arreglo de strings con las keys con orden en routes. 
        """
        self.routes = {
            "seleccionarPruebas": {
                "name": "Seleccionar pruebas",
                "controller": None,
                "view": None,
                "switch_fun": None
            },
            "informacionSujeto": {
                "name": 'Información de Sujeto',
                "controller": None,
                "view": None,
                "switch_fun": None
            },
            "fluidezVerbal": {
                "name": 'Prueba Fluidez Verbal',
                "controller": None,
                "view": None,
                "switch_fun": None
            },
            "denominacion": {
                "name": 'Prueba Denominación',
                "controller": None,
                "view": None,
                "switch_fun": None
            },
            "comprensionVerbal": {
                "name": 'Prueba Comprensión Verbal',
                "controller": None,
                "view": None,
                "switch_fun": None
            },
            "memoriaVisoespacial": {
                "name": 'Prueba Memoria Visoespacial',
                "controller": None,
                "view": None,
                "switch_fun": None
            },
            "tmt": {
                "name": 'Prueba TMT',
                "controller": None,
                "view": None,
                "switch_fun": None
            },
            "abstraccion": {
                "name": 'Prueba Abstracción',
                "controller": None,
                "view": None,
                "switch_fun": None
            },
            "digitos": {
                "name": 'Prueba Dígitos',
                "controller": None,
                "view": None,
                "switch_fun": None
            },
            "sdmt": {
                "name": 'Prueba SDMT',
                "controller": None,
                "view": None,
                "switch_fun": None
            },
            "lns": {
                "name": 'Prueba LNS',
                "controller": None,
                "view": None,
                "switch_fun": None
            },
            "d2": {
                "name": 'Prueba D2',
                "controller": None,
                "view": None,
                "switch_fun": None
            },
            "hopkins": {
                "name": 'Prueba Hopkins',
                "controller": None,
                "view": None,
                "switch_fun": None
            },
            "stroop": {
                "name": 'Prueba Stroop',
                "controller": None,
                "view": None,
                "switch_fun": None
            },
            "torreLondres": {
                "name": 'Prueba Torre de Londres',
                "controller": None,
                "view": None,
                "switch_fun": None
            },
            "motivoDeportivo": {
                "name": 'Prueba Motivos Deportivos',
                "controller": None,
                "view": None,
                "switch_fun": None
            },
            "pittsburgh": {
                "name": 'Prueba de Pittsburgh',
                "controller": None,
                "view": None,
                "switch_fun": None
            },
            "scl90": {
                "name": 'Prueba SCL-90',
                "controller": None,
                "view": None,
                "switch_fun": None
            },
            "report": {
                "name": 'Reporte',
                "controller": None,
                "view": None,
                "switch_fun": None
            },
            "dummyWindow": {
                "name": 'NA',
                "controller": None,
                "view": None,
                "switch_fun": None
            },
        }
        self.updatePossibleRoutes(routingOrder)

    def updatePossibleRoutes(self, routingOrder):
        self.possibleRoutes = routingOrder
        self.entries = None
        self.entries = self.getEntries()

    def __len__(self):
        return len(self.entries)

    def getEntries(self):
        if self.entries is not None:
            return self.entries

        entries = []
        for key, fun in self.possibleRoutes:
            if not key in self.routes:
                raise NameError("Not a possible route called {}".format(key))

            self.routes[key]["switch_fun"] = fun
            entries.append(key)

        return entries

    def getEntrieNames(self):
        return [self.routes[key]["name"] for key in self.entries][:-1]

    def getRouteViewAndController(self, routeKey):
        view = self.getView(routeKey)
        controller = self.getController(routeKey)
        return view, controller

    def setView(self, routeKey, value=None):
        self.routes[routeKey]["view"] = value

    def getView(self, routeKey):
        if self.routes[routeKey]["view"] is None:
            self.setView(routeKey, QtWidgets.QWidget())

        return self.routes[routeKey]["view"]

    # *args dame todos los argumentos restantes
    def setController(self, routeKey, controller, *args):
        if controller is None:
            self.routes[routeKey]["controller"] = controller
            return

        view = self.getView(routeKey)
        params = [view]
        for arg in args:
            params.append(arg)

        tmp_controller = controller(*params)
        next_fun = self.findNextSwitchWindowFun(routeKey)
        tmp_controller.switch_window.connect(next_fun)
        self.routes[routeKey]["controller"] = tmp_controller

    def getController(self, routeKey):
        return self.routes[routeKey]["controller"]

    def resetRouterViews(self, skipMain):
        for key in self.possibleRoutes:
            if key[0] == "informacionSujeto"\
                    or key[0] == "seleccionarPruebas":  # TODO change for intial view
                continue

            self.setView(key[0], None)

    def resetRouterControllers(self, skipMain):
        for key in self.possibleRoutes:
            if key[0] == "informacionSujeto"\
                    or key[0] == "seleccionarPruebas":  # TODO change for intial view
                continue

            self.setController(key[0], None)

    def findNextSwitchWindowFun(self, currentKey):
        if currentKey == "report":
            return self.routes["dummyWindow"]["switch_fun"]

        if currentKey == "informacionSujeto":
            return self.routes["informacionSujeto"]["switch_fun"]

        if currentKey == "seleccionarPruebas":
            return self.routes["seleccionarPruebas"]["switch_fun"]

        for idx, [key, _] in enumerate(self.possibleRoutes):
            if currentKey != key:
                continue

            nextKey = self.possibleRoutes[idx+1][0]
            # print(nextKey, self.routes[nextKey])
            return self.routes[nextKey]["switch_fun"]

    def getNextPageKey(self, currentKey):
        for idx, [key, _] in enumerate(self.possibleRoutes):
            if currentKey != key:
                continue

            nextKey = self.possibleRoutes[idx+1][0]
            return nextKey
