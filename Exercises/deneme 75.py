# def ekran(): # burada fonksiyonu tanımladık.
#     a=10 # değişkeni tanımladık.
#     return a #  burada ise a değerini sonra başka yerde kullnmak üzere return foknsiiyonu ile hafıza alıyoruz. yani döndürüyoruz.
# print("a değişkeninin değeri:",ekran()) # ekrana basıyoruz fonksiyonu

# *******************************************************

# def geriSayma(n): # burada fonksiyon oluşturuldu.
#     print(n) # fonksiyon içine verdiğimiz değer ekrana bastırıldı.
#     if n>-7: # burada koşul ifadesi oluşturuldu.
#         return geriSayma(n-1)# geriSayma fonksyonu çağrıldığı yere dönmesi için return ile bağlandı.
# geriSayma(8)

# *********************************************************

# def islem(a,b,c=0,d=0):
#     return a*b+c-d
# print(islem(10,4,2,1))

# *********************************************************

# def kare(x):# fonksiyon tanımlandı.
#     a = x*x # x**2 de karesi demektir.
#     print(a) # a değeri ekrana basıldı
#     return a # return fonksiyonu ile hafızaya alındı. kare fonksiyonu ne zaman çağrılsa a değerini bu fonksiyon içersinde döndürecektir.
# kare(3)
# kare(4)
#  print fonkisyonu da return ile aynı işi yapıoyr gibi görünebilir . evet kısmne öle ama biz her zaman çıktıyı ekrana basmak zorunda değiliz veya basmamız gerekmeyebilir. yani fonksiyon çalşısın bir değer üretsin ve ekrana basmasın veya ekrana bsacak bir durum yok ortam yok. o zaman üretilen değer sonra çağrılmak üzrere veya başka bir yerde kullanılmak üzerehafıza alınır. biz çağırdığımız zaman artık nereye çağırırsak hangi programam oraya geri döndürür.

# *************************************************************

# def douple(sayi):
#     return sayi*2
# print(douple(5))

# *************************************************************

# def toplama(a,b,c): # fonksiyon tanımlandı
#     x=a+b+c # 3 değişkenin toplamı bir x değişkenine atandı.
#     print(x)
#     return x # x değeri return ile döndürülüyor.
# toplama(1,2,3)

# *************************************************************

# def double(a):# fonksiyon tanımlandı.
#     return a*2# return ile fonksiyon içine gönderilen değer döndürüldü.
# def kare(b):
#     return b*b
# def toplam(c):
#     return c+3
#
# print(toplam(kare(double(2)))) # burada önce double(2) için bir değer döndürülüyor. daha sonra double dan return ile dönen değer kare fonkiisyonuna gönderiliyor. oradan çıkan sonuç return ile döndürülüp toplam fonskiyonuna gönderiliyor. buradan return ile döndürlen sonuç ekrana bastırılıyor.

# *************************************************************

# def cember(yariCap): # fonksiyon tanımlandı.
#     alan=3.14*yariCap**2 # alan için yapılacak işlem tanımlandı
#     cevre=2*3.14*yariCap # çevre için yapılacak işlem tanımlandı.
#     return alan,cevre # burada alan ve çever ssonuçları dödrülmek üzere return ile hafızaya alındı.
#
# x,y = cember(5) # burada cmber () fonksiyonuna 5 değeri gönderildi. yarıCap=5 oldu. yarıCap yerine 5 yazıldığı zaman x alan için y de çevere için atanmış değişkenler oluyor.
# print(x) # burada x ile alan sonucunu ekrana bastırıyoruz.
# print(y) # burada y ile cevre sonucunu ekrana bastırmış oluyoruz.

# ***************************************************************

# ax**2 + bx + c denklem

# def kokBul(a,b,c):# burada fonskiyon tanımlandı.
#     delta = (b**2 - 4*a*c) # kök bulmak için foksiyon içinde delta tanımlandı.
#     if (delta<0): # koşul yazıldı. delta küçük ise diye.
#         print("Reel Kök Bulunamadı") # koşul sağlanırsa ekrana basılacak olan iifade yazıldı.
#         return # bu return direk fonksiyonu bitirmek için kullanıldı. koşul sağlandığı için
#
#     x1 = (-b - delta**0.5)/2*a # burada denkelmin birinci kökü hesaplandı.
#     x2 = (-b + delta**0.5)/2*a # burada denkelmein ikinci kökü hesaplandı.
#     return (x1,x2) # burada ise bulduğumuz değerleri direk dış dünyada kullankam üzere döndürme yapıyoruz. yani hafıza alıyoruz.
#
# a = int(input("a:")) # bu aşağıda yazılanlar fonksiyonun dışında. a b ve c değerleri kullanıcıdan alındı.
# b = int(input("b:"))
# c = int(input("c:"))
# sonuc = kokBul(a,b,c) # fonksiyon çağrıldı. ve sonuc değişkenine atandı.
# print(sonuc) # ekrana print ile sonuç basıldı.

# *******************************************************************************








