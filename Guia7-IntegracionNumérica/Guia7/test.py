from Integral import Integral

integral = Integral()
print("Problema 1:")
print("integrate 1-e^(-2x) dx from x=0 to 4")
print("Valor Real = 3.5002")
#Trapecio
real = 3.5002
entrada = "(1 - E ** (-2 * x))"
a = 0
b = 4
var = integral.trapecio(entrada, a, b, 1)
print("|-> Simple {} ; error % > {}".format(str(var), str(((real-var) / real) *100)))
var = integral.trapecio(entrada, -a, b, 5)
print("|-> N=5 {} ; error % > {}".format(str(var), str(((real-var) / real) *100)))
var = integral.trapecio(entrada, a, b, 10)
print("|-> N=10 {} ; error % > {}".format(str(var), str(((real-var) / real) *100)))
var = integral.trapecio(entrada, a, b, 100)
print("|-> N=100 {} ; error % > {}".format(str(var), str(((real-var) / real) *100)))
#Simpson 1/3
var = integral.simpson13(entrada, a, b, 1)
print("|-> Simple {} ; error % > {}".format(str(var), str(((real-var) / real) *100)))
var = integral.simpson13(entrada, a, b, 5)
print("|-> N=5 {} ; error % > {}".format(str(var), str(((real-var) / real) *100)))
var = integral.simpson13(entrada, a, b, 10)
print("|-> N=10 {} ; error % > {}".format(str(var), str(((real-var) / real) *100)))
var = integral.simpson13(entrada, a, b, 100)
print("|-> N=100 {} ; error % > {}".format(str(var), str(((real - var) / real) * 100)))
#Simpson 3/8
var = integral.simpson38Simple(entrada, a, b)
print("|-> Simple {} ; error % > {}".format(str(var), str(((real - var) / real) * 100)))

print("\n------------------------------------------------------------------------------------------\n")
print("integrate 1-x-4x^3 + 2x^5 dx from x=-2 to 4")
print("Valor Real = 1104")
#Trapecio
real = 1104
entrada = "1 - x - 4 * x**3 + 2 * x **5"
a = -2
b = 4
var = integral.trapecio(entrada, a, b, 1)
print("|-> Simple {} ; error % > {}".format(str(var), str(((real-var) / real) *100)))
var = integral.trapecio(entrada, -a, b, 5)
print("|-> N=5 {} ; error % > {}".format(str(var), str(((real-var) / real) *100)))
var = integral.trapecio(entrada, a, b, 10)
print("|-> N=10 {} ; error % > {}".format(str(var), str(((real-var) / real) *100)))
var = integral.trapecio(entrada, a, b, 100)
print("|-> N=100 {} ; error % > {}".format(str(var), str(((real-var) / real) *100)))
#Simpson 1/3
var = integral.simpson13(entrada, a, b, 1)
print("|-> Simple {} ; error % > {}".format(str(var), str(((real-var) / real) *100)))
var = integral.simpson13(entrada, a, b, 5)
print("|-> N=5 {} ; error % > {}".format(str(var), str(((real-var) / real) *100)))
var = integral.simpson13(entrada, a, b, 10)
print("|-> N=10 {} ; error % > {}".format(str(var), str(((real-var) / real) *100)))
var = integral.simpson13(entrada, a, b, 100)
print("|-> N=100 {} ; error % > {}".format(str(var), str(((real - var) / real) * 100)))
#Simpson 3/8
var = integral.simpson38Simple(entrada, a, b)
print("|-> Simple {} ; error % > {}".format(str(var), str(((real - var) / real) * 100)))

print("\n------------------------------------------------------------------------------------------\n")
print("integrate  (x + 2/x)^2 dx from x=-2 to 4")
print("Valor Real = 8.3333")
#Trapecio
real = 8.3333
entrada = "(x + (2 / x)) **2"
a = 1
b = 2
var = integral.trapecio(entrada, a, b, 1)
print("|-> Simple {} ; error % > {}".format(str(var), str(((real-var) / real) *100)))
var = integral.trapecio(entrada, -a, b, 5)
print("|-> N=5 {} ; error % > {}".format(str(var), str(((real-var) / real) *100)))
var = integral.trapecio(entrada, a, b, 10)
print("|-> N=10 {} ; error % > {}".format(str(var), str(((real-var) / real) *100)))
var = integral.trapecio(entrada, a, b, 100)
print("|-> N=100 {} ; error % > {}".format(str(var), str(((real-var) / real) *100)))
#Simpson 1/3
var = integral.simpson13(entrada, a, b, 1)
print("|-> Simple {} ; error % > {}".format(str(var), str(((real-var) / real) *100)))
var = integral.simpson13(entrada, a, b, 5)
print("|-> N=5 {} ; error % > {}".format(str(var), str(((real-var) / real) *100)))
var = integral.simpson13(entrada, a, b, 10)
print("|-> N=10 {} ; error % > {}".format(str(var), str(((real-var) / real) *100)))
var = integral.simpson13(entrada, a, b, 100)
print("|-> N=100 {} ; error % > {}".format(str(var), str(((real - var) / real) * 100)))
#Simpson 3/8
var = integral.simpson38Simple(entrada, a, b)
print("|-> Simple {} ; error % > {}".format(str(var), str(((real - var) / real) * 100)))

print("\n------------------------------------------------------------------------------------------\n")
print("integrate  (4x -3)^3 dx from x=-3 to 5")
print("Valor Real = 2056")
#Trapecio
real = 2056
entrada = "(4 * x - 3) **3"
a = -3
b = 5
var = integral.trapecio(entrada, a, b, 1)
print("|-> Simple {} ; error % > {}".format(str(var), str(((real-var) / real) *100)))
var = integral.trapecio(entrada, -a, b, 5)
print("|-> N=5 {} ; error % > {}".format(str(var), str(((real-var) / real) *100)))
var = integral.trapecio(entrada, a, b, 10)
print("|-> N=10 {} ; error % > {}".format(str(var), str(((real-var) / real) *100)))
var = integral.trapecio(entrada, a, b, 100)
print("|-> N=100 {} ; error % > {}".format(str(var), str(((real-var) / real) *100)))
#Simpson 1/3
var = integral.simpson13(entrada, a, b, 1)
print("|-> Simple {} ; error % > {}".format(str(var), str(((real-var) / real) *100)))
var = integral.simpson13(entrada, a, b, 5)
print("|-> N=5 {} ; error % > {}".format(str(var), str(((real-var) / real) *100)))
var = integral.simpson13(entrada, a, b, 10)
print("|-> N=10 {} ; error % > {}".format(str(var), str(((real-var) / real) *100)))
var = integral.simpson13(entrada, a, b, 100)
print("|-> N=100 {} ; error % > {}".format(str(var), str(((real - var) / real) * 100)))
#Simpson 3/8
var = integral.simpson38Simple(entrada, a, b)
print("|-> Simple {} ; error % > {}".format(str(var), str(((real-var) / real) *100)))
