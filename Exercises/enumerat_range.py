fruits = ["elma", "armut", "çilek", "kira"] # burada bir adet liste tanımlandı. bu listeyi biz kendimiz tanımladık.
# dışarıdan input gibi fonksiyon kullanarak elde etmedik.

print(fruits[0]) # burada print fonksiyon kullanarak fruits listesinin sıfırıncı indeksindeki elemanı ekrana yazdırdık.
# çıktı
# elma


for i in fruits: # burada yukarıda oluşturduğumuz listenin elemanları for döngüs ile i değişkenine atılarak elde edildi.
    print(i) # burada her döngüde elde ettiğimiz i değerlerini print fonksiyonun ile ekrana bastırdık.
# çıktı
#elma
# armut
# çilek
# kira


for sub_number in range(len(fruits)): # burada yularıda oluşturuduğumuz liste üzerinden bir for döngüsü oluşturduk.
    # burada önemli olan şey şu range fonksiyonu kullanrak hangi aralıkta olması gerektiğini yani bu döngünün
    # nereye kadar kaça kadar devam edeceğini belirttik. bu sınırı yani range fonskiyonun sınırını ise içersindeki
    # len fonksiyonu kullanarak listenin boyu hesaplandı ve bu boy (sayı değeri) range fonskiyonun elemanı olarak
    # sınır değeri oldu.
    print("{}. {}". format(sub_number, fruits[sub_number])) # burada  format fonksiyon kullanarak hangi indekste hangi
    # eleman olduğunu print fonskiyonu ile ekrana yazdırdık.
# çıktı
# 0. elma
# 1. armut
# 2. çilek
# 3. kira


for sıra, oge in enumerate(fruits,1): #  yukarıdaki aynı liste üzerinde bir for döngüsü oluşturduk bu döngü üzerinde
    # enumerate fonskiyonu kullanarak furits listesinin elemanları sıra
    print("{}. {}".format(sıra,oge))

# 1. elma
# 2. armut
# 3. çilek
# 4. kira