from MetodoCerrado import MetodoCerrado
import math

print('----------EJERCICIO 1----------')
print('----------ROOT = 6.40----------')
var = '-0.5 * x**2 + 2.5 * x + 4.5'
xl = 6
xu = 7
iteraciones = 34
mc = MetodoCerrado(var, xl, xu)
for i in range(0, iteraciones):
    mc.getRaicesByBiseccion()
# print(str(valores))
mc.showResults()
print('---------------------------------------')
print('----------EJERCICIO 2----------')
print('----------ROOT = 0.41----------')
var = '5 * x**3 - 5 * x**2 + 6 * x - 2'
xl = 0
xu = 1
es = 0.5
mc = MetodoCerrado(var, xl, xu)
mc.getRaicesByBiseccion()
n = len(mc.valores)-1
while (mc.valores[n]['error'] == None or math.fabs(mc.valores[n]['error']) > es):
    mc.getRaicesByBiseccion()
    n = len(mc.valores)-1
# print(str(valores))
mc.showResults()
print('---------------------------------------')
print('----------EJERCICIO 3----------')
print('----------ROOT = 16.32----------')
var = '-25182 * x - 90 * x**2 + 44 * x**3 - 8 * x**4 + 0.7 * x**5'
xl = 15
xu = 18
es = 0.5
mc = MetodoCerrado(var, xl, xu)
mc.getRaicesByBiseccion()
n = len(mc.valores)-1
while (mc.valores[n]['error'] == None or math.fabs(mc.valores[n]['error']) > es):
    mc.getRaicesByBiseccion()
    n = len(mc.valores)-1
# print(str(valores))
mc.showResults()
print('---------------------------------------')
print('----------EJERCICIO 4----------')
print('----------ROOT = 1.419----------')
var = "0.7 - ln(x**2)"
xl = 0.5
xu = 2
iteraciones = 10
mc = MetodoCerrado(var, xl, xu)
for i in range(0, iteraciones):
    mc.getRaicesByBiseccion()
# print(str(valores))
mc.showResults()
print('---------------------------------------')
print('----------EJERCICIO 5----------')