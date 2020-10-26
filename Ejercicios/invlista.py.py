# -*- coding: utf-8 -*-
"""
Created on Mon Aug 24 21:01:55 2020

@author: Aldana
"""

def invertir_lista(lista):
    fin = len(lista)
    invertida = [None]*fin #crea una lista con la cant necesaria de None instanciados 
    for i, e in enumerate(lista):
        invertida[fin-1-i] = e #como los indices comienzan en 0 es necesario restar 1
    return invertida
        

invertida_1 = invertir_lista([1, 2, 3, 4, 5])

invertida_2 = invertir_lista(['Bogotá', 'Rosario', 'Santiago', 'San Fernando', 'San Miguel'])