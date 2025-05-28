print("""
************************************
Geometrik Şekil Tahmin Etme Programı
************************************

Şekil Bilgileri

1. Kare
2. Dikdörtgen
3. Üçgen

""")

v1=input("Hangi Şekli Bulmaya Çalışıyorsunuz:")

if (v1=="2"):
    print("Seçtiğiniz Şekil Dörtgendir.")
    k1=int(input("Birinci Kenarın Ölçüsünü Giriniz:"))
    k2=int(input("İkinci Kenarın Ölçüsünü Giriniz:"))
    k3=int(input("Üçüncü Kenarın Ölçüsünü Giriniz:"))
    k4=int(input("Dördüncü Kenarın Ölçüsünü Giriniz:"))
    if (k1==k2==k3==k4 ): # veya (and k1==k3 and k1==k4) parantez içerisindeki kodu yazarak da aynı şeyi elde edebiliriz
        print("Şekil Karedir.")
    elif ((k1==k2 and k3==k4) or ((k1==k3 and k2==k4))):
        print("Şekil Dikdörtgendir.")
    else:
        print("Şekil Sıradan Dörtgendir")
elif (v1=="1"):
    print("Seçtiğiniz Şekil Dörtgendir.")
    m1=int(input("Birinci Kenarın Ölçüsünü Giriniz:"))
    m2=int(input("İkinci Kenarın Ölçüsünü Giriniz:"))
    m3=int(input("Üçüncü Kenarın Ölçüsünü Giriniz:"))
    m4=int(input("Dördüncü Kenarın Ölçüsünü Giriniz:"))
    if (m1==m2 and m1==m3 and m1==m4):
        print("Şekil Karedir")
    elif ((m1==m2 and m3==m4) or (m1==m3 and m2==m4)):
        print("Şekil Dikdörtgendir.")
    else:
        print("Şekil Sıradan Dörtgendir.")
elif (v1=="3"):
    print("Seçtiğiniz Şekil Üçgendir.")
    f1=int(input("Birinci Kenarın Ölçüsünü Giriniz:"))
    f2=int(input("İkinci Kenarın Ölçüsünü Giriniz:"))
    f3=int(input("Üçüncü Kenarın Ölçüsünü Giriniz:"))
    if (abs(f1+f2)>f3 and abs(f1+f3)>f2 and abs(f2+f3)>f1):
        print("Bir Üçgendir.")
    elif (f1==f2 and f1==f3): # veya ( f1==f2==f3 ) şeklinde de yazılabilir.
        print("Şekil Eşkenar Üçgendir")
    elif (f1==f2 and f1!=f3) or (f1==f3 and f1!=f2) or (f2==f3 and f2!=f1):
        print("İkiniz Kenar Üçgen")
    else:
        print("Üç Kenarı da Farklı Üçgendir.")
else:
    print("Geçersiz Giriş Yaptınız...")
# çıktı:
# *** Geometrik Şekil Tahmin Etme Programı ***
# " Şekil Bilgileri
#
# 1. Kare
# 2. Dikdörtgen
# 3. Üçgen
#
#
# Hangi Şekli Bulmaya Çalışıyorsunuz:2
# Seçtiğiniz Şekil Dörtgendir.
# Birinci Kenarın Ölçüsünü Giriniz:2
# İkinci Kenarın Ölçüsünü Giriniz:3
# Üçüncü Kenarın Ölçüsünü Giriniz:4
# Dördüncü Kenarın Ölçüsünü Giriniz:5
# Şekil Sıradan Dörtgendir

# print fonksiyonu ile programın adı ekrana bastırılıyor.
# daha sonra print fonksiyonu ile şekil bilgileri ekrana bastırılıyor.
# daha sonra input ile kullanıcıdan v1 değişkenine atanmak üzere daha önce tanımlanan şeklin numrası isteniyor.
# daha sonra tek tek if elif ve else bloklarında şeklin kare, dikdörtgen veya üçgen olma durumları tek tek kontrol
# edilip o blok içinde belirtilen print ifadesi ile ekrana bastırılıyor.
# else bloğunda ise geçersiz işlem yapıldı ise onu ekrana print bastırılıyor.



