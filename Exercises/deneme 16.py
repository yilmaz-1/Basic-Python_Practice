print("Armstrong Sayı Tespit Programı")

sayı=input("Sayı:")

basamak_sayısı=len(sayı)

sayı= int(sayı)

basamak =0

toplam=0

gecici_sayı = sayı

while (gecici_sayı > 0):

    basamak = gecici_sayı % 10 # bu kodda kullanıcıdan alınan sayının biler basamağı bulunuyor. gecici_sayi nin 10 ile böülümünden kalan demek oda bieler basamağını veriyor bize.
    print("basamak:",basamak) # bir önceki kodda buluğumuz basamğı ekrana prin foksiyonu ile akrana basıoruz.
    toplam += basamak ** basamak_sayısı # globalde tanımladığımız toplam=0 değişkenine daha önce bulduğumuz basamağın karesi alınıyor. buda basamak sayısı ile alınıyor.
    print("toplam:",toplam) # bu kodda bir önceki kodda elde ettiğimiz toplam ekrana print ile yazdırılıyor.
    gecici_sayı =gecici_sayı // 10 # bu kodda geçici sayının 10 ile bölümünden bölümü elde ediyoruz burada mod // foksiyonun kullanıyoruz. böylelikle sayının onlar basamğında olan sayıyı buluyoruz.
    print("gecici_sayı",gecici_sayı)

if (toplam == sayı):
        print("Sayı armstrong sayıdır.")
else:
        print("Sayı armstrong sayı değldir.")
# çıktı:
# Armstrong Sayı Tespit Programı
# Sayı:143
# basamak: 3
# toplam: 27
# gecici_sayı 14
# basamak: 4
# toplam: 91
# gecici_sayı 1
# basamak: 1
# toplam: 92
# gecici_sayı 0
# Sayı armstrong sayı değldir.

# bu program armstrong sayıyı bulma programıdır.
# bu program yukarıdan aşağıya doğru çalışmaya başladığı zaman sayı değişkeni ile kullanıcıdan bir sayı girmesi isteniyor.
# daha sonra kullanıcının girdiği sayının basamak sayısı len foksiyonu ile hesaplanıyor. saha sonra kullanıcının girdiği sayı int fonksiyonu ile veri tipi dönüşümü yapılıyor.
# aynı şekilde globalde basamak ve toplam olmak üzere 2 değişken sıfıra eşitlenip tanımlanıyor.
# gecici sayı isimli bir sayı tanımlanıp o da kullanıcının girdiği sayıya eşitleniyor.
# prgrom while döngüsü ile oluşturuluyor ve koşuluda geçici sayı sıfırdan büyük olduğu her durumda çalışsın isteniyor.
#


















