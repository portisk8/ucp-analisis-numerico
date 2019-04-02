from MetodoCerrado import MetodoCerrado
from matplotlib import pyplot
import math

metodo = int(input(
    "Ingrese el número del metodo que desea utilizar:\n1) Método Bisección\n2) Método Falsa posicion\n>>>"))
var = input(
    "Ingrese funcion polinómica: Ej: -25182 * x - 90 * x**2 + 44 * x**3 - 8 * x**4 + 0.7 * x**5 \n >>> ")
xl = float(input("Ingrese xl: Ej: 15\n>>> "))
xu = float(input("Ingrese xu: Ej: 18\n>>> "))
es = float(input("Ingrese porcentaje de error tolerable: 10\n>>> "))
if(metodo == 1):
    print("-------- METODO BISECCION ---------")
    mc = MetodoCerrado(var, xl, xu)
    mc.metodoBiseccion()
    n = len(mc.valores)-1
    while (mc.valores[n]['error'] == None or math.fabs(mc.valores[n]['error']) > es):
        mc.metodoBiseccion()
        n = len(mc.valores)-1
    # print(str(valores))
    mc.showResults()
    print("-----------------------------------")
elif (metodo == 2):
    print("------ METODO FALSA POSICION ------")
    fp = MetodoCerrado(var, xl, xu)
    fp.metodoFalsaPosicion()
    n = len(fp.valores)-1
    while (fp.valores[n]['error'] == None or math.fabs(fp.valores[n]['error']) > es):
        fp.metodoFalsaPosicion()
        n = len(fp.valores)-1
    # print(str(valores))
    fp.showResults()
    print("-----------------------------------")
else:
    print("Vuelva a ejecutar el programa.")


def f1(x):
    return eval(var)


if(metodo == 1 or metodo == 2):
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
