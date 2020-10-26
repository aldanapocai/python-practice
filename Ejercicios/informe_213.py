#informe.py 2.12 2.13 lista de diccionarios: representar cada cajón del camión con un diccionario en vez de una tupla.

import csv
import sys

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
    nombre_archivo = sys.argv[1]
else:
    nombre_archivo = 'Data/camion.csv'
    
camion = leer_camion(nombre_archivo)    
print(camion)