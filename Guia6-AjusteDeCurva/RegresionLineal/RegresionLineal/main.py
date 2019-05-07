
import numpy as np
import matplotlib.pyplot as plot
from util import obtenerA0A1MinimoCuadrado
Ve = 10 #Voltios (V)
R = 12000 #Ohm
C = 0.00022 #Faradio (F)

texp = [] #Tiempo experimental
Vexp = [] #Voltaje experimental
x0 = 2.5
x1 = 2.8
def evaluarTEnModelo(t):
    return  np.exp(np.log(Ve) + (-t * 1/(R*C))) #Esto corresponde a la Ecuacion de la descarga del capacitor linealizada

#Linealizacion
def funcionLinealizada(t):
	return np.log(Ve) + (-t * 1/(R*C))
def funcionDeAjuste(tau, Ve, t):
	return Ve * np.exp(-t/tau)
	
def descargaCapacitor(x):
    return Ve * (np.exp(-x * 1/(R*C)))
def interpolacionPolNewtonPrimerGrado(x):
    return descargaCapacitor(x0) + ((descargaCapacitor(x1) - descargaCapacitor(x0))/ (x1 - x0) ) * (x - x0)
def obtenerDatos():
    f = open("datos.txt", "r")
    i = int()
    aux = int(0)
    for linea in f.readlines():
        linea = linea.split("   ")
        aux = aux +1
        for i in range (1,101):
            if aux <2:
                    a = float(linea[i])
                    texp.append(a)
            if aux >1:
                    b = float(linea[i])
                    Vexp.append(b)


# Linea que mejor se ajusta a la curva
obtenerDatos()
y = []
for item in Vexp:
	y.append(np.log(item))
a1, a0 = obtenerA0A1MinimoCuadrado(texp,y)

tau = -1/a1
Ve = np.exp(a0)


print('Ajuste Lineal')
print('y = {} + {} x'.format(str(a0),str(a1)))

print('R*C(teórico): {}\nR*C(experimental) : {}\nError: {}%'.format(str(R*C), str(tau), str(abs((((R*C)-tau)/(R*C))*100))))


# GRAFICAMOS
# Create the vectors X and Y
x = np.array(range(11))


#Graficamos la funcion linealizada de la ecuacion
y = funcionDeAjuste(tau, Ve, x)
# Create the plot
#plot.plot(x,y,label='Ajuste Lineal',color='orange')
plot.plot(x,y,label='Funcion Linealizada',color='red')
plot.scatter(texp, Vexp, label='Valores Experimentales')
plot.legend()
plot.show()



## Comparacion de datos
#print("| {0:<13} |{1:^22} |{2:^22}".format(
#        "Valor Exp", "Valor Teorico", "Error Rel. Aprox"))
#for index, x in enumerate(texp):
#	aux = funcionLinealizada(x)
#	errorRelativoAprox = abs(((Vexp[index] - aux)/Vexp[index])*100)
#	print("| {0:<13} |{1:<22} |{2:<22}".format(
#            str(Vexp[index]), str(aux), str(errorRelativoAprox)+'%'))

print("\n\n| {0:<13} |{1:^22} |{2:^22}".format(
        "Valor Exp", "Valor Inter.Pol.Newton", "Error Rel. Aprox"))
for index, x in enumerate(texp):
	aux = interpolacionPolNewtonPrimerGrado(x)
	errorRelativoAprox = abs(((Vexp[index] - aux)/Vexp[index])*100)
	print("| {0:<13} |{1:<22} |{2:<22}".format(
            str(Vexp[index]), str(aux), str(errorRelativoAprox)+'%'))
## GRAFICAMOS
## Create the vectors X and Y
#x = np.array(range(11))
#y = a0 + a1*x

##Graficamos la funcion linealizada de la ecuacion
#y2 = funcionLinealizada(x)
## Create the plot
##plot.plot(x,y,label='Ajuste Lineal',color='orange')
#plot.plot(x,y2,label='Funcion Linealizada',color='red')
#plot.scatter(texp, Vexp, label='Valores Experimentales')
#plot.legend()
#plot.show()