
while True: # burada while ile bir döngü oluşturulmuştur. True ile de bu döngü sürekli çalıştırılması istenmiştir. program çalıştığı zaman girilen sayı ne olursa olsun sürekli bizden yeni sayı girmesi isteniyor.
    enterNumber = int(input(" 1 ile 100 Arasında Bir Sayı Giriniz:")) # kullanıcıdan input fonksiyonu ile sayı isteniyor. aynı zamanda da veri tipi dönüşümü int fonksiyonu ile yapılmaktadır.

    if (enterNumber >0 and enterNumber < 100 ): # burda kullanıcının girdiği sayı 0 dan büyük ve 100 den küçük ise
        print("Girdiğiniz Sayı Belirtilen Aralıkta.") # bu blok çalışıyor ve ekrana yazıdırılıyor.

    else: # if bloğunda ki koşul ifadesi sağlanmaz ise bu blokta ki diğer şartlar için kontrol yapılır ve bu blok çalıştırılır.
        print("Girdiğiniz Sayı Belirtilen Aralıkta Değildir.") # ekrana yazdırılır.
# çıktı:
# #1 ile 100 Arasında Bir Sayı Giriniz:99
# Girdiğiniz Sayı Belirtilen Aralıkta.
#  1 ile 100 Arasında Bir Sayı Giriniz:55
# Girdiğiniz Sayı Belirtilen Aralıkta.
#  1 ile 100 Arasında Bir Sayı Giriniz:66
# Girdiğiniz Sayı Belirtilen Aralıkta.
#  1 ile 100 Arasında Bir Sayı Giriniz:101
# Girdiğiniz Sayı Belirtilen Aralıkta Değildir.
#  1 ile 100 Arasında Bir Sayı Giriniz:


# # Burada şunu yaptık: kullanıcıdan 1 ile 100 arasında bir sayı girmesini istedik.
# ve bu sayı eğer belirtilen aralıkta ise ekrana " Girdiğiniz Sayı Belirtilen Aralıktadır."
# yazsını bastırdık. ve bunu if komutu ile yaptık. Eğer girilien sayı belirtilen aralıkta değilse,
# ekrana "Girdiğiniz Sayı Belirtilen Aralıkta Değildir." ifadesini yazdırdık.
# burada while Ture kullanmamızın amacı şu:
# program yukarından aşağıya dopru okumaya başlıyor kotları. sonra biz ne kod yazdıysak onları tek tek
# yapıp sonlanıyor ama while True ile yaptığımız şey şu: program çalışıyor ve tekrar tekrar bizden o sayıyı istiyor.
# bu işlem sürekli devam ediyor. ta ki biz bunu sınırlayan bir ifade koymadığımız sürece. kod bloklarındaki şartlar
# sağlandığı sürece devam eder program ve sürekli tekrar tekrar sizden sayı ister.
#
# aşağıda da görüldüğü üzere biz break komutu ile programı sonlamasını istediğimiz zaman sayıyı ister hangi blok çalıştı
# ise çalşır ve program break komutu ile sonlanır.

while True: # burada while ile bir döngü oluşturulmuştur. True ile de bu döngü sürekli çalıştırılması istenmiştir. fakat burda aşağıda ki kod bloklarında yer alan break ifadesi programın sürekli çalışmasını engellemek için yazılmıştır.
    enterNumber = int(input(" 1 ile 100 Arasında Bir Sayı Giriniz:")) # kullanıcıdan input fonksiyonu ile sayı girmesi isteniyor. bu sayı int fonksiyonu ile de veri tipi dönüşümü yapılıyor.

    if (enterNumber > 0 and enterNumber < 100): #  if koşul bloğunda kullanıcıdan istenen sayı eğer hem 0 dan büyük hemde 100 den küçük ise
        print("Girdiğiniz Sayı Belirtilen Aralıkta.") # bu blok ta yer alan kod çalışmaya başlıyor ve ekrana print ile yazdırılıyor.
        break # bu blokta ise program sonlanıyor. break ifadesi programı sonlandırmak için kullanılan bir  ifadedir.

    else: # bu blok, yularıda ki if bloğu çalışmaz ise , yani oradaki koşul durumu sağlnmaz ise devreye giriyor ve çalşıyor.
        print("Girdiğiniz Sayı Belirtilen Aralıkta Değildir.") # blokta yer alana ifade print ile ekrana bastırılıyor.
        break # program sonlanıyor.

# çıktı:
#  1 ile 100 Arasında Bir Sayı Giriniz:95
# Girdiğiniz Sayı Belirtilen Aralıkta.
# program sonlandı.

# 1 ile 100 Arasında Bir Sayı Giriniz:101
# Girdiğiniz Sayı Belirtilen Aralıkta Değildir.
# program sonlandı.

# bu foksiyon while True kullanılmadan da yapılabilirdi. o zaman sizden sayıyı ister ve hangi blokta çlışırsa çalışır
# ve program sonlanır. sizden yeniden yeniden sayı isteyip program kendi kendine çalışmazdı. fonksiyon aşağıdaki gibi
# olurdu


enterNumber = int(input(" 1 ile 100 Arasında Bir Sayı Giriniz:"))# burada kullanıcıdan input ile bir sayı girmesi isteniyor. daha sonra aynı kod bloğu içnde int fonksiyonu ile de veri tipi dönüşümü yapılıyor.

if (enterNumber >0 and enterNumber < 100 ): # if koşulu ile kullanıcının girdiği sayı eğer 0 dan büyük ve 100 den küçük ise kod çalışıyor.
    print("Girdiğiniz Sayı Belirtilen Aralıkta.")# ekrana kod bloğundaki ifade print ile yazdırılıyor.
else: # eğer if bloğunda ki şart sağlanmaz ise else bloğunda ki şart devreye giriyor ve bu lok çalışıyor.
    print("Girdiğiniz Sayı Belirtilen Aralıkta Değildir.") # ekrana yazsırılıyor.

# çıktı:
# 1 ile 100 Arasında Bir Sayı Giriniz:85
# Girdiğiniz Sayı Belirtilen Aralıkta.
# program sonlandı.

# 1 ile 100 Arasında Bir Sayı Giriniz:101
# Girdiğiniz Sayı Belirtilen Aralıkta Değildir.
# program sonlandı.
