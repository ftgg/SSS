import cv2read as cread
import matplotlib.pyplot as plt
import numpy as np


def avg_stdabw(array):
    avg = np.mean(array)    
    std = 0
    for y in range(0,array.shape[0]):
        for x in range(0,array.shape[1]):
            std = std + ((array[y][x] - avg) ** 2) / (array.size -1)
    std = np.sqrt(std)
    return avg, std
    
    
def subimg(img):
    return npframe[:,0:110],npframe[:,120:260],npframe[:,280:410],npframe[:,420:560],npframe[0:460,570:640]
    
frame = cread.bildoeffnen("../Bilder/graustufen_korrigiert.png")

npframe = np.array(frame, dtype=np.uint8)


#plt.imshow(npframe, cmap='gray', interpolation='bicubic')

subimgs = [] 
subimgs = subimg(npframe)

i = 0

for img in subimgs:
    i = i+1
    avg, std = avg_stdabw(img)
    print(str(avg) + " & " + str(std))

def machmal(a, b):
    ad = a - b
    pd = ad / a
    print("& " + str(ad) + " & " + str(pd*100) +" \\\\")    

#Werte und abweichungen von original:
#9.36988636364 & 7.49026922212
#39.1486458333 & 5.99208565559
#85.778525641 & 6.92558105036
#126.990104167 & 8.85840071638
#152.387360248 & 9.1517897154

#Werte und abweichung korrigiert:
#9.25975378788 & 7.19829300606
#38.6003125 & 4.50868560208
#83.8205448718 & 2.5536580808
#127.321220238 & 2.3223536311
#157.074037267 & 1.8587960295

#print("grau 1: (wert, stdabw)")
#machmal(9.36988636364, 9.25975378788)
#machmal(7.49026922212, 7.19829300606)
#print("grau 2:")
#machmal(39.1486458333, 38.6003125)
#machmal(5.99208565559, 4.50868560208)
#print("grau 3:")
#machmal(85.778525641, 83.8205448718)
#machmal(6.92558105036, 2.5536580808)
#print("grau 4:")
#machmal(126.990104167, 127.321220238)
#machmal(8.85840071638, 2.3223536311)
#print("grau 5:")
#machmal(152.387360248, 157.074037267)
#machmal(9.1517897154, 1.8587960295)

#ändergunen
grau 1: (wert, stdabw)
& 0.1101325757599998 & 1.1753885958251438 \\
& 0.2919762160600001 & 3.898073719403119 \\
grau 2:
& 0.5483333333000004 & 1.4006444453656832 \\
& 1.4834000535100005 & 24.755988795422855 \\
grau 3:
& 1.957980769200006 & 2.2826001666134252 \\
& 4.37192296956 & 63.12716489445664 \\
grau 4:
& -0.33111607099999674 & -0.260741632721679 \\
& 6.53604708528 & 73.78360151617713 \\
grau 5:
& -4.686677019000001 & -3.0755024638347663 \\
& 7.2929936859 & 79.68926202082478 \
