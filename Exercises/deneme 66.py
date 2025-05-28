for i in range(1,15,3): # i değişkenini range(1,15,3) aralığında belirtilen elemanlar üzerinde gez. 1 den 15 e kadar 3 er 3 er gez.
    print(i) # range(1,15,3) bu aralıkta her i elemanını ekrana bastır

print(list(range(1,15,3))) # range(1,15,3) fonksiyonunda aralıkları belirtilen , 1 den 15 e kadar 3 er 3 er atlayarak liste yapıp ekrana yazdırıyor.

#çıktı
# 1
# 4
# 7
# 10
# 13
# [1, 4, 7, 10, 13]

# ****************************************

index=0
greeting="Hello There"

for letter in greeting:
    print(f"index: {index} letter: {letter}")
    index+=1

#çıktı:
# index: 0 letter: H
# index: 1 letter: e
# index: 2 letter: l
# index: 3 letter: l
# index: 4 letter: o
# index: 5 letter:
# index: 6 letter: T
# index: 7 letter: h
# index: 8 letter: e
# index: 9 letter: r
# index: 10 letter: e

# greeting değişkenini tanımladık. amaç bu değişken üzerinde letter değişkeni gezerek ekrana bu greeting değişkenin
# karakterlerini ve hangi indeks te olduğu yazdırmak. bu yüzden index sıfırdan başlatıldı.
#cod çalıştırıldığında for döngüsü ile greetign üzerinde letter değişkeni gezerek devamında print fonksiyonu ile
# ekrana o karakterin önce index ini sonra da karakteri basıyor. index her döngünün sonunda 1 artırılarak basılacak
# karakter kalmayana kadar devam ediyor.

# ***************************************************

greeting="hello"
for item in enumerate(greeting):
    print(item)

# çıktı:
# (0, 'h')
# (1, 'e')
# (2, 'l')
# (3, 'l')
# (4, 'o')

# bir önceki cod da yaptığımız print(f"index: {index} letter: {letter} ve index değişkenini hiç global de tanımlamadan
# enumerate() fonksiyonu ile bir string in karakterlerini ekrana kaçıncı index olduğu ile birlikte bastırabiliriz.
# çıktıda görüldüğü üzere bize liste şeklinde verdi.

# *******************************************************

greeting="hello"
for index, item in enumerate(greeting): # index print fonksiyonu içindeki index için, item ise print fonksiyonu içindeki
    #letter için yazıldı.
    print(f"index: {index} letter: {item}")

# çıktı:
# index: 0 letter: h
# index: 1 letter: e
# index: 2 letter: l
# index: 3 letter: l
# index: 4 letter: o

# enumerate() fonksiyonu kullanarak greetin içerisinde tanımlanan hello string inin krakterleri liste olmadan
# direk hengi indekse hangi krakter gelecek şekilde ekrana bastırıldı.

# ********************************************************

liste1=[1,2,3,4,5]
liste2=["a","b","c","d","e"]

print(list(zip(liste1,liste2)))

# # çıktı:
# # [(1, 'a'), (2, 'b'), (3, 'c'), (4, 'd'), (5, 'e')]

# burada iki liste birleşitirildi. birinci listedeki elemanlar 2. listedeki elemanlar ile eşleştrildi ve
# bu liste list fonkisyonu ile yeni bir lister oluşturularak 1,a ya 2,b ye 3,c ye gelecek şekilde
# indeks numralarına göre yerleştirildi. kaç liste olursa olsun yazılabilir.

# *************************************************************

liste1=[1,2,3,4,5]
liste2=["a","b","c","d","e"]

for item in zip(liste1,liste2):
    print(item)

# çıktı:
# (1, 'a')
# (2, 'b')
# (3, 'c')
# (4, 'd')
# (5, 'e')

# *********************************************************************

liste1=[1,2,3,4,5]
liste2=["a","b","c","d","e"]

for a,b in zip(liste1,liste2):
    print(a)

# çıktı:
# 1
# 2
# 3
# 4
# 5

# burada item yerine a,b gibi iki değişken yazıldı burada a=zip içindeki liste1 ve b=zip içineki liste2 yerine
# basılıyor. böylelikle ekrana print(a) dediğiniz zaman sadece a değeri için liste 1 in elemanları basıldı.
# print(b) yazılsa idi ekrana sadece liste2 elemanları basılacaktı. print(a,b) yazılsa idi ekrana

# çıktı:
# 1 a
# 2 b
# 3 c
# 4 d
# 5 e
# liste içerisinden çıkmış halde basılır karakterler.













