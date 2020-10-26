# -*- coding: utf-8 -*-
"""
Created on Thu Sep 10 15:02:25 2020

@author: Aldana_Pocai

"""
import csv

def parse_csv(f, select = None, types = None, has_headers = True, silence_errors = False):
    ''' 
    Parsea cualquier iterable en una lista de resgitros
    Se puede seleccionar sólo un subconjunto de las columnas, determinando el parámetro select, que debe ser una lista de nombres de las columnas a considerar.
    '''
    if select and has_headers== False:
        raise RuntimeError('Para seleccionar, necesito encabezados.')
    rows = csv.reader(f)    
    registros = []
    if has_headers == False:
        for row in rows:
            if not row: #Saltea filas sin registros
                continue
            if types:
                row = ([func(val) for func, val in zip(types, row)])
            registros.append(tuple(row))
    else:
        #Lee los encabezados
        headers = next(rows)
       
        # Si se indicó un selector de columnas,
        #    buscar los índices de las columnas especificadas. (index)
        # Y en ese caso achicar el conjunto de encabezados para diccionarios
        if select:
            indices = [headers.index(nombre_columna) for nombre_columna in select]
            headers = select
        else:
            indices = []
               
        for i, row in enumerate(rows):
            if not row: #Saltea filas sin registros
                continue
            #Filtrar la fila si se especifican select
            if indices:
                row = [row[index] for index in indices]
                    
            #Convertir a los tipos indicados 
            try:
                if types:
                    row = [func(val) for func, val in zip(types, row)]
            except Exception as e:
                if not silence_errors:
                    print(f'Row:{i+1} : No pude convertir {row}')
                    print(f'Row:{i+1} : Motivo: {e}')
                    continue
                else:
                    continue
            #Arma el diccionario  
            registro = dict(zip(headers, row))
            registros.append(registro)
    return registros


#%% Version vieja
    
  # def parse_csv(nombre_archivo, select = None, types = None, has_headers = True, silence_errors = False):
  #   ''' 
  #   Parsea un archivo CSV en una lista de resgitros
  #   Se puede seleccionar sólo un subconjunto de las columnas, determinando el parámetro select, que debe ser una lista de nombres de las columnas a considerar.
  #   '''
  #   if select and has_headers== False:
  #       raise RuntimeError('Para seleccionar, necesito encabezados.')
        
  #   with open(nombre_archivo) as f:
  #       rows = csv.reader(f)
  #       registros = []
  #       if has_headers == False:
  #          for row in rows:
  #               if not row: #Saltea filas sin registros
  #                   continue
  #               if types:
  #                   row = ([func(val) for func, val in zip(types, row)])
  #               registros.append(tuple(row))
  #       else:
  #           #Lee los encabezados
  #           headers = next(rows)
            
  #           # Si se indicó un selector de columnas,
  #           #    buscar los índices de las columnas especificadas. (index)
  #           # Y en ese caso achicar el conjunto de encabezados para diccionarios
  #           if select:
  #               indices = [headers.index(nombre_columna) for nombre_columna in select]
  #               headers = select
  #           else:
  #               indices = []
               
  #           for i, row in enumerate(rows):
  #               if not row: #Saltea filas sin registros
  #                   continue
  #               #Filtrar la fila si se especifican select
  #               if indices:
  #                   row = [row[index] for index in indices]
                    
  #               #Convertir a los tipos indicados 
  #               try:
  #                   if types:
  #                       row = [func(val) for func, val in zip(types, row)]
  #               except Exception as e:
  #                   if not silence_errors:
  #                       print(f'Row:{i+1} : No pude convertir {row}')
  #                       print(f'Row:{i+1} : Motivo: {e}')
  #                       continue
  #                   else:
  #                       continue
  #               #Arma el diccionario  
  #               registro = dict(zip(headers, row))
  #               registros.append(registro)
  #   return registros  