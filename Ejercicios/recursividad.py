# -*- coding: utf-8 -*-
"""
Created on Sat Oct 17 14:27:12 2020

@author: Aldana
"""

#%% Implementacion recursiva
def factorial(n):
    """Precondición: n entero positivo
       Devuelve: n!"""
    if n == 1:
        return 1
    return n * factorial(n - 1)

#%% Implementacion recursiva detallada
def factorial(n):
    if n ==1:
        r = 1
        return r
    
    f = factorial(n-1)
    r = n * f
    return r

factorial(3)

#%%Implementacion iterativa
def factorial(n):
    """Precondicion n positivo. Devuelve n!."""
    fact = 1
    for num in range(n, 1, -1):
        fact *= num
    return fact

    
a = factorial(3)


#%% Diseno de algoritmos recursivos

def sumar(lista):
    """Precondicion len(lista)>=1.
        Devuelve la suma de los elementos de la lista."""
    res = 0
    if len(lista) != 0:
        res = lista[0] + sumar(lista[1:])
    return res
        

#%%Ejercicio 10.2

def sumar_enteros(desde, hasta):
    """Suma enteros de forma recursiva"""
    if desde == hasta:
        return 0
    return 1 + sumar_enteros(desde+1, hasta)

#Tests
suma = sumar_enteros(4,9)

suma_2 = sumar_enteros(-5,6)

suma_3 = sumar_enteros(1,100)


#%%Ejercicio 10.3 Digitos

def cant_digitos(num):
    """Cuenta la cantidad de digitos de un numero.
    
    Precondicion: el numero ingresado debe ser entero positivo
    """
    if num <= 0:
        return 0
    n = str(num)
    return 1 + cant_digitos(num - int(n[0])*10**(len(n)-1))

#Tests

dig_1 = cant_digitos(1)
dig_1_bis = cant_digitos(8)
dig_2 = cant_digitos(15)
dig_5 = cant_digitos(25676)


#%%10.4 Potencias

def es_potencia(potencia, base):
    """Calcula de forma recursiva si un numero es potencia de cierta base"""
    if potencia == 1:
        return True
    if potencia <= 0:
        return False
    return es_potencia(potencia/base, base)

#Tests

es_potencia(8, 2)
es_potencia(64, 4)
es_potencia(70, 10)
es_potencia(1, 2)


