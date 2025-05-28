
# def kare(sayı):
#     return sayı*sayı
# liste=[1,2,3,4,5,6]
# print(list(map(kare,liste)))



# liste1 = [2,3,4]
# liste2 = [1,5,9,11,55]
#
# def kucuk(x,y):
#     if x<y:
#         return x
#     return y
#
# print(list(map(kucuk,liste1,liste2)))

# çıktı:
# [1, 3, 4]
# burada fonksiyona kaç adet liste veya iterasyon göndermek istiyorsak tanımladığımız fonksiyonun içinde onu karşılamalı
# burada map fonksiyonu içine gönderilen liste lerden boyu en kısa olana göre iterasyon yaptı. liste1 den x değerini
# yani 2 yi aldı liste 2 den de 1 değerini aldı koşul bloğunda kontrol etti. kontrpol sonucunda x<y koşulu sağlanmayınca
# y değerrini dönderdi.


# from functools import reduce
# number =[11,3,9,12,4,15,66]
#
# def findmax(a,b):
#     if a>b:
#         return a
#     return b
#
# print(reduce(findmax,number))

#çıktı:

#Listenin ilk 2 elamanını aldı ve find_max içerisine gönderdi yani find_max(11,3) yaptı ve 11 sayısını döndü.
# find_max(11,9) yaptı ve 11 döndü.
# find_max(11,12) yaptı ve 12 döndü.
# find_max(12,4) yaptı ve 12 döndü.
# find_max(12,15) yaptı ve 15 döndü.
# find_max(15,66) yaptı ve 66 döndü.
# liste içinde eleman kalmadığı için işlemi sonlandırdı ve son döndüğü değer olan 66 yı döndürdü.


# from functools import reduce
# def toplama(sayı1,sayı2):
#     return sayı2+sayı1
#
# sayılar=range(1,32)
#
# print(reduce(toplama,sayılar))
# burada tamolarak olan şey şudur: biz bir fonksiyon tanımlayrak belli aralıktaki sayıları toplamak istiyoruz.
# bunu aşağıda yazdığımız for döngüsü ile de yapabilirken biz reducefonksiyonu kullanarak yazmayı deniyoruz.
# öncelikle 'from functools import reduce' diyerek kullanacağımız reduce fonksiyonunu import ediyoruz. daha sonra
# işlem yaptıracağımız fonksiyonu def altında tanımlıyoruz. def altında tanımladığımız fonksiyon bize diyorki:
# fonksiyon argümanlı içine gelen 2 argümanı (sayı1 ve sayı2 ) toplayacağım ve bubu size return ile döndereceğim.
# yani bizim 2 tane sayıyay yani argümana ihtiyacımız var. daha sonra fonksiyondan bağımsız olarak sayılar isminde
# bir değişken tanımlayıp bu değişkenin elemanlarının da range ile belirlenen aralıktan alınmasını istiyoruz.
# buradan bize 1 den başalayan ve 32 e kadar giden (32 dahil değil ) sayılardan oluşan eleman sıralaması veriyor.buda tm
#gelelim print ifadesi içinde reduce fonksiyonunu çağırdık. reduce fonksiyonu içinde de toplama fonksiyonunu çağırıyoruz
# reduce() foknsiyonu toplama fonkisyonuna diyor ki: sayılar değişkeninden gelen 2 değeri al ve bunu kendi fonksiyonu
# içinde işleme tabi tut be bir değer çıkar diyor. ve işlemler aşağıda ki gibi devam edeiyor...
# [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31]
# reduce fonksiyonu, sayılar değişkeni için range fonksiyonu ile oluşturulan üstteki listeden 1 ve 2 değerini alıyor ve
# bu değerleri toplama() fonksiyonuna gönderiyor toplama(1,2) şeklinde, toplama fonksiyonu buradan 1+2=3 işlemini
# yapıyor ve bize 3 değerini döndürüyor.
#daha sonra reduce fonksiyonu toplama (1,2) den dönen 3 değeri ile listede ki 4 değerini alıyor ve toplama fonksiyonuna
# gönderiyor toplama(3,4) şeklinde, toplama fonksiyonu burdan 3+4=7 işlemini yapıyor ve bize 7 değerini döndürüyor.
# toplam(7,5) = 12
# toplam(12,6) = 18
# toplam(18,7) = 25 bu şekilde tek tek her elemanı alarak devam edip..
#
#en son çıktı olarak
# bize
#496 sonucu dönüyor.




