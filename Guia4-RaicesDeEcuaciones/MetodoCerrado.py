''' 
    Clase para hallar raices mediante funciones utilizando libreria sympy
    Basandose en el metodo cerrado para una variable
'''
import sympy


class MetodoCerrado(object):

    def __init__(self, funcion, xl, xu):
        self.funcion = sympy.sympify(funcion)
        self.xl = xl
        self.xu = xu
        self.xr = None
        self.valores = []
        self.x = sympy.symbols('x', real=True)

    def getXRByBiseccion(self):
        return (self.xl + self.xu) / 2

    def calcularErrorAproximado(self):
        n = len(self.valores)
        if(n > 0):
            error = ((self.xr - self.valores[n-1]['xr']) / self.xr) * 100
            return error
        else:
            return None

    def getRaicesByBiseccion(self, iteracion=None):
        if(iteracion != None):
            for i in range(0, iteracion):
                self.xr = self.getXRByBiseccion()
                ea = self.calcularErrorAproximado()
                self.valores.append(
                    {"xl": self.xl, "xu": self.xu, "xr": self.xr, "error": ea})
                fdex = self.funcion.subs({'x': self.xr})
                if(fdex > 0):
                    self.xl = self.xr
                else:
                    self.xu = self.xr
        else:
            self.xr = self.getXRByBiseccion()
            ea = self.calcularErrorAproximado()
            self.valores.append(
                {"xl": self.xl, "xu": self.xu, "xr": self.xr, "error": ea})
        return self.valores

    def getRaicesByFalsaPosicion(self, iteracion):
        pass
