import random # burada random modülünü programa dahil ettik. amacımız tombala kartında yer alan numaraları resgele
# program tarafından tahmin ettirip elde etmek.

kartNumaraları=[] # random modülü ile elde ettiğimiz numaraları burada tanımladığımız boş listeye atmak için oluşturudk.

while len(kartNumaraları)<16: # burada bir adet while döngüsü oluşturduk. amacımız bu döngü ile kart numaralını elde
    # etmek. tombala kartında 15 adet numra olduğu için burada dngüyü 15 defa döncek şekilde yani kart numaralının
    # boyundan yani sayısından küçük olduğu sürece dönmesini istedik. böylelikle 15 defa dönecek ve her döngüde bir
    # sayı alacak.
    numara=random.randint(1,91) # her döngüde aldığı sayıları 1 ile 91 arasıdan alacak ve bunu numara değişkenine atacak
    if numara not in kartNumaraları: # her döngüde aldığı sayı tobala kartımızda yer almıyor ise yani kartNumaraları
        # isimli değişkenin içersinde yer almıyor ise
        kartNumaraları.append(numara) # bu numara yı kartNumaraları isimli değişkene atacak.
# neden kart numaraları isimli değişkenin içersinde aynı numaradan olmasını istemedik: çünkü tombala kartında da aynı
# sayı birden fazla yer almadığı için.
kartNumaraları.sort() # burada elde ettiğimiz sayıları küçükten büyüğe doğru sıralama yaptık.

print(f" Tombala Kart Numaralarınız: {kartNumaraları}") # burada elde ettiğimiz sayıları ekrana liste şeklinde bastırdık
sayac=3 # burada bir adet sayac isminde bir değişken oluşturduk. amacımız: sayıları okuyan yani sisteme giren kişi
# kartlarda yer alan sayılaradan farklı bir sayı söyler ise ona 3 hak verip sonun da onun oyundan atmak. yani 0 ile 91
# arasında bir sayı girmesini sağlamak.

while len(kartNumaraları)>0: # burada while ile bir döngü kuruldu. ve bu döngü elde ettiğimiz kartNumraları değişkenin
    # listesinin boyundan büyük olduğu sürece devam etsin istedik. çünkü bu kart boyu kadar (15 adet) sayı okunacak ..
    okunanSayi=int(input(f"Lütfen Bir Sayı Okuyunuz (Giriniz): ")) # kullanıcıdan bir sayı girmesini istiyoruz.

    if okunanSayi>90 or okunanSayi<0: # eğer girilen sayı 90 dan büyük veya 0 dan küçük ise
        sayac -= 1 # hakkından 1 azalt
        if sayac == 0: # eğer sayac sıfır ise
            print("Program Sonlandı") # ekrana yaz.
            quit() # programdan çık
        else: # değilse
            print("Lütfen 1 ile 90 arasında bir rakam giriniz.") # ekrana yaz
        continue # aşağıdaki hiç bir kodu okuma direk başa döne , yani bir dıştaki kod bloğuna
    else: # değilse
        if okunanSayi in kartNumaraları: # eğer okunan sayı kartNumaraları değişkeni içersinde yer alıyor ise
            print(f"{okunanSayi} sayısı tombala kartınız da var.") # ekrana yaz
            kartNumaraları.remove(okunanSayi) # yer alan numrayı listeden, kartNumaraları değişkeninden at...
            print(f"yeni kart numaralarınız: {kartNumaraları}") # ekrana yaz
        else:# değilse
            print(f"{okunanSayi} sayısı kartınızda yer almamaktadır.") # erkana yaz

print("Bildiniz..") # döngü sonlandıktan sonra ekrana yaz...

