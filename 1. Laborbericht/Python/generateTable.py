# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import numpy as np

data =np.genfromtxt('../v1_data.csv',delimiter=',')

l = []
for x,y,z in data:
    tupel = (str(y)[0:5],str(z)[0:5])
    print(" & {0} & {1} &  & \\\\".format(tupel[0],tupel[1]))
#print(data)
#np.savetxt("v1_data.csv", data, delimiter=",")