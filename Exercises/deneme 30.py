def toplama(*parametreler): # toplama isminde sınırsız argüman tanımlı bir fonksiyon tanımlanmıştır. argümanın önüne koyulan * ifadesi o fonksiyon içine sınırsız sayıda argüman gönderilebilir anlamına gelmektedir.
    toplam=0 # toplam değişkeni tanımlanmışıtr.
    print("Parametreler:",parametreler) # ekrana bastırılıyor.
    for i in parametreler: # for ile döngü kuruluyor. girilen parametreler içinden i değeleri alınıyor. parametler üzerinde gezinerek.
        toplam+=i # her aldığımız i değeri toplam değişkenine atanıp toplanıyor.
    return toplam # return ile bu toplam daha sonra çağrılmak üzere tutuluyor.

print(toplama(1,2,3,4,5,6,7,8,9,10))
# çıktı:
# Parametreler: (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
# 55