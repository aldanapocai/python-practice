# -*- coding: utf-8 -*-
"""
Created on Wed Sep 30 12:48:56 2020

@author: Aldana
"""

import pandas as pd 
import os

directorio = 'Data'
archivo = 'data_verde.csv'
fname = os.path.join(directorio, archivo)
df = pd.read_csv(fname)




