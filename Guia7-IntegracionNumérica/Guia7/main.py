from Integral import Integral


integral = Integral()
var = 'S'
while var.lower() =='s':
	eq = input("Ingrese Ecuacion.Ej: 1 - (E**(-2*x))\n> ")
	a = float(input("Desde: \n> "))
	b = float(input("Hasta: \n> "))
	formula = int(input("Con que regla quiere resolverlo? \n1_Trapecio\n2_Simpson 1/3\n3_Simpson 3/8 Simple\n> "))
	if(formula == 1):
		n = int(input("Ingrese cantidad de Intervalos: \n> "))
		print("Resultado: > {}".format(str(integral.trapecio(eq, a, b, n))))
	elif formula == 2:
		n = int(input("Ingrese cantidad de Intervalos: \n> "))
		print("Resultado: > {}".format(str(integral.simpson13(eq, a, b, n))))
	elif formula == 3:
		print("Resultado: > {}".format(str(integral.simpson38Simple(eq, a, b))))
	var = int(input("Desea continuar? (s/n): "))
