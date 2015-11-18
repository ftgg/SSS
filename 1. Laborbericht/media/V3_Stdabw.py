import os
import numpy as np
import math

path = os.getcwd()

for file in os.listdir(path):
    if "v3_l" in file:
        tmp = np.genfromtxt(file,delimiter=",") 
        xl = tmp[:,1] #längenmessung
l = np.mean(xl)
        
for file in os.listdir(path):
    if "v3_b" in file:
        tmp = np.genfromtxt(file,delimiter=",") 
        xb = tmp[:,1] #breitenmessung
b = np.mean(xb)

#summe aller differenzen / anzahl -1
empirischeS = []
anzahl = 0
summe = 0
for value in xl:
    value = (float(value) - float(l)) ** 2
    summe = float(summe) + float(value)
    anzahl = anzahl + 1

empirischeS.append(math.sqrt(summe / (anzahl - 1)))

anzahl = 0
for value in xb:
    value = (float(value) - float(b)) ** 2
    summe = float(summe) + float(value)
    anzahl = anzahl + 1

empirischeS.append(math.sqrt(summe / (anzahl - 1)))
   
#Standartabweichung Mittelwert 
Stdabwm = []
for empstd in empirischeS:    
    Stdabwm.append(empstd / math.sqrt(anzahl)) 
print(Stdabwm)