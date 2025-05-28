# Burada TC kimlik numrası foramtını kontrol eden bir program yazıldı.
# TC kimlik Numrasında ilk 11 ramkamın toplamının birler basamağı TC numrasının 11. rakamına eşit olur.

tcNo= input("Lütfen TC Kimlik Numaranızı Yazınız: ") # burada kullanıcından kimlik numrası girmesini istiyoruz.
print("                                         ")
ilkOnrakam= tcNo[:10] # Girilen kimlik numrasının ilk on rakamı str formatında alınıyor.
print(f"Girilen TC Kimlik Numarasının İlk On Rakamı: {ilkOnrakam}")
print("                                         ")
sonrakam= tcNo[10] # burada girilne tc numrasının son rakamı alınıyor.
print(f"Girilen TC Kimlik Numrasının Sonrakamı: {sonrakam}")
print("                                         ")
toplam= 0 # burada ise toplam isminde bir değişken tanımladık. çünkü kodun ilerleyen ksıımlarında döngü kurularak
# toplam elde edilmeye çalışılacak . toplam değişkeni lazım olacak.

for rakam in ilkOnrakam: # burada bir döngü kuruldu. her döngüde TC numrasının ilk on rakamı içersinden bir rakam,
    # rakam değişkeni olarak alınırak,
    toplam= toplam+int(rakam) # toplam değişkeni ile toplanıyor.

print(f"Girilen TC Kimlik Numrasının İlk On Rakamının Toplamı: {toplam}")
print("                                         ")


toplam=str(toplam) # burada toplam değişkeni str ye çevrildi. çnkü ileride tc kimlik no nun son rakmı ile kıyaslama
# yapılacağı için str fomatında olması lazım.

print(f"Girilen TC Kimlik Numarasın Biler Basmağındaki Sayı: {toplam[-1]}")
print("                                         ")
if toplam[-1]==sonrakam: # eğer ilk on rakımın toplamının birler basmapındaki rakam ( biler basamağındaki sayıya
    # [-1] kodu ile eriştik ) Girilen TC nosunun son rakamına eşit ies
    print("Geçerli Formatta kimlik Numarası Girdiniz...") # ekrana yaz.
else: # değilse
    print("Geçersiz Formatta Kimlik Numarası Girdiniz...") # ekrana yaz
