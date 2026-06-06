import sys
import math
import numpy as np

H = np.array([ #bu örnekte 1 sınıfı=a 2 sınıfı=b olarak adlandırılacaktır
    [1, 2, 1],
    [3, 4, 2],
    [5, 0, 1],
    [1, 5, 1],
    [2, 2, 2]
])
x = H[:,0]
y = H[:,1]
sinif = H[:,2]
aGrup = 0
bGrup = 0

n = H.shape[0]
k = int(np.round(np.sqrt(n)))
if k == 1:
    print("Veri seti çok küçük. Tahmin sonuçları güvenilir olmayacağından program sonlandırıldı")
    sys.exit()
if k % 2 == 0:
    k += 1


a = int(input("Sorgunuzun x değerini giriniz: "))
b = int(input("Sorgunuzun y değerini giriniz: "))

sorgu = [a,b]

d = []
for i in range(len(x)):
    x1 = x[i]
    y1 = y[i]
    oklidMesafe = np.sqrt((x1 - sorgu[0])**2 + (y1 - sorgu[1])**2)
    d.append(oklidMesafe)

b = np.argsort(d)

for i in range(k):
    t = b[i]
    s = sinif[t]
    if s == 1:
        aGrup += 1
    else:
        bGrup += 1

if aGrup > bGrup:
    print(f"{sorgu} sorgusu a grubuna ait bir veridir")
else:
    print(f"{sorgu} sorgusu b grubuna ait bir veridir")

