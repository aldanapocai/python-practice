# -*- coding: utf-8 -*-
"""
Created on Mon Aug 24 20:32:16 2020

@author: Aldana
"""
def busqueda_lineal_lordenada(lista,e):
    i=0
    if lista[i]<e and i<len(lista):
        i+=1
    else:
        i = -1
    return i
    


def buscar_u_elemento(lista, n):
    pos = -1
    
    for i, elemento in enumerate(lista):
        if elemento == n:
            pos = i
    
    return pos

def buscar_n_elemento(lista, n):
    cant = 0
    for elemento in lista:
        if elemento == n:
            cant += 1
    return cant
            

def maximo(lista):
    m = lista[0]
    for e in lista:
        if e > m:
            m = e
    return m     

def minimo(lista):
    m = lista[0]
    for e in lista:
        if e < m:
            m = e
    return m       