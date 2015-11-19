import cv2read as cread
import matplotlib.pyplot as plt
import numpy as np

def avg_stdabw(array):			# berechnet die Standartabweichung des Bildes
    avg = np.mean(array)    		# Durchschnittswert des Bildes bestimmen
    std = 0
    for y in range(0,array.shape[0]):
        for x in range(0,array.shape[1]): # Standartabweichung bei jedem Pixel berechnen
            std = std + ((array[y][x] - avg) ** 2) / (array.size -1) # quadratischer Fehler
    std = np.sqrt(std)			# da std mit ² berechnet wurde, benötigt man jetzt noch die Wurzel
    return avg, std			# gibt durchschnittswert und Standartabweichung zurück
    
    
def subimg(img):			# Teilt das Graustufenbild in die einzelnen Graustufen auf
					# mindestens 10 pixel differenz zwischen den werten,
					# da die übergänge nicht exakt gerade sind
    return npframe[:,0:110],npframe[:,120:260],npframe[:,280:410],npframe[:,420:560],npframe[0:460,570:640]
    
frame = cread.bildoeffnen("../Bilder/graustufen_korrigiert.png")
npframe = np.array(frame, dtype=np.uint8)
subimgs = [] 				# korrigiertes Graustufenbild einlesen und aufspalten
subimgs = subimg(npframe)

for img in subimgs:			# Mittelwert und Standartabweichung des Bildes ausgeben
    avg, std = avg_stdabw(img)
    print(str(avg) + " & " + str(std))
