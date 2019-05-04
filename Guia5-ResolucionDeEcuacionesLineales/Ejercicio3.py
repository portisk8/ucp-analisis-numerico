from sympy import *
from matplotlib import pyplot
from sympy.solvers.solveset import linsolve

var = "(-24 + (8 * x) ) / 4"
var2 = "34 - (6 * x)"

x, y, z = symbols('x, y, z')
eq1 = 4*y - 8*x + 24
eq2 = y + 6*x - 34
print("Raices: \n{}".format(solve([eq1, eq2], (x, y))))


def f1(x):
    return eval(var)


def f2(x):
    return eval(var2)


# Valores del eje X que toma el gráfico.
axisX = range(-10, 10)
# Graficar ambas funciones.
pyplot.plot(axisX, [f1(i) for i in axisX])
pyplot.plot(axisX, [f2(i) for i in axisX])
pyplot.axhline(4, color="lightblue")
pyplot.axvline(5, color="lightblue")

# Limitar los valores de los ejes.
pyplot.xlim(-10, 10)
pyplot.ylim(-20, 20)
# Mostrarlo.
pyplot.show()
