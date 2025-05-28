def asal_mi (sayı):
    if sayı==1:
        return False
    elif sayı==2:
        return True
    else:
        for i in range(2,sayı):
            if sayı % i ==0:
                return False
        return True

# yukarıda asal_mi adında bir argümanlı (sayı) bir fonksyon tanımlandı. daha sonra ilk if bloğunda kullanıcıdan daha
# sonra istenecek olan sayı değişkeni 1 olması durumda bize return ile False döndürmesi istendi. eğer sayı 2 olursa
# return ile bize True döndürmesi istendi. eğer if ve elif bloklarındaki kod çalışmaz ise else bloğunda ki kod
# çalışır ise for döngüsü ile 2 den başlayarak kullanıcın giridiği değere kadar range fonksiyonu ile al ve diğer
# kod satırındaki if bloğuna geçiyoruz.eğer i değiişkeni ile 2 başlayıp kullanıcıdan aldığımız değere kadar olan
# bütün sayılar arasında her hangi biri kullanıcıyı tam kalansız böler ise bize return ile False değeri dönderecek.
# eğer bu kod bloğu çalışmaz ise yani hiç bir i değeri sayıyı tam ve kalansız bölmez ise bize for döngüsü return ile
# True döndürecek.

while True:
    sayı = input("Sayı: ")

    if sayı == "q":
        break
    else:
        sayı=int(sayı)

        if asal_mi(sayı):
            print(f"{sayı}'sayısı asal bir sayıdır.")
        else:
            print(f"{sayı}'sayısı asal bir sayı değildir.")
# yukarıda yapacağımız işlem ile ilgili fonksiyonu tanımlamıştık. burada ise while ile bir döngü oluşturup kullanıcıdan
# her seferinde  bir sayı alıp kontorl etmemizi sağlıyor.
# while ile başlayan kod bloğunda ise: önelikle kullnıcıdan bir sayı isteniyor. çünkü bu sayıyı kontorl edeceğiz
# asal mi değil mi diye. daha sonra da if bloğunda kullanıcı sayı yerine q harfini girerse program sonlansın istiyoruz.
# break ifadesi ile . bu kod satırına kadar hala asal_mi isimli fonksiyonu çağımadık daha. eğer bu if bloğunda ki şart
# sağlanmaz ise else bloğundaki koşul çalışacak. kullanıcıdan istemiş olduğumuz sayı işlem yacapımız için int fonksiyonu
# ile integer e çeviriyoruz. daha sonra yukarıda def asal_mi adlı fonksiyonu çağırıyoruz. çünkü bütün şartlar diğer
# kod bloklarında kontorl edildi. artık fonksiyonu çağırabiliriz. fonskiyonu çağırdığımızda ilk if elif blokları
# kontrol edilecek. o şartlar sağlanmadığı için else bloğu çalışacak (tbai bu durum giridğimiz sayıya göre değişir.)
# asal_mi fonksiyonun else bloğu içindeki for döngüsünden True ifadesi dönerse ekrana print ifadesi içindeki
# {sayı}'sayısı asal bir sayıdır yazacak eğer bize else bloğu içinden False ifadesi dönerse bize ekrana
# {sayı}'sayısı asal bir sayı değildir yazacak
# çıktı:
# Sayı: 19
# 19'sayısı asal bir sayıdır.

#