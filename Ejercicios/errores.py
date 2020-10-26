# -*- coding: utf-8 -*-
"""
Created on Mon Aug 24 01:05:54 2020

@author: clase
"""
#%% 3.1

def tiene_a(expresion):
    res = False
    n = len(expresion)
    i = 0
    
    while i<n:
        if res == False: 
            if expresion[i] == 'a':
                res = True
            
            else:
                res = False
            i += 1
    return res

x = tiene_a('UNSAM 2020')
y = tiene_a('abracadabra')
z = tiene_a('La novela 1984 de George Orwell')