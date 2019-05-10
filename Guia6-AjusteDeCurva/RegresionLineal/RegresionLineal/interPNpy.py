# -*- coding: utf-8 -*-
"""
Created on Fri May 10 01:02:39 2019

@author: Agustin
"""



def interpolacionPolNewtonPrimerGradoX(fx,fx0,fx1,x0,x1):
    #definimos el numerador
    numerador = (x1 - x0) * (fx - fx0)
    #feinimos el denominador
    denominador = fx1 - fx0
    
    #retornamos el valor de x
    return (numerador / denominador) + x0
    
# f(x) = f(x0) + [ f(x1) - f(x0) / (x1 - x0) ] * ( x - x0 ) 