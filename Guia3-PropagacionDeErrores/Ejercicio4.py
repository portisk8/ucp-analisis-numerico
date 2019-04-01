"""
Repita el problema anterior, pero considere 
una esfera de cobre con un radio de 0,15 ±0,01 m
e = 0,9 ± 0,05 
T = 550 ± 20.
"""

import math
import sympy
# H= AeO T**4
# H = Watts
r = 0.15  # A = area de la superficie de la esfera que equivale a 4pir^2
deltaR = 0.01
e = 0.9  # e = emisividad
deltaE = 0.05
s = 5.67e-8  # s = constante de stefan-Boltzmann = 5.67e-8
T = 550  # T = temperatura absoluta
deltaT = 20
# Calculo el valor verdadero
vv = 4 * (math.pi) * (r**2) * e * s * (T**4)

x, y, z = sympy.symbols('x,y,z', real=True)
H = 4 * math.pi * x**2 * y * s*(z**4)


def derivarRespectoDe(valor):
    if(valor == "r"):  # Derivo en funcion de r (Area de la superficie)
        return sympy.diff(H, x).evalf(subs={x: r, y: e, z: T})
    elif (valor == "e"):  # Derivo en funcion de e (Emisividad)
        return sympy.diff(H, y).evalf(subs={x: r, y: e, z: T})
    elif (valor == "t"):  # Derivo en funcion de t (Tiempo)
        return sympy.diff(H, z).evalf(subs={x: r, y: e, z: T})


print("---------------------------------")
print("La ley de Stefan-Boltzmann se utiliza para estimar la velocidad de cambio de la energía H para una determinada superficie:")
print("---------------------------------")
print("|    H = A * e * s * T^4")
print("|    H = 4pi*r^2 * e * s * T^4")
print("---------------------------------")
print("|")
print("| r = 0,15 m")
print("| △ r = 0.01 m")
print("| e = 0,9")
print("| △ e = 0.05")
print("| s = 5.67e-8 W m^-2 K^-4")
print("| T = 550 K")
print("| △ T = 20 K")
print("|")
print("------------- RESULTADO -------------")
print("|")
# Resuelvo la formula de Stefan-Boltzmann mediante la formula de propagacion de errores
resultado = (derivarRespectoDe("r") * deltaR) + \
    (derivarRespectoDe("e") * deltaE) + (derivarRespectoDe("t") * deltaT)
print("| H = {} W".format(str(vv)))
print("| △ H = {} W".format(str(resultado)))
print("|     |_ Con esto podemos decir que H varia en ± △ H cuando △ r ±0.01 ; △ e ±0.05 ; △ T ±20")
error1 = resultado * 100 / vv
print("| Error % = {}".format(str(error1)))
print("|")
