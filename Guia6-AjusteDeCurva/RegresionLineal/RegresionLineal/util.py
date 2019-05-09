import numpy as np

def obtenerA0A1MinimoCuadrado(x,y):
	'''params:
			x: Array
			y: Array
		returns:
			a0: float
			a1: float'''
	sumxy = 0
	sumx2 = 0
	for index, yi in enumerate(y):
		sumxy += x[index]*yi
		sumx2 += x[index]**2
	numerador = len(x) * sumxy - np.sum(x)*np.sum(y)
	denominador = len(x) * sumx2 - (np.sum(x) **2)
	a1 = numerador / denominador
	a0 = np.average(y) - a1* np.average(x)
	return a1, a0
	
 # y = a0  +  a1 X
 # a1 = [n*sum(xi*yi) - sum xi * sum yi ] / [n * sum xi^2 - (sum xi)^2]
 # a0 = y raya - (a1 * x raya)
 # a1 = -1 / tau => tau = -1 / a1
 # a0 = Ln Ve => Ve = e ^ a0