import sympy
from sympy.plotting import plot
from sympy.abc import x


class Integral(object):
	"Clase para resolver Integrales Definidas, Los parámetros de entrada del programa serán: intervalo de integración, cantidad de \
				segmentos n en los que se divide el intervalo de integración, función a evaluar. Los resultados\
						que debe proporcionar el programa son: Valor I de la integral, error relativo\
								porcentual aproximado o verdadero, según corresponda. Recordar presentar los resultados\
										de forma clara y detallada, además, el programa debe estar debidamente comentado."

	def __init__(self):
		pass

	def trapecio(self, func, a, b , n=1):
		if(n==1):
			print("\n----- Trapecio Simple -----")
			print (sympy.sympify(func))
			return self.trapecioSimple(func, a, b , n)
		else:
			print("\n----- Trapecio Compuesto -----")
			print (sympy.sympify(func))
			return self.trapecioCompuesto(func, a, b , n)
	
	def trapecioSimple(self, func, a, b , n=1):
		a, b = self.sortAB(a, b) #Obtengo en orden de menor a mayor a y b
		func = sympy.sympify(func)
		fa = func.subs({'x': a}).evalf()
		fb = func.subs({'x': b}).evalf()
		base = abs(b-a)/n
		return (((fa+fb) /2) * base)

	def trapecioCompuesto(self, func, a, b, n):
		a, b = self.sortAB(a,b)
		ts = self.trapecioSimple(func, a, b, n)
		h = abs(b-a)/n
		area = 0
		func = sympy.sympify(func)
		# ts = (func.subs({'x': a}).evalf() + func.subs({'x': b}).evalf() / 2)
		for k in range(1, n):
			aux = a + k*h
			faux = func.subs({'x': aux}).evalf()
			area += faux
		return ((area * h)+ ts)

	def simpson13(self,func,a,b,n=1):
		if(n==1):
			print("\n----- Simpson 1/3 Simple -----")
			print (sympy.sympify(func))
			return self.simpson13Simple(func,a,b)
		else:
			print("\n----- Simpson 1/3 Compuesto -----")
			print (sympy.sympify(func))
			return self.simpson13Compuesto(func,a,b,n)

	def simpson13Simple(self,func,a,b):
		func = sympy.sympify(func)
		a, b = self.sortAB(a, b)
		h = (b-a)/6
		m= (a+b)/2
		area = func.subs({'x': a}).evalf() + 4 * func.subs({'x': m}).evalf() + func.subs({'x': b}).evalf()
		return area * h

	def simpson13Compuesto(self,func,a,b,n):
		func = sympy.sympify(func)
		a, b = self.sortAB(a, b)
		h = (b-a)/n
		suma = 0
		for j in range(1,n): # Equivale a n-1
			aux = a + j*h
			if j %2 == 0: # j es par
				if j <= n-1: # Equivale a n-2
					suma += 2 * func.subs({'x': aux}).evalf()
			else:
				suma += 4 * func.subs({'x': aux}).evalf()
				
		return ((h/3) * (func.subs({'x': a}).evalf() + suma + func.subs({'x': b})))

	def simpson38Simple(self, func, a, b):
		print("\n----- Simpson 3/8 Simple -----")
		func = sympy.sympify(func)
		print (func)
		a, b = self.sortAB(a, b)
		h = (b-a)/n
		return ((3*h)/8) * func.subs({'x': a}).evalf() + 3*func.subs({'x': (2*a + b)/3}).evalf() + 3*func.subs({'x': (a + 2*b)/3}).evalf() + + 3*func.subs({'x': b}).evalf()

	def sortAB(self,a,b):
		if(a > b):
			aux = a
			a = b
			b = aux
		return a,b
