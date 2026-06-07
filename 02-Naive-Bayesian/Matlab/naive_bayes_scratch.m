H = [ 1 3  1;
      2 0 -1;
      3 1  1;
      1 2  1;
      3 5 -1;
      4 2  1;
      2 4 -1;
      1 1  1;
      3 3 -1];

x = H(:,1);
y = H(:,2);
sinif = H(:,3);

sorgu_x = input("sorgunuzun x değerini giriniz: ");
sorgu_y = input("sorgunuzun y değerini giriniz: ");
sorgu = [sorgu_x,sorgu_y];

n_toplam = size(H,1); %toplam veri sayısını matrisin satır sayısından alıyoruz
n_bir = sum(sinif == 1); %sınıfı 1 olan toplam veri sayısını tutar
n_eksi = sum(sinif == -1); %sınıfı -1 olan toplam veri sayısını tutar

unique_x = length(unique(x)); %x sütunundaki benzersiz değer sayısı
unique_y = length(unique(y)); %x sütunundaki benzersiz değer sayısı

p_bir = n_bir / n_toplam; %veri setindeki bir verinin sınıfının 1 olma olasılığı (prior probability)
p_eksi = n_eksi / n_toplam; %veri setindeki bir verinin sınıfının 1 olma olasılığı (prior probability)

x_bir_adet = sum(x(sinif == 1) == sorgu(1)); %sınıfı 1 olan verilerin x değerleri ile sorgunun x değerini karşılaştır. Sorgunun x'ine eşit olanların toplamı
y_bir_adet = sum(y(sinif == 1) == sorgu(2)); %sınıfı 1 olan verilerin y değerleri ile sorgunun y değerini karşılaştır. Sorgunun y'ine eşit olanların toplamı
                                             %yani sorgudaki x değeri veri setinde kaç kez 1 sınıfına ait olarak görülür
x_eksi_adet = sum(x(sinif == -1) == sorgu(1)); %aynı işlemler -1 sınıfı için de tekrar edilir
y_eksi_adet = sum(y(sinif == -1) == sorgu(2));

p_x_sorgu_bir = (x_bir_adet + 1) / (n_bir + unique_x); %sorgudaki x değeriin veri setinde 1 sınıfına ait olma olasılığı. paylara eklenen +1 laplace smoothingdir 
p_y_sorgu_bir = (y_bir_adet + 1) / (n_bir + unique_y); %sorgudaki y değeriin veri setinde 1 sınıfına ait olma olasılığı 

skor_bir = p_bir * p_x_sorgu_bir * p_y_sorgu_bir; %bulduğumuz sonuçlarla sorgunun bütün olarak 1 sınıfına ait olma olasılığının hesabı (posterior probability)

p_x_sorgu_eksi = (x_eksi_adet + 1) / (n_eksi + unique_x); %sorgudaki x değeriin veri setinde -1 sınıfına ait olma olasılığı 
p_y_sorgu_eksi = (y_eksi_adet + 1) / (n_eksi + unique_y); %sorgudaki y değeriin veri setinde -1 sınıfına ait olma olasılığı 

skor_eksi = p_eksi * p_x_sorgu_eksi * p_y_sorgu_eksi; %bulduğumuz sonuçlarla sorgunun bütün olarak 1 sınıfına ait olma olasılığının hesabı (posterior probability)

if skor_bir > skor_eksi
    fprintf('Tahmin Edilen Sınıf: 1 (Skor: %f)\n', skor_bir); 
else                                                                %olasılığı yüksek olan sınıfa ait olarak yazdırılır
    fprintf('Tahmin Edilen Sınıf: -1 (Skor: %f)\n', skor_eksi);
end
