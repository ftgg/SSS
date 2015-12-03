# -*- coding: utf-8 -*-
"""
Created on Mon Nov  2 16:17:45 2015

@author: edc10
"""

import numpy as np
import os



data =np.genfromtxt('v1_dataOLD.csv',delimiter=',')

i = 0
for file in os.listdir():
    if "v1_data_" in file:
        tmp = np.genfromtxt(file,delimiter=",")
        print(np.max(tmp[1]))
        data[i:i+1,2] = np.max(tmp[:,1])-np.min(tmp[:,1])
        i = i + 1   
print(data)
np.savetxt("v1_data.csv", data, delimiter=",")