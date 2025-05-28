print("********* Hesap Makinesi Programı*********") # burada print fonksiyon içerisinde programın adı tanımlanmıştır.

c= input("İşlemin Adını Yazı İle Giriniz:") #  burada c isiminde bir adet değişken tanımlanmış fakat bu değişken input
# fonksiyonu kullnılarak dışarıdan kullanıcıdan alınmıştır. kullanıcıdan aldığımız bu değişken çift tırnak içersinde
# yazdığımız için str tipindedir. yani karakterdir sınıfındadır.

a=int(input("Birinci Sayıyı Giriniz:")) # burada  a isminde değişken tanımladık ve bu değişkeni kullanıcıdan input
# fonksiyonu kullanarak aldık. Aldığımız bu değeri ( ki biz burda kullanacıdan sayısal bir ifade bekliyoruz)
# int fonksiyonu kullanarak integer tipine çeviriyoruz. çünkü bu değeri matematiksel işleme sokacağız.
b=int(input("İkinci Sayıyı Giriniz:")) # burada b isminde bir değişken tanımladık ve bu değişkeni input fonksiyonu
# ile dışarıdan aldık ve bu değeri de int fonksiyonu ile de veri tipi donüşümü yaptık.

if (c=="toplama"): # burada if ile bir şart bloğu oluşturduk. bu oluşturduğumuz koşul bloğunun şartı ise: eğer
    # c değeri toplama isimli değişkene eşit olursa bu blok çalışsın istedik.
    print("Sayıların Toplamı:", a+b) # burada ise yukarıda tanımlana if şart bloğu sağlanıyorsa bu şart bloğunu
    # içerisinde yer alan print fonksiyonu çalışsın istedik. print fonksiyonu girinti olarak şart bloğunun içesinde
    # olduğu için if doğru ise bu blook çalışacak ve ekrana a ve b sayılarının toplamını basacak.
elif (c=="çıkarma"): # burada ise yukarıda tanımlanan if bloğundaki şart sağlanmazsa ise program yukarıdan aşağıya
    # okumaya devam edecek ve bu blok ile karşılacak. eğer bu blokta yer alan ifade koşul sağlanırsa burası çalışacak.
    # bu şart bloğu içerisinde ise şu denilmektedir. eğer c değişkeni çikarma isimli str ifadesine eşitse
    # bu koşul bloğunu çalıştır demek.
    print("İki Sayının Farkı:", a-b) # burada ise eğer elif bloğu içerisnde ki koşul sağlanır ve bu blok çalışır ise
    # bu blok içerisindeki girinti olarka da belli oluyor print ifadesi çalışsın demek oluyor. ve böylelilkle a ve b
    # değerinin farkı ekrana print fonksiyonu ekrana bastırılıyor.
elif (c=="çarpma"): # python da program yukarıdan aşağıya okunmaya devam ediyor. okdukça hangisi doğru ise onu ve
    # içerisindeki girintiyi çalıştırıyor. burada ise yularıdaki hiç bir koşul sağlanmadı ise bu blok kontrol edliyor.
    # eğer blok içerisindeki  c değişkeni çarpma str ifadesine eşit ise şartı sağlanıyor ise bu blok ve girintileri
    # çalışsın diyor.
    print("İki Sayını Çarpımı:", a*b) # burada da elif bloğu çalşıtı ise print ile a ve b değerleirnin çarpımı ekrana
    # yazdırılıyor.
elif(c=="bölme"): # yukarıda da anlattığımız gibi yukarıdaki hiç bir şart bloğu sağlanmadı ve çalışmadı ise bu blok
    # kontrol ediliyor ve eğer c değişkeni bölme str  ifadesine eşitse bu blok ve içersindeki kodlar çalışsın istiyoruz.
    print("İki Sayının Bölümü:", a/b) # elif bloğu çalışması ile böylelikle print ile ekrana ekrana a ve b
    # değerlerinin bölümü yazdırılıyor.
else: # burada hiç bir şart belirtmiyoruz. bu şu demek; yukarıda ne kadar şart tanaımladık ise ve hiç bir
    # şart sağlanmadı ve çalışmadı ise artık bunu yap demek.
    print("Geçersiz Seçim Yaptınız...")  # bu koşul bloğunun içerisnde yer alan print fonksiyonu ekrana yazdırıldı.

# bu program da basit dört işlem yapan bir hesap makinesi yazılmıştır.
# program şu şekilde çalışmaktadır. öncelikle print() fonkisyonu ile porgramın adı bastırılıyor. sonra c değişkenine
# atanmak üzere kullanıcıdan input yapmak istediği işlemin adını yazması isteniyor. daha sonra kullanıcıdan a ve b olmak
# üzere iki adet değişken input fonksiyonu ile isteniyor.bu a ve b değişkenleri int fonksiyonnu ile integer e çevriliyor
# daha sonra if elif else kalıbı ile şartlar oluşuturuluyor. kullnaıcı toplama yazdığı zaman girilen sayıların toplamı
# print fonksiyonu ile ekrana bastırılıyor. aynı bu şekilde diğer işlemler de girilen sayılar ve işleme göre işlem
# yapılıp sonuç print foksiyonu ile ekrana basılıyor. else bloğunda ise geçersiz işlem girildiği zaman print ile ekrana
# geçersiz seçim yaptınız bastırılıyor.