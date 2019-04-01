import math
import sympy
# H= AeO T**4

#Prueba 1
# H = Watts
A = 0.15 # A = area de la superficie
e = 0.9 # e = emisividad
s = 5.67e-8 # s = constante de stefan-Boltzmann = 5.67e-8
T = 650 # T = temperatura absoluta
deltaT = 20
deltaT2 = 40
#Calculo el valor verdader
vv = A*e*s*(T**4)

x = sympy.symbols('x', real=True)
H = A*e*s*(x**4)

#Calculo la derivada respecto a T
derivadaT = sympy.diff(H,x).subs(x,T)

print("---------------------------------")
print("La ley de Stefan-Boltzmann se utiliza para estimar la velocidad de cambio de la energía H para una determinada superficie:")
print("---------------------------------")
print("|    H = A * e * s * T^4")
print("---------------------------------")
print("|")
print("| A = 0,15 m²")
print("| e = 0,9")
print("| s = 5.67e-8 W m^-2 K^-4")
print("| T = 650 K")
print("| △ T = 20 K")
print("| △ T2 = 40 K")
print("|")
print("------------- RESULTADO Con T ± 20 -------------")
print("|")
#Resuelvo la formula de Stefan-Boltzmann mediante la formula de propagacion de errores
resultado = derivadaT * deltaT
print("| H = {} W".format(str(vv)))
print("| △ H = {} W".format(str(resultado)))
print("|     |_ Con esto podemos decir que H varia en ± △ H cuando T= ±20")
error1 = resultado * 100 / vv
print("| Error % = {}".format(str(error1)))
print("|")
#Prueba 2 con error de ± 40
print("------------- RESULTADO Con T ± 40 -------------")
print("|")
#Resuelvo la formula de Stefan-Boltzmann mediante la formula de propagacion de errores
resultado2 = derivadaT * deltaT2
print("| H = {} W".format(str(vv)))
print("| △ H = {} W".format(str(resultado2)))
print("|     |_ Con esto podemos decir que H varia en ± △ H cuando T= ±40")
error2 =  resultado2 * 100 / vv
print("| Error % = {}".format(str(error2)))
print("|")
print("---------------------------------")
