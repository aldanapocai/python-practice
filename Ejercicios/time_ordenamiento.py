# -*- coding: utf-8 -*-
"""
Created on Tue Oct 27 19:01:46 2020. 

@author: AldanaPocai
"""

import time
import timeit as tt
import random
import copy
from matplotlib import pyplot as plt
import numpy as np

#%%

def generar_lista(N):
    """ 
    Genera genere una lista aleatoria de largo N con números enteros del
    1 al 1000 (puede haber repeticiones).
    """
    lista = []
    for i in range(N):
        lista.append(random.randint(1,1000))
    return lista
 
#%% ORDENAMIENTO POR SELECCION 

def ord_seleccion(lista):
    """Ordena una lista de elementos según el método de selección.
       Pre: los elementos de la lista deben ser comparables.
       Post: la lista está ordenada. Devuelve cantidad de comparaciones realizadas.
       """

    # posición final del segmento a tratar
    n = len(lista) - 1
    # mientras haya al menos 2 elementos para ordenar
    while n > 0:
        # posición del mayor valor del segmento
        p = buscar_max(lista, 0, n)
        # intercambiar el valor que está en p con el valor que
        # está en la última posición del segmento
        lista[p], lista[n] = lista[n], lista[p]

        # reducir el segmento en 1
        n = n - 1
    
def buscar_max(lista, a, b):
    """Devuelve la posición del máximo elemento en un segmento de
       lista de elementos comparables.
       La lista no debe ser vacía.
       a y b son las posiciones inicial y final del segmento"""

    pos_max = a
    for i in range(a + 1, b + 1):
        if lista[i] > lista[pos_max]:
            pos_max = i
    return pos_max

#%% ORDENAMIENTO POR INSERCION
def ord_insercion(lista):
    """Ordena una lista de elementos según el método de inserción.
       Pre: los elementos de la lista deben ser comparables.
       Post: la lista está ordenada."""
    for i in range(len(lista) - 1):
        # Si el elemento de la posición i+1 está desordenado respecto
        # al de la posición i, reubicarlo dentro del segmento [0:i]
        if lista[i + 1] < lista[i]:
            reubicar(lista, i + 1)

def reubicar(lista, p):
    """Reubica al elemento que está en la posición p de la lista
       dentro del segmento [0:p-1].
       Pre: p tiene que ser una posicion válida de lista."""
    v = lista[p]
    # Recorrer el segmento [0:p-1] de derecha a izquierda hasta
    # encontrar la posición j tal que lista[j-1] <= v < lista[j].
    j = p
    while j > 0 and v < lista[j - 1]:
        # Desplazar los elementos hacia la derecha, dejando lugar
        # para insertar el elemento v donde corresponda.
        lista[j] = lista[j - 1]
        j -= 1

    lista[j] = v
    
#%% ORDENAMIENTO POR BURBUJEO
def ord_burbujeo(lista):
    """
    Ordena una lista de elementos según el método de burbujeo.
    
    Pre: los elementos de la lista deben ser comparables.
    Post: la lista está ordenada.
    """
    for m in range(1,len(lista)): #Se realizan len(lista) recorridos de la lista.
        for i in range(len(lista)-m):
            if lista[i] > lista[i+1]: #La cant de intercambios sera <= len(lista), siendo = en el peor caso.  
                lista[i], lista[i+1] = lista[i+1], lista[i]
   

#%% 11.7 Merge Sort

def merge_sort(lista):
    """Ordena lista mediante el método merge sort.
       Pre: lista debe contener elementos comparables.
       Devuelve: una nueva lista ordenada."""
    if len(lista) < 2:
        lista_nueva = lista
    else:
        medio = len(lista) // 2
        izq = merge_sort(lista[:medio])
        der = merge_sort(lista[medio:])
        lista_nueva = merge(izq, der)
    return lista_nueva

def merge(lista1, lista2):
    """Intercala los elementos de lista1 y lista2 de forma ordenada.
       Pre: lista1 y lista2 deben estar ordenadas.
       Devuelve: una lista con los elementos de lista1 y lista2."""
    i, j = 0, 0
    resultado = []

    while(i < len(lista1) and j < len(lista2)):
        if (lista1[i] < lista2[j]):
            resultado.append(lista1[i])
            i += 1
        else:
            resultado.append(lista2[j])
            j += 1

    # Agregar lo que falta de una lista
    resultado += lista1[i:]
    resultado += lista2[j:]

    return resultado


#%%Experimento 11.8 Funciones

def generar_listas(Nmax):
    #Lista donde se van a guardar las listas
    listas = []
   #generacion de listas 
    for i in range(Nmax):
        list = generar_lista(i+1)
        listas.append(list)
    return listas
 
    
def experimento_timeit_ordenamiento(metodo,listas, num):
    """
    Realiza un experimento usando timeit para evaluar el método
    ingresado de ordenamiento de listas
    con las listas pasadas como entrada
    y devuelve los tiempos de ejecución para cada lista
    en un vector.
    El parámetro 'listas' debe ser una lista de listas.
    El parámetro 'num' indica la cantidad de repeticiones a ejecutar el método para cada lista.
    """
    tiempos = []
    global lista
    
    for lista in listas:
        #Evaluo el metodo correspondiente en una copia nueva para cada interaccion
        if metodo == ord_seleccion:
            tiempo = tt.timeit('ord_seleccion(lista.copy())', number = num, globals =globals())
        elif metodo == ord_insercion:
            tiempo = tt.timeit('ord_insercion(lista.copy())', number = num, globals =globals())            
        elif metodo == ord_burbujeo:
            tiempo = tt.timeit('ord_burbujeo(lista.copy())', number = num, globals =globals())
        elif metodo == merge_sort:
            tiempo = tt.timeit('merge_sort(lista)', number = num, globals =globals())            
        else:
            return print("Ingrese un metodo de ordeamiento correcto")
        #Guardo  el resultado
        tiempos.append(tiempo)
        # paso los tiempos a arrays
    tiempos = np.array(tiempos)
    
    return tiempos

#%%Experimento en si a ejecutar
#Numero de elementos de la lista mas larga
Nmax = 100
listas_seleccion = generar_listas(Nmax)
listas_insercion = copy.deepcopy(listas_seleccion)
listas_burbujeo = copy.deepcopy(listas_seleccion)
listas_merge_sort = copy.deepcopy(listas_seleccion)

#Coord x
largo_lista = np.arange( Nmax)
#Coord y
tiempos_seleccion = experimento_timeit_ordenamiento(ord_seleccion, listas_seleccion, 100)
tiempos_insercion = experimento_timeit_ordenamiento(ord_insercion, listas_insercion, 100)
tiempos_burbujeo = experimento_timeit_ordenamiento(ord_burbujeo, listas_burbujeo, 100)
tiempos_merge_sort = experimento_timeit_ordenamiento(merge_sort, listas_merge_sort, 100)

#Graficos
plt.plot(largo_lista, tiempos_seleccion, label = "Seleccion")
plt.plot(largo_lista, tiempos_insercion, label="Insercion")
plt.plot(largo_lista, tiempos_burbujeo, label ="Burujeo")
plt.plot(largo_lista, tiempos_merge_sort, label = "Merge Sort")
plt.xlabel("Cantidad de elementos en la lista")
plt.ylabel("Tiempos de ejecucion")
plt.title("COMPARACION ORDENAMIENTOS DE LISTAS")
plt.legend()


