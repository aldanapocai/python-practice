# leer_precios.py

import csv
import sys
from pprint import pprint

def leer_precios(nombre_archivo):
    with open(nombre_archivo, 'rt') as f:
        precios = {}
        rows = csv.reader(f)
        n = 0
        for row in rows:
            n += 1
            try:
                precios[row[0]] = float(row[1])
            except IndexError:
                print(f'Linea {n} sin datos')
    return precios

if len(sys.argv) == 2:
    nombre_archivo = sys.argv[1]
else:
    nombre_archivo = 'Data/precios.csv'

precios = leer_precios(nombre_archivo)
pprint(precios)