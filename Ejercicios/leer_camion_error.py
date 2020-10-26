# -*- coding: utf-8 -*-
"""
Created on Mon Aug 24 20:06:20 2020

@author: Aldana
"""

import csv
from pprint import pprint
import copy

def leer_camion(nombre_archivo):
    camion=[]
    registro={}
    with open(nombre_archivo,"rt") as f:
        filas = csv.reader(f)
        encabezado = next(filas)
        for fila in filas:
            registro[encabezado[0]] = fila[0]
            registro[encabezado[1]] = int(fila[1])
            registro[encabezado[2]] = float(fila[2])
            a = copy.deepcopy(registro)
            camion.append(a)
    return camion

camion = leer_camion("Data/camion.csv")
pprint(camion)