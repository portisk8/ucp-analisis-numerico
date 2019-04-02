from MetodoAbierto import MetodoAbierto
import math

metodo = int(input(
    "Ingrese el número del metodo que desea utilizar:\n1) Método Punto Fijo\n2) Método Newton-Raphson\n>>> "))
f = input("Ingrese funcion separada G(x): Ej: (1.8 * x + 2.5) **(1/2) \n>>> ")
xi = float(input("Ingrese punto inicial: EJ: 5\n>>> "))
tolerancia = float(input("Ingrese tolerancia de error: Ej: 0.05\n>>> "))


if(metodo == 1 or metodo == 2):
    ma = MetodoAbierto(f, xi, metodo)
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
else:
    print('No seleccionó ningun metodo. Vuelva a iniciar el programa.')
print('---------------------------------------')
