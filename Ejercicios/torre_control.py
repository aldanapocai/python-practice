# -*- coding: utf-8 -*-
"""
Created on Tue Oct 13 15:08:36 2020

@author: Aldana
"""

class Cola:
    '''Representa a una cola, con operaciones de encolar y desencolar.
    El primero en ser encolado es tambien el primero en ser desencolado.
    '''

    def __init__(self):
        '''Crea una cola vacia.'''
        self.items = []

    def encolar(self, x):
        '''Encola el elemento x.'''
        self.items.append(x)

    def desencolar(self):
        '''Elimina el primer elemento de la cola 
        y devuelve su valor. 
        Si la cola esta vacia, levanta ValueError.'''
        if self.esta_vacia():
            raise ValueError('La cola esta vacia')
        return self.items.pop(0)

    def esta_vacia(self):
        '''Devuelve 
        True si la cola esta vacia, 
        False si no.'''
        return len(self.items) == 0
    
    
class TorreDeControl(Cola):
    """Modela el trabajo de una torre de control de un aeropuerto 
    con una pista de aterrizaje:
    Los aviones que están esperando para aterrizar tienen prioridad sobre
    los que están esperando para despegar
    """
    def nuevo_arribo(self, arribo):
        super().encolar(arribo)
    

    def nueva_partida(partida):
        super().desencolar()        
    
        
    