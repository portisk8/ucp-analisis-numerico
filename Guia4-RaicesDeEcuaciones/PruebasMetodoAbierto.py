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
print('----------EJERCICIO 6----------')
print('----------ROOT = 2.71934----------')
f = 'x**2'
g = '1.8 * x + 2.5'
# funcion = sympy.simpify(funcion)
xi = 2
tolerancia = 0.05
ma = MetodoAbierto(f, g, xi)
ma.metodoPuntoFijo()
n = len(ma.valores)-1
try:
    while (ma.valores[n]['error'] == None or math.fabs(ma.valores[n]['error']) > tolerancia):
        ma.showIndex(n)
        ma.metodoPuntoFijo()
        n = len(ma.valores)-1
    # print(str(valores))
    ma.showResults()
except Exception as error:
    print("[Error] > {}\n No converge en un punto".format(error))
print('---------------------------------------')
