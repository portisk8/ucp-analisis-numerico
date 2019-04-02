from MetodoCerrado import MetodoCerrado
from matplotlib import pyplot
import math


var = input(
    "Ingrese funcion polinómica: Ej: -25182 * x - 90 * x**2 + 44 * x**3 - 8 * x**4 + 0.7 * x**5 \n >>> ")
xl = float(input("Ingrese xl: Ej: 15\n>>> "))
xu = float(input("Ingrese xu: Ej: 18\n>>> "))
es = float(input("Ingrese porcentaje de error tolerable: 10\n>>> "))

mc = MetodoCerrado(var, xl, xu)
mc.getRaicesByBiseccion()
n = len(mc.valores)-1
while (mc.valores[n]['error'] == None or math.fabs(mc.valores[n]['error']) > es):
    mc.getRaicesByBiseccion()
    n = len(mc.valores)-1
# print(str(valores))
mc.showResults()


def f1(x):
    return eval(var)


# Valores del eje X que toma el gráfico.
axisX = range(-20, 20)
# Graficar ambas funciones.
pyplot.plot(axisX, [f1(i) for i in axisX])
# Establecer el color de los ejes.
pyplot.axhline(0, color="red")
# Limitar los valores de los ejes.
pyplot.xlim(-20, 20)
pyplot.ylim(-250000, 25000)
# Mostrarlo.
pyplot.show()
