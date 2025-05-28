print ("""
********************************************
Girilen Sayılardan Büyük Olanı Bulma Programı
********************************************
""")

a = float(input("Birinci Sayıyı Giriniz: "))
b = float(input("İkinci Sayıyı Giriniz: "))
c = float(input("Üçüncü Sayıyı Giriniz: "))

if ( a > b and a > c):
    print("En Büyük Sayı: ", a)
elif (b > a and b > c):
    print("En Büyük Sayı: ", b)
elif ( c > b and c > a):
    print("En Büyük Sayı: ", c)
else:
    print("Geçersiz Giriş Yaptınız...")

# bu programda kullanıcıdan alınan 3 farklı sayının hangisinin büyük olduğunu bulmamıza yarıyor.
# öncelikle print ile programın adı ekrana basılıyor.
# daha sonra kullanıcıdan a ,b ve c olmak üzere 3 adet sayı alıyoruz input fonksiyonu ile .
# daha sonra bu aldığımız sayıları float fonksiyonu ile float a çeviriyoruz.
# daha sonra if elif ve else kod blokları ile tek tek her sayı için büyük olma durumlarını kontrol ediyoruz.
# hangi blokta bu şart sağlanırsa o bloğun içinde yer alan print ifadesi çalıştırılıp ekrana yazılıyor.
# else bloğunda ise print ile geçersiz işlem yapıldı ise o ekrana yazılıyor.