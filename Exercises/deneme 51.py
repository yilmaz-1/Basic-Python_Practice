a = int(input("1. sayı: ")) # kullanıcıdan birinci sayı input fonksiyonu ile alınıyor ve int fonksiyonu ile veri tipi dönüşümü yapılıyor. a değerine atılıyor.
b = int(input("2.sayı:")) # kullanıcıdan birinci sayı input fonksiyonu ile alınıyor ve int fonksiyonu ile veri tipi dönüşümü yapılıyor. b değerine atılıyor.
c = int(input("3.sayı:")) # kullanıcıdan birinci sayı input fonksiyonu ile alınıyor ve int fonksiyonu ile veri tipi dönüşümü yapılıyor. c değerine atılıyor.

if (a > b and a > c): # koşul oluşturuluyor. koşul sağlanır ise program bu kod da çalışıyor ve
    print("en büyük a") # ekrana bastırılıyor.
elif ( b > a and b > c): # koşul oluşturuluyor. koşul sağlanır ise program bu kod da çalışıyor ve
    print("en büyük b") # ekrana bastırılıyor.
elif (c > a and c > b): # koşul oluşturuluyor. koşul sağlanır ise program bu kod da çalışıyor ve
    print("en büyük c") # ekrana bastırılıyor.

# çıktı:
# 1. sayı: 5
# 2.sayı:2
# 3.sayı:3
# en büyük a

# *********************************************

def buyukkucuk(a,b,c): # burada fonksiyon oluşturuluyor. bu sonksion üç adet argümana sahip.
    if (a>b and a>c): # bu kod bloğunda koşul oluşturuluyor. eğer bu koşul sağlanırsa program bu kod da çalşıcak ve
        print("a en büyük") # ekrana yazdırılacak.
    elif (b>a and b>c): # bu kod bloğunda koşul oluşturuluyor. eğer bu koşul sağlanırsa program bu kod da çalşıcak ve
        print("b en büyük") # ekrana yazdırılacak.
    elif (c>a and c>b): # bu kod bloğunda koşul oluşturuluyor. eğer bu koşul sağlanırsa program bu kod da çalşıcak ve
        print("c en büyük") # ekrana yazdırılacak.
    return # return ile bu buuykkucuk(a,b,c) fonksiyonu daha sonra başka başka yerlerde kullanılmak üzere tutulup geri döndürülüyor.

while True: # while True ile döngü kuruluyor.
    a = input("a :") # kullanıcıdan input fonksiyonu ile a değeri alınıyor.
    b = input("b :") # kullanıcıdan input fonksiyonu ile b değeri alınıyor.
    c = input("c :") # kullanıcıdan input fonksiyonu ile c değeri alınıyor.
    if ( a == "q" or b=="q" or c=="q"): # koşul durumu oluşturuluyor. koşul sağlanırsa program bu blokta çalışıyor ve
        print("sistemden çıkış yapıldı") #ekrana yazdırılıyor.
        break
    else:
       a = int(a)
       b = int(b)
       c = int(c)
       print(buyukkucuk(a,b,c))

# çıktı:
# a :1
# b :2
# c :3
# c en büyük
# None
# a :q
# b :q
# c :q
# sistemden çıkış yapıldı