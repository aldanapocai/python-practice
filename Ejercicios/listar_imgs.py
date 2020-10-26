# -*- coding: utf-8 -*-
"""
Created on Wed Sep 30 10:35:41 2020.

listar_imgs.py

@author: Aldana
"""
import os


def listar_imgs(directorio):
    """ 
    Imprime todos los archivos .png que se encuentren en algún
    subdirectorio del directorio dado.
    """
    
    for root, dirs, files in os.walk('directorio'):
        for name in files:
            if name.endswith(".png"):
                print(os.path.join(root, name))
    

def main(argv):
    return listar_imgs(argv[1])


if __name__ == '__main__':
    import sys
    main(sys.argv)
    
