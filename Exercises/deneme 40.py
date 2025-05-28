d=10 # golabalde tanımlanmış değişken
def fonksiyon(): # argümansız olarak fonksiyon tanımlandı.
    global d # burada global de tanımladığımız d değişkenini almak istediğimizi belirttik.
    d = 4 # yerelde tanımlanmış değişken. fakat bu koda gelince fonksiyon ekndi içinde aynı isimli bir değişken görünce bir üst satırda tanımlanmış değişken yerine burada ki değişkeni kullanmaya karar veriyor.
    print(d) # ekrana basıyor.

fonksiyon()# argümansız olarak çağrılıyor
# çıktı:
#4

print(d) # golabl de d değişkeni değişince değişmiş değişken ile ekrana basıyor.
# çıktı:
#4

# program çalıştığı zaman, bir tane global d değişkeni oluşuyor ve fonksiyonumuz çağrıldığı zaman global d ifadesiyle
# globaldeki d değişkeni kullanmak istediğimizi söylüyoruz. fakat devamında d=4 ifadesi ile globalde tanımladığımız
# d değişkeninin değerini değiştirmiş oluyoruz.