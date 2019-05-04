
import numpy as np
import matplotlib.pyplot as plot

Ve = 10 #Voltios (V)
R = 12000 #Ohm
C = 0.00022 #Faradio (F)

texp = [] #Tiempo experimental
Vexp = [] #Voltaje experimental

def evaluarTEnModelo(t):
	prueba = np.exp(np.log(Ve) + (-t * 1/(R*C))) #Esto corresponde a la Ecuacion de la descarga del capacitor linealizada
	return prueba

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
sumxy = 0
sumx2 = 0
for index, item in enumerate(texp):
	sumxy += item*Vexp[index]
	sumx2 += item**2

a1numerador = len(texp) * sumxy - np.sum(texp)*np.sum(Vexp)
a1denominador = len(texp) * sumx2 - (np.sum(texp) **2)

a1 = a1numerador / a1denominador
a0 = np.average(Vexp) - a1* np.average(texp)

print('Ajuste Lineal')
print('y = {} + {} x'.format(str(a0),str(a1)))

# Comparacion de datos
print('Valor Exp   Valor Teorico      Error Rel. Aprox.')
for index, x in enumerate(texp):
	aux = evaluarTEnModelo(x)
	errorRelativoAprox = abs(((Vexp[index] - aux)/Vexp[index])*100)
	print('{} - {} - {}'.format(str(Vexp[index]), str(aux), str(errorRelativoAprox)) + "%")

# GRAFICAMOS
# Create the vectors X and Y
x = np.array(range(10))
y = a0 + a1*x

# Create the plot
plot.plot(x,y,label='Ajuste Lineal')
plot.scatter(texp, Vexp)
plot.show()