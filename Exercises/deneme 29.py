def üçleçarp(a): # üçleçarp isminde tek argümanlı bir fonksiyon tanımlanıyor.
    print("1.fonksiyon çalıştı") # ekrana print ile basılıyor.
    return a*3 # return ile argümanın 3 ile çarpılmış hali daha sonra çağrılmak üzere tutuluyor.

def ikiyletopla(a): # ikiyletopla isminde 1 argümanlı bir fonksiyon tanımlanıyor.
    print("2.fonksiyon çalıştı") # ekrana bastırılıyor.
    return a+2 # return ile daha sonra çağrılmak üzere toplam tutuluyor.

def dördeböl(a): # dördeböl isminde 1 argümanlı fonksiyon tanımlanıyor.
    print("3.fonksiyon çalıştı") # ekarna bastırılıyor.
    return a/4 # return ile argümanın 4 e bölümü daha sonra çağrılmak üzere tutuluyor.

print(dördeböl(ikiyletopla(üçleçarp(5)))) # print fonksiyonu içerisinde ilk olarak üçleçarp fonksiyonu çalışması için 5 argümanı ile çağrılıyor. daha sonra üçleçarp fonkiyonundan gelen sonuç ikiyletopla fonksiyonuna gönderiliyor ve buradan gelen sonuç dördeböl fonksiyonuna gönderiliyor. dördeböl foksiyonundan elde edilen sonuç ekrana print fonksiyonu ile bastırılıyor.
# çıktı:
# 1.fonksiyon çalıştı
# 2.fonksiyon çalıştı
# 3.fonksiyon çalıştı
# 4.25