import math
import numpy as np
import sympy
import mpmath

x1 = 3
x = sympy.symbols('x', real=True)
fx = sympy.log(x)
x0 = 1
h = x1 - x0

valorVerdadero = mpmath.log(3)


print ("Valor Verdadero > {}".format(str(valorVerdadero)))

def derivada(funcion,orden):
    return sympy.diff(funcion,x,orden).subs(x,x0) #Funcion de la libreria sympy para calcular derivadas de orden n. 

def polyTaylor(funcion,orden): #Funcion que calcula el polinomio de taylor recibiendo como parametro la funcion y el orden
    valor = 0
    i = 0
    while i <= orden:
        numerador = derivada(fx,i)
        denominador = math.factorial(i)
        valor += (numerador / denominador) * h
        i+=1
    return valor

print("Orden     Resultado     Error")
for n in range(0,5):
    poli = polyTaylor(fx,n)
    error = (valorVerdadero - poli) / valorVerdadero * 100
    print("{}         {}             {}%".format(str(n),str(poli.p / poli.q),str(error)))