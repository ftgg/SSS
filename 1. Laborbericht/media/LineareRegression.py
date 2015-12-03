import os
import matplotlib.pyplot as plt
import numpy as np

path = os.getcwd()

for file in os.listdir(path):
    if "Xv1_data" in file:
        tmp = np.genfromtxt(file,delimiter=",") 
        y = tmp[:,0] #y-Achse = abstand in cm
        x = tmp[:,1] #x-Achse = Spannung in V

xl = []
yl = []

for current in x:
    xl.append(np.log(current))
    
for current in y:
    yl.append(np.log(current))

xlnp = np.array(xl)
A = np.vstack([xlnp, np.ones(len(x))]).T
m, c = np.linalg.lstsq(A, yl)[0]
print(m,c)
#Lineare regression
plt.plot(xlnp, yl, 'bo', label="Werte logarithmiert")
plt.plot(xlnp, m * xlnp + c, 'r', label='Ausgeichsgerade')
plt.legend()
plt.ylabel("Abstand in cm")
plt.xlabel("Spannung in V")
plt.text(-0.8, 2.7, r'$y={-0.704} x + {2.048}$', fontsize=12)
plt.grid(True)
plt.show()
