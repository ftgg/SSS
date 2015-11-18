# -*- coding: utf-8 -*-
"""
Created on Mon Nov  2 16:13:14 2015

@author: edc10
"""

import numpy as np
from TekTDS2000 import *

scope = TekTDS2000()
x,y = scope.getData(1,1000,2500)
np.savetxt('v3_laenge.csv', np.transpose([x,y]), delimiter=",")

input()
x,y = scope.getData(1,1000,2500)
np.savetxt('v3_breite.csv', np.transpose([x,y]), delimiter=",")