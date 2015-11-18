import cv2read as x
import matplotlib.pyplot as plt
import numpy as np
import cv2


def getimgmean(filename):
    avg = np.zeros((480, 640), dtype=np.double)
    for i in range(1,11):
        avg = avg + x.bildoeffnen("../Bilder/" + filename + str(i) + ".png") /10
    pic = avg
    #pic=x.contrastMax(avg)
    #plt.imshow(pic, cmap='gray', interpolation='bicubic')
    return pic

bild = getimgmean("weissbild_")
img = np.array(bild)
#plt.imshow(bild, cmap='gray', interpolation='bicubic')

cv2.imwrite("../Bilder/weissbildMean.png", img)
