from MetodoCerrado import MetodoCerrado
from matplotlib import pyplot


var = input("Ingrese funcion polinómica: Ej: -0.5 * x**2 + 2.5 * x + 4.5 \n>>> ")
xl = float(input("Ingrese xl:\n>>> "))
xu = float(input("Ingrese xu:\n>>> "))
iteraciones = int(input("Ingrese cantidad de iteraciones:\n>>> "))
if(iteraciones == 0):
    iteraciones = None

mc = MetodoCerrado(var, xl, xu)
valores = mc.getRaicesByBiseccion(iteraciones)
# print(str(valores))
print("{0:<3}{1:^20}{2:^20}{3:^20}{4:^20}".format(
    "Iteracion", "xl", "xu ", "xr", "error"))
for i, v in enumerate(valores):
    print("{0:<3}{1:>20}{2:>20}{3:>20}{4:>20}".format(
        str(i), str(v['xl']), str(v['xu']), str(v['xr']), str(v['error'])))


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
