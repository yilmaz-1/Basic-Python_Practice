sayilar = [1,3,5,7,9,12,19,21] # sayilar isminde bir liste tanımlanıyor.
a=[] # boş liste tanımlanıyor.
for i in sayilar: # for döngüsü ile sayilar listesi üzerinde gezinerek i değeleri elde ediliyor.
    if (i % 3 ==0): # for döngüsü ile elde ettiğimiz i ler eğer 3 e tam kalansız bölünüyor ise
        a.append(i) # bu i leri boş olan a listesine at.
print(a) # a listesi ekrana yazdırılıyor.

#çıktı:
#[3, 9, 12, 21]

# **************************************************

sayilar = [1,3,5,7,9,12,19,21] # sayilar isminde bir liste tanımlanıyor.
toplam=0 # toplam değişkeni tanımlanıyor. çünkü bu değişken for döngüsü içinde kullanılacağı için hata olmaması için sıfıra eşitlendi.
for x in sayilar: # for döngüsü ile sayilar listesi üzerinde gezinerek x değeleri elde ediliyor.
    toplam+=x # her döngüde elde edilen bu x değerleri toplam değişkenine atanarak toplanıyor.
print(toplam) # dönü bittikten sonra toplam değişkeni print fonksiyonu ile ekrana yazdırılıyor.

# çıktı:
# 77

# ***************************************************

sayilar = [1,3,5,7,9,12,19,21] # sayilar isminde bir liste tanımlanıyor.
b = [] # boş liste tanımlanıyor.

for j in sayilar: # for döngüsü ile sayilar listesi üzerinde gezinerek j değeleri elde ediliyor.
    if ( j % 2 !=0): # for döngüsü ile elde ettiğimiz j değerleri eğer iki ile kalansız bölünmüyor ise yani kalan sıfıra eşit değilse
        j**=2 # bu elde ettiğimiz j değerlerinin karesi alınıyor.
        b.append(j) # ve bu karesi alınan j değerleri boş olan b listesine atılıyor.
print(b) # ekrana bu yeni b listesi yazdırılıyor.

# çıktı:
# [1, 9, 25, 49, 81, 361, 441]

# *******************************************************

sayilar = [1,3,5,7,9,12,19,21] # sayilar isminde bir liste tanımlanıyor.
c = []
def ucunkatisayilar(sayilar): # ucunkatisayilar isimli bir argümana sahip bir fonksiyon tanımlanıyor.
    for k in sayilar:  # for döngüsü ile sayilar listesi üzerinde gezinerek k değeleri elde ediliyor.
        if ( k % 3 ==0): # for döngüsü ile elde ettiğimiz k değerleri eğer 3 e tam kalansız bölünüyor ise
            c.append(k) # bu k değerleri boş olan c listesine at.
    print(c) # bu yeni c listesi ekrana yazdırılıyor.
    return # fonksiyon çağrılmak üzere döndürülüyor.

ucunkatisayilar(sayilar)

# çıktı:
#[3, 9, 12, 21]

# *******************************************************

sayilar = [1,3,5,7,9,12,19,21]



def sayitoplama(sayilar):
    toplam=0
    for i in sayilar:
        toplam+=i
        print(i)
    print(toplam)
    return

sayitoplama(sayilar)

# çıktı:
# 1
# 3
# 5
# 7
# 9
# 12
# 19
# 21
# 77

# ***********************************************************

# sayilar = [1,3,5,7,9,12,19,21]
#
# k=[]
# def sayilarinkaresi(sayilar):
#     for x in sayilar:
#         x**=2
#         k.append(x)
#     print(k)
#     return
# sayilarinkaresi(sayilar)

# çıktı:
# [1, 9, 25, 49, 81, 144, 361, 441]
