#informe.py 
#los precios en camion.csv son los precios pagados al productor de frutas mientras que
# los precios en precios.csv son los precios de venta en el lugar de descarga del camión.


import csv
import sys
from pprint import pprint

def leer_camion(nombre_archivo):
    with open(nombre_archivo, 'rt') as f:
        camion = []
        d = {}
        rows = csv.reader(f)
        headers = next(rows)
        
        for row in rows:
            d = {
                'nombre' : row[0],
                'cajones' : int(row[1]),
                'precio' : float(row[2])
                }
            camion.append(d)
    return camion

if len(sys.argv) == 2:
    nombre_archivo_prod = sys.argv[1]
else:
    nombre_archivo_prod = 'Data/camion.csv'
    
camion = leer_camion(nombre_archivo_prod)    

def leer_precios(nombre_archivo):
    with open(nombre_archivo, 'rt') as f:
        precios = {}
        rows = csv.reader(f)
        n = 0
        for row in rows:
            n += 1
            try:
                precios[row[0]] = row[1]
            except IndexError:
                print(f'Linea {n} sin datos')
    return precios
    
    
if len(sys.argv) == 3:
    nombre_archivo_venta = sys.argv[1]
else:
    nombre_archivo_venta = 'Data/precios.csv'

precios = leer_precios(nombre_archivo_venta)