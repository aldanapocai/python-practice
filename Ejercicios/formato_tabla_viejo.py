# -*- coding: utf-8 -*-
"""
Created on Sun Oct  4 21:18:33 2020

@author: Aldana
"""

class FormatoTabla:
    def encabezado(self, headers):
        """ Crea el encabezado de la tabla."""
        raise NotImplementedError()
        
    def fila(self, rowdata):
        """Crea una unica fila de datos de la tabla"""
        
        raise NotImplementedError()
        
class FormatoTablaTXT(FormatoTabla):
    """Genera una tabla en formato TXT ."""
    
    def encabezado(self, headers):
        for h in headers:
            print(f'{h:>10s}', end = " ")
        print()
        print(('-'*10 + ' ')*len(headers))

    def fila(self, data_fila):
        for d in data_fila:
            print(f'{d:>10s}', end = " ")
        print()    
        
class FormatoTablaCSV(FormatoTabla):
    """Genera una tabla formato CSV"""
    
    def encabezado(self, headers):
        print(','.join(headers))
    
    def fila(self, rowdata):
        print(','.join(rowdata))
        
class FormatoTablaHTML(FormatoTabla):
    """Genera una tabla formato HTML"""
    
    def encabezado(self, headers):
        print('<tr>', end = '')
        for h in headers:
            print(f'<th>{h}</th>', end = '')
        print('</tr>', end='')
        print()
        
    def fila(self, rowdata):
        print('<tr>', end = '')
        for d in rowdata:
            print(f'<td{d}</td>', end = '')
        print('</tr>', end='')       
        print()
        
def crear_formateador(fmt):
    """Llama a la clase que da formato segun lo indicado por el usuarie."""
    if fmt == 'txt':
        return FormatoTablaTXT()
    elif fmt == 'csv':
        return FormatoTablaCSV()
    elif fmt == 'html':
        return FormatoTablaHTML()
    else:
        raise RuntimeError(f'Unknown format {fmt}')
        
        
def imprimir_tabla(lista, col_select, formato):
    """ Imprime una tabla mostrando, de una lista de objetos de tipo 
    arbitrario, una lista de atributos especificados por el usuarie
    """
    formato.encabezado(col_select)
    for l in lista:
        rowdata = [str(getattr(l, col)) for col in col_select]
        formato.fila(rowdata)