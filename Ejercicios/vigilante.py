#vigilante.py
# -*- coding: utf-8 -*-
"""
Created on Mon Nov  2 23:51:58 2020

@author: AldanaPocai
"""

import os
import time

def vigilar(filename):
    """Obtiene los datos que se generan del archivo"""
    f = open(filename)
    f.seek(0, os.SEEK_END)
    while True:
        line = f.readline()
        if line == "":
            time.sleep(0.5)
            continue
        else:
            yield line

if __name__ == '__main__':
    for line in vigilar('Data/mercadolog.csv'):
        fields = line.split(',')
        nombre = fields[0].strip('"')
        precio = float(fields[1])
        volumen = int(fields[2])
        if volumen > 1000:
            print(f'{nombre:>10s} {precio:>10.2f} {volumen:>10d}')
        