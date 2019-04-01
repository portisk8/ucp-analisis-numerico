"""
La siguiente serie infinita converge a un valor de f(n) = (π**4)/90 conforme n tiende a infinito.
Escriba un programa de precisión sencilla para calcular f(n) con n=1 hasta
n=10000. Luego, modifique el programa para que realice la sumatoria en sentido inverso:
n=10000 hasta n=1. En cada caso calcule el error verdadero relativo porcentual. Explique
los resultados obtenidos.

"""
import math
import numpy as np


valorVerdadero = math.pow(math.pi,4)/90
print ("Valor verdadero    : " + str(valorVerdadero))

valor = 0
for n in range(1,10000):
    valor += np.float64(1 / (n**4))  

# print (str(valor))
print ("Valor incrementando: " + str(valor))
errorV1 = (valorVerdadero - valor)/valorVerdadero * 100
print ("|_ Error : " + str(errorV1) +"%")
#Explicación: En este caso hubo menos error que en el segundo en el que se decrementa.

valor2 = 0
for n in range(10000, 0, -1):
    valor2 += np.float64(1 / (n**4))

errorV2 = (valorVerdadero - valor2)/valorVerdadero * 100
print ("Valor decrementando: " + str(valor2))
print ("|_ Error : " + str(errorV2)+"%")
#Explicación: En este caso hubo mas error que en el primero en el que se incrementa.



