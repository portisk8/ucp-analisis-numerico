import math

valorVerdadero = 6.737947e-3
print("valor Verdadero: " + str(valorVerdadero))

#PUNTO 1

valor1 = 0
for x in range(20):
    coef = (-1)**x
    num = math.pow(5,x)
    denom = math.factorial(x)
    valor1 += coef * (num / denom)

errorV1 = (valorVerdadero - valor1)/valorVerdadero * 100

print("Valor 1: " + str(valor1))
print("|_Error: " + str(errorV1) + " %")

#PUNTO 2

valor2 = 0
for x in range(20):
    num = math.pow(5,x)
    denom = math.factorial(x)
    valor2 += num / denom

valor2 = 1 / valor2
errorV2 = (valorVerdadero - valor2)/valorVerdadero * 100

print("Valor 2: " + str(valor2))
print("|_Error: " + str(errorV2) + " %")
