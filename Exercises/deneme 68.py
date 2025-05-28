# modülün bu methodunu kullandığımız zaman 0 ile 1 arasında rastgele birsayı üretilir.
# üretilen bu sayıda dikkat edilmesi gereken nokta , üretilen bu sayı 0 olabilirken 1 olamaz.
# yani [0,1) aralığında oluşmaktadır. random.random şeklinde kullanılır.

import random # bu modülü import etmeden modül çalışmaz.
print(random.random())
# # çıktı:
# # 0.7287286341833029

# ***********************************************************

import random
sayi1=random.random() # randomdan türetilen random fonksiyonu kullanırak print ile sayi
# ekrana basıldı. yani ilk random sınıfın adıdır. import tan geliyor. import ile çağırılan
# modülün sınıfıdır. ikinci ramdom ise eklemiş olduğumuz sınıfın içerisindeki foksiyondur.
print(sayi1)
# çıktı 0 ile 1 arasında rastgele üretilmiş ve float tipinde değerler verir. her çalıştırmamızda
# farklı bir sayı verir.
# 0.12633826207603072

# ***********************************************************

import random
sayi2=random.randint(1,10)
print(sayi2)
# bu kod da önce random modolü import edildi.
# ikinci satırda ki kod da 1. random, import ettiğimiz modülün sınıfı olan random,
# devamında yer alan randint ise bu modül ile çalışcak olan fonksiyondur. randint fonksiyonu
# integer tipinde belli aralıklar arasında rasgele sayı üreten bir fonksiyon.
# çıkıt:
# 9

# ************************************************************

import random
sayi3=random.uniform(1,5)
print(sayi3)
# bu kod da ilk olarak random modülü import edildi. sonra sayi3 değişkeni tanımlandı.
# sayi3 değişkeni tanımlanırken yazılan ilk random import edilen modülün sınıfından geliyor. devamında yer alan uniform ise çalıştırmak
# istediğimiz fonksiyonu temsil ediyor.
# .uniform() fonksiyonu ile belirttiğimiz aralık olan 1 ve 5 arasında float tipinde rasgele sayılar üretir.
# çıktı:
# 2.573590265213089

# ***********************************************************

import random
liste=[1,3,"mehmet",4,"hasan",5]
a=random.choice(liste)
print(a)
# çıktı:
# hasan
# çıktı:
# mehmet
# çıktı:
# 4
# çıktı:
# hasan
# bu kod da liste içerisinden rasgele bir eleman seçeceğimiz için import random
# modülünü çağırdık. zaten globalde tanımlanan listemiz mevcuttu.
# a değişken : random modülünün sınıfı olan random yazıldı (2. random bu) sonra da
# bu liste içerisnden seçimi yapacak bu modül ile çalışacak foksiyon olan choice foknsiyonu
# .choice() ile eklendi. her seferinden listeden herhangi bir elemanı çekmek için random.choice ile yapıldı.
# print ile de liste ekrana basıldı.

# ****************************************************************

import random
tahminSayısı=5
b=random.randint(1,15)
sayac=0
puan=100 # burada kullnıcıya yaptığı doğru tahmin için puan vermek amacı ile tanımlandı.
print("Toplam 5 Tahmin Hakkınız Bulunmaktadır.")
print("Toplam 100 Puanınız Bulunmaktadır.")
print("Her Yanlış Tahmin Yaptığınızda 20 Puanınız Düşecektir.")

