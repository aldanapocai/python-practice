# -*- coding: utf-8 -*-
"""
Created on Mon Oct  5 16:32:52 2020

@author: Aldana
"""

class Punto():
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f'({self.x}, {self.y})'

    # Used with `repr()`
    def __repr__(self):
        return f'Punto({self.x}, {self.y})'


class Rectangulo():
    def __init__(self,punto_a, punto_b):
        self.punto_a = punto_a
        self.punto_b = punto_b
    
    def base(self):
         x_a = getattr(self.punto_a, 'x', None)
         x_b = getattr(self.punto_b, 'x', None)
         if x_a < x_b:
             return x_b - x_a
         else:
             return x_b - x_a
             
    def altura(self):
        y_a = getattr(self.punto_a, 'y', None)
        y_b = getattr(self.punto_b, 'y', None)
        if y_a < y_b:
            return y_b - y_a
        else:
            return y_a - y_b


