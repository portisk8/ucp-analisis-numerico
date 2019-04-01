import math

x = 0.3*math.pi
rad = math.radians(x)
ValorVerdadero = math.cos(rad)
print ("Valor Verdadero: " + str(ValorVerdadero))

#Aplicando McLaurin
def getCos(x, n):
    valorAprox = 0
    for i in range(n):
        coef = (-1)**i # Me define si resto o sumo 
        num = x**(2*i) # Numerador
        denom = math.factorial(2*i) # Calculo el factorial del denominador
        valorAprox += ( coef ) * ( (num)/(denom) )
    return valorAprox

#PASO 1: Obtengo la tolerancia segun la cantidad de cifras significativas
cs = 8
es = (0.5 * math.pow(10,2-cs))
print ("TOLERANCIA    : " + str(es))
iteracion = 0
valorAprox = getCos(rad,iteracion)
ea = math.fabs((ValorVerdadero - valorAprox) / ValorVerdadero * 100)

while ea > es:
    iteracion += 1
    valorAprox = getCos(rad,iteracion)
    ea = math.fabs((ValorVerdadero - valorAprox) / ValorVerdadero * 100)

print ("Valor aprox    : " + str(valorAprox))
print ("|_Iteracion Nro: " + str(iteracion))
print ("|_ Error : " + str(ea))

