# -*- coding: utf-8 -*-
"""
Created on Wed Sep  2 09:49:00 2020

@author: Aldana
"""

import random


def generar_punto():
    x = random.random()
    y = random.random()
    return x,y


N=1000
M=0

for i in range(N):
    x,y = generar_punto()
    if x**2 + y**2 < 1 :
       M +=1 


pi = 4 * M/N

print(f'Pi estimado es: {pi}')