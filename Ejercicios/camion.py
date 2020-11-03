# -*- coding: utf-8 -*-
"""
Created on Mon Nov  2 22:53:48 2020

@author: AldanaPocai
"""
#camion.py

class Camion:
    
    def __init__(self, lotes):
        self.lotes = lotes
        
    def __iter__(self):
        return self.lotes.__iter__()
        
    def precio_total(self):
        return sum([l.costo() for l in self.lotes])
        
    def contar_cajones(self):
        from collections import Counter
        cantidad_total = Counter()
        for l in self.lotes:
            cantidad_total[l.nombre] += l.cajones
        return cantidad_total
        
    

    
    