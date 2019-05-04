
'''
Ejercicios con matrices
'''
import numpy as np

A = [[4, 7],
     [1, 2],
     [5, 6]]
matrizA = np.array(A, int)
print(matrizA)
shape = matrizA.shape
print("Dimension: {}x{}".format(shape[0], shape[1]))
B = [[4, 3, 7],
     [1, 2, 7],
     [1, 0, 4]]
matrizB = np.array(B, int)
print(matrizB)
shape = matrizB.shape
print("Dimension: {}x{}".format(shape[0], shape[1]))

C = [[3],
     [6],
     [1]]
matrizC = np.array(C, int)
print(matrizC)
shape = matrizC.shape
print("Dimension: {}x{}".format(shape[0], shape[1]))

D = [[9, 4, 3, 6],
     [2, -1, 7, 5]]
matrizD = np.array(D, int)
print(matrizD)
shape = matrizD.shape
print("Dimension: {}x{}".format(shape[0], shape[1]))

E = [[1, 5, 8],
     [7, 2, 3],
     [4, 0, 6]]
matrizE = np.array(E, int)
print(matrizE)
shape = matrizE.shape
print("Dimension: {}x{}".format(shape[0], shape[1]))

F = [[3, 0, 1],
     [1, 7, 3]]
matrizF = np.array(F, int)
print(matrizF)
shape = matrizF.shape
print("Dimension: {}x{}".format(shape[0], shape[1]))

G = [7, 6, 4]
matrizG = np.array(G, int)
print(matrizG)
shape = matrizG.shape
print("Dimension: {}".format(shape[0]))
