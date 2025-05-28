print("""****************
Bir sayının asal olup olmadığını bulma

Programdan çıkmak için 'q' ya basın.
****************
""")
def asal_mi(sayi): # burada asal_mi isimli bir argümanlı bir fonksiyon tanımlanıyor.
    for i in range(2,sayi): # range fonksiyonu ile 2 den başlayarak kullnıcının girdiği sayıya kadar giden bir liste elde ediliyor. bu liste üzerinde for döngüsü ile gezinerek i değerleri alınıyor.
        if (sayi % i == 0 ): # for döngüsü ile elde ettiğimiz listeden aldığımız i değerleri tek tek kullnıcının girdiği sayıyı bölüp bölmediği kontrol ediliyor. eğer herhangi bir i değeri sayıyı tam kalansız böler ise
            return False # return ile bize False dönderiyor. biz bu fonksiyonu farkl farkl sayılar için programın farklı yerlerinde kullanabilir. çünkü return ifadesi bize bu imkanı sağlıyor.
    return True # eğer ki if bloğunda ki şart sağlanmaz ise bu blokta ki return ile bize True dönderiyor.


while True: # döngü oluşturulmuştur. program doğru çalıştığı sürece döngü devam edecektir. ve bize sürekli bir sayı soracaktır.
    sayi = input("Sayı:") # kullanıcıdan input ile bir sayı istiyoruz.
    if (sayi == "q"): # sayı yerine q ifadesini girerese kullanıcı
        print("Programdan Çıkılıyor...") # ekrana yazdırılıyor ve
        break # program sonladırılıyor.
    sayi = int(sayi) # if bloğu çalışmaz ise girilen sayı int ile veri tipi dönüşümü yapılır.
    if (sayi == 1): #  eğer sayı 1 ise
        print(sayi, "asal bir sayı değildir.") # ekrana bastırılır. print(f"(girdiğiniz {sayi} sayısı asal değildir) buda f string yöntemi ile yazma.
    elif (sayi == 2): # eğer sayı 2 ise
        print(sayi, "asal bir sayıdır.") # ekrana yazdırılır. print(f"(girdiğiniz {sayi} sayısı asaldır) buda f string yöntemi ile yazma.
    elif (sayi==0): # eğer sayı 0 ise
        print(sayi,"asal bir sayı değildir.")  # ekrana bastırılır. print(f"(girdiğiniz {sayi} sayısı asal değildir) buda f string yöntemi ile yazma.
    else: # eğer yukarıda ki durumlardan hiç biri çalışmaz ise else bloğu devreye giriyor ve çalışıyor.
        if (asal_mi(sayi)): # bu blokta yukarı da tanımlanan fonksiyon çağrıldığında, eğer bu def asal_mi fonksiyonu bize return ile True döndürüyor ise
            print(sayi,"asal bir sayıdır.") # ekrana bunu basar . print(f"(girdiğiniz {sayi} sayısı asaldır) buda f string yöntemi ile yazma.
        else: # eğer asal_mi fonksiyonu bize return ile False döndürüyor ise
            print(sayi,"asal bir sayı değildir.") # ekrana bastırılır. print(f"(girdiğiniz {sayi} sayısı asal değildir) buda f string yöntemi ile yazma.

# çıktı:
# ****************
# Bir sayının asal olup olmadığını bulma
#
# Programdan çıkmak için 'q' ya basın.
# ****************
#
# Sayı:0
# 0 asal bir sayı değildir.
# Sayı:1
# 1 asal bir sayı değildir.
# Sayı:2
# 2 asal bir sayıdır.
# Sayı:3
# 3 asal bir sayıdır.
# Sayı:4
# 4 asal bir sayı değildir.
# Sayı:5
# 5 asal bir sayıdır.
# Sayı:6
# 6 asal bir sayı değildir.
# Sayı:7
# 7 asal bir sayıdır.
# Sayı:9
# 9 asal bir sayı değildir.
# Sayı:

