#Importamos numpy para hacer utilización de funciones y constantes necesarias
import numpy as np

#importamos matplotlib.pyplot para poder graficar
import matplotlib.pyplot as plot

# Importamos funciones declaradas de forma externa al main
from a0a1MinCuad import obtenerA0A1MinimoCuadrado
from interPNpy import interpolacionPolNewtonPrimerGradoX

Ve = 10 #Voltios (V)
R = 12000 #Ohm
C = 0.00022 #Faradio (F)

texp = [] #Tiempo experimental
Vexp = [] #Voltaje experimental

# Esto corresponde a la Ecuacion de la descarga del capacitor linealizada
def evaluarTEnModelo(t):
    return  np.exp(np.log(Ve) + (-t * 1/(R*C))) 
# Obtención de t en la Función de descarga del capacitor
def obtenerTdeDescargaCap(Vc):
    numerador = (np.log10(Vc / 10 ) * R * C)
    denominador = np.log(np.e)
    
    return -1 * ( numerador / denominador )

# Linealizacion
def funcionLinealizada(t):
	return np.log(Ve) + (-t * 1/(R*C))

def funcionDeAjuste(tau, Ve, t):
	return Ve * np.exp(-t/tau)

# Función de Descarga del Capacitor	
def descargaCapacitor(x):
    return Ve * (np.exp(-x * 1/(R*C)))

    

#def interpolacionPolNewtonPrimerGrado(x):
#    return descargaCapacitor(x0) + ((descargaCapacitor(x1) - descargaCapacitor(x0))/ (x1 - x0) ) * (x - x0)

# función para la obtención de los datos alojados en el .txt (originalmente .dat)
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


#obtenemos los datos del .txt
obtenerDatos()

#rellenamos un arreglo con el ln de los voltajes experimentales
y = []
for item in Vexp:
	y.append(np.log(item))

#obtenemos tanto a0 como a1     
a1, a0 = obtenerA0A1MinimoCuadrado(texp,y)

#calculamos los parámetros incógnitas
tau = -1/a1
Ve = np.exp(a0)

# imprimimos resultados y errores
print('\n-Ajuste Lineal')
print('y = {} + {} x'.format(str(a0),str(a1)))
print('R*C(teórico): {}\nR*C(experimental) : {}\nError: {}%'.format(str(R*C), str(tau), str(abs((((R*C)-tau)/(R*C))*100))))

#calculamos el tau experimental con Interpolación Pol. de Newton en primer grado
tauNewton =  interpolacionPolNewtonPrimerGradoX(Vexp[0]*0.37,descargaCapacitor(Vexp[35]),descargaCapacitor(Vexp[34]), Vexp[35] , Vexp[34])

# imprimimos resultados y errores
print('\n-Interpolación Polinomial de Newton de Primer Grado')
print('R*C: {}\nError: {}%'.format(str(tauNewton),str(abs((((R*C)-tauNewton)/(R*C))*100))))

# GRAFICAMOS
# Create the vectors X and Y
x = np.array(range(11))


#Graficamos la funcion linealizada de la ecuacion
y = funcionDeAjuste(tau, Ve, x)
# Create the plot
#plot.plot(x,y,label='Ajuste Lineal',color='orange')
print("\n-Gráfica:")
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

#print("\n\n| {0:<13} |{1:^22} |{2:^22}".format(
#        "Valor Exp", "Valor Inter.Pol.Newton", "Error Rel. Aprox"))
##for index, x in enumerate(Vexp):
#	aux = interpolacionPolNewtonPrimerGrado(x)
#	errorRelativoAprox = abs(((Vexp[index] - aux)/Vexp[index])*100)
#	print("| {0:<13} |{1:<22} |{2:<22}".format(
##    print ("pos:{} valor:{}".format(str(index),str(x)))
#            str(Vexp[index]), str(aux), str(errorRelativoAprox)+'%'))
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