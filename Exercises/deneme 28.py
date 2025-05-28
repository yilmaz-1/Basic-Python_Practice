def toplama(a,b,c): # toplama isminde 3 argümanlı bir fonksiyon tanımlanıyor.
    return a+b+c # return ile bu argümanların toplamı daha sonra çağrılmak üzere toplanıyor.

def ikiyle_carp(a): # ikiyle_carp isminde 1 argümanlı bir fonksiyon tanımlanıyor.
    return a*2 # return ile bu argümanın 2 ile çarpılmış hali daha sonra kullanmak üzere çarpılıor.

toplam=toplama(3,4,5) # toplam değişkenşne toplama fonksiyonu atanıyor .

print(ikiyle_carp(toplam)) # ikiyle_carp fonksiyonu içine toplam değişkeni gönderilerek ekrana bastırılıyor.
# çıktı:
# 24
