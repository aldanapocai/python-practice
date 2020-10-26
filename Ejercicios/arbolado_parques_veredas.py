# -*- coding: utf-8 -*-
"""
Created on Sun Oct  4 15:49:44 2020.

arbolado_parques_veredas.py

@author: Aldana_Pocai
"""

import pandas as pd
import os


#Abrí ambos datasets a los que llamaremos df_parques y df_veredas.
archivo_parques = 'data_verde.csv'
fname_parques = os.path.join('Data', archivo_parques)
df_parques = pd.read_csv(fname_parques)

archivo_veredas = 'arbolado-publico-lineal-2017-2018.csv'
fname_veredas = os.path.join('Data',archivo_veredas)
df_veredas = pd.read_csv(fname_veredas)


# Para cada dataset armate otro seleccionando solamente las filas 
# correspondientes a las tipas (llamalos df_tipas_parques y df_tipas_veredas, 
# respectivamente) y las columnas correspondientes al diametro a la altura del 
# pecho y alturas. Hacelo como copias (usando .copy() como hicimos más arriba) 
# para poder trabajar en estos nuevos dataframes sin modificar los dataframes 
# grandes originales. Renombrá las columnas que muestran la altura y el diámetro 
# a la altura del pecho para que se llamen igual en ambos dataframes, para ello
#  explorá el comando rename.


df_tipas_parques = df_parques[df_parques['nombre_cie'] == 
'Tipuana Tipu'][['nombre_cie','diametro','altura_tot']].copy()

df_tipas_veredas = df_veredas[df_veredas['nombre_cientifico'] == 'Tipuana tipu'][['nombre_cientifico','diametro_altura_pecho', 'altura_arbol']].copy()

#renombro columnas
df_tipas_veredas = df_tipas_veredas.rename(columns = {'nombre_cientifico' : 'nombre_cie', 
'diametro_altura_pecho' : 'diametro', 'altura_arbol' : 'altura_tot' })


# Agregale a cada dataframe (df_tipas_parques y df_tipas_veredas) una columna 
# llamada 'ambiente' que en un caso valga siempre 'parque' y en el otro caso 'vereda'.

df_tipas_parques['ambiente'] = 'parque'
df_tipas_veredas['ambiente'] = 'vereda'

#Se juntan ambos datasets
df_tipas = pd.concat([df_tipas_veredas, df_tipas_parques])


# boxplot para los diámetros a la altura del pecho de la tipas distinguiendo
#  los ambientes (boxplot('diametro_altura_pecho',by = 'ambiente')).
df_tipas.boxplot('diametro', by = 'ambiente')

#Boxplot de alturas
df_tipas.boxplot('altura_tot', by = 'ambiente')


