import os
import matplotlib.pyplot as plt
import numpy as np
import math

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
xhochm = []
yr = []
for current in x:
    xhochm.append(current ** m)
#y = e^c*x^m
print(c, m)
ec = (math.e ** c)
for current in xhochm:
    yr.append(ec * current)
  
plt.plot(x, yr, 'ro')
plt.plot(x, yr, 'r',label="Rückrechnung")
plt.plot(x, y, "b", label="Original")
plt.text(0.9, 32, r'$y=e^{b} * x^{a}$', fontsize=15)
plt.legend()
plt.grid(True)
plt.ylabel("Abstand in cm")
plt.xlabel("Spannung in V")
plt.show()