# toplam=0
#
# for i in range(1,100):
#     toplam+=i
#
# print(toplam)


# from functools import reduce
#
# def faktoriyel(sayi1,sayi2):
#     return sayi1*sayi2
#
# sayılar=range(1,7)
#
# print(reduce(faktoriyel,sayılar))

# yukarıda ki fonksiyon da bir sayınınn faktörüyelini almak için yazıldı. daha sonra bu fonksiyon içinde
# tanımlanmış sayı1 ve sayı2 argümanları nın yerine gönderilmek üzere sayılar isminde range fonksiyonu ile 1 den 7 ye
# kadar olan aralıkta elde edilmiş sayılar dizisi oluşturulmuştur. daha sonra da print fonksiyonu içinde reduce
# fonksiyonu çalıştırıldı. buraya kadar tamam.
# reduce fonskiyonu diyor ki: benim çalışma mantığım şu şekildedir: bana işlem yapmam için bir adet fonksiyon ve
# bu fonskiyonu iterasyona sokacağım liset veya listeler ver. reduce(fonksiyon,itersayon) gibi...
# Sayılar =[1,2,3,4,5,6) oluştu. daha soonra reduce fonskyonu bu liste içinde ilk iki elemanı alarak faktöriyel
# fonksiyonuna yolladı. faktoriyel(1,2)
# faktoriyel(1,2) = 1*2=2 değeri döndü. reduce bu değeri belleğe aldı. daha sonra listenin 3. elemanı olan
# 3 elemanını alıp faktoriyel foksiyonuna yolladı faktoriyel(2,3)
# daha sonra faktoriyel(6,4) = 24
# daha sonra faktoriyel (24,5) = 120
# daha sonra faktoriyel (120,6) = 720 bize en son reduce foksiyonu ile dönen ve print ile ekrana yazdırılan değer.

# buda reduce fonlksiyonu kullanmadan faktöriyel hesaplamanın diğer yolu
# carpma=1
#
# for i in range(1,7):
#     carpma*=i
#     i+=1
# print(carpma)
#çıktı:
# 720




# import re # regular Expression = düzenli ifadeler. filtreleme fonskiyonuu kullanırken bunu modülü import etmemiz gerekli
# def teksayı(sayı):
#     return sayı%2==1
# liste=range(1,10)
# print(list(liste))
# print(list(filter(teksayı,liste)))

# yukarıda ki fonksiyonda tam olarak ne oluyor. öncelikle filter fonksiyonun çalışabilmesi için re modülünü
# import ediyoruz.
# daha sonra yapmak istediğimiz fonksiyonu def ifadesi altında. daha sonra da hangi aralıkta ki tek sayıları bulmak
# istiyorsak o listeyi range fonsksiyonu ile elde ettik ve bunu da liste isimli değişeken atadık. daha sonra da print
# ile liste ekrana basılıyor(burda maksat oluşan listeyi görmek)
# en sonun da da print ile filtre fnskiyonu print ile ekrana basılıyor.
# [1, 2, 3, 4, 5, 6, 7, 8, 9]
# filter fonksiyonu yukarıda ki liste içerisinden ilk elemanı alıyor. daha sonra bu elemanı teksayı fonksiyonuna
# gönderiyor.
# teksayı(1) buradan 1%2==0 şartı sağlanmadığı için tek sayı fonksiyonu bize 1 değerini geri döndürmüyor.
# daha sonra teksayı fonskiyonuna 2 değeri gönderiliyor filtre fonksiyonu ile.
# teksayı(2) 2 değeri return kısmında şartı sağladığı için bu değer bize döndürülüyor ve list fonskiyonu ile liste
# yapmak için belekte tutuluyor.
# daha sonra sırası ile diğer elemanlar tek tek deneniyor ve aşağıda ki liste oluşuyor.
# [1, 3, 5, 7, 9]

# yukarıda filter () fonskiyonu ile yazdığımız kod fo döngüsü ile yazdık.
# liste=[]
# for i in range(1,10):
#     if i%2!=0:
#        liste.append(i)
# print(liste)

# çıktı:
# [1, 3, 5, 7, 9]

# aslında bu map() reduce() filter() donskiyonları çok uzun işlemleri yapmakta çok kısa sürelerde yapmamızı sağlıyor.



























