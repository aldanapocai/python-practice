# -*- coding: utf-8 -*-
"""
Created on Sun Oct  4 18:45:52 2020.

mareas_fft.py

@author: Aldana_Pocai
"""

import pandas as pd

df = pd.read_csv('Data/OBS_SHN_SF-BA.csv', index_col = 'Time', parse_dates = True)


dh = df['12-25-2014': ].copy()

delta_t = -1 #tiempo que tarda la marea entre ambos puertos
delta_h = 17 #diferencia de los 0 de escala entre ambos puertos

pd.DataFrame([dh['H_SF'].shift(delta_t) - delta_h, dh['H_BA']]).T.plot()
