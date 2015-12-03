import os
import numpy as np
import math

#a und b aus LineareRegression
a = -1.40898573049
b = 2.91477669005


def kennlinie(x):
    return (math.e ** b) * (x ** a)

def deltay(x,dx):
    return a * (math.e ** b) * (x ** (a-1)) * dx
    
def listandmean(search):
    for file in os.listdir(os.getcwd()):
        if search in file:
            tmp = np.genfromtxt(file,delimiter=",") 
            werte = tmp[:,1] #längenmessung
    mittelwert = np.mean(werte)
    return werte,mittelwert

def summe(liste,mittelwert):
    summe = 0
    for value in liste:
        value = (float(value) - float(mittelwert)) ** 2
        summe = float(summe) + float(value)
    return summe
    
#aus Datei einlesen
xl,l = listandmean("v3_l")
xb,br = listandmean("v3_b")

#summe aller differenzen / (anzahl -1)
empirischeS = []
anzahl = 1500

empirischeS.append(math.sqrt(summe(xl,l) / (anzahl - 1)))
empirischeS.append(math.sqrt(summe(xb,br) / (anzahl - 1)))

#Standartabweichung Mittelwert 
Stdabwm = []
for empstd in empirischeS:    
    Stdabwm.append(empstd / math.sqrt(anzahl)) 
    
#delta y = y'(x) * stdabw
dyl = deltay(l,Stdabwm[0])
dyb = deltay(br,Stdabwm[1])

#l und br in cm
lincm = kennlinie(l)
bincm = kennlinie(br)

#A = l * br
#dA = sqrt((l*dyl)²+(br*dyb)²)
A = lincm * bincm
dA = math.sqrt((lincm*dyl)** 2 + (bincm*dyb) ** 2)
print(A)
print(dA)
