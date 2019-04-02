import sympy
from sympy.plotting import plot
from sympy.abc import x


class MetodoAbierto(object):
    "Clase Que usa Metodos de [1]Punto Fijo y [2]Newton-Raphson para hallar la raiz de una funcíon por aproximación"

    metodos = {1: {'key': 1, 'value': 'Método Punto Fijo'},
               2: {'key': 1, 'value': 'Método Newton-Raphson'}}

    def __init__(self, funcionF, xi, metodo=None):
        "Funcion: str, xl: float, xu:float"
        self.funcionF = sympy.sympify(
            funcionF)
        self.xi = xi
        self.xf = None
        self.xr = None
        self.valores = []
        try:
            self.metodo = self.metodos[metodo]
        except:
            pass

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
        self.xf = self.funcionF.subs({'x': self.xi}).evalf()
        return self.evaluar()

    def metodoNewtonRaphson(self):
        "Implementa el método de Newton-Raphson"
        numerador = self.funcionF.subs({'x': self.xi}).evalf()
        denominador = sympy.diff(self.funcionF).subs({'x': self.xi}).evalf()
        self.xf = self.xi - (numerador/denominador)
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

    def printMetodo(self):
        print(self.metodo['value'])

    def aplicarMetodo(self):
        "Si se definió previamente el metodo en el constructor"
        try:
            if(self.metodo['key'] == 1):
                return self.metodoPuntoFijo()
            elif(self.metodo['key'] == 2):
                return self.metodoNewtonRaphson()
        except:
            pass
