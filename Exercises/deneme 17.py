print("Armstrong Sayı Tespit Etme Programı") # yazdığımız fonksiyonun ismi ekrana print fonksiyonu ile bastırılıyor.

sayı=input("Sayı:") # kullanıcıdan input fonksiyonu ile sayı girmesi isteniyor.

basamak_sayısı=len(sayı) # burada kullanıcının girdiği sayının basamak adedi len () fonksiyonu ile tespit edilip basamak_sayısı değişkenine atanıyor.

sayı=int(sayı) # burada kullanıcıdan alınan sayı int() fonksiyonu ile integere çeviriliyor. çünkü kullanıcından alına sayı aslında string bir ifade. ve str olan bir ifadeyi matematiksel işlemem saokamayız. onun için kullanıcıdan alınan sayı int e çevrilmelidir.

basamak=0 # basamak isminde bir değişken tanımlayıp ve bunu 0 a eşitliyoruz. çünkü bu değişkeni kullanacağız. sıfır olması yapaacağımız dögüde doğru sonuç vermesi için önemli.

toplam=0 # toplam isminde bir değişken tanımlıyoruz. amaç döngü içinde bu değişkeni kullanacağız. böylelikle sonuç hatalı çıkmaması için 0 a eşitliyoruz.

ilk_sayı=sayı # burada ilk sayı isminde bir değişken tanımlıyoruz. bu değişkene de kullanıcıdan aldığımız sayıyı atıyoruz. çünkü bu ilk sayı değişkenini döngü içinde kullanacağız.

while (ilk_sayı > 0): # burada döngü oluşuturuldu. ve ilk sayı değişkeni 0 dan büyük olduğu sürece True vermesi koşulu ile döndürmesi isteniyor. her True sonucu aldıkça döngü başlıyor ve kod bloğunda olan diğer kodlar çalışıyor.

    basamak= ilk_sayı % 10 # burada basamak sayısı kullanıcdan aldığımız ve ilk sayı değişkenine atadığımız sayının 10 ile bölümü ile birler basamğında olan sayıyı tespit ediyoruz. ve bu tespit ettiğimiz sayıyı basamk isimli değikene atıyoruz.

    print("basamak:",basamak) # burada bir önceki kodda elde etitğimiz 1 ler basamağındaki  rakam ekrana basılıyor.

    toplam += basamak ** basamak_sayısı # burada glablde tanımladığımız toplam isimli değişkene yularıda elde ettiğimiz basamak değişkeninde ki rakam kullanılarak ve ilk kullanıcıdan aldığımız sayının basmak sayısı kullanıralak toplam değişkenine atanıyor.

    print("toplam:",toplam) # sonra bu toplam ekrana basılıyor.

    ilk_sayı //=10 #  //=10 bu fonskiyon bir sayının 10 ile böülümünden elde edilen bölümü bulmaya yarıyor. burada ilk sayının 10 ile bölümünden elde edilen bölüm bulunuyor.

    print("sayı:",ilk_sayı)# bir üst satırdaki kod ile ilk sayı, sayının 10 ile bölümünden elde edilen bölüm oluyor ve buda ekrana basılıyor. daha sonra ilk sayımız değişti ve ve elde edilen bölüm ooldu. sonra döngü başa dönüyor ve while bloğunda belirtilen koşul sağlanıp sağlanmadığı kontrol edilir. sağlanoyr ise terkar aynı işlemler yapılıyor.

if (sayı==toplam): # while koşulu sağlanmadığı zaman döngü bitiyor ve program bir sonraki if bloğuna geliyor. burada ilk başta kullanıcının girdiği sayı while döngüsünde hesaplattığımız toplam değişkenine eşit ise

    print("Armstrong Sayıdır.") # ekrana armstrong sayıdır yazısı basılıyor.

else: # değilse ekrana armstrong sayı değildir yazısı basılıyor.

    print("Armstron Sayı Değildir.")