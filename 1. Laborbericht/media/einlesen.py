#!/usr/bin/env python

import os
import numpy as np
import matplotlib.pyplot as plt

X = np.linspace(-np.pi, np.pi, 256, endpoint=True)
C,S = np.cos(X), np.sin(X)

plt.plot(X,C)
plt.plot(X,S)

plt.show()

i = 0
for file in os.listdir(os.getcwd()):
    if "v1_data_" in file:
        tmp = np.genfromtxt(file,delimiter=",")
        print(np.max(tmp[:,1]))
        #data[i:i+1,2] = np.max(tmp[:,1])-np.min(tmp[:,1])
        #i = i + 1   
#print(data)
#np.savetxt("v1_data.csv", data, delimiter=",")