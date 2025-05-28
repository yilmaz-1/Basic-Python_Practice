sayi=int(input("Bir sayı giriniz:"))

asalmi= True # globalde bu değişken True olarak tanımlandı.
# **********************
if sayi==1: # eğer bu kod bloğunda yer alan şart sağlanır ise yani sayı 1 e eşit olur ise
    asalmi= False # asalmi değişkenini False olarak ver.

for i in range(2,sayi): # for döngüsü ile range fonksiyonu kullanılarak 2 den başlayıp kullanıcının girdiği değere kadar olan aralıkta bir liste oluşturuluyor. ve bu listeden i değerleri olarak elelmanlar alınıyor.
    if (sayi % i ==0): # yukarıda elde etiiğimiz i değerleri tek tek sayıyı bölmesi için bir koşul oluşturuluyor. for döngüsü ile elde edilen liste içinden elde edilen i değerlerinden herhangi biri sayıyı tam kalansız böler ise,
        asalmi= False # globalde tanımladığımız asalmı değişkenini False olarak tanımla.
        break # ve fonksiyonu sonladır.
if asalmi: # burada yeniden bir koşul kod bloğu oluşturuluyor ve asalmi değişkeni True mu diye kontrol ediliyor. yukarıda ki for döngüsünden elde edilen asalmı değişkenini okuyor program. for döngüsünden elde edilen asalmi True olarak çıktı verdi ise
    print("sayı asaldır.") # ekrana yazdırıyor.
else: # eğer for döngüsünden çıkan asalmi değişkeni bize True değilde False olarak çıktı ise o zaman bu kod bloğu çalışmaya başlıyor.
    print("sayı asal değildir.") # ekrana yazdırıyor.

# ********************************

sayi=int(input("Bir sayı giriniz:"))

if (sayi==1):
    print("sayı asal değildir.")
elif (sayi==2):
    print("sayı asaldır.")
elif (sayi==0):
    print("sayı asal değildir.")
for i in range(2,sayi):
    if (sayi % i ==0):
        print("sayı asal değildir.")
        break
    else:
        print("sayı asaldır.")
        break

# yukarıda yazılan program da asal sayı bulma progarmıdır. her iki program da asal sayıyı bulmaya yarıyor.
# ilk programın çalışması şu şekilde: sayi değişkeni ile kullanıcıdan input() fonksiyonunu kullanarak sayı istiyoruz.
# sonra bu aldığımız sayıyı int() foksiyonu ile integer e çeviriyoruz. sonra asalmi diye bir değişken tanımlayıp bunu
# True olarak atıyoruz. bu yaptıklarımız hep global de yapılan atamalar. yani foksiyon değişdiği zaman bu atamalar
# değişmiyor. daha sonra if koşulu ile sayının 1 olması durumu yazıldı. eğer sayı 1 olursa bizim yukarında
# tanımladığımız asalmi değişkenini if bloğu altında False olarak tanımlıyoruz. bu şu anlama geliyor: asalmi değişkeni
# yukarıda True olarak tanımlanmıştı ama eğer kullanıcının giridği sayı 1 olursa bu True olan asalmi değişkeni direk
# False olarak ekrana basılıyor. sonra devamında for döngüsü ile range fonksiyonu ile belirtilen aralıkta yani başlagıcı 2 olan ve
# kullanıcının girdiği sayıya kadar i değeri al diyor. for bloğunun altında bulunan if bloğu ile sayının range
# foksiyonu ile elde ettiğimiz i lerden herhangi birine bölünmesi durumunda el başta tanımladığımız asalmi değişkenin
# False olarak tanımlıyoruz ve False geliyorsa direk break ile kırıyoruz foksiyon orada bitiyor.
# devamında ise if ile asalmi değişkenin şartlarını tanımlıyoruz. eğer asalmi değişkeni True ise, ekrana sayı asaldır
# basılıyor. else bloğunda ise asalmi değişkeni False dönüyorsa ekrana sayı asal değildir basılıyor.
# bu kod da 0 ı işlemlere dahil etmediğimiz için hatalı sonuç alacağız.
# ikinci kod da aynı işlevi yapmaktadı. asal sayıyı bulmak için kullanılıyor. bu kod da normal if elif kalıbı ile
# kullanıcının girdiği 1,2 ve 0 olma durumları değerlendirilmiştir. bu sayıları girdiği zaman tanımlı bolğunun altında
# ekrana yazılması greek talimat verilmiştir. ama kullnıcı farklı bir sayı gidiği zaman devamında yazılan for döngüsü
# ile tanımlana şartlar uygulanamya başlanır. range fonskiyonu ile belirtilen aralıkta i değeriaranır. bulunan i
# i değerleri eğer sayiyi tam bölüyorsa bu sayı asal değildir diye ekrana basılır. ama sayıyı tem bölmüyor ise else
# bloğunda asaldır ifadesi basılır.










