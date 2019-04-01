import math
import numpy as np
from sympy import (symbols,diff)


x1 = 2
x = symbols('x', real=True)
fx = 25* x**3 - 6* x**2 + 7* x - 88
x0 = 1
h = x1 - x0

valorVerdadero = 25* x1**3 - 6* x1**2 + 7* x1 - 88


print ("Valor Verdadero > {}".format(str(valorVerdadero)))

def derivada(funcion,orden):
    return diff(funcion,x,orden).subs(x,x0) #Funcion de la libreria sympy para calcular derivadas de orden n. 

def polyTaylor(funcion,orden): #Funcion que calcula el polinomio de taylor recibiendo como parametro la funcion y el orden
    valor = 0
    i = 0
    while i <= orden:
        numerador = derivada(fx,i)
        denominador = math.factorial(i)
        valor += (numerador / denominador) * (h ** i)
        i+=1
    return valor

print("Orden     Resultado     Error")
for n in range(0,4):
    poli = polyTaylor(fx,n)
    error = (valorVerdadero - poli) / valorVerdadero * 100
    print("{}         {}             {}%".format(str(n),str(poli),str(error.p / error.q)))