c=5 # globalde tanımlanmış bir değişken
def fonksiyon (): # fonksiyon argümanı olmadan tanımlanmıştır.
    c=2 #yerelde tanımlanmış bir değişken
    print(c) # ekrana basıyor.

fonksiyon() # fonksiyon bloğu içinde yerel de tanımlanmış değişkeni (c) kullandı.
# çıktı:
#2

print(c) # globalde tanımlanmış (c) değişkeni kullandı. çünkü bu kodun def fonksiyonnu ile alakası olmadığı için globalde tanımlanan c kullanıldı.
# çıktı:
# 5