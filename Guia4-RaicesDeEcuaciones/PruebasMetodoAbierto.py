from MetodoAbierto import MetodoAbierto
import math
import sympy

print('----------EJERCICIO 5----------')
print('----------ROOT = 1.97----------')
f = 'x'
g = '2 * sin(x **(1/2))'
# funcion = sympy.simpify(funcion)
xi = 6
tolerancia = 0.001
ma = MetodoAbierto(f, g, xi)
ma.metodoPuntoFijo()
n = len(ma.valores)-1
while (ma.valores[n]['error'] == None or math.fabs(ma.valores[n]['error']) > tolerancia):
    ma.metodoPuntoFijo()
    n = len(ma.valores)-1
# print(str(valores))
ma.showResults()
print('---------------------------------------')
