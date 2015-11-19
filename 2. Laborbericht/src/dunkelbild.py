import cv2read as cread
import numpy as np
import cv2

def getimgmean(filename):			# berechnet das durchschnittsbild
    avg = np.zeros((480, 640), dtype=np.double)	# zu beginn ein Schwarzes Bild
    for i in range(1,11):			# alle 10 aufgenommenen Bilder mit gewichtung 1/10
						# zu einem durchschnitts Bild zusammen addieren.
        avg = avg + cread.bildoeffnen("../Bilder/" + filename + str(i) + ".png") /10
    return avg

bild = getimgmean("weissbild_")			# durchschnittliches Weissbild berechnen
img = np.array(bild)				# in ein numpy array in uint8 umwandeln
cv2.imwrite("../Bilder/weissbildMean.png", img)	# errechnetes Weissbild Speichern
