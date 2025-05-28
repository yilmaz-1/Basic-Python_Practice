print("Sayı Toplama") # print fonksiyonu ile programın adı ekrana basılıyor.
print("Çıkmak İçin 'q' ya Basın") # kullanıcı işle yapmak istemez ise q ile çıkış yapabileceği bilgisi veriliyor.

toplam=0 # global de toplam değişkeni tanımlanıyor.

while True: # burada şart sağlandığı sürece döngü sürekli çalışmaya devam edecek. True ifadesi bunu anlatıyor.
    sayı = input("Sayı:")# kullanıcıdan input ile sayı isteniyor.

    if (sayı == "q"):#  eğer kullanıcı sayı yerine q harfi girerse
        print("programdan çıkış yapılıyor") # print ile ekrana programdan çıkış yapılıyor yazısı yazdırılıyor.
        break # bu komut ile döngü kırlıp devam etmesi engelleniyor. böylelikle program sonlanıyor.
    sayı = int(sayı) # if bloğunda kullanıcı q yerine sayı rakam girerese. bu girilen sayı str özellikte olduğu için bu sayı int fonksiyonu ile integere çevriliyor.

    toplam+=sayı # golabl de tanımladığımız toplam değişkenine her döngüde sayı eklenerek while döngüsü True olduğu sürece devam ediyor. döngü False olduğu zaman ise,
print("Toplam:",toplam) # döngünün dışında print ile toplam ekrana yazdırılıyor.


# iki kodda da aynı işlev yapılıyor. birinde if else kalıbı kullanılırken diğerinde sadece if bloğu içinde tanımlandı.

# print("Girilen Sayıların Toplamı")
# print("Çıkmak İçin 'q' ya Basın")
#
# toplam =0
# while True:
#
#      sayı = input("Sayı:")
#
#      if (sayı == "q"):
#          print("Programdan Çıkış Yapılıyor")
#          break
#      else:
#          sayı = int(sayı)
#          toplam+=sayı
# print("Toplam:",toplam)