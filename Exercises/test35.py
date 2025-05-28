# a=5 # globalde tanmlanan a değeri. programın heryerinde istediğimiz zaman kullanılabilir. silinmez.
#
# def fonksiyon():
#     a=10 # kod bloğu içinde tanımlana a değeri. bu değer fonksiyon çalıştığında oluşturulan bellek ile çalışır.
#     # fonksiyon bittiğinde belek ile silinir yok olur. fonksiyon globalde tanımlanan a değişkeni yerine kendi
      # içerisinde tanımlanan a değişkenini kullanıyor.
#     print(a)
#
# fonksiyon() # fonksiyon çağrıldığında içerisinde tanımlanan a=10 değerini kullandı.
# print(a) # burada ise fonksiyondan bağımsız çalışan bir kod oldığu için burada ki a değeri globalde tanımlanan a
# # değerini aldı.
# # çıktı:
# # 10
# #5

#***************************************
# a=5 # Globalde tanımlanan değer
# def fonksiyon():
#    print(a) # a değeri globalde tanımlandığı için bu a değeri herhang bir fonksiyon tarafından kullanılabilir. Ki
#    # burada da kullanıldı.
#
# fonksiyon() # fonksiyon çağrıldığında golbalde ki a değerini kullanarak işlem yaptı.
# #çıktı
# # 5

# def fonksiyon():
#     print(s) # ne globalde ne yerelde (yani fonksiyon bloğu içerisinde) herhangibir s değeri, tanımlanmadığı için
#     #çıktı hata verecektir.
#
# fonksiyon()
# # çıktı:
# # hata veriyor.

#******************************************
# a=10 # globalde tanımlanan değişken.
# def fonksiyon():
#     global a # yerelde tanımlanan değişken
#     a=4
#     print(a)
# fonksiyon()
# print(a)
#çıktı:
#4
#4

# yukarıda ki kodda anlatılmak istenen durum şudur:
# fonksiyon çağrıldığında globalde bir adet a değişkeni oluşuyor. daha sonra fonksiyon çalışıyor ve fonksiyon kod bloğu
#içerisinde global a ile biz bu kod bloğu içerisnde globalde tanımlanan a değerini kullanmak istedğimizi söylüyoruz.
# fonksiyon çalışmaya devam ettiğinde a=4 değeri ile karşılaşıyor ve bölelikle bizim glolde kullanmak istediğimiz a
# burada tanımlanan 4 değeri ile değiştirilmiş oluyor.yani yeni global değerimiz 4 olmuş oluyor.

#******************************************

while True:
    deger =5
    print(deger)
    break
print(deger)
#çıktı:
#5
#5

if True:
    a= 10
    print(a)
print(a)
#çıktı:
#10
#10

# yularıda ki 2 örnekte de görüleceği üzere if ve while bloklarında tanımlanan değişkenler yerel bir değişken yerine
# globalde tanınmlanan bir değişken olmuşturlar. globalde tanımlanan bir değişken sayılırlar. Local değişkenler sadece
# fonksiyonalra ve sınıflara özgü bir değişken durumudur.













