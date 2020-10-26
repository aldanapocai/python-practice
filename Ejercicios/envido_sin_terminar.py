# -*- coding: utf-8 -*-
"""
Created on Wed Sep  2 09:37:12 2020

@author: Aldana
"""
import random


valores = [1, 2, 3, 4, 5, 6, 7, 10, 11, 12]
palos = ['oro', 'copa', 'espada', 'basto']
naipes = [(valor, palo) for valor in valores for palo in palos]

mano = random.sample(naipes, k =3)

#Mezclar
random.shuffle(naipes)
print(naipes)