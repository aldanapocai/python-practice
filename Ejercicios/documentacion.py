# -*- coding: utf-8 -*-.
#Ejercicio 6.8: Funciones y documentación
"""
Created on Wed Sep 23 13:08:33 2020

@author: Aldana_Pocai
"""

def valor_absoluto(n):
    """
    Pre: se debe ingresar un numero.
    
    Pos: Se devuelve el valor absoluto de dicho numero.
    """
    if n >= 0:
        return n
    else:
        return -n
    #n invariante
    

def suma_pares(l):
    """
    Pre: recibe una lista con numeros.
    
    Pos: devuelve la sumatoria de los numeros pares de dicha lista.
    """
    res = 0
    for e in l:
        if e % 2 ==0:
            res += e
        else:
            res += 0

    return res #invariante: res

def veces(a, b):
    '''
    Pre: recibe dos numeros, b debe ser entero
    Pos: devuelve 'a' veces 'b' 
    '''
    res = 0
    nb = b #cant de veces totales a sumar a 
    while nb != 0: 
        #print(nb * a + res)
        res += a
        nb -= 1 #una vez efectuada la suma, hace que b tenga una suma menos que realizar
    return res

def collatz(n):
    '''
    Pre: recibe un n distinto de 0. 
    Pos: devuelve la sequencia de collatz: la cantidad de pasos para llegar al 1
    '''    
    res = 1

    while n!=1:
        if n % 2 == 0:
            n = n//2
        else:
            n = 3 * n + 1
        res += 1

    return res

