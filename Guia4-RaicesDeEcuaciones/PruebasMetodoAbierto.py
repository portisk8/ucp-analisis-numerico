from MetodoAbierto import MetodoAbierto
import math
import sympy

print('----------EJERCICIO 5----------')
print('----------ROOT = 1.97----------')
print("-------- METODO PUNTO FIJO -------")
f = '2 * sin(x **(1/2))'
# funcion = sympy.simpify(funcion)
xi = 6
tolerancia = 0.001
ma = MetodoAbierto(f, xi)
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
print("-------- METODO PUNTO FIJO -------")
f = '(1.8 * x + 2.5) ** (1/2)'
# funcion = sympy.simpify(funcion)
xi = 5
tolerancia = 0.05
ma = MetodoAbierto(f, xi)
ma.metodoPuntoFijo()
n = len(ma.valores)-1
try:
    while (ma.valores[n]['error'] == None or math.fabs(ma.valores[n]['error']) > tolerancia):
        ma.metodoPuntoFijo()
        n = len(ma.valores)-1
    # print(str(valores))
    ma.showResults()
except Exception as error:
    print("[Error] > {}\n No converge en un punto".format(error))
print('---------------------------------------')
print('----------ROOT = 2.71934----------')
print("-------- METODO NEWTON-RAPHSON -------")
f = '- x**2 + 1.8 * x + 2.5'
xi = 5
tolerancia = 0.05
ma = MetodoAbierto(f, xi)
ma.metodoNewtonRaphson()
n = len(ma.valores)-1
try:
    while (ma.valores[n]['error'] == None or math.fabs(ma.valores[n]['error']) > tolerancia):
        ma.metodoNewtonRaphson()
        n = len(ma.valores)-1
    # print(str(valores))
    ma.showResults()
except Exception as error:
    print("[Error] > {}\n No converge en un punto".format(error))
print('---------------------------------------')
print('----------EJERCICIO 7----------')
print('----------ROOT = 8.03----------')
print("-------- METODO NEWTON-RAPHSON -------")
f = '(1 + 4 * x**2 - 0.5 * x **3)/5.5'
xi = 2
tolerancia = 0.01
ma = MetodoAbierto(f, xi, 2)
ma.aplicarMetodo()
n = len(ma.valores)-1
try:
    while (ma.valores[n]['error'] == None or math.fabs(ma.valores[n]['error']) > tolerancia):
        ma.aplicarMetodo()
        n = len(ma.valores)-1
    # print(str(valores))
    ma.showResults()
except Exception as error:
    print("[Error] > {}\n No converge en un punto".format(error))
print('---------------------------------------')
