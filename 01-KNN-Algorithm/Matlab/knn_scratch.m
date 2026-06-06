H = [1 2 1; %bu örnekte 1 sınıfı a 2 sınıfı b sınıfı olarak adlandırılacaktır
    3 4 2;
    5 0 1;
    1 5 1;
    2 2 2];

x = H(:,1); %ilk sütunu sütun olarak x içine atar
y = H(:,2); %ikinci sütunu y içine
sinif = H(:,3); %üçüncü sinif içine
agrup = 0;
bgrup = 0;
k = 3; %kök(n) üzerinden hesaplanan k değeri
sorgu = [4,3] 

for i=1:length(x)
    x1 = x(i,1); 
    y1 = y(i,1); %döngü içinde noktaların x ve ylerini alır
    d(i) = sqrt((x1-sorgu(1))^2 +((y1-sorgu(2))^2)); %sorgunun o noktaya olan öklid mesafesini bi liste içinde tutar
end

[a,b] = sort(d); %listeyi küçükten büyüğe sıralar ve sıralanan mesafelerin orijinal indekslerini b içinde tutar
for i=1:k %en yakın k komşuya bakılıyor
    t = b(i); %mesafenin orijinal indeksini t üzerinde tutuyoruz
    s = sinif(t); %t içine gönderilen indeks sayesinde minimum mesafede olduğu komşunun sınıf değerini buluyoruz
    if s==1 
        agrup = agrup + 1; %incelenen komşu a grubundaysa agrup sayısı 1 artar
    else
        bgrup = bgrup + 1; %incelenen komşu b grubundaysa bgrup sayısı 1 artar
    end
end

if agrup>bgrup %verilen sorgu verisinin en yakın komşularına bakılarak sınıfı baskın gelen sınıf olarak tahmin edilmiş olur
    disp("sorgu a grubuna aittir");
else
    disp("sorgu b grubuna aittir");
end
