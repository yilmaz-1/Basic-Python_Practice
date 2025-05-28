# şifre en az 8 karakter, en az 1 büyük harf, en az 1 küçük harf, en az bir sayı içermelidir.

buyuk= "ABCDEFGHIJKLMNOPRSTVYZWXQ" # burada bir adet büyük harf listesi tanımlandı.
kucuk= " abcdefghijklmnoprstvyzwxq" # burada bir adet küçük harf listesi tanımlandı.
digit= "0123456789" # burada bir adet dijital sayılar tanımlandı.

sifre = input("Lütfen Şifrenizi Giriniz: ") # burada kullanıcıdan bir adet şifre girmesi istendi.

bhsayi=0 # başlangıçta büyük harf sayısı sıfır olarak tanımlandı. sebebi şu döngü içerisinde bu sayı hala sıfır ise
# şifre güvensiz msjı dönmesi sağlanacak.
khsaiy=0 # aynı şekilde burada da küçük harf sayısı tanımlandı.
dsayi=0 # dijital sayılar tanımlandı.

for i in sifre: # for döngüsü ile her döngüde kullanıcının girdiği şifre içerisindeki her bir karakter i değişkeni
    # olarak alınıyor.
    if i in buyuk: # her döngüde alınan bu i değişkeni büyük harf listesi içerisinde olup olmadığı kontrol ediliyor.
        # Eğer o liste içerisinde var ise,
        bhsayi+=1 # bhsayi değişkeni bir artırılarak bu koşul bloğu sonlanıp sonraki kod bloğuna geçiliyor.

    if i in kucuk: # her döngüde alınan i değeri küçük harf listesi içerisinde var ise ,
        khsaiy+=1 # khsayi değişkeni 1 artırılarak kod bloğu sonlanıp diğer kod bloğuna geçiliyor.

    if i in digit: # eğer her döngüde alınan i değeri sayılar listesi içersinde var  ise,
        dsayi+=1 # dsayi değişkeni 1 artırılarak döngü bir sonraki i değerini almak üzere başa döner. eğer i değeri
        # kalmadı ise döngü sonlanıp bir sonraki kod bloğuna devam eder.

if (bhsayi==0) or (khsaiy==0) or (dsayi==0) or (len(sifre)<8): # burada yukarıdaki kod bloğundan bağımsız olarak bir
    # şart bloğu oluşturuldu. eğer if bloğu içerisinde yer alan şartlardan her hangi biri sağlanır ise
    print("Güvensiz Şifre") # ekrana yazdırılır.
else: # hiç biri sağlanmaz ise
    print("Güvenli Şifre") # ekrana yazdırılır.

