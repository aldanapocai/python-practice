#Costo_camion.py
#Escribí un programa llamado costo_camion.py que abra el archivo, lea las líneas,
# y calcule el precio pagado por los cajones cargados en el camión. MODULO CSV

import csv
#Abrir el archivo camion.csv
f = open('camion.csv','rt')

rows = csv.reader(f)

costo_total = 0.0 

#Salteo la primera linea
headers = next(rows)
print(headers)

#Lee cada linea restante
for row in rows:
    print(row) 
    n_cajones = float( row[1])
    costo_por_cajon = float(row[2])
    costo_por_fruta = n_cajones*costo_por_cajon
    costo_total +=costo_por_fruta

print()    
print('El Costo total del camion es:',costo_total)
f.close()