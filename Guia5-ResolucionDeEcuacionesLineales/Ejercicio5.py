import numpy as np
import math
import time

start_time = time.time()

A = [[-3, -1, 3, -2, -3, -2, -5, 9, -6],
     [-6, -4, 8, -6, -4, -7, -8, 5, -8],
     [4, 2, 7, 6, -8, 9, -5, -8, 6],
     [-9, 1, -8, -8, 4, -3, -4, 7, 9],
     [4, 2, 1, 7, -4, 2, 2, 2, -1],
     [-7, 5, 6, 3, 4, -6, 8, 3, 2],
     [5, -8, 7, -8, 4, 2, 6, -3, -8],
     [1, 5, 1, -5, -9, 7, 4, 4, -7],
     [-9, -7, -8, -5, 5, 3, 8, 7, 5]]

matrizA = np.array(A)

B = [80, 115, 127, -101, 28, -60, -2, 32, -108]
matrizB = np.array(B)

result = np.linalg.solve(matrizA, matrizB)
determinante = np.linalg.det(matrizA)

print("Resultados para las variables:")
for i, item in enumerate(result):
    print("| |_ x{}: {}".format(str(i+1), str(item)))

print("|\n|_ Determinante = {}".format(str(determinante)))
print("|_ Tiempo de ejecución: {} segundos".format(str(time.time() - start_time)))
