def yasHesapla(dogumYili): # burada yasHesapla isimli ve bir argümana sahip fonksiyon tanımlanıyor.
    return 2019 - dogumYili # return ile bu fonksiyon başka yerlerde veya programlarda kullanmak üzere döndürülüyor.


ageCinar = yasHesapla(1995) # yasHesapla fonksiyonuna 1995 argümanı gönderilerek çağrılıyor ve fonksiyon sonucu elde edilen sonuç ageCinar değişkenine atanıyor.
ageAhmet = yasHesapla(2012) # yasHesapla fonksiyonuna 2012 argümanı gönderilerek çağrılıyor ve fonksiyon sonucu elde edilen sonuç ageAhmet değişkenine atanıyor.

print(ageAhmet) # ekrana yazdırılıyor.
print(ageCinar) # ekrana yazdırılıyor.

# çıktı:
# 7
# 24

def emeklilikHesabı(dogumYili,isim):
    """
    bu foksiyoonun amacı emeklilik süresine ne kadar kadldığını hesaplamaktır.
    böylelikle fonksiyon bizden input olarak doğum yılını istiyor
    output olarak da emeklilik süresini veritor.

    """
    yas= yasHesapla(dogumYili) # yukarıda tanımladığımız fonksiyonu bu fonksiyon içinde çağırdık ve yas değişkenine atadık.
    emeklilik = 65 -yas
    if emeklilik > 0:
        print(f"emeklilik kalan süreniz {emeklilik} yıl dır.")
    else:
        print("zaten emeklisiniz")

emeklilikHesabı(1983,"mehmet")
# #
# #
# # def faktoriyel (sayi): # burada fonksiyonun ismini tanımladık. ve argumanını yazdık parantez içinde.
# #     faktoriyel =1 # burada faktöriyel değişkenini 1 den başlattık . çünkü bu değişken çarpım işleminde sürekli kullanılacakır.
# #     if (sayi==1 or sayi==0):# burada 1ve 0 ın özel bir durumu olduğu için if bloğu içinde 1 v 0 girildiği zaman oluşacak durum oluşturuldu.
# #         print(f"faktöriye {faktoriyel}")# if bloğunda oluşan koşul sağlanırsa bu blok altında yer alan print fonksiyonu devreye girip ekrana print içerisnde tanımlanan ifadeyi bastırıyor.
# #     else: # bu blokta ise if bloğu koşulu sağlanmazsa eğer bu blok çalışıyor. program çalışmaya başladığı zaman kod yukarıdan aşağıya doğru okunuyor ve sırası ile hangi şartlar hangi blokta tutuyor ise o blok çalıyor. diğer bloklar ise çalışmadan devam ediyor.
# #         while (sayi>=1):# else bloğu çalışmaya başladı ve altında yer alan kod while çalışmaya başlıyor.burad while döngüsü diyor ki: kullanıcının girdiği sayi 1 den büyük veya 0 a eşit olana kadar bu program tekrar tekrar çalışsın.
# #             faktoriyel*=sayi# if else bloğu dışında tanımladığımız faktöriyel değişkeni bu kısımda her döngüde sayı ile çarpılıyor. fakat bu sayı bir sonraki kodda 1 azaltılıdğı için her döngüde aynı sayı ile çarpılmıyor.
# #             sayi-=1 # 1. döngüde sayı 5 2. dögünde sayı 4 vs şekliden devam ediyor sayı. ve böylelikle sayı her döngüde 1 azaltılıyor.
# #         print(f"{faktoriyel}")# son olarak  while döngüsü altında döngü bittikten sonra sonucu ekrana yazdırmak için print fonksiyonu kullanıldı.
# #
# # faktoriyel(5) # def anahtar sözcüğü ile fonksiyon yukarıda tanımlandı. biz bu fonksiyonu istediğimiz her yerde adını yazarak çağırabiliriz.
# # # çıktı:
# # # 120
# #
# # faktoriyel(10)
# # # çıktı:
# # # 3628800
# #
#
# def selamla(x ="yok"): # burada bir foksiyon tanımladık.ismi selamla. bu foksiyonun argümanı x. eğer bu fonksiyona herhangi bir arguman vermeden çağırırsak bu x e varsayılan olarak atanan "yok" argumanı atanır.
#     print(f"isminiz: {x}")
#
# selamla("mehmet")
# # çıktı:
# # mehmet
# selamla()
# # çıktı:
# # yok