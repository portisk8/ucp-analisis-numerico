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
	
