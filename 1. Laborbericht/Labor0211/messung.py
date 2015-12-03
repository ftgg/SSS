# -*- coding: utf-8 -*-
"""
Created on Mon Nov  2 14:27:42 2015

@author: edc10
"""

import numpy as np
from TekTDS2000 import *

scope = TekTDS2000()

dists = np.linspace(10,70,20)
res = np.zeros((20,3))

for i in range(len(dists)):
    print('Abstand ' + str(dists[i]))
    input()
    x,y = scope.getData(1,1000,2500)
    np.savetxt("v1_data_" + str(dists[i]) + ".csv",np.transpose([x,y]), delimiter=",")
    res[i, 0] = dists[i]
    res[i, 1] = np.mean(y)
    res[i, 2] = np.max(y) - np.min(y) #delta V
np.savetxt("v1_data.csv", res, delimiter=",")