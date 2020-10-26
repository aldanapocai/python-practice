#Costo_camion.py
#Escribí un programa llamado costo_camion.py que abra el archivo, lea las líneas,
# y calcule el precio pagado por los cajones cargados en el camión.
import csv
import sys

def costo_camion(nombre_archivo):

    #Abrir el archivo camion.csv
    f = open(nombre_archivo,'rt')
    filas = csv.reader(f)
    costo_total = 0.0 

    #Salteo la primera linea
    headers = next(filas)
    #Lee cada linea restante
    for n_fila, fila in enumerate(filas, start = 1):
        record = dict(zip(headers, fila))
        try:
            n_cajones = int(record['cajones'])
            costo_por_cajon = float(record['precio'])
            costo_por_fruta = n_cajones*costo_por_cajon
            costo_total +=costo_por_fruta
        except ValueError:
            print(f'Los datos de la linea {n_fila} no son numericos. No se utilizaron para el calculo')
    
    return costo_total
    f.close()
    
if len(sys.argv) == 2:
    nombre_archivo = sys.argv[1]
else:
    nombre_archivo = 'Data/camion.csv'
  
costo = costo_camion(nombre_archivo)

print(f'Costo del camion {costo}')