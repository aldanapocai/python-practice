# -*- coding: utf-8 -*-
"""
Created on Tue Sep 29 18:40:06 2020.

@author: Aldana_Pocai
"""
from matplotlib import pyplot as plt
import numpy as np

# Crea una figura nueva, de 8x6 pulgadas, con 80 puntos por pulgada
plt.figure(figsize=(8, 6), dpi=80)


# Crea un nuevo subplot, en una grilla de 1x1
plt.subplot(1,1,1)

X  = np.linspace(-np.pi, np.pi, 256)
C, S = np.cos(X), np.sin(X)

# Plotea el coseno con una línea azul contínua de ancho 1 (en pixeles)
plt.plot(X, C, color="blue", linewidth=1.0, linestyle="-")

# Plotea el seno con una línea verde contínua de ancho 1 (en pixeles
plt.plot(X, S, color="green", linewidth=1.0)

#Rango del eje x
plt.xlim(-4.0, 4.0)

#Marcas en el eje x
plt.xticks(np.linspace(-4, 4, 9))

#Rango del eje y 
plt.ylim(-1.0, 1.0)

#Ponemos marcas en el eje y
plt.yticks(np.linspace(-1, 1, 5))



#Mostrar resultado en pantalla
plt.show()





