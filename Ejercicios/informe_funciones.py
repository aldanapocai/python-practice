#tabla_informe.py 
#los precios en camion.csv son los precios pagados al productor de frutas mientras que
#los precios en precios.csv son los precios de venta en el lugar de descarga del camión.

import csv
import sys
from fileparse import parse_csv


def leer_camion(nombre_archivo):
    '''
    Lee registros de un archivo de datos CSV con 3 columnas.
    La primer fila debe ser el encabezado. 
    '''
    with open(nombre_archivo, 'rt') as f:
        camion = []
        d = {}
        rows = csv.reader(f)
        headers = next(rows)
        
        for n_linea, row in enumerate(rows, start = 2):
            record = dict(zip(headers, row))
            try:
                d = {
                    'nombre' : record['nombre'],
                    'cajones' : int(record['cajones']),
                    'precio' : float(record['precio'])
                    }
                camion.append(d)
            except ValueError: 
                print(f'En el archivo {nombre_archivo}, linea {n_linea} sin datos : {row}')
                
    return camion
   

def leer_precios(nombre_archivo):
    '''
    Lee un archivo y devuelve el precio de un item en un diccionario 
    '''
    with open(nombre_archivo, 'rt') as f:
        precios = {}
        rows = csv.reader(f)
        for n_linea, row in enumerate(rows):    
            try:
                precios[row[0]] = float(row[1])
            except IndexError:
                print(f'En el archivo {nombre_archivo}, linea {n_linea} sin datos : {row}')
    return precios
    

def hacer_informe(lista_camion, precios):
    '''
    Devuelve una lista de tuplas de los valores necesarios para realizar el informe
    '''
    informe = []
    for n in lista_camion:
        articulo = n['nombre']
        precio_v = precios[articulo]
        cambio = precio_v - n['precio']
        info = (articulo, n['cajones'], precio_v, cambio )
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
    camion = parse_csv(nombre_archivo_camion, types = [str, int, float])
    precios = dict(parse_csv(nombre_archivo_precios, types = [str,float], has_headers=False))
    informe = hacer_informe(camion, precios)
    imprimir_informe(informe)



#El archivo argumento de la funcion leer_precios debe ser colocado como segundo argumento sino leera por defecto 'Data/precios.csv'
#El archivo argumento de la funcion leer_camion debe ser colocado como primer argumento sino leera por defecto 'Data/camion.csv'
        
if len(sys.argv) == 2:
    nombre_archivo_camion = sys.argv[1]
    nombre_archivo_precios = 'Data/precios.csv'
elif len(sys.argv) == 3:
    nombre_archivo_camion = sys.argv[1]
    nombre_archivo_precios = sys.argv[2]
else:
    nombre_archivo_camion = 'Data/camion.csv'
    nombre_archivo_precios = 'Data/precios.csv'
    
#informe_camion(nombre_archivo_camion, nombre_archivo_precios)