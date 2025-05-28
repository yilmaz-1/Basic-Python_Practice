import turtle

def renkliKare_ciz(renk,genislik):
    turtle.home()
    turtle.pencolor(renk)
    for i in range(4):
        turtle.fd(genislik)
        turtle.left(90)

# yukarıda tanımlanan programın tanımlanması burada bitiyor. bundan sonra yazılan her şey tanımlanan programndan
# bağımsız çalışacaktır.

krenk=input("Lütfen Renk Giriniz: ")
kgenislik=int(input("Lütfen Genişlik Bilgisini Giriniz: "))

wn=turtle.Screen() # programa diyoruz ki bu yukarıda tanımladığımız renkliKare_ciz fonksiyonunu çağırmadan önce bir
# grafik penceresi aç sonra aşağıdaki fonksiyon çağırma işlmelerini yap.

# renkliKare_ciz(renk="yellow",genislik=50) # yukarıda tanımlanan fonksiyon bu şekilde de çağrılabilir. fakat burada
# önemli olan şey şu: kullanıcıdan aldığınızrenk ve genişlik bilgisini bu fonskiyon içersinde kullanmamaış oluruz.
#kullanıcıdan alınan bilgileri kullanarak bu fonskiyonu çağırmak isityor isek aşağıdaki gibi fonksiyonu çağırmamız lazım

renkliKare_ciz(krenk,kgenislik) # yukarıda 2 parametreli tanımlanan fonksiyon bizim kullanıcadn aldığımız değerler
# gönderilerek çağrıldı. krenk değişkeni renk parametresi yerine geçti, kgenislik değişkeni ise genislik parametresi
# yerine geçti.

wn.mainloop() # kullanıcı açılan pencereyi kapatmadan otomatik olarak kapanmasın diyoruz.