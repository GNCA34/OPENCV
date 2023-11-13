import cv2
import numpy as np
'''Bu kodda fareyi hareket ettirdikçe farenin koordinatlarını yazdırıyor'''
def draw(event,x,y,flags,param):
    print(x,y)
    pass

img=np.ones((512,512,3),np.uint8)

cv2.namedWindow("paint")

cv2.setMouseCallback("paint",draw)

while(1):
    cv2.imshow("paint",img)
    if cv2.waitKey(1) & 0xFF==ord("q"):
        break
    
cv2.destroyAllWindows()
        