# -*- coding: utf-8 -*-
"""
Created on Sun Oct 25 15:30:29 2020.

@author: AldanaPocai
"""

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
    comp = 0 #comparaciones a realizar 
    # mientras haya al menos 2 elementos para ordenar
    while n > 0:
        # posición del mayor valor del segmento
        p = buscar_max(lista, 0, n)
        comp += n #buscar_max realiza en este caso n-0 comparaciones
        # intercambiar el valor que está en p con el valor que
        # está en la última posición del segmento
        lista[p], lista[n] = lista[n], lista[p]
        # print("DEBUG: ", p, n, lista)

        # reducir el segmento en 1
        n = n - 1
    
    return comp

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
    comp = 0
    for i in range(len(lista) - 1):
        # Si el elemento de la posición i+1 está desordenado respecto
        # al de la posición i, reubicarlo dentro del segmento [0:i]
        if lista[i + 1] < lista[i]:
            reubicar(lista, i + 1)
        comp +=1
        # print("DEBUG: ", lista)
    return comp

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
    Ordena una lista de elementos según el método de inserción.
    
    Pre: los elementos de la lista deben ser comparables.
    Post: la lista está ordenada.
    """
    comp =0
    for m in range(1,len(lista)): #Se realizan len(lista) recorridos de la lista.
        for i in range(len(lista)-m):
            if lista[i] > lista[i+1]: #La cant de intercambios sera <= len(lista), siendo = en el peor caso.  
                lista[i], lista[i+1] = lista[i+1], lista[i]
            comp +=1
    return comp    


#%% COMPARACIONES ENTRE METODOS

#Experimento 1 con una lista

# a = generar_lista(5)

# a_seleccion = copy.deepcopy(a)
# a_insercion = copy.deepcopy(a)
# a_burbujeo = copy.deepcopy(a)

# comp_seleccion = ord_seleccion(a_seleccion)
# comp_insercion = ord_insercion(a_insercion)
# comp_burbujeo = ord_burbujeo(a_burbujeo)

#11.4 Experimento con 100 listas de largo 10
# comp_seleccion = []
# comp_insercion = []
# comp_burbujeo = []
# N = 100 #Cantidad de veces a realizar el experimento
# for i in range(N):
#     list = generar_lista(10)
#     list_seleccion = copy.deepcopy(list)
#     list_insercion = copy.deepcopy(list)
#     list_burbujeo = copy.deepcopy(list)
    
#     comp_seleccion.append(ord_seleccion(list_seleccion))
#     comp_insercion.append(ord_insercion(list_insercion))
#     comp_burbujeo.append(ord_burbujeo(list_burbujeo))
    

# prom_seleccion = sum(comp_seleccion)/N
# prom_insercion = sum(comp_insercion)/N    
# prom_burbujeo = sum(comp_burbujeo)/N
    
# print("COMPARACION DE METODOS DE ORDENAMIENTO - PROMEDIOS")
# print("---------------------------------------------------")
# print("SELECCION       INSERCION       BURBUJEO")
# print(f'   {prom_seleccion}           {prom_insercion}            {prom_burbujeo}')


#%%11.5 COMPARACION GRAFICAMENTE

comparaciones_seleccion = np.empty(256, dtype = np.int64)
comparaciones_insercion = np.empty(256, dtype = np.int64)
comparaciones_burbujeo = np.empty(256, dtype = np.int64)

for i in range(1,257):
    list = generar_lista(i)
    list_seleccion = copy.deepcopy(list)
    list_insercion = copy.deepcopy(list)
    list_burbujeo = copy.deepcopy(list)
    
    
    comparaciones_seleccion[i-1] = ord_seleccion(list_seleccion)
    comparaciones_insercion[i-1] = ord_insercion(list_insercion)
    comparaciones_burbujeo[i-1] = ord_burbujeo(list_burbujeo)  
    
largo_lista = np.arange(1,257)

#Graficos

plt.plot(largo_lista, comparaciones_seleccion, label="Seleccion")
plt.plot(largo_lista, comparaciones_insercion, label="Insercion")
plt.plot(largo_lista, comparaciones_burbujeo, label ="Burujeo")
plt.xlabel("Cantidad de elementos en la lista")
plt.ylabel("Comparaciones realizadas")
plt.title("COMPARACION ORDENAMIENTOS DE LISTAS")
plt.legend()

<<<<<<< HEAD
#%% 11.7 Merge Sort

def merge(izq, der, comp):
    """Recibe dos listas ordenadas y devuelve una nueva al intercalarlas de forma ordenada."""
    resultado = []
    i = j = 0
    while( i<len(izq) and j<len(der)):
        comp +=1
        if (izq[i] < der[j]):
            resultado.append(izq[i])
            i +=1
        else:
            resultado.append(der[j])
            j +=1
    resultado += izq[i:]
    resultado += der[j:]
    return resultado, comp




def merge_sort(lista, comparaciones = 0):
    """Ordena una lista por el metodo merg sort."""    
    comparaciones +=1
    if len(lista) < 2:
        return lista, comparaciones
    else:
        medio = len(lista) // 2
        izq, c1 = merge_sort(lista[:medio])
        der, c2 = merge_sort(lista[medio:])
        comparaciones += c1 + c2
    lista_nueva, comparaciones = merge(izq, der, comparaciones)
    return lista_nueva, comparaciones

lista = [6, 7, -1, 0, 5, 2, 3, 8]


lista_nueva, comparaciones = merge_sort(lista)

=======
>>>>>>> 12668302a2ea93517bde4d8cdb01759865f8b743

    

