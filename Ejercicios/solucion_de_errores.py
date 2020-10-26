# -*- coding: utf-8 -*-
"""
Created on Mon Aug 24 01:04:30 2020

@author: Aldana
"""
#solucion_de_errores.py
#Ejercicios de errores en el código
#%%
#Ejercicio 3.1. Función tiene_a()
#El error esta en que la funcion lo que verdaderamente devuelve es si la ultima letra es a.
        # Esto ocurre ya que aunque se encuentre una a y la funcion en esa letra devuelva true, sigue analizando
        #las siguientes letras y cambia el valor de retorno a False si no son a. 
        #Tampoco identifica las 'a' mayusculas. 

#    Lo corregí agregando la a mayuscula a la condicion del if, y agregando un 'break' cuando las condiciones
#    son verdaderas, asi no sigue analizando el resto de las letras. 
#


#    A continuación va el código corregido
def tiene_a(expresion):
    n = len(expresion)
    i = 0
    while i<n :
        if expresion[i] == 'a' or expresion[i] == 'A': #agrego cond
            return True
            break #agrego 
        else:
            return False
        i += 1

 
a = tiene_a('UNSAM 2020')
b = tiene_a('abracadabra')
c = tiene_a('La novela 1984 de George Orwell')

#%%
#Ejercicio 3.2. Función tiene_a(), nuevamente
#Comentario: Falto poner ':' en ciertas lineas, para comparar es '==' y no '='. False estaba mal escrito.
#               Es necesario agregar la condicion para 'a' mayuscula.

#Codigo corregido

def tiene_a(expresion):
    n = len(expresion)
    i = 0
    while i<n:
        if expresion[i] == 'a' or expresion[i] == 'A': #agrego condicion
            return True
        i += 1
    return False

a = tiene_a('UNSAM 2020')
b = tiene_a('La novela 1984 de George Orwell')



#%%
#Ejercicio 3.3. Función tiene_uno()
#Comentario: En el caso de que el usuario ingrese algo distinto a un string no funciona.
#es necesrio convertir la entrada a un string con str()

#Codigo corregido

def tiene_uno(expresion):
    exp = str(expresion) #linea agregada
    n = len(exp) #cambio de variable
    i = 0
    tiene = False
    while (i<n) and not tiene:
        if exp[i] == '1': #cambio de variable
            tiene = True
        i += 1
    return tiene


a = tiene_uno('UNSAM 2020')
b = tiene_uno('La novela 1984 de George Orwell')
c = tiene_uno(1984)


#%%Ejercicio 3.4: Alcances
#La funcion no devolvia nada. 
#Codigo corregido:
    
def suma(a,b):
    c = a + b
    return c  #linea agregada
a = 10
b = 15
c = suma(a,b)
print(f"La suma da {a} + {b} = {c}")

#%%Ejercicio 3.5: Pisando memoria

#No funciona ya que en el ciclo for se van pisando los valores del diccionario registro, ya que siempre se referencia a la misma
#Para solucionarlo realizo una copia profunda de cada registro 
#Codigo corregido

import csv
from pprint import pprint
import copy #importo esta libreria

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
            a = copy.deepcopy(registro) #Agrego esta linea
            camion.append(a) #Modifico 'registro' por 'a'
    return camion

camion = leer_camion("Data/camion.csv")
pprint(camion)


