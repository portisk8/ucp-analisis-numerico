from MetodoAbierto import MetodoAbierto
import math


f = input("Ingrese funcion separada G(x): Ej: 2 * sin(x **(1/2)) \n>>> ")
xi = float(input("Ingrese punto inicial: EJ: 0.5\n>>> "))
tolerancia = float(input("Ingrese tolerancia de error: Ej: 0.001\n>>> "))

ma = MetodoAbierto(f, xi)
ma.metodoPuntoFijo()
n = len(ma.valores)-1
while (ma.valores[n]['error'] == None or math.fabs(ma.valores[n]['error']) > tolerancia):
    ma.metodoPuntoFijo()
    n = len(ma.valores)-1
# print(str(valores))
ma.showResults()
print('---------------------------------------')
