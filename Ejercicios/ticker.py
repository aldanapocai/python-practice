# -*- coding: utf-8 -*-
"""
Created on Tue Nov  3 13:59:56 2020

@author: AldanaPocai
"""
from vigilante import vigilar
from informe import leer_camion
import csv
import formato_tabla
    


def elegir_columnas(rows, indices):
    for row in rows:
        yield [row[index] for index in indices]
        
def cambiar_tipo(rows, types):
    for row in rows:
        yield [func(val) for func, val in zip(types, row)]

def hace_dicts(rows, headers):
    for row in rows:
        yield dict(zip(headers, row))
        
def filtrar_datos(filas, nombres):
    for fila in filas:
        if fila['nombre'] in nombres:
            yield fila

def parsear_datos(lines):
    rows = csv.reader(lines)
    rows = elegir_columnas(rows, [0,1,2])
    rows = cambiar_tipo(rows, [str, float, float])
    rows = hace_dicts(rows, ['nombre', 'precio', 'volumen'])
    return rows

def ticker(archivo_camion, archivo_data, formato = 'txt'):
    rows = parsear_datos(vigilar(archivo_data))
    camion = leer_camion(archivo_camion)
    rows = filtrar_datos(rows, camion )
    formateador = formato_tabla.crear_formateador(formato)
    formateador.encabezado(['Nombre', 'Precio', 'Volumen'])
    for row in rows:
        row = list(row.values())
        formateador.fila(row)
        

if __name__ == '__main__':
    ticker('Data/camion.csv', 'Data/mercadolog.csv')
        