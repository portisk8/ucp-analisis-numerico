from MetodoCerrado import MetodoCerrado
from matplotlib import pyplot


var = input("Ingrese funcion polinómica: Ej: -0.5 * x**2 + 2.5 * x + 4.5 \n>>> ")
xl = float(input("Ingrese xl:Ej: 6\n>>> "))
xu = float(input("Ingrese xu: Ej: 7\n>>> "))
iteraciones = int(input("Ingrese cantidad de iteraciones:\n>>> "))
if(iteraciones == 0):
    iteraciones = None

mc = MetodoCerrado(var, xl, xu)
for i in range(0, iteraciones):
    mc.metodoBiseccion()
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
