# -*- coding: utf-8 -*-
"""
Created on Tue Oct 13 15:08:36 2020

@author: AldanaPocai
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
    
    
class TorreDeControl():
    """Modela el trabajo de una torre de control de un aeropuerto 
    con una pista de aterrizaje:
    Los aviones que están esperando para aterrizar tienen prioridad sobre
    los que están esperando para despegar
    """
    
    def __init__(self):
        """ Crea una cola de arribos y otra de partidas ambas vacias"""
        self.arribos = []
        self.partidas = []
        
        
    def nuevo_arribo(self, arribo):
        self.arribos.append(arribo)
    

    def nueva_partida(self, partida):
        self.partidas.append(partida)
        
    
    def esta_vacia(self):
        '''Devuelve 
        True si la cola esta vacia, 
        False si no.'''
        if len(self.arribos) == 0  and len(self.partidas) == 0:
            return True

    
    def ver_estado(self):
        """ Muestra los vuelos en cola para despegar y aterrizar."""
        if self.esta_vacia():
            print("No hay vuelos en espera")
        else:
            if len(self.arribos) != 0:
                print(f"Vuelos esperando para aterrizar: {self.arribos[0]}", end = "" )
                for i in range(len(self.arribos)-1):
                    print(f', {self.arribos[i+1]}', end = " ")
                print()
            if len(self.partidas) != 0:
                print(f"Vuelos esperando para despegar: {self.partidas[0]}", end = "" )
                for i in range(len(self.partidas)-1):
                    print(f', {self.partidas[i+1]}', end = " ")   
        
    def asignar_pista(self):
        if self.esta_vacia():
            print("No hay vuelos en espera")
        else:
            if len(self.arribos) != 0:
                print(f'El vuelo {self.arribos[0]} aterrizó con éxito.')
                self.arribos.pop(0)
            elif len(self.partidas) != 0:
                print(f'El vuelo {self.partidas[0]} despegó con éxito.')
                self.partidas.pop(0)
