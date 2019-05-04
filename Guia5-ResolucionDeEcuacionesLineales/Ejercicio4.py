import numpy as np
import math
import time

A = [[0, 2, 5],
     [2, 1, 1],
     [3, 1, 0]]

matrizA = np.array(A)

B = [9, 9, 10]
matrizB = np.array(B)

result = np.linalg.solve(matrizA, matrizB)
determinante = np.linalg.det(matrizA)

print("Resultados para las variables:")
for i, item in enumerate(result):
    print("| |_ x{}: {}".format(str(i+1), str(round(item, 2))))

print("|\n|_ Determinante = {}".format(str(round(determinante, 1))))
