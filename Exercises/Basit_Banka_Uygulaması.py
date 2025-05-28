print("""
**************************
Erşan Bank a Hoşgeldiniz...
***************************
"""
      ) # burada print fonksiyonu kullanrak banka adını ekrana yazdırdık.

print("""
Yapmak İstediğiniz İşlemi Seçiniz

1. Bakiye Sorgulama.

2. Para Yatırma

3. Para Çekme. 

4. İşlemi İptal Et.


"""
      ) # burada ise ekrana yapmak istediğimiz işlem menülerini ekrana yazdırdık.



bakiye= 2000 # golbalde bir adet bakiye değişkeni tanımladık. döngü dışı bir değişken bu. döngü ile alakası yok.
# ama döngü sonda kullanıcıdan alacağımız veriler ile değişebilir.

system_onay="e" # bir adet onay değişkeni tanımladık. sebebi ise program içerisinde bu onayı kullanıcıya sorarak
# kullanmak için.

system_red="h" # bir adet red değişkeni tanımladık. aynı onay gibi bu da programımızın içerisnde kullanacağız.

sys_userName="mmehmet"
sys_passcode= 1234
pass_number=3

user_Name = input("Kullanıcı Adınızı Giriniz: ")
user_passcode =int(input("Kullanıcı Şifrenizi Giriniz: "))

if sys_userName==user_Name and sys_passcode==user_passcode:


