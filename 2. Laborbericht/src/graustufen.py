import cv2read as x
import matplotlib.pyplot as plt
import numpy as np


def avg_stdabw(array):
    avg = np.mean(array)    
    std = 0
    for a in array:
        std = std + ((std - avg) ** 2) / (array.size -1)
    std = np.sqrt(std)
    return avg, std
    
    
def subimg(img):
    return npframe[:,0:110],npframe[:,120:260],npframe[:,280:410],npframe[:,420:560],npframe[0:460,570:640]
    
frame = x.bildoeffnen("../Bilder/graustufen.png")

npframe = np.array(frame, dtype=np.uint8)


#plt.imshow(npframe, cmap='gray', interpolation='bicubic')

subimgs = [] 
subimgs = subimg(npframe)

i = 0

for img in subimgs:
    i = i+1
    avg, std = avg_stdabw(img)
    print(str(avg) + " & " + str(std))


#Werte und abweichungen von original:
#9.36988636364 & 0.857679061801
#39.1486458333 & 2.92549736845
#85.778525641 & 5.84137056353
#126.990104167 & 7.77458540309
#152.387360248 & 10.222753968

#Werte und abweichung korrigiert:
#9.25975378788 & 0.847988590476
#38.6003125 & 2.88894074077
#83.8205448718 & 5.73409428818
#127.321220238 & 7.79002978778
#157.074037267 & 10.427834354