# -*- coding: utf-8 -*-
"""
Created on Sun Nov  1 23:32:16 2020

@author: Aldana
"""

from matplotlib import pyplot as plt
import numpy as np

def randomwalk(largo):
    """Devuelve la sumatoria de pasos de una caminata aleatoria"""
    pasos = np.random.randint(-1, 2, largo)
    return pasos.cumsum()

N = 100000

colores = ['b','g', 'r', 'c','m','y'	,'k','#E75E41', '#DABBFE', '#fffa8c', '#E9CBD0',
          '#FFE2EA']
#En esta lista se guardaran las trayectorias generadas
randomwalks = []

plt.clf()
fig = plt.figure()
plt.xlabel('tiempo')
plt.ylabel('Distancia al origen')
plt.title("12 Caminatas al azar")
plt.xticks([]), plt.yticks([])
#Graficá 12 trayectorias en la misma figura, con diferentes colores.
plt.subplot(2, 1, 1)
for i in range(12):
    walk = randomwalk(N)
    plt.plot(walk, color = colores[i])
    randomwalks.append(walk)
plt.show()

#Averiguar cual es la trayectoria que mas se desvia
randomwalks_abs_max = [max([abs(pasos) for pasos in walk]) for walk in randomwalks]
trayec_desviada_index = randomwalks_abs_max.index(max(randomwalks_abs_max))

#Grafico de la trayectoria que MAS se desvia
plt.subplot(2,2,1)
plt.title("La caminata que mas se aleja")
plt.plot(randomwalks[trayec_desviada_index])
plt.xticks([]), plt.yticks([])

#Averiguar cual es la trayectoria que MENOS se desvia
randomwalks_abs_sum = [sum([abs(pasos) for pasos in walk]) for walk in randomwalks]
tray_estable = randomwalks_abs_sum.index(min(randomwalks_abs_sum))

#Grafico de la trayectoria que MENOS se desvia
plt.subplot(2,2,2)
plt.title("La caminata que menos se aleja")
plt.plot(randomwalks[tray_estable], color = colores[tray_estable])
plt.xticks([]), plt.yticks([])

