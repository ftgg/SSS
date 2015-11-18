#import matplotlob.pyplot as plt
import cv2
#import numpy as np
import sys
import numpy as np
#plt.imshow(pic, cmap='gray', interpolation='bicubic')

#new_pic = ((pic - min_va) * (255.0 / max_val - min_val))

def bildoeffnen(filename):
    pic = cv2.imread(filename)
    pic = cv2.cvtColor(pic, cv2.COLOR_BGR2GRAY)
    return pic


def einlesen(filename):
    cap = cv2.VideoCapture(0)
    if (not cap.isOpened()):
        print("fehlgeschlagen")
        sys.exit(-1)
    
    while(True):
        ret, frame = cap.read()
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        cv2.imshow("frame", gray)
        if(cv2.waitKey(1) & 0xFF == ord('q')):
            cv2.imwrite(filename, gray)
            break;
                
    cap.release()
    cv2.destroyAllWindows()

def contrastMax(pic):
    newPic = np.zeros((pic.shape[0],  pic.shape[1]), dtype=np.uint8)
    minVal = np.min(pic)
    maxVal = np.max(pic)
    for y in range(0,pic.shape[0]):
        for x in range(0,pic.shape[1]):
            if (maxVal-minVal) != 0:
                newPic[y][x]= (float(pic[y][x]- minVal)*(255.0/(maxVal-minVal)))
            else:
                newPic[y][x]= 0
    return newPic
#for i in range(1,11):
#    einlesen("../Bilder/dunkelbild" + str(i) + ".png")
    
def print_inf():
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
   
#for i in range(1,11):
#    einlesen("../Bilder/graustufen.png")
   
#print_inf() OLD    
#frame width:   640.0
#frame height:  480.0
#----------------------------------
#brightness:    54.0
#contrast:      29.0
#saturation:    0.0
#----------------------------------
#gain:          35.0
#exposure:      -2.0
#----------------------------------
#white balance: 5668.0

#print_inf() NEW
#frame width:   640.0
#frame height:  480.0
#----------------------------------
#brightness:    75.0
#contrast:      27.0
#saturation:    38.0
#----------------------------------
#gain:          53.0
#exposure:      -1.0
#----------------------------------
#white balance: 8986.0
