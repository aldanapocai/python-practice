# -*- coding: utf-8 -*-
"""
Created on Tue Sep  1 18:30:57 2020

@author: Aldana
"""
#%% 4.7 Generala no necesariamente servida

import random
import sys
from collections import Counter


def tirar(n):
    tirada = []
    for i in range(n):
        tirada.append(random.randint(1,6))
    return tirada


def es_generala(tirada):
    lenght = len(tirada)
    for i in range(lenght):
        if tirada[i] == tirada[0]:
            result = True
        else:
            result = False
            break   
    return result

def separa_tirada(tirada):
    repetidos = []
    a_tirar = []
    cuenta_ocurrencias = Counter(tirada)  #Dicc desordenado de los valores y cuantas ocurrencias tienen
    resultado_mas_comun = cuenta_ocurrencias.most_common(1)[0][0] #Obtengo el elemento mas comun (1) y con el [0][0] su valor y no el numero de iterancias
    lenght = len(tirada)
    for i in range(lenght):
        if tirada[i] == resultado_mas_comun:
            repetidos.append(tirada[i])  
        else:
            a_tirar.append(tirada[i])
    return repetidos, a_tirar



def jugada():
    #Tirada 1
    n = 5 #Cantidad de dados a tirar inicial 
    tirada1 = tirar(n)
    x = es_generala(tirada1)
    
    if x == True:
        print('Generala servida')
        return True
    else:
        dados_repetidos, dados_a_tirar = separa_tirada(tirada1)
        #Tirada 2
        n = len(dados_a_tirar)
        tirada2 = tirar(n)
        tirada2.extend(dados_repetidos) #Anexo las dos tiradas
        x = es_generala(tirada2)
        if x == True:
             print('Generala en la segunda ronda')
             return True
        else:
            dados_repetidos, dados_a_tirar = separa_tirada(tirada2)
            #Tirada 3
            n = len(dados_a_tirar)
            tirada3 = tirar(n)
            tirada3.extend(dados_repetidos)
            x = es_generala(tirada2)
            if x == True:
                print('Generala en la tercera ronda')
                return True
            else:
                return False

#Para determinar si hubo generala servida           
def jugada_generala_servida():
    #Tirada 1
    n = 5 #Cantidad de dados a tirar inicial 
    tirada1 = tirar(n)
    x = es_generala(tirada1)
    if x == True:
        return True
    else:
        return False
    
def probabilidad(N):
    G = sum([jugada() for i in range(N)])
    M = sum([jugada_generala_servida() for i in range(N)])
    prob = G/N
    prob2 = M/N
    print(f' Tire {N} veces, de las cuales {G-M} saque generala no necesariamente servida, y {M} generala servida')
    print(f'Podemos estimar la probabilidad de sacar generala no necesariamente servida mediante {prob:.6f} y de sacar generalada servida {prob2:.6f}')
    return prob

#Para ingresar parametro

if len(sys.argv) == 2:
    N = sys.argv[1]
else:
    N=100
    
    
probabilidad = probabilidad(N)

#%%EXTRA
#Para poder ir viendo como van saliendo las tiradas en una jugada
def jugada_a_imprimir():
    #Tirada 1
    n = 5 #Cantidad de dados a tirar inicial 
    tirada1 = tirar(n)
    print(f'Primera ronda: {tirada1}')
    x = es_generala(tirada1)
    
    if x == True:
        print('Generala servida en la primera ronda')
        return True
    else:
        dados_repetidos, dados_a_tirar = separa_tirada(tirada1)
        #Tirada 2
        n = len(dados_a_tirar)
        tirada2 = tirar(n)
        tirada2.extend(dados_repetidos) #Anexo las dos tiradas
        print(f'Segunda ronda: {tirada2}')
        x = es_generala(tirada2)
        if x == True:
             print('Generala en la segunda ronda')
             return True
        else:
            dados_repetidos, dados_a_tirar = separa_tirada(tirada2)
            #Tirada 3
            n = len(dados_a_tirar)
            tirada3 = tirar(n)
            tirada3.extend(dados_repetidos)
            print(f'Tercera ronda: {tirada3}')
            x = es_generala(tirada2)
            if x == True:
                print('Generala en la tercera ronda')
                return True
            else:
                return False

