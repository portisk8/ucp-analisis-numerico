import numpy as N
import matplotlib.pyplot as plot
'''https://github.com/tiagopereira/python_tips/wiki/Scipy%3A-curve-fitting

La adaptación polinómica es uno de los casos más simples y uno de uso frecuente. 
La forma rápida y fácil de hacerlo en python es usar polyfit de numpy. 
Es rápido, confiable y fácil de usar. Entonces, ¿por qué quieres más? 
Bueno, una razón es que si desea los errores para los coeficientes ajustados. 
El polyfit de Numpy no los computa. Una opción más complicada de usar pero más completa es usar odrpack de scipy's 
(Regresión de distancia ortogonal).
'''

def graficarCurvaMejorAjuste(x, y):
    fit = N.polyfit(x,y,6)
    y_new = N.polyval(fit,x)
    # plot.plot(x, y, 'b-')
    plot.scatter(x, y,label='Valores Experimentales')
    plot.plot(x, y_new, 'r-')
    plot.show()
    