print("""
***************************************
Beden Kitle Endeksi Hesaplama Programı
***************************************
""")

boy = float(input("Lütfen Boyunuzun Uzunluğunu Giriniz (metre olarak: 1.65 gibi): "))
kilo = float(input("Lütfen Kilonuzu Girinizi (kg): "))
endeks = (kilo / (boy*boy))

if (endeks > 30):
    print("Kilonuz Çok Fazla. Obez Sıfındasınız.")
elif (25 < endeks < 30 ):
    print("Fazla Kilolusunuz")
elif ( 18.5 < endeks < 25):
    print("Normal")
elif (endeks < 18.5):
    print("Zayıf")
else:
    print("Hatalı Giriş Yaptınız...")
# print ile programın adı ekrana bastırılıyor. daha sonra kullanıcıdan boy ve kilo bilgileri input ile isteniyor.
# daha sonra bu bilgiler sırası ile boy ve kilo değişkenlerine atanıyor. ve folat ile veri tipi dönüşümü yapılıyor.
# daha sonra bu alınan bilgiler indeks değişkeni içine atanıyor.
# daha sonra if elif ve else fonksiyonu ile indeks te hesaplanan değer he kod bolğunda karşılaştırılıp  hangi blokta
# sağlanıyor ise o bloğun içinde yer alan print fonksiyonu ile ekrana bastırılıyor.
# daha sonra else fonkisyonu ile geçersiz giriş yapıldı ise o bloğun içinde yer alan print ifadesi ekrana bastırılıyor.