# -*- coding: utf-8 -*-
"""
Created on Fri May 10 01:02:39 2019

@author: Agustin
"""



def interpolacionPolNewtonPrimerGrado(fx,fx0,fx1,x0,x1):
    
    numerador = (x1 - x0) * (fx - fx0)
    denominador = fx1 - fx0
    
    
    return (numerador / denominador) + x0
    