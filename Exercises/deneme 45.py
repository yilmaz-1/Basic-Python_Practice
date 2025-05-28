# Asal sayı bulma fonksiyonunu yazma

def asal_sayı(sayı): # asal_sayı isimli bir argümana sahip bir fonksiyon tanımlanıyor.
    if (sayı==1 or sayı==0): # if elif else den oluşan koşul bloğunun ilki olan if koşul bloğu oluşturuluyor. burada fonksiyona argüman olarak gönderdiğimiz sayı eğer 1 veya 0 ise return fonksiyonu ile bize False dönder.
        return False # return ifadesi ile bize burda False dönderiyor.
    elif (sayı == 2): # elif bloğunda ise fonksiyona gönderilen sayı eğer 2 ise , return ifadesi ile bize True döndermesini istiyoruz.
        return True # burada bize return ile True dönderiyor.
    else: # else bloğunda ise yukarıdaki if ve elif bloğunda ki şartlar sağlanmaz ise bu blok devreye giriyor ve bu bloktaki işlemler yapılıyor.
        for i in range (2,sayı): # for döngüsü kullanılarak, range fonksiyonu ile 2 den başlayıp 2 dahil, foksiyon içine gönderdiğimiz argüman olan sayıyıa kadar bir liste oluşturup ve bu listeden elemanları i değeri olarak alıyor.
            if (sayı % i ==0): # for döngüsü ile elde ettiğimiz i değelerlerini bu if koşul bloğunda , fonksiyon içine gönderidiğimiz argüman olan sayıyı kalansız bölüm bölmediği kontrol ediliyor. eğer i değeleri sayıyı kalansız bölüyor ise
                return False # return ifadesi ile bile False döndürüyor. Bu if bloğu için geçerli.
        return True # burada ise if bloğu çalışmaz yani kalansız bölmez ise return ile True döndürüyor.

# yukarıda fonksiyon tanımlanması bitti. biz bu fonksiyonu istediğimiz zaman istedğimiz yerde çağırıp kullanabiliriz. return ifadeleri ile de daha sonra çağırıp kullanabilieceğimiz de belirtmiş olduk.

while True: # burada doğru olduğu sürece çalşımasını istediğimiz bir döngü oluşturuyoruz. while zaten döngü kalıbı Treu ise doğru olduğu sürece çalışsın demek.
    sayı= input("Sayı:") # döngü her çalıştığında kullanıcıdan bir adet sayı girmesini istiyoruz. bu sayı yularıda tanımladığımız fonksiyonun argümanı olan sayı değişkeni zaten.
    if (sayı == "q"): # burada if bloğunda, kullanıcıdan sayı değişkeni için bir sayı girmesini istediğinde program kullanıcıda ifadesini girerse,
        print("Sistemden Çıkış Yapılıyor...")# ekrana bu ifade yazdırılıyor
        break # program burada kırılıyor ve sonlanıyor.
    else: # eğer if bloğu çalışmaz ve else bloğuna gelirse program bu blok altında tanımlanan kodlar çalışacak.
        sayı = int(sayı) # else bloğu çalıştığında ise while True altında kullanıcıdan isteidğimiz yukarıda argümanı olan sayı değişkenini burada integere çviripi veri tipi dönüşümü yapıyoruz.
        if (asal_sayı(sayı)): # burada if else yapısı ile koşul oluşturuluyor. bu blokta if koşulu içinde yukarıda tanımladığımız asal_sayı fonskiyonu çağrılıyor. if koşulu diyor ki bu fonksiyon bu if bloğu içinde True dönerse , yani bize foknsiyon Ture sonucu gönderirse
            print("Sayı Asaldır.") # ekrana basılıyor.
        else: # eğer ki if bloğu içinde çağrılan fonksiyon çalıştıpında bize False dönerse o zaman bu else bloğu çalışıyor ve
            print("Sayı Asal Değildir.") # ekrana basılıyor.

# çıktı:
# Sayı:5
# Sayı Asaldır.
# Sayı:18
# Sayı Asal Değildir.
# Sayı:



