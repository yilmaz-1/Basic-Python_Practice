print("*** FAKTÖRİYEL HESAPLAMA PROGRAMI ***")
print("Eğer Çıkmak İstiyorsanız 'q' ya Basınız.")


while True:
    sayı =input("Sayı:")
    if (sayı=="q"):
        print("Programdan Çıkış Yapılıyor..")
        break
    else:
        sayı=int(sayı)
        faktöriyel = 1
    for i in range(2,sayı+1):
        print("Faktöriyel",faktöriyel,"i:",i)
        faktöriyel *= i
    print("Faktöriyel",faktöriyel)

# *** FAKTÖRİYEL HESAPLAMA PROGRAMI ***
# Eğer Çıkmak İstiyorsanız 'q' ya Basınız.
# Sayı:5
# Faktöriyel 1 i: 2
# Faktöriyel 2 i: 3
# Faktöriyel 6 i: 4
# Faktöriyel 24 i: 5
# Faktöriyel 120
# Sayı:

# print ile fonksiyonun adı ve bir sonraki print ile de çıkmak için q ya basınız ifadesi ekrana basılıyor.
# while True ile bu program yazıldı. çünkü döngü doğru olduğu her duruda tekrardan başlamasını istiyoruz.
# while True altında kullanıcıdan hesaplamak istediğimiz sayıyı input foksiyonu ile alıyoruz.
# daha sonra if bloğu içinde istenene koşul sağlandığı taktirde print fonksiyonu devreye giriyor ve break ile döngü sonlanıyor.
# aksi durumda else bloğunda yer alan koşul devreye giriyor ve sayı int fonksiyonu ile integere dönüştürülüyor.
#
