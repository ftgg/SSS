#Empirische Standartabweichung
    #aufsummieren aller abstände (zwischen punkt und y)²
    #teilen durch anzahl messungen -1 und dann wurzel ziehen
import os
import matplotlib.pyplot as plt
import numpy as np
import math

for file in os.listdir(os.getcwd()):
    if "Xv1_data" in file:
        tmp = np.genfromtxt(file,delimiter=",") 
        x = tmp[:,0] #x-Achse = abstand in cm
        y = tmp[:,1] #y-Achse = Spannung in V?

empirischeS = []
index = 0
anzahl = 0

for file in os.listdir():
    if "v1_data_" in file:
        tmp = np.genfromtxt(file,delimiter=",")
        werte = tmp[:,1] 
        summe = 0
        anzahl = 0
        for value in werte:
            value = (float(value) - float(y[index])) ** 2
            summe = float(summe) + float(value)
            anzahl = anzahl + 1
            #print(value)
        empirischeS.append(math.sqrt(summe / (anzahl - 1)))
        index = index + 1
    
#Standartabweichung Mittelwert 
Stdabwm = []
index = 0
for empstd in empirischeS:    
    Stdabwm.append(empstd / math.sqrt(anzahl))
    index = index + 1