while True: # burada bir döngü bloğu oluşturduk. bu döngü bloğunun koşulu ise True ifadesi dir. Yani burada
    # şu denilmektedir: bu döngü doğru olduğu sürece yani sağlandığı sürece ( True ) olduğu sürece sürekli
    # başa dönsün ve çalışsın.

    işlem=input("Yapmak İstediğiniz İşlemi Seçiniz:") # burada ise işlem isminde bir adet değişken tanımlanmıştır.
    # Bu değişken ise input fonksiyonu ile kullanıcıdan dışarıdan alınmıştır. burada amaç şu: eğer bu işlem değişkeni
    # döngü dışında tanımlanmış olsa idi sonraki yazdığımız kodlarda bu eğer tekrar döngü başa döndüğünde yeniden işlem
    # menüsünden işlem menüsünden işlem seçmemiz gererkli olsa idi bunu elde edemeyeceğimiz için bu işlem değişkeni
    # döngü içerisinde tanımlandı.

    if (işlem == "1"): # burada if bloğu içerisinde bi koşul bloğu oluşturuldu. eğer kullanıcıdan alınan işlem isimli
        # değişken 1 str ifadesine eşit olursa
        print("Bakiyeniz:",bakiye) # ekrana print ile bakiye değerini yazdır.

    elif (işlem=="2"): # eğer işlem değişkeni 2 str ifadesine eşit olursa
        tutar=int(input("Yatırmak istediğiniz Tutarı Giriniz:")) # kullanıcıdan input ile yatırmak istediği tutarı al
        # ve onu int tipine dönüştür. dönüştürülmüş bu değeri tutar isimli değişkene at.
        kullanıcı_onay=input("Onaylyorsanız 'e' Onaylamıyorsanız 'h' Yazın:") # burada ise kullanıcıdan input ile
        # onay istiyoruz. bu tutarı yatırmak isteyip istemdiği ile ilgili.

        if(kullanıcı_onay == system_onay): # burada ise eğer kullanıcıdan aldığımız onay sistemdeki onay ile eşleşirse
            # yani e ise
            print("Yatırılan Tutar {} :".format(tutar)) # ekrana yatırmak istediği tutarı yazdır.
            bakiye +=tutar # burda ise döngü dışında tanımlanan bakiyeye yatırmak istediği tutarı ekle
            print(f"Yeni Bakiyneiz: {bakiye}") # ekrana yeni bakiyeyi yazdır.

        elif (kullanıcı_onay == system_red): # burada ise kullanıcının red verme durumunda yapılacak işlemi tanımladık.
            print(f"Mevcut Bakiyeniz: {bakiye}") # ekrana bakiye değeri yazdırılıyor.
            print("Ana Menüye Yönlendiriliyorsunuz...") # kullanıcının ana menüyü yönlendirildiği bilgisi veriliyor.
            print("""
            Yapmak İstediğiniz İşlemi Seçiniz

            1. Bakiye Sorgulama.

            2. Para Yatırma

            3. Para Çekme. 

            4. İşlemi İptal Et.


            """) # burada ana menü bilgisi ekrana yazdırılıyor.
            continue # hiç aşağıdaki kodları okuma direk döngü başına dön ve yeniden başla döngüye demek.

    elif (işlem == "3"): # burada ise kullanıcı ana menüden 3 numaralı işlemi seçmesi durumunda yapılacak
        # işlemler sıralandı.

        çekme=int(input("Çekmek İstediğiniz Tutarı Giriniz: ")) # burada kullanıcıdan input ile çekmek istediği
        # değeri alıyoruz ve bunu da int fonksiyonu ile veri tipi dönüşümü yapıyoruz.

        kullanıcı_onay = input("Onaylyorsanız 'e' Onaylamıyorsanız 'h' Yazın:") # burada input ile kullanıcından
        # bir adet input fonksiyonu ile onay durumu bilgisi alıyoruz.

        if ((bakiye - çekme) > 0): # burada ise kullanıcının çekmek istediği mikraın kontorlü yapılıyor.
            # bu çekmek istediği miktarın  bakiyeden büyük olması durumunda bu koşul bloğu çalışacak.

            if (kullanıcı_onay == system_onay): # burada ise kullanıcıdan alınan onay ile
                # sistedmde kayıtlı olan onay bilgisi karşılaştırılıyor. eğer aynı ise bu kod bloğu altıdaki
                # kodlar çalışacak.

                print("Çekilen Tutar {} :".format(çekme)) # ekrana kullanıcın çekmek istediği miktar basılacak.
                bakiye -= çekme # burada ise döngü dışında tanımladığımız bakiyeden bu çemkmek isdeğimiz
                # miktar düşülecek.
                print(f"Yeni Bakiyeniz: {bakiye}") # ekrana yeni bakiye yazdırılacak.

            elif (kullanıcı_onay == system_red): # burada ise kullanıcıdan alınan onay bilgisi red olması halinde
                # yapılacak işlemler tanımlanmışyır.

                print(f"Mevcut Bakiyeniz: {bakiye}") # ekrana kullanıcının mevcut bakiyesi yazdırılacak.

                print("Ana Menüye Yönlendiriliyorsunuz...") # kullanıcı tekrardan ana menüye yönlendirildiği bilgisi
                # ekrana yazdırılıyor.

                print("""
                Yapmak İstediğiniz İşlemi Seçiniz

                1. Bakiye Sorgulama.

                2. Para Yatırma

                3. Para Çekme. 

                4. İşlemi İptal Et.


                """) # ana menü bilgileri yazdırılıyor.
                continue # burada şu deniyor: aşağıdaki hiç bir kodu okuma . direk döngübaşına dön ve yeniden başla.

        else: # burada ise kullanıcının çekmek istediği bakiye yetirsiz ise yani mevcut bakiyesinden daha büyük
            # bir bakiye çekmek istemesi durumunda çalışacak.

            print("Bakiyeniz Yetersiz..") # ekrana bakiyenin yetersiz olduğu bilgisi yazdırılacak.
            print("Ana Menüye Yönlendiriliyorsunuz...")  # kullanıcı tekrardan ana menüye yönlendirildiği bilgisi
            # ekrana yazdırılıyor.
            print("""
            Yapmak İstediğiniz İşlemi Seçiniz

            1. Bakiye Sorgulama.

            2. Para Yatırma

            3. Para Çekme. 

            4. İşlemi İptal Et.


            """) # ana menü bilgileri ekrana yazdırılıyor.
            continue # devamındaki hiç bir kod çalıştırılmadan döngü başa dönüyor.

    elif (işlem=="4"): # kullanıcının 4 numaralı işlemi seçmesi durumunda,
        print("İşleminiz İptal Edilmiştir.") # işelmin iptal yazısı ekrana yazdırılıyor.
        print("Programdan Çıkış Yapılıyor...") # programdan çıkdılığının bilgisi veriliyor.
        break # ve burada ise program burada kırılarak sonlandırılıyor. döngü başa dönmüyor.
    else: # eğer kullanıcı bilgi işlem menüsünde yer alan işelmlerden her hangi birini seçmemesi durumunda
        # yapılacaklar tanımlanmıştır.
        print("Geçersiz Giriş Yaptınız.") # geçersiz giriş yaptınız bilgisi ekrana yazdırılıyor.
        print("Ana Menüye Yönlediriliyorsunuz...") # kullanıcı ana menüye yönlendirliyor. bilgisi veriliyor.
        print("""
        Yapmak İstediğiniz İşlemi Seçiniz

        1. Bakiye Sorgulama.

        2. Para Yatırma

        3. Para Çekme. 

        4. İşlemi İptal Et.


        """) # bilgiler ekrana yazdırılıyor.
        continue # döngü tekrar başa dödüyor.


