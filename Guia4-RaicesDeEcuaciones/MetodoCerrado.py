import sympy
from sympy.plotting import plot


class MetodoCerrado(object):
    "Clase Que usa Metodos de Biseccion y Falsa Posicion para hallar la raiz de una funcíon por aproximación"

    def __init__(self, funcion, xl, xu):
        "Funcion: str, xl: float, xu:float"
        self.funcion = sympy.sympify(funcion)
        self.xl = xl
        self.xu = xu
        self.xr = None
        self.valores = []
        self.x = sympy.symbols('x', real=True)

    def getXRByBiseccion(self):
        return (self.xl + self.xu) * 0.5

    def getXRByFalsaPosicion(self):
        numerador = self.funcion.subs({'x': self.xu}) * (self.xl - self.xu)
        denominador = self.funcion.subs(
            {'x': self.xl}) - self.funcion.subs({'x': self.xu})
        return self.xu - (numerador / denominador)

    def calcularErrorAproximado(self):
        n = len(self.valores)
        if(n > 0):
            error = ((self.xr - self.valores[n-1]['xr']) / self.xr) * 100
            return error
        else:
            return None

    def evaluarXR(self):
        ea = self.calcularErrorAproximado()
        self.valores.append(
            {"xl": self.xl, "xu": self.xu, "xr": self.xr, "error": ea})
        fdex = self.funcion.subs({'x': self.xr})
        fdexl = self.funcion.subs({'x': self.xl})
        if(fdexl*fdex <= 0):
            self.xu = self.xr
        else:
            self.xl = self.xr
        return self.valores

    def metodoBiseccion(self):
        "Implementa el método de Biseccion"
        self.xr = self.getXRByBiseccion()
        return self.evaluarXR()

    def metodoFalsaPosicion(self):
        "Implementa el método de Falsa Posicion"
        self.xr = self.getXRByFalsaPosicion()
        return self.evaluarXR()

    def showResults(self):
        print("| {0:<9} |{1:^20} |{2:^20} |{3:^20} |{4:^20}".format(
            "Iteracion", "xl", "xu ", "xr", "error"))
        print("|{0:<11}|{1:^21}|{2:^21}|{3:^21}|{4:^20}".format(
            "-----------", "---------------------", "---------------------", "---------------------", "---------------------"))
        for i, v in enumerate(self.valores):
            print("| {0:<9} |{1:>20} |{2:>20} |{3:>20} |{4:>20}".format(
                str(i), str(v['xl']), str(v['xu']), str(v['xr']), str(v['error'])))

    def plotLog(self):
        p = plot(self.funcion)
        return p
