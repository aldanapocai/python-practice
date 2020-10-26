# -*- coding: utf-8 -*-
"""
Created on Sun Aug 23 14:41:26 2020

@author: cosme_fulanito_1
"""

#arboles.py

import csv
from pprint import pprint
import sys
#%%
# Carga el archivo con los datos requeridos de los arboles de BS AS
if len(sys.argv) == 2:
    nombre_archivo = sys.argv[1]
else:
    nombre_archivo = 'data_verde.csv'
    parque = 'GENERAL PAZ'

#%%
##Define la funcion para leer datos del parque
def leer_parque(nombre_archivo, parque):
    record = {}
    l_parque = []
   
    with open(nombre_archivo, 'rt', encoding='utf8') as f:
        rows = csv.reader(f)
        encabezados = next(rows)
        for row in rows:
            record = dict(zip(encabezados, row))
            if record['espacio_ve'] == parque:
                l_parque.append(record)
    
    return l_parque


#%%
# Define la funcion para listar las especies por parque
def especies(lista_arboles):
    datos_especie = {}
    l_especies = []
    for i in lista_arboles:
        datos_especie = dict(i)
        for k in datos_especie:
            if k == 'nombre_com':
                l_especies.append(datos_especie['nombre_com'])
    return set(l_especies)
    

#%%    
# Define la funcion para contar árboles de una determinada especie en un parque
def contar_ejemplares(lista_arboles):
    from collections import Counter
    tenencias = Counter()
    for i in lista_arboles:
        datos_especie = dict(i)
        datos_especie['num'] = 1
        tenencias[datos_especie['nombre_com']] += int(datos_especie['num'])
    return tenencias

#%%
# Define la funcion para obtener las alturas de una especie en un parque
def obtener_alturas(lista_arboles, especie):
    al_especies = []
    for i in lista_arboles:
        if i['nombre_com'] == especie:
            al_especies.append(float(i['altura_tot']))
    return al_especies


#%%
# Define la funcion para obtener las inclinaciones de los ejemplares de una especie en un parque
def obtener_inclinaciones(lista_arboles, especie):
    incl = []
    for i in lista_arboles:
        if i['nombre_com'] == especie:
            incl.append(i['inclinacio'])
    return incl

## Define la funcion para contar árboles de una determinada especie en un parque
#%%
# NO FUNCIONA
'''
def especimen_mas_inclinado(lista_arboles):
    datos_especie = {}
    incl = []
    listita = []
    for i in lista_arboles:
        datos_especie = dict(i)
        for k in datos_especie:
            if k == 'nombre_com':
                listita.append(datos_especie['nombre_com'])
        
        if i['nombre_com'] == especie:
            incl.append(i['inclinacio'])
            lis = zip(listita, incl)
    pprint(lis)
    return lis           
'''                
#%%
# Para realizar los parques utiliza un for para cada uno de los parques listados en la variable 'parque'

parque = ['GENERAL PAZ', 'ANDES, LOS', 'CENTENARIO']
lista_arboles = []

for i in parque:
    p = leer_parque(nombre_archivo, i)
    lista_arboles.append(p)

    n = []
    le = []
    mc = []
    al_promedio = []
    al_maxima = []
    sp_inc = []
    mas_incl = []

    for j in lista_arboles:
        numero = len(j)
        n.append(numero)
    
        lista_especies = especies(j)
        le.append(lista_especies)

        tenencias = contar_ejemplares(j)
        mc.append(tenencias.most_common(5))
    
        especie = 'Jacarandá'
        alturas = obtener_alturas(j, especie)
        al_maxima.append(round(max(alturas),2))
        al_promedio.append(round(sum(alturas)/len(alturas),2))
        
        inclinados = obtener_inclinaciones(j, especie)
        sp_inc.append(inclinados)
        
#        inc_esp_list = especimen_mas_inclinado(j)
#        mas_incl.append(inc_esp_list)

#%%
# Resultados en forma de tabla para todos los parques
print(f'--------------------------------------------------------------------------')
print(f'                          |{parque[0]:^15}|{parque[1]:^15}|{parque[2]:^15}')
print(f'                          ------------------------------------------------')

print(f' Numero de Arboles        |{n[0]:^15}|{n[1]:^15}|{n[2]:^15}')
print(f' Altura maxima {especie}  |{al_maxima[0]:^15}|{al_maxima[1]:^15}|{al_maxima[2]:^15}')    
print(f' Altura prom   {especie}  |{al_promedio[0]:^15}|{al_promedio[1]:^15}|{al_promedio[2]:^15}')    
print(f'--------------------------------------------------------------------------')

#Lista de especies total y comunes para todos los parques
print(f' \n Especies mas comunes {parque[0]}:') 
pprint(mc[0])
print(f' \n Especies mas comunes {parque[1]}:') 
pprint(mc[1])
print(f' \n Especies mas comunes {parque[2]}') 
pprint(mc[2])

pprint(f' \nEjemplares inclinados de {especie} en {parque[0]}:')
pprint(f'{sp_inc[0]}')

pprint(f' \nEjemplares inclinados de {especie} en {parque[1]}:')
pprint(f'{sp_inc[1]}')

pprint(f' \nEjemplares inclinados de {especie} en {parque[2]}:')
pprint(f'{sp_inc[2]}')


pprint(f' \n Lista de Especies {parque[0]}:') 
pprint(le[0])


print(f' \n Lista de Especies {parque[1]}:') 
pprint(le[1])

print(f' \n Lista de Especies {parque[2]}:') 
pprint(le[2])
