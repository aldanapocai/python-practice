# -*- coding: utf-8 -*-
"""
Created on Wed Sep 16 21:41:12 2020

@author: Aldana
"""

def incrementar(s):
    carry = 1
    l = len(s)
    
    for i in range(l-1,-1,-1):
        if (s[i] == 1 and carry == 1):
            s[i] = 0
            carry = 1
        else:
            s[i] = s[i] + carry
            carry = 0
    return s

def listar_secuencias(n):
    '''
    Devuelve una lista con todas las secuencias binarias de longitud n
    '''
    secuencias = []
    seq = [0]*n
    secuencias.append(seq)
    aux = seq.copy()
    for i in range(2**n-1): #otra forma: while aux != [1]*n:
        seq_sig = incrementar(aux)
        secuencias.append(seq_sig)
        aux = seq_sig.copy()
    return secuencias


def busqueda_secuencial(lista, x):
    '''Si x está en la lista devuelve el índice de su primera aparición, 
    de lo contrario devuelve -1.
    '''
    comps = 0 # inicializo en cero la cantidad de comparaciones
    pos = -1
    for i,z in enumerate(lista):
        if z == x:
            comps +=1
            pos = i
            break
    return pos , comps