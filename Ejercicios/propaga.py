# -*- coding: utf-8 -*-
"""
Created on Mon Aug 24 21:12:46 2020

@author: Aldana

"""
#Uso funcion del archivo anterior

def invertir_lista(lista):
    fin = len(lista)
    invertida = [None]*fin #crea una lista con la cant necesaria de None instanciados 
    for i, e in enumerate(lista):
        invertida[fin-1-i] = e #como los indices comienzan en 0 es necesario restar 1
    return invertida

#Como tengo que realizar este proceso dos veces, preferi dejarlo en una funcion

def propagar_aux_un_sentido(vector):
    fin_lista = len(vector)-1 
    for i, fosforo in enumerate(vector):
            if fosforo == 1 and not vector[i-1] == -1:
                vector[i-1] = 1
            if fosforo == 1 and i < fin_lista:
                if not vector[i+1] == -1:
                    vector[i+1] = 1
    return vector

def propagar(lista):
    vector = propagar_aux_un_sentido(lista) #propago en un sentido
    vector_aux = propagar_aux_un_sentido(invertir_lista(vector)) #propago la lista inversa de la recien propagada
    vector_final = invertir_lista(vector_aux) #la vuelvo a invertir asi se corresponde con la original
    return vector_final


propa_1 = propagar([ 0, 0, 0,-1, 1, 0, 0, 0,-1, 0, 1, 0, 0])

propa_2 = propagar([ 0, 0, 0, 1, 0, 0])