from MetodoAbierto import MetodoAbierto
import math

f = input("Ingrese funcion separada F(x): Ej: x**2 \n>>> ")
g = input("Ingrese funcion separada G(x): Ej: 1.8 * x + 2.5 \n>>> ")
xi = float(input("Ingrese punto inicial: EJ: 5\n>>> "))
tolerancia = float(input("Ingrese tolerancia de error: Ej: 0.05\n>>> "))


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
