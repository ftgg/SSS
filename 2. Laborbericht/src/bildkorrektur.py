import numpy as np
import dunkelbild as dk
import cv2read as cvread
import matplotlib.pyplot as plt
import cv2

darkimg = dk.getimgmean("dunkelbild_")  # Dunkelbild durchschnitt
whiteimg = dk.getimgmean("weissbild_")  # Weissbild durchschnitt
wimg_cmp = whiteimg - darkimg           # Weissbild ohne thermisches Rauschen
whiteNorm = wimg_cmp / np.mean(wimg_cmp)# Weissbild Normiert

#-------Bild zur korrektur einlesen
img2 = np.array(cvread.bildoeffnen("../Bilder/graustufen.png")) # original Bild
img = (img2 - darkimg) 			# PixelOffset abziehen
for x in range(0,img.shape[1]):
    for y in range(0,img.shape[0]):
        if not whiteNorm[y][x] == 0:	# keine Division durch 0 zulassen
	    # Pixelweise durch Weissbild teilen, Sensitivität anpassen
            img[y][x] = img[y][x] / whiteNorm[y][x]

cv2.imwrite("../Bilder/graustufen_korrigiert.png", img) # korrigiertes Bild
