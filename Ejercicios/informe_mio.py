# -*- coding: utf-8 -*-
#informe.py

"""
Created on Mon Sep 21 19:40:40 2020

@author: Aldana_Pocai



"""

from fileparse import parse_csv
from lote import Lote
from camion import Camion

def leer_camion(nom_archivo):
    '''
    Lee un archivo de lotes en un camión 
    y lo devuelve como lista de diccionarios con claves
    nombre, cajones, precio.
    '''
    with open(nom_archivo) as lines:
        camion_dicts = parse_csv(lines, select=['nombre','cajones','precio'], 
                                 types=[str,int,float])
    #lo devuelve como lista de elementos de la clase lote
    camion = [Lote(d['nombre'], d['cajones'], d['precio']) for d in camion_dicts]
    return Camion(camion)
    
    
def leer_precios(nom_archivo):
    '''
    Lee un archivo CSV con data de precios 
    y lo devuelve como un diccionario
    con claves nombres y con sus precios como valores
    '''
    with open(nom_archivo) as lines:
        return dict(parse_csv(lines, types = [str,float], has_headers = False))

#%%
def hacer_informe(lista_camion, precios):
    '''
    Devuelve una lista de tuplas de los valores necesarios para realizar el informe
    '''
    informe = []
    for n in lista_camion:
        articulo = n.nombre
        precio_v = precios[articulo]
        cambio = precio_v - n.precio
        info = (articulo, n.cajones, precio_v, cambio )
        informe.append(info)
    return informe



def imprimir_informe(informe):
    ''' Imprime el formulario con formato'''
    print(' Nombre     Cajones     Precio     Cambio')
    print('---------- ---------- ---------- ----------')
    for nombre, cajones, precio, cambio in informe:
         precio_v = f"${precio:.2f}"
         print(f'{nombre:>10s} {cajones:>10d} {precio_v:>10} {cambio:>10.2f}')

def informe_camion(nombre_archivo_camion, nombre_archivo_precios):
    camion = leer_camion(nombre_archivo_camion)
    precios = leer_precios(nombre_archivo_precios)
    informe = hacer_informe(camion, precios)
    imprimir_informe(informe)

#%%
def main(arg):
    if len(arg) < 3:
        raise SystemExit(f'Uso adecuado: {arg[0]} ' 'archivo_camion archivo_precios')
    elif len(arg) == 3:
        informe_camion(arg[1], arg[2])
    elif len(arg) == 4:
        informe_camion(arg[1], arg[2], arg[3])
  
   
#%%
if __name__ == '__main__':
    import sys
    main(sys.argv)
    
