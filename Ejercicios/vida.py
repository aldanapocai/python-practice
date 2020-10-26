# -*- coding: utf-8 -*-
"""
Created on Tue Sep 29 20:38:24 2020.

vida.py



@author: Aldana
"""

from datetime import datetime, date, timedelta

#%%Ejercicio 7.1: Segundos vividos
def segundos_vida(nac):
    """
    Pre: fecha de nacimiento .Ingresar con formato dd/mm/yyyy.
    
    Pos: segundos vividos
    """
    nac = datetime.strptime(nac, '%d/%m/%Y')
    timestamp_nac = datetime.timestamp(nac)
    
    now = datetime.today()
    timestamp_now = datetime.timestamp(now)

    vivido = timestamp_now - timestamp_nac
    
    return int(vivido)

#%%Ejercicio 7.2: Cuánto falta
def dias_primavera():
    """Devuelve los dias que faltan para la siguiente primavera."""
    now = date.today()
    primavera = date(year = now.year, month = 9, day = 21 )
    cuanto_falta = int((primavera - now).days)
    
    if cuanto_falta < 0:
        cuanto_falta = cuanto_falta + 365
    
    return cuanto_falta
    

#%% Ejercicio 7.3: Fecha de reincorporación
licencia_comiezno = date(2020, 9, 26)
licencia_fin = licencia_comiezno + timedelta(days=200)


#%%Ejercicio 7.4: Días hábiles
feriados = ['12/10/2020', '23/11/2020', '7/12/2020', '8/12/2020', '25/12/2020']
def dias_habiles(inicio, fin, feriados):
    """
    Pre: Ingresar con formato 'dd/mm/yyyy'.
    
    Pos: dias habiles en un periodo
    """
    fecha = datetime.strptime(inicio, '%d/%m/%Y')
    fin = datetime.strptime(fin, '%d/%m/%Y')
    feriados = [datetime.strptime(fecha, '%d/%m/%Y') for fecha in feriados]
    
    cont = 0
    try:
        while fecha != fin:
            fecha += timedelta(days=1)
            if fecha not in feriados and fecha.weekday() in [0,1,2,3,4]:
                cont +=1
    except OverflowError as e: 
        print(f'Error: {e}. Verifique que la fecha inicial es anterior a la final')
        
    return cont
        
x= dias_habiles('30/09/2020','08/10/2020', feriados)       
    