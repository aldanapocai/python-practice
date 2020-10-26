# -*- coding: utf-8 -*-
# 11.2
"""
Created on Sun Oct 25 14:13:01 2020.

@author: AldanaPocai
"""


""" Ordenar por burbujeo una lista de tamaño N insume tiempo del orden de N^2, 
    en cuanto a recorridos por realizar. 
    Las comparaciones a realizar pueden ser 0 si la lista esta ordenada o en el peor caso N. 
"""

def ord_burbujeo(lista):
        """
        Ordena una lista de elementos según el método de inserción.
        
        Pre: los elementos de la lista deben ser comparables.
        Post: la lista está ordenada.
        """
        
        for m in range(1,len(lista)): #Se realizan len(lista) recorridos de la lista.
            for i in range(len(lista)-m):
                if lista[i] > lista[i+1]: #La cant de intercambios sera <= len(lista), siendo = en el peor caso.  
                    lista[i], lista[i+1] = lista[i+1], lista[i]
                    


#%%Tests

lista_1 = [1, 2, -3, 8, 1, 5]
lista_2 = [1, 2, 3, 4, 5]
lista_3 = [0, 9, 3, 8, 5, 3, 2, 4]
lista_4 = [10, 8, 6, 2, -2, -5]
lista_5 = [2, 5, 1, 0]

listas = [lista_1,lista_2, lista_3, lista_4, lista_5]
for i, lista in enumerate(listas):
    print(f'Lista {i} original: {lista}')
    ord_burbujeo(lista)
    print(f'Lista {i} ordenada: {lista}')
    