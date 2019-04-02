from MetodoCerrado import MetodoCerrado
from matplotlib import pyplot
import math

var = input(
    "Ingrese funcion polinómica: Ej: 5 * x**3 - 5 * x**2 + 6 * x - 2 \n>>> ")
xl = float(input("Ingrese xl: Ej: 0\n>>> "))
xu = float(input("Ingrese xu: Ej: 1\n>>> "))
es = float(input("Ingrese porcentaje de error tolerable:\n>>> "))

mc = MetodoCerrado(var, xl, xu)
mc.metodoBiseccion()
n = len(mc.valores)-1
while (mc.valores[n]['error'] == None or math.fabs(mc.valores[n]['error']) > es):
    mc.metodoBiseccion()
    n = len(mc.valores)-1
# print(str(valores))
mc.showResults()


def f1(x):
    return eval(var)


# Valores del eje X que toma el gráfico.
axisX = range(-10, 15)
# Graficar ambas funciones.
pyplot.plot(axisX, [f1(i) for i in axisX])
# Establecer el color de los ejes.
pyplot.axhline(0, color="red")
# Limitar los valores de los ejes.
pyplot.xlim(-10, 10)
pyplot.ylim(-10, 10)
# Mostrarlo.
pyplot.show()
