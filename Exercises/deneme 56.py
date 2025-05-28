isim=input("isim:") # isim değişkeni input fonksiyonu ile kullanıcıdan alınıyor.
yas=int(input("yaş:")) # yas değişken input fonksiyonu ile kullanıcıdan alınıyor ve int fonksiyonu ile veri tipi dönüşümü yapılıyor.
egitim=input("eğitim:") # eğitim değişkeni kullanıcıdan input fonksiyonu ile alınıyor.

if (yas >=18 and (egitim=="lise" or egitim == "üniversite")):
    print("ehliyet alabilirsiniz")
elif (yas<18 or (egitim!="lise" or egitim!="üniversite")):
    print("ehliyet alamazsınız")
else:
    print("geçersiz giriş")

# çıktı
#isim:mehmet
# yaş:32
# eğitim:üniversite
# ehliyet alabilirsiniz

# *************************************************************

while True: # döngü oluşturulmuş.
    isim=input("isim:")
    yas=int(input("yaş:"))
    egitim=input("eğitim:")
    if (yas >=18 and (egitim=="lise" or egitim == "üniversite")):
        print("ehliyet alabilirsiniz")
    elif (yas<18 or (egitim!="lise" or egitim!="üniversite")):
        print("ehliyet alamazsınız")

# çıktı:
# isim:mehmet
# yaş:32
# eğitim:lise
# ehliyet alabilirsiniz
# isim:

# **************************************************************************************

def ehliyetBilgi(isim,yas,egitim): # ehliyetBilgi isminde üç argümanlı bir fonksiyon tanımlanıyor.
    if (yas >=18 and (egitim=="lise" or egitim == "üniversite")): # koşul oluşturuluyor.
        print("ehliyet alabilirsiniz") # koşul sağlanırsa ekrana basılıyor.
    elif (yas<18 or (egitim!="lise" or egitim!="üniversite")):
        print("ehliyet alamazsınız")
    return # return ile fonksiyon döndürülüyor.


while True: # döngü oluşturuluyor.
    isim=input("isim:") # isim değişkeni input fonksiyonu ile kullanıcıdan alınıyor.
    yas=int(input("yaş:")) # yas değişken input fonksiyonu ile kullanıcıdan alınıyor ve int fonksiyonu ile veri tipi dönüşümü yapılıyor.
    egitim=input("eğitim:") # eğitim değişkeni kullanıcıdan input fonksiyonu ile alınıyor.
    print("ehliyet durumu") # ekrana basılıyor.
    ehliyetBilgi(isim, yas, egitim) # burada fonksiyon döngü içinde çağrılıyor. buradan gelen sonuç da fonksiyonda nasıl tanımlandı ise ona göre ekrana baslıyor.

# çıktı:
# isim:mehmet
# yaş:32
# eğitim:üniversite
# ehliyet durumu
# ehliyet alabilirsiniz
# isim:


