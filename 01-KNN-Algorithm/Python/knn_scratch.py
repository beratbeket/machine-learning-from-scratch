import sys
import math
import numpy as np

def knn_hesapla(H,sorgu):
    def oklid_hesapla(nokta1,nokta2):
        return np.sqrt((nokta1[0] - nokta2[0])**2 + (nokta1[1] - nokta2[1])**2)
    n = H.shape[0]
    if n <=2:
        raise RuntimeError("VERİ_SETİ_YETERSİZ")
    
    x = H[:,0]
    y = H[:,1]
    sinif = H[:,2]
    aGrup = 0
    bGrup = 0
    
    d = []
    for i in range(len(x)):
        oklidMesafe = oklid_hesapla([x[i],y[i]],sorgu)
        d.append(oklidMesafe)

    k = int(np.round(np.sqrt(n)))
  
    if k % 2 == 0:
        k += 1
    
    c = np.argsort(d)

    for i in range(k):
        t = c[i]
        s = sinif[t]
        if s == 1:
            aGrup += 1
        else:
            bGrup += 1

    if aGrup > bGrup:
        return f"{sorgu} sorgusu a grubuna ait bir veridir"
    else:
        return f"{sorgu} sorgusu b grubuna ait bir veridir"

    
H = np.array([ #bu örnekte 1 sınıfı=a 2 sınıfı=b olarak adlandırılacaktır
    [1, 2, 1],
    [3, 4, 2],
    [5, 0, 1],
    [1, 5, 1],
    [2, 2, 2]
])

while True:
    try:
        a = int(input("Sorgunuzun x değerini giriniz: "))
        b = int(input("Sorgunuzun y değerini giriniz: "))
        try:
            tahmin = knn_hesapla(H,[a,b])
            print(tahmin)
            break
        except RuntimeError:
            print("\033[1;31m" + "HATA !!! Veri seti KNN için çok yetersiz! ".center(100,"*") + "\033[0m")
    except ValueError:
        mesaj = " HATA!!! yalnızca tamsayı değerler ile tahmin yapılabilmektedir. Tekrar değer giriniz! ".center(100,"*")
        print("\033[1;31m" + mesaj + "\033[0m")
    else:
        break







