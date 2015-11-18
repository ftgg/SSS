import os
import matplotlib.pyplot as plt
import numpy as np

path = os.getcwd()

for file in os.listdir(path):
    if "Xv1_data" in file:
        tmp = np.genfromtxt(file,delimiter=",") 
        y = tmp[:,0] #y-Achse = abstand in cm
        x = tmp[:,1] #x-Achse = Spannung in V
# durschnittliche Messergebnisse
plt.plot(x, y, "k",label = "Übertragungskennlinie")
plt.plot(x,y,"ro",label = "Werte original")
plt.ylabel("Abstand in cm")
plt.xlabel("Spannung in V")
plt.legend()
plt.grid(True)
plt.show()
