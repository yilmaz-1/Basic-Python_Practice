
stockEmail = "mmehmetisik@hotmail.com" # mevcut bir email tanımlıyoruz.
stockPassword = 12345 # mevcut bir şifre tanımlıyoruz.



enterYouremail= input("Email Adresinizi Giriniz:") # kullanıcıdan emailini girmesini istiyoruz.
enterYourPassword = int(input("Şifrenizi Giriniz:")) # kullanıcıdan şifresini girmesini istiyoruz. int fonksiyonu ile veri tipi dönüşümü yapılıyor.

if ( stockEmail == enterYouremail and stockPassword == enterYourPassword ): # if bloğunda sistemde kayıtlı mail adresi ile sistem de kayıtlı şifre kullanıcının girdiği mail adresi ve şifre ile karşılaştırılıyor. eğer bu her iki eşitlikte aynı anda eşleşiyorsa burada zaten bu eşleşme and operatörü ile sağlanmış,
    print("Sisteme Başarı İle Giriş Yaptınız...") # ekrana yazdırılıyor.
elif (stockPassword !=enterYourPassword or stockEmail != enterYouremail): # if bloğunda ki şart sağlanmaz ise bu blok çalışıoyr. sistemde kayıtlı mail ile sistemde kayıtlı şifre, kullanıcının giridği mail ve şifre ile karşılaştırılıyor. herhangi birisi eşit değilse,
    print("Email veya şifreniz hatalı.") # ekrana yazdırılıyor.
else: # yularıda ki her iki durum sağlanmaz ise if ve elif bloklarında yer alan durumlar
    print("Geçersiz Giriş Yaptınz") # ekrana yazdırılıyor.









































