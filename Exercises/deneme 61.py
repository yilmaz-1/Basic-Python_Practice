ürünler = [
    {'name':'samsung s6','price':'3000'},
    {'name':'samsung s7','price':'4000'},
    {'name':'samsung s8','price':'5000'},
    {'name':'samsung s9','price':'6000'},
    {'name':'samsung s10','price':'7000'},
]
# ürünler isimli bir liste tanımlanıyor.
# toplam =0 # toplam isimli bir değişken sıfıra eşitlenip tanımlanıyor.
# for i in ürünler: # for döngüsü ile ürünler listesi üzerinde gezinerek i değerleri elde ediliyor.
#     fiyat=int(i['price']) # for döngüsü ile elde edilen i değerlerinin birinci indeksinde price ifadesine denk gelen stringler alınıp int foksiyonu ile veri tipi dönüşümü yapılarak, değişkenine atanıyor.
#     toplam+=fiyat # yukarıda elde ettiğimiz fiyat değişkenleri her döngüde toplam değişkenine atanarak toplanıyor.
# print(toplam) # toplam değişkeni print ile ekrana bastırılıyor.

# çıktı:
# 25000

# ******************************************************************

for i in ürünler: # for döngüsü ile ürünler listesi üzerinde gezinerek i değerleri elde ediliyor.
    #k = int(i['price']) eğer bu kodu koullancaksak,
    if (int(i['price'])<=5000): # buraya direk k <=5000 yazıp çalıştırabiliriz.
        print(i['name'])

# çıktı:
# samsung s6
# samsung s7
# samsung s8



