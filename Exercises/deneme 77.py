# def square (num): return num ** 2 # bu kullanım ile normal alt alta yazılan klasik kullanım ile aynı şeydir.
#
# numbers = [1,3,5,9]

#print(map(square,numbers)) # bu şekilde yapıldığı zaman çıktıyı bize adres olarak veriyor.
#çıktı :
#<map object at 0x000001E9A7F83A08>  bellek üzerinde böle bir adres olarak veriyor.


#print(list((map(square,numbers)))) # bu şekilde yapıldığı zaman ise çıktıyı bize liste halinde veriyor.
# çıktı:
# [1, 9, 25, 81]

# for item in map(square,numbers):
#     print(item)
# çıktı:
# 1
# 9
# 25
# 81


# def square (num): return num ** 2
# numbers = [1,3,5,9]
# result = list(map(lambda num: num ** 2, numbers)) # burada square methodu yok. burada bu square in yaptığı işlemi isimsiz yani (lambda num: num ** 2, numbers) foksiyonu ile yaptırmış olduk.
# print(result)
# # çıktı:
# # [1, 9, 25, 81]





# ***********************************************************************
#  map () fonksiyonu,bir dizin,n elemanlarına uygulancak işlemlerde kullnılır.

# liste =[2,3,4,5,6] # herhangi bir liste tanımladık.
# yeni_liste=list(map(lambda x:x**2,liste)) # yeni listeyi lsite üzerinde yapılacak olan işlmei tanımladık. burada map () foksiyonu kullanık. çümnkü listenin her elemanı için bu işlemin uygulanmasını istiyoruz. bundan dolayı map () fonskiyonu kullandık.
# print(yeni_liste) # yeni liste ekrana basıldı.
# # çıktı:
# # [4, 9, 16, 25, 36]


# yukarıda ki kod ile aşağıda ki kod aynı işlevi yapmakta . farkı şu: birisi map fonksiyonu kullanıldı ve kod daha derli toplu oldu. aşağıda ki kodda ise for döngüsü ile biraz daha uzun yazıldı. ama sonuçta her ikiside aynı sonucu veriyor. map () fonksiyonu uzun ve önemli kodlamalarda çok praktiklik sağlar.


# liste1=[2,3,4,5,6] # burada, elemanıları üzerinde işlme yapacağımız bir liste tanımlandı.
# yeni_liste1 =[] # liste1 elemanları üzerinde yaptığımız işlemle sonucu elemanları atacağımız boş liste.
# for i in liste1: # for döngüsü ile bu liste1 elemanları üzerinde tek tek elemanaşrı geziyoruz .
#     a = i**2 # burada for döngüsü ile elde ettiğiimiz elemanlara her döngüde uygualancak işlem tanımlandı.
#     yeni_liste1.append(a) # burada her döngüde liste1 elemanı üzerinde işlem yapıldıktan sonra o eleman yeni listeye atılıyor.
# print(yeni_liste1) # yeni liste ekrana bastırılıyor.
# ****************************************************************************


# def ikikat (x): # burada x değerinin 2 katını alan bir fonksiyon tanımlandı.
#     return x*2
#
# def yari(x): # burada x değerinin yarısını alan bir foksiyon tanımlandı.
#     return x/2
#
# fonk=[ikikat,yari] # burası önemli. burada foksiyon dizisi tanımlandı. yani yukarıda tanımladığımız fonksiyonlar bir dizi içerisinde tanımlandı.
#
# for i in range(5): # for döngüsü ile range fonksiyonu kullanılarak 0 dan 5 kadar olan elemanlar tek tek alındı.
#     deger = list(map(lambda x: x(i),fonk)) # alınan bu elemanlara map () fonskiyonu ile fonk fonksiyon dizisi içinde yer alan fonksiyondaki işlemler uygulandı. x in değeri for döngüsü ile elde edilen i değeri alındı. sonra bu i değerine fonk fonksiyon dizisi içinde yer alan fonksiyonlar uygulandı.
#     print(deger) # deger değişkeni ekrana basıldı
# # çıktı:
# # [0, 0.0] i nin değeri sıfır alındı. sonra bu i değeri x e atıldı. ilk eleman  x in 2 katı, ikinci eleman ise x in 2 ye bölünmesinin sonucu.
# # [2, 0.5] i nin değeri 1 alındı. sonra bu i değeri x e atıldı. ilk eleman  x in 2 katı, ikinci eleman ise x in 2 ye bölünmesinin sonucu.
# # [4, 1.0]
# # [6, 1.5]
# # [8, 2.0]

# burada map () bir listeye birden fazla fonksiyonun uygulanmasını gördük. dizi içerisindeki her bir elemana ulaşıp her bir elemaı bir foksiyon üzerinden geçirdik.

# **********************************************************************************



