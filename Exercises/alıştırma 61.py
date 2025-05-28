"""
Hata Yakalam - try, ecxept, finally blokları
bu konuda hata yakalama ve bunları ile ilgili mesajları nasıl yazdıracağımızı öğreneceğiz.

try:
    Hata çıkarabiliecek bütün kodlar buraya yazılıyor.
    Eğer hata çıkarsa program uygun olan except bloğuna girecek.
    Hata oluşursa try bloğunun geri kalanındaki işlemler çalışmayacak
except Hata1:
    Hata1 oluştuğunda burası çalışacak.
except Hata2:
    Hata2 oluştuğunda burası çalışacak.
    //
    //
    //
    //
    //
finally:
    Mutlaka çalıması gereken kodlar buraya yazılacak. Bu blok her türlü çalışacak.


"""

"""


a = int("asfnaogfne")
print(a)


yukarıdaki kod çalıştırıldığında hata verecek. 

Traceback (most recent call last):
  File "D:\PYTHON\kotlamalar 3\ boş2.py", line 24, in <module>
    a = int("asfnaogfne")
ValueError: invalid literal for int() with base 10: 'asfnaogfne'

=> yani diyorki int fonskiyonu sadece integer olan ifaderler için kullanılır. 10 tabanda yazılan sayılar için kullanılır 
bizim ifade bu şartları sağlamadığı için hata verdi.
peki biz durumu nasıl çözeriz? aşağıdaki kod da görüldüğü gibi çözülür.

"""


"""

try: # hata oluşturucak bütün bu koddlar bu blok içerisine yazıldı. hata oluştuğunda bu kod bloğu çalıştı.
    a = int("asfnaogfne")
    print("program try bloğu içersinde çalıştı.")
except: # burada ise bize verilecek msj yazıldı. burada bir durum var. biz hatanın türünü yazmadık. direk except deyip
    # bıraktık. bu durumda python oluşabilecek bütün hatalar bu except bloğu içersine girecek. buda bize hangi tür hata
    # oluşturuğunu tespit edememize neden olacak. Eğer buraya except ValueError yazsaydım bu sefer de sadece valueerror
    # hatası verdiğin de program bu kod bloğu çalışacaktı. buraya giercekti.
    print("Bir hata oluştu...")


"""


"""
try: # bu blok içerisine hata çıkabiliecek kodlar yazıldı. bu blok içersinde yer alan a, b  ve a/b ifadesi hata verecek
    # kodlar. Çünkü a ve b değerleri int formatında girilmediği zaman program hata verecek. Diğer bir yandan a/b ifadesi
    # eğer b ifadesi int olmasına rağmen sıfır (0) girlirse bu kod da hata verecekdir. İşte bu hata verme ihtimaline
    # karşı hata çıkaracak kodlar bu blok içersine yazıldı.
    a = int(input("Sayı1:")) # burada kullanıcıdan bir a değeri girmesini istedik.
    b = int(input("Sayı2: ")) # burada kullanıcıdan bir sayı girmesini istiyoruz.
    print(a/b) # kullanıcının girdiği a ve b değerli matematiksel bir işleme bölme işlemine tabi tutularak print ifadesi
    # ile ekrana yazdırılıyor.
except ValueError: # yukarıda try bloğu içerisine yazdığımmız kodlar hata vereceğini bildiğimiz içi onları oraya yazdık.
    # Şimdide bu blok içerisine ise try bloğu içerisine yazdığımız kodların hata mesajlarını yazacağız. Yukarıdaki
    # kodlarda az çok hangi hatayı vereceğini programcı olarak tahmin ettiğimiz için o hata mesajını blok içine
    # yazıyoruz. istersek bütün hata mesajlarını tek blok da tanımlayabiliriz [except(ValueError,ZeroDivisionError)]
    # veya ayrı ayrı blok lar ile de tanımlama
    # yapabiliriz. Şöyle bir durumda da olabilir: hangi hata mesajını bize döndüreceğini eğer tahmin edemiyorsak
    # bilemiyorsak, hiç bir hata msj adı yazılmdan da tanımlama yapılabilir. Hata mesajı olmadan yapılan tanımlamada,
    # python da yer oalan yani gömülü olan bütün hata durumları bu kod bloğu içerisine gireibilir. Hata mesajı
    # tanımlanır ise sadece o hata mesajı o kod bloğuna girer.
    print("Lütfen doğru formatta giriniz..") # burada ise print ile kendi hata mesajımızı ekrana yazdırıyoruz.
except ZeroDivisionError: # bir önceki except bloğunda olduğu şeylrein aynısı burada da oluyor. Sadece hata türleri
    # farklı.
    print("Bir sayı sıfıra bölünemez.")# python da varsayılan hata mesajı yerine bizim kendi mesajımız bize gösterilecek
finally: # bu kod bloğu ise mutlaka çalışmasını istediğim kodlraın yazıldığı yerdir. Eğer biz bir kodun mutlaka
    # çalışmasını  istiyorsak onu bu kod bloğu içersine yazıyoruz.
    print("Finally bloğu çalıştı...")
print("Bloklar sona erdi.")# bütün bloklar bittiğinde ise bu kod çalışacak. bu kod , try except bloğundan bağımsızdır.
"""



"""
HATA FIRTLATMA 

Bazen kendi yazdığımız fonskiyonlar yanlış kullanılırsa kendi hatalarımızı üretip Python da bu hataları fırlatabilirz.
Bunun için ise raise anahtar kelimesini kullanacağız. Hata fırlatma kalıbı aşağıdaki gibidir.

    raise HataAdı(opsiyonel Hata Mesajı)

"""

def terscevir(s): # burada tercvir isminde bir argümanlı bir fonksiyon tanımlandı.
    if type(s)!=str: # eğer bu fonskiyonun içine gönderilen s değişekninin tipi (type) string bir ifade değilse,
        # yani sayılsal bir ifade ise, harflarden veya diğer karakletlerden oluşmuyor ise
        raise ValueError("Lütfen Doğru Formatta Giriniz.")# program bize ValueError hatası verecek veingilizce mesaj
        # yazacak. Biz bu python da gömülü olan mesaj yerine kendimizin belirlediği mesajı yazdırmak fırlatmak istiyoruz
    else: # değilse, yani istediğimiz formatta str string ifade girildi ise
        return s[::-1] # ifadeyi ters çevir ve return ile fonksiyonu çağırdığımız yere gönder.

print(terscevir(s=123)) # program print fonskiyonu içerisnde çağrılıp ekrana yazdılırılıyor.

 # yukarıda bir fonksiyon tanımlandı. Bu fonskiyon hata çıkarma durumu da olabilir. zaten biz bu durumu fonskiyon
# içersinde raise ile fırlattık. Şimdi ise try except finally ile de bu hatayı yakalayalım.

try:
    print(terscevir(s=12)) # fonksiyonun bu blok içersine alınmasının en büyük sebebi ise bu fonskiyon hata veerebilecek
    # kodlar olduğu için. hata oluştuğu zaman try bloğu içerisinde yakalanması için bu blok içersine yazıldı.
except ValueError: # bu blokta ise hata yakalandı.
    print("Fonksiyon Hata Verdi...") # ekrana yazdırıldı.