while tahminSayısı>0: # while ile bir döngü oluşturulmuştur. fakat burda ki döngünün koşulu: tahminSayısı>0 olana kadardır. bu şart sağlandığı sürece tahmin yapmamızı isteyecek program.
    tahminSayısı -= 1 # burada tahminSayısı değişkeni her döngüde 1 azaltılarak döngü sonsuza kadar devam etmesi engellenmiştir.
    sayac+=1 # sayaç kurmamızın sebebi ise döngü kaçıncı defa da tamamlandı ve tahmin kaçıncı döngüde doğru sonuçlandı onu tespit etmek. sayaç her döngüde 1 artırılarak kaçıcı döngüde doğru tahmin edildiğini tespit etmek.
    puan1=(puan)-(20*(sayac-1)) #burada sayac-1 yazılmasının sebebi sayıyı bilidği turda ki 20 puan düşülmesini önlemektir.
    # aksi taktirde bildiği turda da puan düşer ve yanlış hesaplama yapar.
    a = int(input("1 ile 15 arasında bir sayı tahmin ediniz:")) # kullanıcıdan input ile sayı girmesi isteniyor ve bu sayı int fonksiyonu ile de veri tipi dönüşümü yapılıyor.
    if (b==a): # eğer programın random.randint() fonksiyonu ile elde ettiği sayı , kullanıcının programa girdiği sayı ile aynı ise; program çalışacak ve
        print(f"Tebrikler {sayac}. Tahminde Bildiniz. Toplam Puanınız {puan1} puandır") # print ile ekrana yazdırılacak. burada f string metodu ile sayac ve puan1 değişkenleri alınarak kullanıldı.
        break # bu kod burada sonlanıyor. çünkü doğru tahmin yapılmış oluyor ve programın tekrar tekrar çalışmasına gerek yok. yani döngü tekrar tekrar çalışmasına gerek yok.
    elif(b>a): # eğer if bloğunda ki kodda yazılmış olan koşul sağlanmaz ise bu kod bloğunda yer alan şart, yani programın ramdom fonksiyonu ile elde ettiği sayı (b) kullanıcının dışarıdan sisteme girdiği sayı (a) dan büyük ise şartı sağlanır ise program çalışıyor.
        print("Daha büyük sayı girniz.") # ekrana print ile bu yazdırılıyor.
    else: # eğer yukarıda yer alan kod bloklarında yer alan şartlardan hiç biri çalışmaz ise bu kod bloğu devreye giriyor ve çalışıyor.
        print("Daha küçük bir sayı giriniz.") # ekrana print ile yazdırılıyor

    if (tahminSayısı==0): # burda yeni bir if koşul durumu tanımlanıyor. eğer ki tahminSayısı değişkeni döngü sonunda 0 a eşit olursa, bu kod bloğu çalışıyor ve
        print("Tahmin Hakkınız Bitti Puanınız 0.") # ekrana print ile yazdırılıyor.
        print("Tutulan Sayı:",b) # ekrana print ile yazdırılıyor.
        break # tahmin hakkımız bittiği için program tekrara tekrar bizden sayı istmemesi için döngü tekrar tekrar çalışmaması için burada sonlandırılıyor.



# ***********************************************************************************************************

import random
tahminHakki=5
sayac=0
tutulanSayi=random.randint(1,100)

while tahminHakki>0:
    tahminHakki-=1
    sayac+=1
    tahminSayisi=int(input("1 ile 100 arasında bir sayı tahmin edin:"))
    if (tahminSayisi>tutulanSayi):
        print("daha küçük bir sayı tahmin ediniz.")
    elif (tutulanSayi>tahminSayisi):
        print("daha büyük bir sayı tahmin ediniz.")
    elif (tahminSayisi==tutulanSayi):
        print(f"tebrikler {sayac}. tahminde bildiniz. ")
        break
    if ( tahminHakki==0):
        print("tahmin hakkınız bitmiştir.")
        print(f"tutulan sayı {tutulanSayi}")
        break

