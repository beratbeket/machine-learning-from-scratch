# 🧠 Machine Learning from Scratch (ML From Scratch)

[![Python Version](https://img.shields.io/badge/python-3.8%2B-blue.svg?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org)
[![NumPy](https://img.shields.io/badge/numpy-%23013243.svg?style=for-the-badge&logo=numpy&logoColor=white)](https://numpy.org)
[![Git](https://img.shields.io/badge/git-%23F05033.svg?style=for-the-badge&logo=git&logoColor=white)](https://git-scm.com)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg?style=for-the-badge)](https://opensource.org/licenses/MIT)

Hazır kütüphanelerin arkasındaki matematiksel ve mantıksal dünyayı kurcalamak, karmaşık algoritmaları temel kod seviyesinde anlaşılır kılmak için sıfırdan inşa edilen makine öğrenmesi reposu.

---

## 🎯 Projenin Amacı ve Temel Felsefesi

Bu depo, hazır makine öğrenmesi kütüphanelerini (Scikit-Learn, TensorFlow vb.) kullanmak yerine, **algoritmaların temel çalışma prensiplerini ve matematiksel teorilerini** derinlemesine anlamak amacıyla geliştirilmektedir.

### ✨ Temel Odak Noktaları:

- **Sıfırdan Algoritma İnşası:** Matematiksel formülleri ve işleme mantıklarını satır satır Python ve Matlab koduna dökerek algoritmaların core mekanizmalarını kavramak.
- **Tekrar Kullanılabilirlik & Mimari:** Kodları düz yazmak yerine; encapsulation (kapsülleme), iç içe fonksiyonlar (_nesned functions_) ve modüler yapılar kullanarak esnek, başka projelere entegre edilebilir yapılar kurmak.
- **Teoriden Gerçek Senaryolara:** `Python Journey` reposundaki temellerden yola çıkarak; orada öğrenilen temel veri yapıları, gelişmiş döngü yapıları, ileri seviye fonksiyonlar ve hata yönetimi (_try-except / raise_) gibi kavramları gerçek dünya yapay zeka senaryolarıyla birleştirerek tecrübe kazanmak.

---

## 🛠️ Kurumsal Git & GitHub İş Akışı (Workflow)

Bu proje yalnızca algoritma geliştirme değil, aynı zamanda **profesyonel bir mühendis gibi** Git ve iş birliği süreçlerini yönetme gayesi taşır. Geliştirme süreci boyunca aşağıdaki standartlar olabildiğince katı bir şekilde uygulanmaktadır:

### 🌿 Branch (Dal) Yönetimi & Yaşam Döngüsü

- Projede doğrudan `main` branch'ine kod pushlanmaz. Her bir algoritma, optimizasyon veya hata düzeltmesi için özel geliştirme dalları açılır (Örn: `refactor/knn-optimization`).
- **📌 Kalıcı Branch Yapısı:** Geliştirme yapılan branch'ler, PR kabul edildikten sonra bile **kesinlikle silinmez**. Projenin evrimsel sürecini, geçmiş mimari kararlarını ve kodun gelişim adımlarını bir arşiv gibi saklamak adına tüm branch yapısı kalıcı olarak korunur. İncelemek, öğrenmek için var olan bu arşiv bir alışkanlık kazanılana kadar tekrar edilebilmek için buradadır.

### 🔀 Pull Request (PR) Mantığı

- Yazılan kodlar ana branch'e aktarılmadan önce PR süreçlerinden geçer. Kod incelemeleri, kodun mimari bütünlüğü ve kapsam (scope) kontrolleri bu aşamada simüle edilir.

### 📝 Semantic Commit Standartları

Commit geçmişinin bir karmaşa yerine okunabilir ve açıklayıcı olması için kurumsal standartlara sahip, başlık ve açıklamadan oluşan commit mesajları kullanılır.

**\***Kullanılan Örnek Bir Commit Anatomisi:**\***
git commit -m "Refactor(knn):python-knn-optimization" -m "Python ile yazılmış knn koduna nesned functions yapısı eklenerek kodun optimizasyonu güçlendirildi ve farklı projelerin içine yerleştirilebilir hale getirildi. Hata yönetimi bloklarıyla kırılması zorlaştırıldı"

---

## 📊 Geliştirilen Algoritmalar & Yol Haritası

### 🔹 K-Nearest Neighbors (KNN) - K-En Yakın Komşu

- **Durum:** ✅ Tamamlandı (`refactor/knn-optimization`)
- **Özellikler:** \* `NumPy` ile matris operasyonları ve Euclidean mesafe hesaplaması.
  - Mesafe hesaplama yapısını koruyan ve global alanı kirletmeyen iç içe fonksiyon (_nesned function_) mimarisi.
  - Veri kümesi boyutuna göre dinamik karekök tabanlı **_k_** seçimi ve çift sayı çıkması durumunda hata önlemek için dinamik tek sayı düzeltmesi.
  - Kullanıcı giriş hatalarını yakalayan `ValueError` ve sistem kısıtlamalarını yöneten `RuntimeError` tabanlı katmanlı hata yönetimi.

### 🔹 Sırada Ne Var? (Yol Haritası)

- [ ] **Support Vector Machines (SVM):**
- [ ] **Naive Bayes:**
- [ ] **K-Means Clustering:**

---

## 🚀 Projeyi Yerelde Çalıştırma

1. Projeyi klonlayın:
   git clone https://github.com/kullanici_adi/machine-learning-from-scratch.git

2. Proje dizinine gidin:
   cd machine-learning-from-scratch

3. Gerekli kütüphaneleri yükleyin:
   pip install numpy

4. İlgili algoritmayı çalıştırın:
   python knn_clean.py

---

## ⚖️ Lisans

Bu proje MIT lisansı altında korunmaktadır. Eğitim ve kişisel gelişim amacıyla serbestçe kullanılabilir, genişletilebilir.
