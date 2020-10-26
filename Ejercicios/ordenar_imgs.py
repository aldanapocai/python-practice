# -*- coding: utf-8 -*-
"""
Created on Wed Sep 30 11:44:53 2020

@author: Aldana
"""

import os
import datetime

if not 'Data//imgs_procesadas/':
    os.mkdir('Data/imgs_procesadas/')

for root, dirs, files in os.walk(".Data/ordenar"):
    for dir in dirs:
        for file in files:
            if file.endswith('.png'):
                fecha = file[-12: -4]
                fecha = datetime.datetime(int(fecha[:4]), int(fecha[4:6]), int(fecha[6:8]))
                ts_fecha = fecha.timestamp()
                file = os.path.join(root, file)
                os.utime(file, (ts_fecha, ts_fecha))
            
            