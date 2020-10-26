# -*- coding: utf-8 -*-
"""
Created on Thu Sep 10 19:42:44 2020

@author: Aldana
"""
def donde_insertar(lista, x, verbose = False):
    '''Búsqueda binaria
    Precondición: la lista está ordenada
    Devuelve la posicion en la que deberia encontrarse x si no está en lista;
    Devuelve p tal que lista[p] == x, si x está en lista
    '''
    if verbose:
        print(f'[DEBUG] izq |der |medio')
    enc = 0 #Si es 1 es porque lo encontro
    izq = 0
    medio = 0
    comp = 0  #Cantidad de comparaciones que realiza
    der = len(lista) - 1
    while izq <= der:
        comp +=1 #por la comparacion del while
        medio = (izq + der) // 2
        if verbose:
            print(f'[DEBUG] {izq:3d} |{der:>3d} |{medio:3d}')
        comp +=1
        if lista[medio] == x:
            pos = medio     # elemento encontrado!
            enc = 1 
        comp +=1 #por mas que haya entrado al if anterior igual va a hacer la comp del sig
        if lista[medio] > x:
            der = medio - 1 # descarto mitad derecha
        else:               # if lista[medio] < x:
            izq = medio + 1 # descarto mitad izquierda
    if enc == 0:
        pos = medio
    return pos, comp

def insertar(lista, x):
    '''
    Precondición: la lista está ordenada
    Devuelve p tal que lista[p] == x, si x está en lista
    Si no esta en la lista lo inserta en la posición correcta y devuelve dicha posicion
    '''
    enc = 0 #Si es 1 es porque lo encontro
    izq = 0
    medio = 0
    der = len(lista) - 1
    while izq <= der:
        medio = (izq + der) // 2
        
        if lista[medio] == x:
            pos = medio     # elemento encontrado!
            enc = 1 
        if lista[medio] > x:
            der = medio - 1 # descarto mitad derecha
        else:               # if lista[medio] < x:
            izq = medio + 1 # descarto mitad izquierda
    if enc == 0:
        pos = medio
        lista[pos] = x
    return pos
    