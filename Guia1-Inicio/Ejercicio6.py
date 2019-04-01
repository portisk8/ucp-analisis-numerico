import math

P = float(input("Ingrese el prestamo: $"))
i = float(input("Ingrese tasa de interes (%): "))
n = int(input("Ingrese cantidad de años a pagar: "))

A = []
for x in range(1, n+1):
    num = i * (math.pow(1+i, x))  # Numerador
    denom = (math.pow(1+i, x)) - 1  # Denominador
    valor = P * (num/denom)  # resultado para A en el año x
    A.append(valor)

print("\n-----------------------------------")
print("Prestamo de ${}".format(str(P)))
print("Tasa de interés del {}%".format(str(i)))
print("-----------------------------------")
print("Año    Pago Anual (A)")
count = 1
for x in A:
    print("{}       ${}".format(str(count), str(round(x, 2))))
    count += 1
