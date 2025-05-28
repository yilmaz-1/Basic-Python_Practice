def ikiyleçarp(x): # ikiyleçarp fonksiyonu bir adet argüman ile tanımlanıyor.
    return x*2 # return ifadesi kullanılarak, fonksiyon içine gönderilen argün 2 ile çarpılıp daha sonra foksiyonu çağırdığımızda geri döndürmek üzere tutuyoruz.
print(ikiyleçarp(2))# foksiyon içine gönderilen 2 argümanı ile çağırılıp ekrana bastırılıyor.
# çıktı:
# 4

# yukarıdaki fonksiyonu list comprehension da yaptığımız gibi tek satırda yazmaya çalışırsak:

ikiyleçarp=lambda x: x*2 # burada lambda ifadesi kullanılarak def ile tanımlanan fonskiyon tek satırda yazıldı.

print(ikiyleçarp(3)) # print fonksiyonu içerisnde ikiyleçarp fonksiyonu 3 argünaı yollanarak çağrıldı ve ekrana basıldı.
# çıktı:
# 6


def toplama(a,b,c): # toplama isminde 3 argünmalı bir fonksiyon tanımlandı.
    return a+b+c # return ile toplanan argümanlar daha sonra çağrılmak üzere tutuldu.
print(toplama(3,4,5))# print fonksiyonu içerisinde toplam fonksiyonu 3 argüman gönderilerek çağrıldı.
# çıktı:
# 12

# yukarıdaki fonksiyonu list comprehension da yaptığımız gibi tek satırda yazmaya çalışırsak:

toplama=lambda a,b,c: a+b+c # toplama fonksiyonu lambda ifadesi kullanılarak 3 argünamlı bir fonksiyon tanımlandı.
print(toplama(3,4,5))# toplama fonksiyonuna 3 argüman gönderilerek çağrıldı ve ekrana basıldı.
# çıktı:
# 12
