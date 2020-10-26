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
        
        for n_linea,row in enumerate(rows, start = 2):
            try:
                d = {
                    'nombre' : row[0],
                    'cajones' : int(row[1]),
                    'precio' : float(row[2])
                    }
                camion.append(d)
            except ValueError: 
                print(f'En el archivo {nombre_archivo}, linea {n_linea} sin datos : {row}')
                
    return camion
   

def leer_precios(nombre_archivo):
    with open(nombre_archivo, 'rt') as f:
        precios = {}
        rows = csv.reader(f)
        for n_linea, row in enumerate(rows):      
            try:
                precios[row[0]] = float(row[1])
            except IndexError:
                print(f'En el archivo {nombre_archivo}, linea {n_linea} sin datos : {row}')
    return precios
    
#El archivo que la funcion leer_precios debe leer debe ser colocado como segundo argumento sino leera por defecto 'Data/precios.csv'
#El archivo que la funcion leer_camion debe leer debe ser colocado como primer argumento sino leera por defecto 'Data/camion.csv'
    
if len(sys.argv) == 2:
    nombre_archivo_prod = sys.argv[1]
    nombre_archivo_venta = 'Data/precios.csv'
elif len(sys.argv) == 3:
    nombre_archivo_prod = sys.argv[1]
    nombre_archivo_venta = sys.argv[2]
else:
    nombre_archivo_prod = 'Data/camion.csv'
    nombre_archivo_venta = 'Data/precios.csv'
    
camion = leer_camion(nombre_archivo_prod) 
precios = leer_precios(nombre_archivo_venta)



#Balance a imprimir

#Costo del camion
costo_camion = 0.0
for s in camion:
    costo_camion += s['cajones'] * s['precio']
print(f'Costo del camion: {costo_camion}.')


#Recaudado con la venta
venta = 0.0
for s in camion:
    venta_item = s['cajones'] * precios[s['nombre']]
    venta += venta_item
print(f'Recaudado en la venta: {venta}.')


#Balance
balance = 0.0
balance = venta - costo_camion
print(f'El balance es: {balance}.')

if balance > 0:
    print('Hubo ganancia!')
else:
    print('Hubo perdida :(')



