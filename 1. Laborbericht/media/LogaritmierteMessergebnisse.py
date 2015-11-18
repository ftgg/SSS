import os
import matplotlib.pyplot as plt
import numpy as np

path = os.getcwd()

for file in os.listdir(path):
    if "Xv1_data" in file:
        tmp = np.genfromtxt(file,delimiter=",") 
        y = tmp[:,0] #x-Achse = abstand in cm
        x = tmp[:,1] #y-Achse = Spannung in V

xl = []
yl = []

for current in x:
    xl.append(np.log(current))
    
for current in y:
    yl.append(np.log(current))

plt.plot(xl, yl, "k")
plt.plot(xl, yl, "bo", label = "Werte logarithmiert") 
plt.ylabel("Logarithmierte Distanzen")
plt.xlabel("Logarithmierte Spannungswerte")
plt.legend()
plt.grid(True)
plt.show()