a = 0 # sayılar isminde bir değişken tanımlandı.
for i in range(10):# burada for ile döngü oluşturuldu. bu döngü range fonksiyonu ile sınırı belirlendi.
    a += int(input("Sayi Giriniz: ")) # burada ise sayilar değişkeni input fonksiyonu ile her döngüde kullanıcıdan
    # alınarak ve bu alınan değerler int fonksiyonu ile veri tipi dönüşümü yapılıp her döngü de toplanmıştır.
print(a/10) # döngü bittikten sonra elde edilen sayıların toplamı print fonksiyonu içersinde 10 a bölünerek
# ekrana yazdırıldı.
