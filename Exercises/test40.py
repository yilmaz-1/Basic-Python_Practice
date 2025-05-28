def mukemmel(sayı):
    toplam = 0
    for i in range(1,sayı):
        if sayı % i ==0:
            toplam+=i
    return toplam == sayı
# yularıda tanımladığımız fonksiyonda bir sayının mükemmel olup olmadığını anlamamıza yarıyor. öncelikle fonksiyon ismi
# yazıldı. dah sonra bu fonksiyon bloğu altında toplam isminde bir değişken tanımlanıp sıfıra eşitlendi.
# çünü bu değişkeni ilerki kod bloklarında kullanıcağız. mükemmel sayı buluren sayının tam bölenerinin toplamı kendisine
# eşit olamsı gerektiği için.  daha sonra ise for döngüsü ile mükemmel sayıyı nasıl bulacağımıza yarayan kod döngüsü
# yazıldı. for döngüsünde range ile 1 den kullanıcının gireceği son sayıya kadar ki aralıkta yer alan sayıları
# i değişkeni ile alıyoruz. daha sonra alğımız bu i değişkenleri kullanıcının giridği sayıyı tam bölüyorsa bunu toplam
# değişkeni ile topluyoruz. daha sonra da return taplam == sayı ifadesi ile elde ettiğimiz toplam yeni sayımız olarak
# bize geri döndürülüyor.

for i in range(1,1001):
    if (mukemmel(i)):
        print(f"mükemmel sayı: {i}")
# for döngüsü ile range fonksiyonu kullanarak 1 den 1001 e kadar olan sayılar i değişkeni ile alıniyor. daha sonra
# if bloğu içerisinde yukarıda tanımladığımız fonksiyon çağrılıyor. eğer for döngüsü ile elde ettiğimiz i değerimiz
# yukarıda fonskiyonda elde ettiğimiz ile ile aynı ise print ile ekrana mükemmel sayı oalrak yaızlıyor.

#çıktı:
#mükemmel sayı: 6
# mükemmel sayı: 28
# mükemmel sayı: 496