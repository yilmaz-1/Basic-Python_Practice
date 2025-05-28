def foksiyon(): # argümanı olmadan bir fonksiyon tanımlandı.
    a=10 # değişken tanımlandı.
    print(a) # değişken ekrana bastırıldı.

foksiyon()
# çıktı:
# 10

foksiyon(5) # fonksiyon argümansız olaraka tanımlanmışken biz içine 1 adet '5' argümanını yolladık. buda fonksiyonun hata vermesine sebep oldu.
# çıktı:
# TypeError: foksiyon() takes 0 positional arguments but 1 was given

print(a) # a değişkeni yok oldu. bu şu demek: a değişkeni def foknsiyon u altında tanımlanmıştır. fonksiyon çağrıldığında çalışıyor ve print(a) ile ekrana değişkeni basıyor ve bitiyor. burada ki print def fonksiyonu altında yer alan print. ama bu print ise fonksiyondan bağımsız tanımlanan ve çağrılan print. içerisinde ki a değişkeni de doğal olarak fonksiyonun değişkeni değildir. bu print içiinde ki a globalde tanımlanması gerekir. def fonksiyonu içinde tanımlanan a ise local de tanımlanmış sadece o fonksiyon çalıştığında çalışan değişkendir.
# çıktı:
# name 'a' is not defined