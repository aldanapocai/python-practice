#Costo_camion.py
#Escribí un programa llamado costo_camion.py que abra el archivo, lea las líneas,
# y calcule el precio pagado por los cajones cargados en el camión.

def costo_camion(nombre_archivo):

    #Abrir el archivo camion.csv
    f = open(nombre_archivo,'rt')

    costo_total = 0.0 

    #Salteo la primera linea
    headers = next(f)

    #Lee cada linea restante
    for line in f:
        row = line.split(',') #Divide la string en una lista
        n_cajones = float(row[1])
        costo_por_cajon = float(row[2])
        costo_por_fruta = n_cajones*costo_por_cajon
        costo_total +=costo_por_fruta
    
    return costo_total
    f.close()