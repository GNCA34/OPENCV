import cv2
import numpy as np



#1
"""

***********
    sifir=np.zeros([300,300])
    bir=np.ones([300,300])

    cv2.namedWindow("sifir",cv2.WINDOW_NORMAL)
    cv2.namedWindow("bir",cv2.WINDOW_NORMAL)

    cv2.imshow("sifir",sifir)
    cv2.imshow("bir",bir)
************
#2
***********
cam=cv2.VideoCapture(0)#bilgisayar kamerası için 0 kullanıyoruz dahili kameralar için 1,2.. şeklinde arttırılabilir.
print(cam.get(3))
print(cam.get(4))

cam.set(3,320)
cam.set(4,240)#get ile kamera boyutunu alıyoruz set ile değiştiriyoruz.

print(cam.get(3))
print(cam.get(4))


if not cam.isOpened():
    print("kamera tanınmadı.")
    exit()
    
    
while True:
    ret,frame =cam.read()#ret kameradan okunup okunmadığını söylüyor frame ise çerçeve
    
    frame=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)#Görüntüyü siyah beyaz formda gösterir.
    

    
    
    if not ret:
        print("Kameradan görüntü okunamıyor..")
        break
    cv2.imshow("kamera",frame)
    if cv2.waitKey(1) & 0xFF ==ord("q"):
        print("görüntü sonlandırıldı.")
        break


cam.release()

*************
"""
##3 Bu kısımda video üzerinde çalışma yapılmıştır.
# # cam=cv2.VideoCapture("Ballıkayalar.mp4",0)

#  while cam.isOpened():
# #     ret,frame=cam.read()
# #     if not ret:
# #         print("Kameradan görüntü okunamıyor..")
# #         break
# #     cv2.imshow("görüntü",frame)
# #     if cv2.waitKey(1) & 0xFF==ord("q"):
# #         print("Video kapatıldı.")
# #         break
# # cam.release()
    


'''Bu kısımda kameradan alınan görüntü kaydediliyor.Harici kamera kullanırsan VideCapture ı 2 yap ya da 1'''   
cam=cv2.VideoCapture(0)
fourrc=cv2.VideoWriter_fourcc(*'XVID')

out=cv2.VideoWriter("video.avi",fourrc,30.0,(640,480))

while cam.isOpened():
    ret, frame=cam.read()
    
    if not ret:
        print("kameradan görüntü alınamadı.")
        break
    
    out.write(frame)
    cv2.imshow("kamera",frame)
    
    if cv2.waitKey(1)==ord("q"):
        print("Videodan ayrıldınız.")
        break
 
cam.release()
out.release()


cv2.destroyAllWindows()