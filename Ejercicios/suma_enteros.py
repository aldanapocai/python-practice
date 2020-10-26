# -*- coding: utf-8 -*-
#6.6 Sumas
"""
Created on Wed Sep 23 12:07:49 2020

@author: Aldana
"""
#Suma usando ciclo

def sumar_enteros(desde, hasta):
    '''Calcula la sumatoria de los números entre desde y hasta.
           Si hasta < desde, entonces devuelve cero.
    
        Pre: desde y hasta son números enteros
        Pos: Se devuelve el valor de sumar todos los números del intervalo
            [desde, hasta]. Si el intervalo es vacío se devuelve 0
    '''
    
    if hasta < desde:
        suma = 0
    else:
        i = 0
        suma = desde
        sig = desde
        while i<(hasta-desde):
            i+=1
            sig+=1
            suma += sig 
    
    return suma

x= sumar_enteros(1,10)


#Suma como diferencia de numeros triangulares

def sum_enteros(desde, hasta):
    '''Calcula la sumatoria de los números entre desde y hasta.
           Si hasta < desde, entonces devuelve cero.
    
        Pre: desde y hasta son números enteros
        Pos: Se devuelve el valor de sumar todos los números del intervalo
            [desde, hasta]. Si el intervalo es vacío se devuelve 0
    '''
    if hasta < desde:
        return 0
    
    else:
        t1 = (desde*(desde+1))/2
        t2= (hasta*(hasta+1))/2
        return int(t2-t1+1)

y = sum_enteros(1,10)


    
