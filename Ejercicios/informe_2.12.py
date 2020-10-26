#informe.py 2.12

import csv
import sys

def leer_camion(nombre_archivo):
    with open(nombre_archivo, 'rt') as f:
        camion = []
        rows = csv.reader(f)
        headers = next(rows)
        
        for row in rows:
            lote = (row[0], int(row[1]), float(row[2]))
            camion.append(lote)
    return camion

if len(sys.argv) == 2:
    nombre_archivo = sys.argv[1]
else:
    nombre_archivo = 'Data/camion.csv'
    
camion = leer_camion(nombre_archivo)    
print(camion)