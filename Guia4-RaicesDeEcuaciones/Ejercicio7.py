from MetodoAbierto import MetodoAbierto
from matplotlib import pyplot
import math

f = input(
    "Ingrese funcion separada G(x): Ej: (1 + 4 * x**2 - 0.5 * x **3)/5.5 \n>>> ")
xi = float(input("Ingrese punto inicial: EJ: 2\n>>> "))
tolerancia = float(input("Ingrese tolerancia de error: Ej: 0.01\n>>> "))


ma = MetodoAbierto(f, xi, 2)
ma.printMetodo()
ma.aplicarMetodo()  # Aplica segun el metodo seleccionado previamente.
n = len(ma.valores)-1
try:
    while (ma.valores[n]['error'] == None or math.fabs(ma.valores[n]['error']) > tolerancia):
        # ma.showIndex(n)
        ma.aplicarMetodo()
        n = len(ma.valores)-1
    # print(str(valores))
    ma.showResults()
except Exception as error:
    print("[Error] > {}\n No converge en un punto".format(error))


def f1(x):
    return eval(f)


# Valores del eje X que toma el gráfico.
axisX = range(-40, 40)
# Graficar ambas funciones.
pyplot.plot(axisX, [f1(i) for i in axisX])
# Establecer el color de los ejes.
pyplot.axhline(0, color="red")
# Limitar los valores de los ejes.
pyplot.xlim(-40, 40)
pyplot.ylim(-40000, 40000)
# Mostrarlo.
pyplot.show()
