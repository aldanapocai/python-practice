#camion_commandline.py

import sys 
from informe_funciones import leer_camion 

if len(sys.argv) == 2:
    nombre_archivo = sys.argv[1]
else:
    nombre_archivo =  'Data/camion.csv'

def costo_camion(nombre_archivo):
    camion = leer_camion(nombre_archivo)
    costo_total = 0.0
    try:
        for i, linea in enumerate(camion):
            costo_fruta = linea['cajones']*linea['precio']
            costo_total += costo_fruta
    except ValueError:
                    print(f'Los datos de la linea {i} no son numericos. No se utilizaron para el calculo')
    return costo_total

# def costo_camion(nombre_archivo):

#     with open(nombre_archivo,'rt') as f:
#         rows = csv.reader(f)
        
#         costo_total = 0.0 
#         n = 0 #Contador de linea

#         #Salteo la primera linea
#         headers = next(rows)
#         n +=1
#         #Lee cada linea restante
#         for row in rows:
#             n += 1
#             try:
#                 n_cajones = int(row[1])
#                 costo_por_cajon = float(row[2])
#                 costo_por_fruta = n_cajones*costo_por_cajon
#                 costo_total +=costo_por_fruta
#             except ValueError:
#                 print(f'Los datos de la linea {n} no son numericos. No se utilizaron para el calculo')
#     return costo_total 
    
    

    
    
costo = costo_camion(nombre_archivo)
print('Costo total:', costo)