#çıktı:
# **************************
# Erşan Bank a Hoşgeldiniz...
# ***************************
#
# Yapmak İstediğiniz İşlemi Seçiniz
#
# 1. Bakiye Sorgulama.
#
# 2. Para Yatırma
#
# 3. Para Çekme.
#
# 4. İşlemi İptal Et.
#
# Yapmak İstediğiniz İşlemi Seçiniz:1
# Bakiyeniz: 2000
# Yapmak İstediğiniz İşlemi Seçiniz:2
# Yatırmak istediğiniz Tutarı Giriniz:300
# Onaylyorsanız 'evet' Onaylamıyorsanız 'hayır' Yazın:evet
# Yatırılan Tutar 300 :
# Yapmak İstediğiniz İşlemi Seçiniz:1
# Bakiyeniz: 2300

# bu program basit banka işlemleri yapmamızı sağlayan bir programdır.
# ilk olarak print ile bankanın ismi ve yapmak istediğimiz işlemler ile ilgili bilgileri ekrana basıyor.
# daha sonra sisteme bakiye, onay ve red bilgilerini tanımlıyoruz.
# while True döngüsü ile program yazılmaya başlıyor. burada while yanında True yazılmasının  sebebi program doğru çalıştığı sürece sürekli bize ne yapmak istediğimiz soracaktır.
# ilk if bolğunda işlem 1 i seçersek direk print fonksiyonu ile ekrana işlem bir de tanımlana durum ekrana basılıyor.
# eğer işlem 2 yi seçersek elif bloğunda yazılan koşul devreye girer ve bizden yatırmak istediğimiz miktarıkullanıcıdan alırız. daha sonra bu tutarı yatırmak istediğimiz tutarı onaylama kodu çalşıyor ve bizden onylayaıp onaylamayacağımızı evet veya hayır ile yazmamızı istiyor.
# devamında if bloğu çalışıyor ve kullnıcını verdiği onay ile sistemde kayıtşı olan onayı karşılaştırıyor.eğer karşılaştırma doğur ise ekrana print ile yatırılan tutuarı bastırıyor ve bakiyeye yatırılan tutuar ekleniyor. eğer karşılaştırma doğru değilse elif bloğunda print ile ekrana çıkış yapılıyor yazıyor ve break ile döngü kırılıyor.
# eğer işlem 3 ü seçersek elif bloğunda yer alan işlem 3 ile ilgili kodlar çalışmaya başlıyor.
# kullanıcıdan çekmek istediği miktarı ve kullanıcı onayını soruyor.
# daha sonra elif bloğu altında yer alan if foksiyonu devreye giriyor.
# (bakiye - çekme) > 0 koşulu sağlanıyorsa eğer tekrardan bir tane if koşulu devreye giriyor ve kullanıcıdan sistem onayı istiyor. eğer sistem onayı kullanıcı onayı ile eşleşiyor ise bloğun devamında ki print fonksiyonu ile ekrana çekilen tutar yazılıyor ve devamında bakiyeden çekilen miktar düşülüyor.
# eğer kullanıcı onayı ile sistem onayı eşleşmiyor ise elif bloğunda yer alan kod da print ile çıkış yapılıyor yazılıyor ve break ile döngü sonlandırılıyor.
# (bakiye - çekme) > 0 if bloğunda ki bu koşul sağlanmaz ise bu bloğun else bloğunda yer alan print foksiyonu devreye girer ve ekrana bakiye yetersiz yazar conntinue ile döngü sonlanmadan döngü başa döner.
# eğer işlem 4 seçilir ise elif bloğundaki print işlemi çalışır ve ekrana işleminiz iptal edilmiştir yazılır break ifadesi ile de döngü sonlanır.
# en sondaki else komutu ile de ekrana geçersiz işlem yaptınız yazılır ve break şle döngü kırılır.
#

