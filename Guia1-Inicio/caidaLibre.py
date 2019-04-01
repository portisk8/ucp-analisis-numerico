# -*- coding: utf-8 -*-
import math
import matplotlib.pyplot as plt


masa = float(input("Valor de la masa: "))
c = float(input("Coeficiente de rozamiento: "))
gravedad = 9.8
e = math.e
tiempoFinal = float(input("Ingrese tiempo final: "))
delta = float(input("Ingrese delta: "))

tiempoInicial = 0
velIinicial = 0


#ejes para graficar
x_axys = [tiempoInicial]
y_axys = [velIinicial]

y_axys_inter = [velIinicial]

cont = delta
vIncremental = 0

while cont < tiempoFinal:
    resultado = ((gravedad*masa)/c) * (1- (e**(-(c/masa)*cont))) #Resolviendo la Ec. Diferencial
    x_axys.append(cont)
    y_axys.append(resultado)
    print('Velocidad real = v_{} = {} m/s'.format(cont,round(resultado,4)))
    vIncremental = vIncremental + (gravedad - ((c/masa)*vIncremental)) * (cont - (cont-delta))
    print('Velocidad aprox = v_{} = {} m/s'.format(cont,round(vIncremental,4)))
    y_axys_inter.append(vIncremental)
    cont += delta

plt.plot(x_axys,y_axys, 'r')
plt.plot(x_axys,y_axys_inter, 'g')
plt.axis([0, tiempoFinal+10, 0, vIncremental+10])
plt.show()