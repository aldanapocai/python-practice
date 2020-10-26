#!/usr/bin/env python3
#costo_camion.py
"""
En el interactivo ingresar:
    
import costo_camion

with open('Data/camion.csv') as f1:
    costo_camion.main(['',f1])
    
@author: Aldana_Pocai


"""



from fileparse import parse_csv

def costo_camion(nombre_archivo):
    camion = parse_csv(nombre_archivo, types = [str, int, float])
    costo_total = 0.0
    try:
        for i, linea in enumerate(camion):
            costo_fruta = linea['cajones']*linea['precio']
            costo_total += costo_fruta
    except ValueError:
                    print(f'Los datos de la linea {i} no son numericos. No se utilizaron para el calculo')
    return costo_total

def main(argv):
    if len(argv) != 2:
        raise SystemExit(f'Uso adecuado: {argv[0]} ' 'archivo_camion')
    costo = costo_camion(argv[1])
    print('Costo total:', costo)


if __name__ == '__main__':
    import sys
    main(sys.argv)
