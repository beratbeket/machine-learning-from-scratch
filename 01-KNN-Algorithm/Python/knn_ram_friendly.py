import numpy as np
import heapq #heap yapısı kendi içinde sıralama yaparak veri sakladığı için

def generator(H):
    for satir in H:
        yield satir

def knn_hesapla(H, sorgu):
    n = H.shape[0]
    if n <= 2:
        raise RuntimeError("VERİ_SETİ_YETERSİZ")
    
    k = int(np.round(np.sqrt(n)))
    if k % 2 == 0:
        k += 1

    veriler = generator(H)
    
    en_yakinlar_heapi = []
    
    for kayit in veriler:
        koordinat = kayit[:2]
        sinif = int(kayit[2])
        
        mesafe = np.sqrt(np.sum((koordinat - sorgu) ** 2))
        
        if len(en_yakinlar_heapi) < k:
            heapq.heappush(en_yakinlar_heapi, (-mesafe, sinif))
        else:                                      #pythonda heap yapısı min heapmiş. bize en büyük değil en küçük değer lazım
            if -mesafe > en_yakinlar_heapi[0][0]: #bu yüzden - ile çarparak değerlein sıralanmasını tersine çeviriyoruz
                heapq.heappop(en_yakinlar_heapi)  #minimum değeri poplar. bizim örneğimizde - ile çarptığımız için maks sayıdan kurtulmuş oluyoruz
                heapq.heappush(en_yakinlar_heapi, (-mesafe, sinif)) #yeni veriyi ekler ve heap kendini yeniden sıralar
                
    aGrup = 0
    bGrup = 0
    
    for _, sinif in en_yakinlar_heapi:
        if sinif == 1:
            aGrup += 1
        else:
            bGrup += 1
            
    if aGrup > bGrup:
        return f"{sorgu} sorgusu a grubuna ait bir veridir"
    else:
        return f"{sorgu} sorgusu b grubuna ait bir veridir"

H = np.array([
    [1, 2, 1],
    [3, 4, 2],
    [5, 0, 1],
    [1, 5, 1],
    [2, 2, 2]
])
a = int(input("Sorgunuzun x değerini giriniz: "))
b = int(input("Sorgunuzun y değerini giriniz: "))
tahmin = knn_hesapla(H, [a, b])
print(tahmin)
