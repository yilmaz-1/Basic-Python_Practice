# aşağıda yazılan program klavyeden basılan tuşalra tepki vererek ekrana da o tepkiyi görmemize yarıyor.
 # programa turtle modülü dahil edildi.

import turtle


turtle.pensize(5)  # kalemin çizdiği çizginin kalınlığı belirlendi.


def ileri():  # argümansız olarak bir adet ileri isimli bir fonksiyon tanımlandı.
    turtle.fd(50)  # 50 birim ileri git.


def geri():  # argümansız olarak bir adet geri isimli bir fonksiyon tanımlandı.
    turtle.backward(50)  # 50 birim geri git.


def sol():  # argümansız olarak bir adet sol isimli bir fonksiyon tanımlandı.
    turtle.left(90)  # 90 derece sola dön


def sag():  # argümansız olarak bir adet sag isimli bir fonksiyon tanımlandı.
    turtle.right(90)  # 90 derece sağa dön


def green():  # argümansız olarak bir adet green isimli bir fonksiyon tanımlandı.
    turtle.pencolor("green")  # kalemin çizdiği çizginin rengi belirlendi.


# şimdi yukarıda tanımladığımız programları parametrelerini vererek tek tek çağıracağız.

wn=turtle.Screen() # yukarıda tanımlanan fonksiyonların gösterileceği bir pencere aç dedik.

turtle.onkeypress(ileri, "Up") # onkeypress fonksiyonun içinde ileri isimli fonskiyon çağrılıyor. eğer klavyeden yukarı
# tuşuna basarsam onkeypress fonskiyonu içerisndeki ileri fonskiyonunu çağır.

turtle.onkeypress(geri, "Down") # onkeypress fonksiyonu içersinde geri isimli fonksiyon çağrılıyor. eğer klavyeden aşağı
# tuşuna basılınca onkeypress fonskiyonu içerisindeki geri isimli fonksiyonu çağır.

turtle.onkeypress(sol, "Left") # onkeypress fonksiyonu içersinde geri isimli fonksiyonu çağırılıyor. eğer klavyeden sol
# yön tuşuna basılınca onkeypress fonskiyonu içerisindeki sol isimli fonskiyon çağrılıyor.

turtle.onkeypress(sag, "Right") # onkeypress fonskiyonu içersindeki sag isimli fonksiyon çağrılıyor. eğer klavyeden sağ
# yön tuşuna basılınca onkeypress fonskiyonu içersindeki sag isimli fonksiyon çağrılıyor.

turtle.onkeypress(green, "g") # onkeypress fonksiyonu içersindeki green isimi fonskiyon çağrılıyor. eğer klavyeden
# g harfine basılınca onkeypress fonskiyonu içerisindeki green isimli fonskiyon çağrılıyor.

turtle.listen() # burada programa diyoruz ki beni dinle ben bir şey yapmadan tuşa basmadan,hiç bir şekilde yularıda
# tanımlanan fonskiyonları çağırma çalıştırma diyoruz. ben önce tuşa basacağım sonrasında
# tanımlı fonskiyonlar çalışaacak.

wn.mainloop() # fonskiyonun gösterildiği pencereyi kullanıcı kapatmadan kapatma. otomatik kapatma.
