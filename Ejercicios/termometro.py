# -*- coding: utf-8 -*-
"""
Created on Wed Sep  2 10:28:42 2020

@author: Aldana
"""

import random
import numpy as np

n=999
temp_real = 37.5
mediciones = [] #Lista con todas las mediciones
for i in range(n):
    error_medicion =  random.normalvariate(0,0.2)
    temp_medida = temp_real + error_medicion
    mediciones.append(temp_medida)
    print(f'Temperatura medida: {temp_medida:.2f}')
    
temp_max = max(mediciones)
temp_min = min(mediciones)
promedio = sum(mediciones)/n
mediciones.sort()
mediana = mediciones[int(n/2)+1]


print()
print(f"Temperatura Maxima: {temp_max:.2f}")
print(f"Temperatura Minima: {temp_min:.2f}")
print(f"Temperatura promedio: {promedio:.2f}")
print(f"Temperatura mediana: {mediana:.2f}")


#Guardar archivo npy
np.save('Data/Temperaturas', mediciones)
