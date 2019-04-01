import math

def getCos(x, n):
    valorAprox = 0
    for i in range(n):
        coef = (-1)**i # Me define si resto o sumo 
        num = x**(2*i) # Numerador
        denom = math.factorial(2*i) # Calculo el factorial del denominador
        valorAprox += ( coef ) * ( (num)/(denom) )
    return valorAprox

valor=float(input("Ingrese el valor de x para cos(x): "))
n=int(input("Ingrese la cantidad de repeticiones: "))

rad = math.radians(valor) # Convierto el valor ingresado a radianes.
valorReal = math.cos(rad) # Valor real obtenido por la libreria de math
valorAprox = getCos(rad,n) # Valor aproximado 

print("Real  > " + str(round(valorReal,4)))
print("Aprox > " + str(round(valorAprox,4)))
#Calculo el porcentaje
porcentaje = ((valorReal - valorAprox) / valorReal) * 100.0
p = porcentaje if porcentaje > 0 else porcentaje * -1 # Esto es para tener el error siempre positivo

print("Error > " + str(round(p,4)) + "%")