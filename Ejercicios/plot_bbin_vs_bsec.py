# -*- coding: utf-8 -*-
"""
Created on Wed Sep 16 23:42:15 2020

@author: Aldana
"""

import random
import matplotlib.pyplot as plt
import numpy as np
from bbin import donde_insertar as busqueda_binaria

def generar_lista(n, m):
    ''' devuelve una lista ordenada de n elementos diferentes entre 0 y m-1'''
    l = random.sample(range(m), k = n)
    l.sort()
    return l

def generar_elemento(m):
    return random.randint(0, m-1)

def busqueda_secuencial_(lista, x):
    '''Si x está en la lista devuelve el índice de su primer aparición, 
    de lo contrario devuelve -1.
    '''
    comps = 0 # inicializo en cero la cantidad de comparaciones
    pos = -1
    for i,z in enumerate(lista):
        comps += 1 # sumo la comparación que estoy por hacer
        if z == x:
            pos = i
            break
    return pos, comps



m = 10000
n = 100
k = 1000
lista = generar_lista(n, m)

def experimento_secuencial_promedio(lista, m, k):
    comps_tot = 0
    for i in range(k):
        x = generar_elemento(m)
        comps_tot += busqueda_secuencial_(lista,x)[1]

    comps_prom = comps_tot / k
    return comps_prom

def experimento_binario_promedio(lista, m, k):
    ''' cuente la cantidad de comparaciones que realiza en promedio (entre k experimentos elementales)
    la búsqueda binaria sobre la lista pasada como parámetro.'''
    comps_tot = 0
    for i in range(k):
        x = generar_elemento(m)
        comps_tot += busqueda_binaria(lista,x)[1]
    comps_prom = comps_tot / k
    return comps_prom


    
#Graficos

largos = np.arange(256) + 1 # estos son los largos de listas que voy a usar
comps_promedio_seq = np.zeros(256) # aca guardo el promedio de comparaciones sobre una lista de largo i, para i entre 1 y 256.
comps_promedio_bin = np.zeros(256)


for i, n in enumerate(largos):
    lista = generar_lista(n,m) #genero lista de largo n 
    comps_promedio_seq[i] = experimento_secuencial_promedio(lista,m,k)
    comps_promedio_bin[i] = experimento_binario_promedio(lista, m, k)

# ahora grafico largos de listas contra operaciones promedio de búsqueda.

plt.plot(largos, comps_promedio_seq, label = 'Busqueda Secuencial')
plt.plot(largos, comps_promedio_bin, label= 'Busqueda Binaria')
plt.xlabel('Largo de la lista')
plt.ylabel('Cantidad de comparaciones')
plt.xlim(0,50)
plt.ylim(0,50)
plt.title('Complejidad de la busqueda')
plt.legend()

