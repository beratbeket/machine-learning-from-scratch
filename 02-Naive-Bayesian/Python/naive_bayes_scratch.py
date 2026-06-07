import numpy as np

def nbayes_hesapla(H,sorgu):
    n_toplam = H.shape[0]
    if n_toplam <=6:
        raise RuntimeError("VERİ_SETİ_YETERSİZ")
    
    x = H[:,0]
    y = H[:,1]
    sinif = H[:,2]
    n_bir = np.sum( sinif == 1)
    n_eksi = np.sum(sinif == -1)
    
    unique_x = len(np.unique(x))
    unique_y = len(np.unique(y))
    
    p_bir = n_bir / n_toplam
    p_eksi = n_eksi / n_toplam

    def olasilik_Hesapla(sutun, hedef_sinif, sorgu_noktasi, unique_sayisi ):
        n_sinif = np.sum(sinif == hedef_sinif)
        eslesen_adet = np.sum(sutun[(sinif == hedef_sinif)] == sorgu_noktasi)
        return (eslesen_adet+1) / (n_sinif +unique_sayisi)
    
    p_x_sorgu_bir = olasilik_Hesapla(x, 1, sorgu[0], unique_x)
    p_y_sorgu_bir = olasilik_Hesapla(y, 1, sorgu[1], unique_y)
    skor_bir = p_bir * p_x_sorgu_bir * p_y_sorgu_bir

    p_x_sorgu_eksi = olasilik_Hesapla(x, -1, sorgu[0], unique_x)
    p_y_sorgu_eksi = olasilik_Hesapla(y, -1, sorgu[1], unique_y)
    skor_eksi = p_eksi * p_x_sorgu_eksi * p_y_sorgu_eksi 

    if skor_bir > skor_eksi:
        return 1,skor_bir   
    else:
        return -1,skor_eksi

    
H = np.array([ 
    [1 ,3  ,1],
    [2 ,0 ,-1],
    [3 ,1  ,1],
    [1 ,2  ,1],
    [3 ,5 ,-1],
    [4 ,2  ,1],
    [2 ,4 ,-1],
    [1 ,1  ,1],
    [3 ,3 ,-1]
])

while True:
    try:
        a = int(input("Sorgunuzun x değerini giriniz: "))
        b = int(input("Sorgunuzun y değerini giriniz: "))
        try:
            tahmin,skor = nbayes_hesapla(H,[a,b])
            print( f"\n Tahmin edilen sınıf={tahmin}. Skor={skor: .6f} ")
            break
        except RuntimeError:
            print("\033[1;31m" + "HATA !!! Veri seti KNN için çok yetersiz! ".center(100,"*") + "\033[0m")
    except ValueError:
        mesaj = " HATA!!! yalnızca tamsayı değerler ile tahmin yapılabilmektedir. Tekrar değer giriniz! ".center(100,"*")
        print("\033[1;31m" + mesaj + "\033[0m")
    else:
        break
