"""
# Elinizde bir dikdörtgenin kenarlarını ifade eden sayı çiftlerinin bulunduğu bir liste olsun.
#
#          [(3,4),(10,3),(5,6),(1,9)]
#
# Şimdi kenar uzunluklarına göre dikdörtgenin alanını hesaplayan bir fonksiyon yazın ve bu listenin her bir elemanına bu fonksiyonu uygulayarak ekrana şöyle bir liste yazdırın.
#
#          [12, 30, 30, 9]

liste = [(3,4),(10,3),(5,6),(1,9)]

def alan_hesapla(x):
    alan = x[0]*x[1]
    return alan


print(list(map(alan_hesapla,liste)))

"""

"""
 # Elinizden her bir elemanı 3'lü bir demet olan bir liste olsun.
# 
#      [(3,4,5),(6,8,10),(3,10,7)]
# 
# Şimdi kenar uzunluklarına göre bu kenarların bir üçgen olup olmadığını dönen bir fonksiyon yazın ve sadece üçgen belirten kenarları bulunduran listeyi ekrana yazdırın.
# 
#      [(3, 4, 5), (6, 8, 10)]

liste1 = [(3,4,5),(6,8,10),(3,10,7)]
def ucgen_mi(x):
    if (abs(x[0]+x[1])>x[2] and abs(x[0]+x[2])>x[1] and abs(x[1]+x[2])>x[0]):
        return True
    else:
        return False
print(list(filter(ucgen_mi,liste1)))

"""

"""
# Elinizde şöyle bir liste bulunsun.
# 
#     [1,2,3,4,5,6,7,8,9,10]
# 
# Bu listenin içindeki çift sayıların toplamını ekrana yazdıran bir fonksiyon yazın.
from functools import reduce

liste2 = [1,2,3,4,5,6,7,8,9,10]

filter = list(filter(lambda x : x % 2 == 0, liste2))

print(filter)

print(reduce(lambda x,y : x+y, filter))

"""



"""

# Elinizde isimlerin ve soyisimlerin bulunduğu iki tane liste olsun.
#
#         isimler -----> ["Kerim","Tarık","Ezgi","Kemal","İlkay","Şükran","Merve"]
#
#         soyisimler -----> ["Yılmaz","Öztürk","Dağdeviren","Atatürk","Dikmen","Kaya","Polat"]
#
# Bu isimleri ve soyisimleri sırasıyla eşleştirin ve ekrana alt alta isimleri ve soyisimleri yazdırın.



names = ["Kerim","Tarık","Ezgi","Kemal","İlkay","Şükran","Merve"]
surnames = ["Yılmaz","Öztürk","Dağdeviren","Atatürk","Dikmen","Kaya","Polat"]

for i,j in zip(names,surnames):
    print(i,j)

"""






