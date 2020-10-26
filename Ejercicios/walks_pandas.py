# -*- coding: utf-8 -*-
"""
Created on Sun Oct  4 14:50:47 2020.

@author: Aldana
"""
import pandas as pd
import numpy as np 

idx = pd.date_range('20200923 14:00', periods = 120, freq = 'min')
s1 = pd.Series(np.random.randint(-1,2,120), index = idx)
s2 = s1.cumsum()

s2.plot()

w = 5
s3 = s2.rolling(w, min_periods=1).mean()
s3.plot

df_series_23 = pd.DataFrame([s2, s3]).T

df_series_23.plot()

horas = 8
idx = pd.date_range('20200923 14:00', periods = horas*60, freq = 'min')
nombres = ['Pedro', 'Santiago', 'Juan', 'Andrés','Bartolomé','Tiago','Isca','Tadeo','Mateo','Felipe','Simón','Tomás']

df_walks = pd.DataFrame(np.random.randint(-1,2,[horas*60,12]).cumsum(axis=0), index = idx, columns = nombres)
df_walks.plot()

w = 45
df_walk_suav = df_walks.rolling(w, min_periods = 1).mean()
nsuav = ['S_' + n for n in nombres]

df_walk_suav.columns = nsuav 

df_walk_suav.plot()


df_walk_suav.to_csv('caminata_apostolico.csv')
