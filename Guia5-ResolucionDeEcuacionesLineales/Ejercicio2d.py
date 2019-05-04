
'''
Ejercicios con matrices
'''
import numpy as np

A = [[4, 7],
     [1, 2],
     [5, 6]]
matrizA = np.array(A, int)

B = [[4, 3, 7],
     [1, 2, 7],
     [1, 0, 4]]
matrizB = np.array(B, int)

C = [[3],
     [6],
     [1]]
matrizC = np.array(C, int)

D = [[9, 4, 3, 6],
     [2, -1, 7, 5]]
matrizD = np.array(D, int)

E = [[1, 5, 8],
     [7, 2, 3],
     [4, 0, 6]]
matrizE = np.array(E, int)

F = [[3, 0, 1],
     [1, 7, 3]]
matrizF = np.array(F, int)

G = [7, 6, 4]
matrizG = np.array(G, int)

print("1)_ [E] + [B] ")
print(matrizE + matrizB)
print("-----------------------------------")
print("2)_ [A] + [F] ")
try:
    print(matrizA + matrizF)
except Exception as e:
    print(e)
print("-----------------------------------")
print("3)_ [B] + [E] ")
print(matrizB + matrizE)
print("-----------------------------------")
print("4)_ 7 * [B] ")
print(7 * matrizB)
print("-----------------------------------")
print("5)_ [E] * [B] ")
print(np.dot(matrizE, matrizB))
print("-----------------------------------")
print("6)_ {C}T ")
print(matrizC.transpose())
print("-----------------------------------")
print("7)_ [B] * [A] ")
print(np.dot(matrizB, matrizA))
print("-----------------------------------")
print("8)_ {D}T ")
print(matrizD.transpose())
print("-----------------------------------")
print("9)_ [A] * [C] ")
try:
    print(np.dot(matrizA, matrizC))
except Exception as e:
    print(e)
print("-----------------------------------")
print("10)_ [I] * [B] ")
try:
    print(np.dot([[1, 0, 0], [0, 1, 0], [0, 0, 1]], matrizB))
except Exception as e:
    print(e)
print("-----------------------------------")
print("11)_ {E}T * [E] ")
try:
    print(np.dot(matrizE.transpose(), matrizE))
except Exception as e:
    print(e)
print("-----------------------------------")
print("12)_ {C}T * [C] ")
try:
    print(np.dot(matrizC.transpose(), matrizC))
except Exception as e:
    print(e)
print("-----------------------------------")
