import cv2
import sys
import numpy as np

def bildoeffnen(filename):		# ließt ein Bild von Verzeichniss als Matrix ein
    pic = cv2.imread(filename)
    pic = cv2.cvtColor(pic, cv2.COLOR_BGR2GRAY)
    return pic

def einlesen(filename):			# nimmt ein Bild von Kamera als Matrix auf
    cap = cv2.VideoCapture(0)
    if (not cap.isOpened()):		# fehlerbehandlung, falls keine Kamera gefunden
        print("fehlgeschlagen")
        sys.exit(-1)
    while(True):			# dauerhaft aktualisiertes Bild auf Monitor ausgeben
        ret, frame = cap.read()
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)	# umwandlung in ein Graubild
        cv2.imshow("frame", gray)	# anzeigen des Bildes
        if(cv2.waitKey(1) & 0xFF == ord('q')):
            cv2.imwrite(filename, gray)	# bei betätigung der Taste 'q' wird das Bild gespeichert
            break;          
    cap.release()
    cv2.destroyAllWindows()

def contrastMax(pic):			# sorgt für einen maximalen Kontrast des übergebenen Bildes
    newPic = np.zeros((pic.shape[0],  pic.shape[1]), dtype=np.uint8)
    minVal = np.min(pic)		# minimalwert, später 255
    maxVal = np.max(pic)		# maximalwert, später 0
    for y in range(0,pic.shape[0]):
        for x in range(0,pic.shape[1]):
            if (maxVal-minVal) != 0:	# division durch 0 vermeiden
                newPic[y][x]= (float(pic[y][x]- minVal)*(255.0/(maxVal-minVal)))
            else:
                newPic[y][x]= 0		# falls maxval == minval wird das Bild schwarz
    return newPic

#for i in range(1,11):			# beispielschleife zum Einlesen der 10 dunkelbilder
#    einlesen("../Bilder/dunkelbild" + str(i) + ".png")

def print_inf():			# gibt Informationen über die Kameraeinstellung aus
    cap = cv2.VideoCapture(0)
    print("frame width:   " + str(cap.get(3)))
    print("frame height:  " + str(cap.get(4)))
    print("----------------------------------")
    print("brightness:    " + str(cap.get(10)))
    print("contrast:      " + str(cap.get(11)))
    print("saturation:    " + str(cap.get(12)))
    print("----------------------------------")
    print("gain:          " + str(cap.get(14)))
    print("exposure:      " + str(cap.get(15)))
    print("----------------------------------")
    print("white balance: " + str(cap.get(17)))
    cap.release()
