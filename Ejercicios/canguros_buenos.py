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
    


# madre_canguro = Canguro('Madre')

# cangurito = Canguro("Hijo")

# madre_canguro.meter_en_marsupio("Mate")

# madre_canguro.meter_en_marsupio({'key_1' : 'car', 'key_2' : 'house'})

# madre_canguro.meter_en_marsupio("chocolate")

# madre_canguro.meter_en_marsupio(cangurito)

# print(cangurito)

#%%canguro_malo.py

"""Este código continene un 
bug importante y dificil de ver
"""

class Canguro:
    """Un Canguro es un marsupial."""
    
    def __init__(self, nombre, contenido=None):
        """Inicializar los contenidos del marsupio.

        nombre: string
        contenido: contenido inicial del marsupio, lista.
        """
        self.nombre = nombre
        if contenido == None:
            self.contenido_marsupio = []
        else:
            self.contenido_marsupio = contenido

    def __str__(self):
        """devuelve una representación como cadena de este Canguro.
        """
        t = [ self.nombre + ' tiene en su marsupio:' ]
        for obj in self.contenido_marsupio:
            s = '    ' + object.__str__(obj)
            t.append(s)
        return '\n'.join(t)

    def meter_en_marsupio(self, item):
        """Agrega un nuevo item al marsupio.

        item: objecto a ser agregado
        """
        self.contenido_marsupio.append(item)

#%%
madre_canguro = Canguro('Madre')
cangurito = Canguro('gurito')
madre_canguro.meter_en_marsupio('billetera')
madre_canguro.meter_en_marsupio('llaves del auto')
madre_canguro.meter_en_marsupio(cangurito)

print(madre_canguro)

# Al ejecutar este código todo parece funcionar correctamente.
# Para ver el problema, imprimí el contenido de cangurito.

print(cangurito)

#El error es que agrega automaticamente los items del marsupio de la madre
# canguro al marsupio del hijo, y se incluye a si mismo. 

#Se resuelve inicializando la variable contenido como None, y creando la lista
#vacia una vez dentro de la funcion. 
