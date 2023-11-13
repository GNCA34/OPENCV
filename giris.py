import cv2
from matplotlib import pyplot as plt
resim =cv2.imread("kizkulesi.jpg",0)#Burada resim okuma işlmei yapılıyor,buradaki 0 resmi siyah beyaz forma dönüştürüyor.

cv2.namedWindow("resim",cv2.WINDOW_NORMAL)#Bu şekilde yapıldığında resimde büyültme küçültme işlemleri yapabiliyoruz.

cv2.imshow("resim",resim)

cv2.imshow("resim penceresi",resim)#Okunan resim gösteriliyor


plt.imshow(resim,cmap="gray")
plt.show()


k=cv2.waitKey(0)
print(k)#Hangi tuşa bastıysan onun ASCII kod  BINARY değerini yazdırıyor

if k==27:
    print("ESC tuşuna basıldı..")
elif k==ord("q"):
    print("q tuşuna basıldı,resim kayıt edildi.")
    cv2.imwrite("kizkulesigri.jpg",resim)#q tuşuna bastığımız zaman kızkulesigri adında fotoğraf kaydedilecek.



cv2.destroyAllWindows()