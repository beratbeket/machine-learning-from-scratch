# 📍 KNN Algoritması 3 Farklı Yaklaşım Düşünce Süreci

## ⚙️ KNN Scratch

_Bu projeye repomun temel mantığı olan from scratch yaklaşımıyla KNN alogritmasının matematiğini daha iyi anlayabilmek için knn_scratch kodunu yazarak başladım. Sonrasında [Generator vs List](https://github.com/beratbeket/aiops-log-intelligence/tree/main/02-Generator-vs-List-Benchmark) karşılaştırmasını yaptım ve aklıma buradaki ilk kodda bütün verileri listelerde tuttuğum takıldı._

## 💻 Ram Friendly

_Bunun üzerine knn_ram_friendly kodunu oluşturdum. Bu kodu yazarken kurtulamadığım bir liste yapısı vardı. Öklid mesafelerini hesaplayıp tek tek kaydettiğim liste yapısı..._

- **Generator:** Bu sorundan kurtulmak için bütün verileri hesaplayıp listeye atmak yerine her bir elemanı bellekte yer işgali yapmadan döndürsem diyerek `generator` kullanmaya karar verdim. Generatoru oluşturdum, verileri tek tek işliyordum ama yine listeye atmadan karşılaştırma yapamıyodum. Bu kısımda aklıma Algoritma Analizi dersinden `heap` geldi. Heap kendi kendine gelenleri sıralamamı sağlaycak bi yapı kurmamı sağlayabilirdi...

- **Heap:** Verileri heap içine attığımda direkt sıralanırdı ama yine bütün bi listeyi heap'e koymak aynı kapıya çıkacaktı. Bunun için heape bir kontrol yapısı kurdum. `En fazla k değeri tutsun ve her yeni değer geldiğinde kıyaslama yapıp max değeri pop ile çıkarsın.` Python kodunu araştırdım, min heap yapısını değerleri - ile çarparak ihtiyacım olan yapıya getirdim ve bellekte olabildiğince az yer işgal eden bu kodu yazmış oldum.

## ⏲️ Time Friendly

_Bu sefer de kodumdaki for döngüleri gözüme takıldı. Her yapıyı kontrol etmek için kolay yol olan for döngüsüne kaçıp uygulamayı zaman açısından verimsiz hale getirmiştim. Bunun üzerine notlarıma bakarak ve araştırma yaparak `Numpy`'ın farklı güçlerini keşfettim..._

- **NumPy:** Mesafeleri her döngüde hesaplamak yerine `NumPy matris operasyonları` kullanarak tek satırda mesafeler matrisini oluşturdum. En yakın k komşuyu döndürmek için for ile sıralama yapmak yerine `np.argpartition` ile en küçük k değeri sıralamaya zaman kaybetmeden hesapladım.

## 🛠 Kullanılan Teknikler

| Yöntem        | Yaklaşım               | Öne Çıkan Özelliği                           |
| :------------ | :--------------------- | :------------------------------------------- |
| **Temel**     | Standart Döngü         | Kod okunabilirliği ve basit hata ayıklama.   |
| **Vektörize** | NumPy Matris İşlemleri | `np.argpartition` ile yüksek hızlı sıralama. |
| **Streaming** | Generator/Iterator     | Sabit bellek tüketimi.                       |
