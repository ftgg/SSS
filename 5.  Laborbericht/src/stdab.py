# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import numpy as np






def stdabw(a,b,i=0):
    stdab = 0
    for k in range(10):
        current = (a[k][0] - b[k][i])**2
        stdab = stdab + current
    stdab = np.sqrt(stdab / (len(a)-1))
    print(stdab)
    
    
    

keithley = np.array([0.512, 1.016, 1.521, 2.033, 2.539, 3.047, 3.559, 4.065, 4.57, 5.073])
DA = np.linspace(0.5,5.0, 10)
#stdabw(keithley,DA)


afg2 = [(0.997 , 0.995 , 0.99609 ),
(1.995 , 1.920 , 1.992 ),
(3.007 , 2.88 , 2.998 ),
(3.996 , 4.02 , 3.984 ),
(4.975 , 5.0 , 4.986 ),
(5.991 , 6.0 , 5.976 ),
(6.994 , 6.99 , 6.992 ),
(7.980 , 7.99 , 7.968 ),
(9.007 , 8.99 , 8.994 ),
(10 , 9.92 , 9.99 )]

stdabw(afg2,afg2,2)