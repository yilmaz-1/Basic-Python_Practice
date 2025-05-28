# def yazdir(kelime,adet): # kelime ve adet değişkenlerini içeren bir foksiyondur.
#     print(kelime*adet) # belirtilen kelime belirtilen adet kadar ekrana yazdırılacaktır.
#
# yazdir("mehmet",3)
# yazdir("mehmet\n", 3)
# # çıktı
# # mehmetmehmetmehmet
# # çıktı
# # mehmet
# # mehmet
# # mehmet
#
# ********************************

# def liste(*args): # burada bir fonksiyon tanımladık. tek yıldız ile bu fonksiyan istediğimiz kadar parametre gönderebiliyoruz.
#     liste=[] # bu şekilde bir boş bir liste oluşturduk
#     for i in args: # for döngüsü ile args ın elemanları üzerinde i değeri geziniyor.
#         liste.append(i) # sonra bu i değeleri append metodu ile i değerleri boş listeye atılıyor.
#     print(liste) # döngü bittikten sonra bu liste print ile ekrana basılıyor.
#     return liste #return ile bu liste başa döndürülğyor yani hafıza aılnıyor da denebilir.
#
# liste(1,2,3,4,5,6,"mehmet"," ")
# # çıktı:
# # [1, 2, 3, 4, 5, 6, 'mehmet', ' ']

# ***************************************

# def asalSayiBulma (a,b): # burada kullanıcıdan aldığımız 2 saayı arasındaki asal sayıları bulmaya yaran program yazıldı.
#     for i in range(a,b+1):# for döngüsü ile range fonksiyonu kullanılarak kullanıcıdan aldığımız 2 sayı arasında i değerleri elde edioruz.
#        if (i>1):# eğer i büyük 1 den ise blok çalışcak
#            for j in range(2,i): # j gibi başka bir değişekn için range fonksiyonu ile 2 den başlayıp i değerine kadar for döngüsü yapılıyor.
#                if (i % j ==0): # bu koşul sağlanırsa asal değildir . break ile döngü kırılıyor.
#                    break
#            else:
#                liste.append(i)
#     print(liste)
#
# a=int(input("Sayı1:"))
# b=int(input("Sayı2:"))
# liste = []
#
# asalSayiBulma(a,b)
# # çıktı
# # [5, 7]

# ****************************************

# def asalSayıBulma(a,b):
#     for i in range(a,b+1):
#         if (i>1):
#             for j in range(2,i):
#                 if (i % j ==0):
#                     break
#             else:
#                 liste.append(i)
#     print(liste)
#
# a=int(input("Sayı1:"))
# b=int(input("Sayı2:"))
# liste = []
#
# asalSayıBulma(a,b)
# # çıktı:
# # Sayı1:1
# # Sayı2:100
# # [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]

# ***************************************************************************

def tamBolenBulma(a): # burada yazılan fonksiyon kullanıcıdan istenen bir sayının tam bölenlerini bulmaya yarar.
    tamBolenler =[] # bulduğumuz tam bölenleri bu boş listeye atıyoruz.
    for i in range(2,a+1): # for döngüsü ile 2 den başlayarak kullanıcıdan aldığımız sayının 1 fazlasına kadar range fonksiiyonu kullanılarak döngü oluşturuldu.
        if ( a % i ==0):# eğer bu döngü içinde elde ettiğimiz i değerlerinden herhangi biri a yı tam bölerse koşulu oluşturuldu.
            tamBolenler.append(i) # burada bu koşul çalşımsası durumda True dönmesi durumunda bulunan i değerleri boş listeye atılıyor.
    print(tamBolenler)# liste ekrana bastırılıyor.
    return tamBolenler
a= int(input("sayı:"))

tamBolenBulma(a)

# çıktı:
# sayı:120
# [2, 3, 4, 5, 6, 8, 10, 12, 15, 20, 24, 30, 40, 60, 120]