# yukarıda yazılan son iki kod da aynı işelvi yapıyor. her ikiside sayı tahmin etme programı.
# fakat her ikisi de aynı işlevi yapsa da biraz farklı yoldan yapılmaya çalışıldı.
# sırası ile açıklarsak her iki programın çalışma sistemini.
# 1. programda : import random ile modülü çağırıldı. çünkü rastgele seçim ile tahmin yapacağımız için
# bu modül kullanıldı. tahmin yapılacak sayı adedi, tahminSayisi değişkeni ile tanımlandı.
# sonra aynı şekilde globalde yani while döngüsü dışında b değişkeni tanımlandı. bu b değişkeni globalde while
# döngüsünün dışında tanımlanmasının sebebi, while döngüsünün bizden her tahmin istemesi durumda b değişkenin
# değişmesini enegllemek. sonra b değişkeni import ettiğimiz modülün sınıfı olan random hemen yanına da randint
# ve (1,15) ile de aralığı yazılarak b değişkeni tanımlandı.random modülün sınıfından, randint ise çalıştıracağımız
# fonksiyondur. sonra kaçıncı tahminde doğru tahmini yaptığımızı belirlemek için sayac isimli bir değişken tanımladık.
# while döngüsü tahminSayısı sıfırdan büyük olana dek bu döngü çalışsın. yani tahmin sayımız  bitene kadar demek yani.
# sonra tahminSayisi her döngünün başında 1 azaltılıyor böylelikle tahnim hakkı biti ise döngüyü sonlandırmamıza
# yarıyor. sayac ise her döngüde 1 artırılarak kaçıncı tahminde doğru bildiğimizi bulmaya yarıyor. daha sonra
# kullanıcıdan a değişkeni ile bir sayı tahmin etmesini istiyoruz. ve bunu input ile alıyoruz ve int ile integere
#  çeviriyoruz.
# daha sonra if bloğu çalışıyor. eğer tahmin ettiğimiz sayı ile random modülü ile elde ettiğimiz sayı aynı ise
# print fonksiyonu kullanılarak f string metodu ile ekrana kaçıncı tahminde doğru bildiğimiz bastırılıp break
# ifadesi ile kod tekrar döngüye girmesin diye kırılıp sonlanır.
# eğer if bloğundaki şart sağlanmaz ise bir sonraki blok olan elif bloğuna geçilir. tahmin ettiğimiz sayı küçük ise
# ramdom modülünün oluşturduğu sayıdan, devamında yer alan kod da print ile ekrana daha büyük bir sayı giriniz basılır.
# eğer bu şart da sağlanmaz ise else bloğunda son şart olan tahmin ettiğimiz sayı büyük olma koşulu şartı aranır ve
# devamında print ile ekrana daha küçük bir sayı giriniz basılır. böylelikle döngünün ilk kısmı biter.
# döngünün 2. kısmında if bloğu ile eğer tahmin sayısı sıfıra eşit oluyor ise devamında yer alan kod ile print ile
# ekrana tahmin hakkınız bitmiştir ifadesi bastırılır sonra print ifadesi ile de random modülü ile tutulan sayı kerana bastırılır
# ve break ifadesi ile döngü tekrar başlamamsı için burada kırılır.

# ****************************************************************************************************************

import random
can=int(input("kaç hak kullanmak istersiniz:")) # burada can saıyısı kullanıcından alınıyor
tahminSayısı=can # burada ise kullanıcıdan alınan can tahminSayısı olarak belirlenip aşağıda ki while döngüsünde döngüye giriyor.
b=random.randint(1,5)
sayac=0
puan=100 # burada kullnıcıya yaptığı doğru tahmin için puan vermek amacı ile tanımlandı.

while tahminSayısı>0:
    tahminSayısı -= 1
    sayac+=1
    puan1=(puan)-((100/can)*(sayac-1)) #burada sayac-1 yazılmasının sebebi sayıyı bilidği turda ki 20 puan düşülmesini
    # önlemektir aksi taktirde bildiği turda da puan düşer ve yanlış hesaplama yapar. 100/can yapılmasının sebebi ise
    # bilemediği her tahmin için 100 puan üzerinden kaç puan düşeceğini hesaplamak için.
    a = int(input("1 ile 5 arasında bir sayı tahmin edin:"))
    if (b==a):
        print(f"tebrikler {sayac}. tahminde bildiniz. Toplam puanınız {puan1} dır")
        break
    elif(b>a):
        print("Daha büyük sayı girniz.")
    else:
        print("Daha küçük bir sayı giriniz.")

    if (tahminSayısı==0):
        print("tahmin hakkınız bitti.")
        print("tutulan sayı:",b)
        break




