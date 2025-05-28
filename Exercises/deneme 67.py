for x in range(10): # bu kod da çıktı ekrana alta alta basar
    print(x)

# çıktı:
# 0
# 1
# 2
# 3
# 4
# 5
# 6
# 7
# 8
# 9

# *********************************************************

numbers =[x for x in range(10)] # bu kod da çıktı bir liste içinde ekrana basar.
print(numbers)

# çıktı:
#  [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# ***************************************************

numbers=[]
for x in range(10): # bu kod da çıktı bir liste içinde ekrana basar.
    numbers.append(x)# append komutu ile elde ettiğimiz x leri boş olan numbers listesine atılır.
print(numbers)
# çıktı:
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# ***********************************************

for x in range(10): # bu kod ile
    print(x**2)
# çıktı:
# 0
# 1
# 4
# 9
# 16
# 25
# 36
# 49
# 64
# 81

# *************************************************

numbers=[x**2 for x in range(10)] # bu kod bir önceki kod ile aynı şeyi anlatmaktadır.
print(numbers)
#çıktı:
# [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

# ilk kodda for döngüsü ile yazılmışken. ikinci kod list comprehension
# ile yazılmıştır.

# ***************************************************

numbers= [x*x for x in range(10) if x%3==0]
print(numbers)

# çıktı:
#[0, 9, 36, 81]

#  range() fonksiyonu ile 0 10 aralığında olan sayıları alıyor for döngüsü ile
# bu sayılardan if bloğunda belirtilen şart ile 3 ile böümünden kalan 0 olanları
# kendisi ile çarpıp print fonksiyonu ile ekrana bastırıyor liste içerisinde.
# list comprehension yönetemi ile

# ****************************************************

myString="hello"
myList=[]

for letter in myString:
    myList.append(letter)
print(myList)

 # çıktı:
 # ['h', 'e', 'l', 'l', 'o']

# ****************************************************

myString="hello"

myList=[letter  for letter in myString]
print(myList)

# # çıktı:
# # ['h', 'e', 'l', 'l', 'o']

# *******************************************************

years=[1983,1999,2008,1956,1986]

ages=[2020- year for year in years] # for döngüsü ile years listesi üzerinde gezinerek elde ettiğimiz year değelerini her bir döngüde 2020 yılından çıkarıyoruz.
print(ages)

# çıktı:
#[37, 21, 12, 64, 34]

# ********************************************************

years=[1983,1999,2008,1956,1986]
ages=[]
for x in years:
    y=2020-x
    ages.append(y)
print(ages)
# # çıktı:
# # [37, 21, 12, 64, 34]

# ********************************************************

sonuc=[x if x%2==0 else "tek" for x in range(1,10)]
print(sonuc)

# bu kod da list comprehensiın yöntemi ile x değeri range(1,10) fonksiyonu ile
# belirtilen aralıkta alındı. if şartı ile sayı çift ise direk o sayı liste içine
# yazıldı değilse else kısmında belirtilen koşul olan tek sayı yerine "tek" o sayı
# bastırılmayıp yazı ile string ifade olan tek kelimesi bastırılmıştır.
# çıktı:
# ['tek', 2, 'tek', 4, 'tek', 6, 'tek', 8, 'tek']

# **********************************************************

sonuc=[]
for x in range(1,10):
    if (x %2==0):
        sonuc.append(x)
    else:
        sonuc.append("tek")
print(sonuc)

# çıtkı:
# ['tek', 2, 'tek', 4, 'tek', 6, 'tek', 8, 'tek']
# bir örnekte list comprehension yöntemi ile yapılan örnek bu kodda normal yöntem
# ile for ve if döngüleri kullanılarak yapılmıştır.

# *************************************************************

result=[]
for x in range(3):
    for y in range(3):
        result.append((x,y))
print(result)
# çıktı:
#[(0, 0), (0, 1), (0, 2), (1, 0), (1, 1), (1, 2), (2, 0), (2, 1), (2, 2)]

#  bu kod şu şekilde çalışıyor: ilk for döngüsü içinde olan x 3 kadar gidecek.
# sonra x ilk yakaladığı eleman olan sıfır da bir sonraki yani içerideki
# döngüye geçecek. sonra bu içeride yer alan for döngüsünün bütün elelmanları ilk
# for döngüsündeki sıfır elemanı ile eşlenip bitene kadar devam edecek.
# sonra ilk for döngüsünün sıfır elemanıo ile ikinci döngünün bütün elemanları eşlenip
# bittikten sonra ilk döngünün 2. elemanı olan 1 elemanı için aynı döngü başlayacak
# bu işlem ilk for döngüsünün bütün elemanlrı bitene kadar devam edecek.
# print() ile result ekrana basılarak kod hatasız sonuçlanacak.

# ***********************************************************************

numbers=[(x,y) for x in range(3) for y in range(3)]
print(numbers)
# çıktı:
# [(0, 0), (0, 1), (0, 2), (1, 0), (1, 1), (1, 2), (2, 0), (2, 1), (2, 2)]
# bir önceki örnekte normal iç içe for döngüleri ile yazdığımız kod ile bu list comprehension
# yöntemi ile yazılan kod aynı şey . zaten çıktılar aynı.


























































