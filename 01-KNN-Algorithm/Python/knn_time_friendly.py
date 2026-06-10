import numpy as np

def knn_hesapla(H, sorgu, k=None):
    n = H.shape[0]
    if n <= 2:
        raise RuntimeError("VERİ_SETİ_YETERSİZ")
    
    if k is None:
        k = int(np.round(np.sqrt(n)))
        if k % 2 == 0: k += 1
    
    koordinatlar = H[:, :2]
    mesafeler = np.sqrt(np.sum((koordinatlar - sorgu)**2, axis=1)) #2 sütunlu koordiantlar dizisinden 2 sütunlu sorguyu çıkar
                                                                    #koordinatların karesini al ve satır bazında toplayıp karekökünü al
    
    en_yakinlarin_indeksleri = np.argpartition(mesafeler, k)[:k] #en küçük k elemanı bul ve ilk k sıraya yerleştir. sıralama önemsiz.
                                                                 #sonrasında ilk k taneyi döndür. bunu yaparak knn_scratch kodundaki for döngüsünden kurtulduk
                                                                 #o for döngüsünde bütün elemanlardan hem en küçük k taneyi buluyorduk hem de tamamını sıralıyorduk
                                                                 #burada ise en küçük k taneyi bulup bütün verileri tek tek sıralamayla uğraşmıyoruz
    en_yakinlarin_siniflari = H[en_yakinlarin_indeksleri, 2]
    
    aGrup = np.sum(en_yakinlarin_siniflari == 1)
    bGrup = np.sum(en_yakinlarin_siniflari == 2)
    
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
