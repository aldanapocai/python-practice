#arboles.py

import csv
import sys
from collections import Counter
from pprint import pprint

#Archivos y cond a leer
if len(sys.argv) == 3:
    archivo_data = sys.argv[1]
    parque = sys.argv[2]
elif len(sys.argv) == 2:
    archivo_data = sys.argv[1]
    parque = 'GENERAL PAZ'
else:
    archivo_data = 'Data/data_verde.csv'
    parque = 'GENERAL PAZ'



#2.22 Lectura de los arboles de un parque, devuelve los registros de determinado parque

def leer_parque(nombre_archivo, parque):
    with open(nombre_archivo, 'rt', encoding='utf8') as f:
        lista           = [] #lista de diccionarios con todo el archivo
        lista_parque    = [] #lista a devolver con info del parque pedido
        d               = {} #diccionario
        arboles         = csv.reader(f)
        header          = next(arboles) #Encabezado
        
        for n_linea, arbol in enumerate(arboles, start = 2):  #la itiracion comienza en 2 ya que los datos comienzan en esa linea
            a = dict(zip(header, arbol)) #registro del arbol que asocia en forma key:value(dict) al encabezado con los valores
            try:
                d = {
                    'long'          :   float(a['long']),
                    'lat'           :   float(a['lat']),
                    'id_arbol'      :   int(a['id_arbol']),
                    'altura_tot'    :   float(a['altura_tot']),
                    'diametro'      :   int(a['diametro']),
                    'inclinacio'    :   float(a['inclinacio']),
                    'id_especie'    :   int(a['id_especie']),
                    'nombre_com'    :   a['nombre_com'],
                    'nombre_cie'    :   a['nombre_cie'],
                    'tipo_folla'    :   a['tipo_folla'],
                    'espacio_ve'    :   a['espacio_ve'],
                    'ubicacion'     :   a['ubicacion'],
                    'nombre_fam'    :   a['nombre_fam'],
                    'nombre_gen'    :   a['nombre_gen'],
                    'origen'        :   a['origen'],
                    'coord_x'       :   float(a['coord_x']),
                    'coord_y'       :   float(a['coord_y'])
                    }
                 
                lista.append(d) #agrego a la lista, el diccionario del arbol recien creado en d
            except ValueError:
                print('Error')
        for i in lista:
            if i['espacio_ve'] == parque:
                lista_parque.append(i)

    return lista_parque
    #return lista #comentar la linea de arriba y descomentar esta para leer todo el archivo
    
lista_parque = leer_parque(archivo_data, parque)

#Ejercicio 2.23: Determinar las especies en un parque
def especies(lista_arboles):
    e = []
    for i in lista_arboles:
        e.append(i['nombre_com'])
    if len(e)>0:
        lista_especies = set(e) #se eliminan duplicados 
        list_species = list(lista_especies) #asi se devuelve una list y no un set
        return list_species
    
#lista_especies = especies(lista_parque)




#Ejercicio 2.24: Contar ejemplares por especie
def contar_ejemplares(lista_arboles):
    cnt = Counter()
    aux = []
    for arbol in lista_arboles:
        aux.append(arbol['nombre_com'])
    for especie in aux: 
        cnt[especie] +=1
    return cnt
    
#contador_especies = contar_ejemplares(lista_parque)



#Ejercicio 2.25: Alturas de una especie en una lista
def obtener_alturas(lista_arboles, especie):
    alturas = []
    for arbol in lista_arboles:
        if arbol['nombre_com'] == especie:
            alturas.append(arbol['altura_tot'])
    return alturas
    
 

 
#%%

#Ejercicio 2.26: Inclinación promedio por especie de una lista

def obtener_inclinaciones(lista_arboles, especie):
    inclinaciones = [] #lista a devolver
    for arbol in lista_arboles:
        if arbol['nombre_com'] == especie:
            inclinaciones.append(arbol['inclinacio'])
        
    return inclinaciones

#Ejercicio 2.27: Especie con el ejemplar más inclinado

def especimen_mas_inclinado(lista_arboles):
    esp_incl_max = {} #diccionario con las especies y su inclinacion maxima
    species = especies(lista_arboles) #convierte set a list para poder enumerarlo
    for especie in species:
        max_incli_especie = max(obtener_inclinaciones(lista_arboles,especie))
        esp_incl_max[especie] = max_incli_especie
    lista_esp_max = list(zip(esp_incl_max.values(), esp_incl_max.keys()))
    mas_inclinado = max(lista_esp_max)
    
    return mas_inclinado

mas_inclinado = especimen_mas_inclinado(lista_parque)

#2.28: Especie con más inclinada en promedio

def especie_promedio_mas_inclinada(lista_arboles):
    esp_incl_max = {} #diccionario con las especies y su inclinacion maxima
    species = especies(lista_arboles) #convierte set a list para poder enumerarlo
    for especie in species:
        inclinaciones = obtener_inclinaciones(lista_arboles,especie)
        prom_inclinacion = sum(inclinaciones)/len(inclinaciones)
        esp_incl_max[especie] = prom_inclinacion
    lista_esp_prom_max = list(zip(esp_incl_max.values(), esp_incl_max.keys()))
    mas_inclinado_prom = max(lista_esp_prom_max)
    
    return mas_inclinado_prom

#%%    
#Ejercicio 2.24 plus: 5 mas frecuentes + calcular la altura promedio 
#y altura máxima de los 'Jacarandá' en los tres parques mencionados.
#plus 2.27 ejemplar mas inclinados
for n in ['GENERAL PAZ', 'ANDES, LOS', 'CENTENARIO']:
    lista_park = leer_parque(archivo_data, n) 
    contador_especies = contar_ejemplares(lista_park)
    especies_comunes = contador_especies.most_common(5)
    mas_inclinado_park = especimen_mas_inclinado(lista_park)
    inclinacion, especimen = mas_inclinado_park
    incl_prom, espec_prom = especie_promedio_mas_inclinada(lista_park)
    print(n)
    pprint(especies_comunes)
    print(f'El {especimen} del parque {n} es el mas inclinado: {inclinacion},')
    print(f' mientras que el mas inclinado en promedio es {espec_prom}: {incl_prom} ')
    print()
    alturas = obtener_alturas(lista_park,'Jacarandá')
    m = max(alturas)
    avg = sum(alturas)/len(alturas)
    print(f'En el parque {n} la altura promedio del Jacarandá es {avg:0.2f} y la altura maxima es {m}')
    
#%%
#Preguntas extras: 
#¿Qué habría que cambiar para obtener la especie con un ejemplar más inclinado de toda la ciudad y no solo de un parque? 


#Que la func leer_parque devuelva todos los registros( comentar 61, descomentar 62). Usar esa lista para las funciones siguientes

#¿Podrías dar la latitud y longitud de ese ejemplar? ¿Y dónde se encuentra (lat,lon) el ejemplar más alto? ¿De qué especie es?   
  
#Se podria usando el id

