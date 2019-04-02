import sympy
from sympy.plotting import plot
from sympy.abc import x


class MetodoAbierto(object):
    "Clase Que usa Metodos de Punto Fijo y Newton-Raphson para hallar la raiz de una funcíon por aproximación"

    def __init__(self, funcionF, funcionG, xi):
        "Funcion: str, xl: float, xu:float"
        self.funcionF = sympy.sympify(
            funcionF)
        self.funcionG = sympy.sympify(
            funcionG)
        self.xi = xi
        self.xf = None
        self.xr = None
        self.valores = []
        self.x = sympy.symbols('x', real=True)

    def calcularErrorAproximado(self):
        n = len(self.valores)
        if(n > 0):
            error = ((self.xf - self.valores[n-1]['xi']) / self.xf) * 100
            if((error > 10 and n > 100) or (n > 100)):
                raise Exception('Error, Iteracion muy alta y/o Error muy alto')
            return error
        else:
            return None

    def evaluar(self):
        ea = self.calcularErrorAproximado()
        self.valores.append(
            {"xi": self.xi, "xf": self.xf, "xr": self.xr, "error": ea})
        self.xi = self.xf

        return self.valores

    def metodoPuntoFijo(self):
        "Implementa el método de Punto Fijo"
        self.xf = self.funcionG.subs({'x': self.xi}).evalf()
        return self.evaluar()

    def showResults(self):
        print("| {0:<9} |{1:^20} |{2:^20} |{3:^20}".format(
            "Iteracion", "xi", "xf", "error"))
        print("|{0:<11}|{1:^21}|{2:^21}|{3:^20}".format(
            "-----------", "---------------------", "---------------------", "---------------------"))
        for i, v in enumerate(self.valores):
            print("| {0:<9} |{1:>20} |{2:>20} |{3:>20}".format(
                str(i), str(v['xi']), str(v['xf']), str(v['error'])))

    def showIndex(self, index):
        v = self.valores[index]
        print("| {0:<9} |{1:>20} |{2:>20} |{3:>20}".format(
            str(index), str(v['xi']), str(v['xf']), str(v['error'])))

    def plotLog(self):
        p = plot(self.funcion)
        return p
