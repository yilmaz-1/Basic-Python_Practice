# aşağıda sayının çift mi tek mi olduğunu tespit eden bir program yer almaktadır.

def cift_mi(sayı): # burada bir adet cift_mi isminde bir fonksiyon tanımlandı. bir elemanlı bir fonksiyondur.
    if (sayı % 2 == 0): # eğer sayı değişkeninin 2 ile bölümünden kalan sıfır ise,
        return sayı # bu fonskiyonun çağrıldığı yere return ile sayı değişkenini döndür yolla.
    else: # değilse
        raise ValueError # fonskiyonun çağrıldığı yere raise ile ValueError hatasının fırlat yolla.
liste = [*range(1,101)] # burada liste isminde bir liste tanımlandı. bu listenin elemanları da range fonksyonu ile 1 den
# başlayarak 101 e kadar olan (101 dahil değil) sayıları bu listenin elemaın olarak atadık. burada yıldız
# kullanılmasının amacı bu bir kural range fonsiyonun çalışması için bu yıldız işaretinin konulması lazım. Bu listeyi
# oluşturmamızın amacı bu liste elemanlarını kontrol edeceğiz. hangisi çift hangisi tek.
liste2 = [] # burada boş bir liste oluşturduk. amacımız liste içerisindeki çift sayıları bunun içersine atarak daha
# düzgün bir yapı elde etmek.
for i in liste: # burada bir for döngüsü ile liste elemanları üzerinde gezerek her döngüde elemanları tek tek alarak
    # cift_mi fonksiyonuna yollayarak işleme tabi tutmak.
    try: # yukarıda hata oluşturacağını düşündüğümüz kodları try bloğu içersine aldık. amacımız hata çıkarsa, bu hatayı
        # burada yakalayıp programın sağlıklı çalışmasını sağlamak.
        cift_mi(i) # fonksiyonun içersine i değişkeni yollanarak çağrıldı.
        liste2.append(i) # daha sonra da elde ettiğimiz i değerlerini append fonksiyonu ile boş olarak tanımladığımız
        # liste2 içersine yoluyoruz.
    except ValueError: # hata türünü tanımladık.
        pass # try except bloğu birlikte kullanıldığı için except bloğu boş kalmasın diye pass deyimi ile bu blok hem
        # hata vermemiş oluyor hemde hemde bu blok içinde yer alan bir şey varsa o kdoların çalışmadan geçilmesini
        # sağlamış oluyoruz.
print(liste2) # liste2 ekrana bastırıldı.



