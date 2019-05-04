
import numpy as np
import matplotlib.pyplot as plot


t = []
V = []
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
                    t.append(a)
            if aux >1:
                    b = float(linea[i])
                    V.append(b)
# Linea que mejor se ajusta a la curva
obtenerDatos()
sumxy = 0
sumx2 = 0
for index, item in enumerate(t):
	sumxy += item*V[index]
	sumx2 += item**2

a1numerador = len(t) * sumxy - np.sum(t)*np.sum(V)
a1denominador = len(t) * sumx2 - (np.sum(t) **2)

a1 = a1numerador / a1denominador
a0 = np.average(V) - a1* np.average(t)

print('Ajuste Lineal')
print('y = {} + {} x'.format(str(a0),str(a1)))

# GRAFICAMOS
# Create the vectors X and Y
x = np.array(range(10))
y = a0 + a1*x

# Create the plot
plot.plot(x,y,label='Ajuste Lineal')
plot.scatter(t, V)
plot.show()