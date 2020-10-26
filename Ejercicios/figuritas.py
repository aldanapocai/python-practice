# -*- coding: utf-8 -*-
"""
Created on Wed Sep  2 12:35:05 2020

@author: Aldana
"""

import random
import numpy as np

#Crear album vacio

def crear_album(figus_total):
    album = np.zeros(figus_total, dtype=np.int64)
    return album

#Si el album esta incompleto devuelve True
def album_incompleto(album):
    for i in album:
        if album[i] == 0:
            return True
            break
        else:
            return False
        
 #Comprar una figurtita aleatoria

def comprar_figu(figus_total):
    figu = random.randint(1,figus_total)
    return figu
       
#4.17 Cuantas comprar para llenarlo

def cuantas_figus(figus_total):
    cant_comprada = 0
    album = crear_album(figus_total)
    while album_incompleto(album) == True:
        figu = comprar_figu(figus_total)
        album[figu-1] = 1 
        cant_comprada +=1
    return cant_comprada


#4.18 promedio para completar el álbum de figus_total figuritas
def promedio(figus_total):
    n_repeticiones = 100
    cant_compras = []
    for i in range(n_repeticiones):
        resultado = cuantas_figus(figus_total)
        cant_compras.append(resultado)
    promedio = np.mean(cant_compras)
    return promedio

#%% Ejercicios con paquetes

def comprar_paquete(figus_total, figus_paquete):
    paquete = [random.randint(1,figus_total) for i in range(figus_paquete)]
    return paquete


def cuantos_paquetes(figus_total, figus_paquete):
    album = crear_album(figus_total)
    paquetes_comprados = 0 
    while album_incompleto(album) == True:
        paquete = comprar_paquete(figus_total, figus_paquete)
        for i in range(len(paquete)):   
            album[paquete[i-1]-1] = 1
            paquetes_comprados +=1
    return paquetes_comprados

compra = cuantos_paquetes(670, 5)

