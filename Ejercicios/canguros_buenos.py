# -*- coding: utf-8 -*-
"""
Created on Wed Oct  7 13:56:22 2020

@author: Aldana
"""

class Canguro():
    def __init__(self, nombre, contenido = []):
        self.nombre = nombre
        self.contenido_marsupio = contenido
    
    def meter_en_marsupio(self, elemento):
        self.contenido_marsupio.append(elemento)
    

    
    def __str__(self):
        """devuelve una representación como cadena de este Canguro.
        """
        t = [ self.nombre + ' tiene en su marsupio:' ]
        for obj in self.contenido_marsupio:
            s = '    ' + object.__str__(obj)
            t.append(s)
        return '\n'.join(t)
    


madre_canguro = Canguro('Madre')

cangurito = Canguro("Hijo")

madre_canguro.meter_en_marsupio("Mate")

madre_canguro.meter_en_marsupio({'key_1' : 'car', 'key_2' : 'house'})

madre_canguro.meter_en_marsupio("chocolate")

madre_canguro.meter_en_marsupio(cangurito)

print(cangurito)
