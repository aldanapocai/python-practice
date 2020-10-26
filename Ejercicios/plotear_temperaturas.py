# -*- coding: utf-8 -*-
"""
Created on Wed Sep  2 12:29:49 2020

@author: Aldana
"""
import numpy as np
import matplotlib.pyplot as plt


temperaturas = np.load('Data/Temperaturas.npy')
plt.hist(temperaturas,bins=10)
