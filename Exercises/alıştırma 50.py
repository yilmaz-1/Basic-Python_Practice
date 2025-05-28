# aşağıda yazdığımız programda amacımız bir ekran açıp o ekranda tıkladığımız yerde rastgele seçilmiş ölçüler de bir
# yıldız çizilmesini sağlamak


import turtle  # burada turtle modülü progama dahil edildi.
import random  # burada programa random modülünü dahil ettik. bu modülü dahil etmemizin asıl nedeni ise program

# içerisinde rastgele seçim yapmayı sağlamak istememiz.

turtle.bgcolor("black")  # zemin rengi siyah yapıldı.

turtle.pencolor("white")  # kalem rengi beyaz olsun yapıldı. yani çizgi rengi.


def yildizciz(x, y):  # burada yildizciz isminde 2 argümanlı bir adet fonskiyon tanımlandı.

    boyut = random.randint(2, 11)  # burada bir adet boyut isminde bir değişken tanımladık. bu değişkene atanacak değeri
    # ise random modülünün randint fonskiyonu ile 2 ile 11 arasından rastgele seçilsin istedik. böyle bir değişken
    # tanımlamamızın nedeni ise: çizdireceğimiz yıldızın boyutunu bu değişken kullanarak belirlemek.

    turtle.penup()  # kalemi kaldı.

    turtle.goto(x, y)  # x y noktasına git.

    turtle.pendown()  # kalemi indir.

    turtle.fillcolor("gray")  # çizeceğimiz yıldızın içinin renginin gri olması istendi.

    turtle.begin_fill()  # içinin renginin doldurama ya başlaması istendi

    for i in range(5):  # burada bir adet for döngüsü tanımlandı. bu döngü range gonskiyonu ile bu döngü
        # 5 defa dönmesi istendi.

        turtle.fd(
            boyut)  # random.randint ile elde ettiğimiz değer boyuta atandıktan sonra o boyut birim kadar ileri git

        """
        => aşağıda ki kodu kullanırsak random modülünü kaldırıp ve turtle.fd(boyut) ifadesini silmemiz gerekli. çünkü 
        zaten biz yıldızın boyutunu kendimiz 10 diyerel belirlemiş oluyoruz.

        turtle.fd(10)  # 10 birim ileri git. burada aslında şunu diyor: 10 birim ileri git derken yıldızın boyutunu
        # söylemiş oluyor. 10 birimlik yıldız çiz diyor.

        """
        turtle.right(120)  # 120 derece sağa dön

        turtle.fd(boyut)  # boyut kadar ileri git.

        """
        turtle.fd(10)  # 10 birim ileri git. burada aslında şunu diyor: 10 birim ileri git derken yıldızın boyutunu
        # söylemiş oluyor. 10 birimlik yıldız çiz diyor.
        """
        turtle.left(48)  # 48 derece sola dön

    turtle.end_fill()  # açtığımız doldurmayı kapat.


wn = turtle.Screen()  # yukarıda tanımlanan fonskiyonun gösterileceği bir pencere aç.

turtle.onscreenclick(yildizciz)  # yukarı da tanımlı olan fonksiyon ekrana tıklama fonksiyonu olan onscreenclick
# fonksiyonu içerisinde çağrılıyor. fonksiyon çift argümanlı olmasına rağmen argümansız çağrılmasının nedeni, erkanda
# bir yere click yapılınca bize x ve y gibi iki nokta vereceği için sıkıntı 2 argümanı almış oluyoruz.

wn.mainloop()  # açılan penecere kullanıcı kapatmadan kaptaılmasın otomatik.
