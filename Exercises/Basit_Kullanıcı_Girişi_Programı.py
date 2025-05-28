print("""
*************************
Kullanıcı Girişi Programı
*************************
""")

sys_kullanıcı_adı="mmehmet"

sys_parola= "12345"

giriş_hakkı=3

while True:
    kullanıcı_adı= input("Kullanıcı Adı:")
    parola = input("Parola:")
    if(kullanıcı_adı!=sys_kullanıcı_adı and parola==sys_parola ):
        print("Kullanıcı Adı veya Parola Hatalı...")
        giriş_hakkı-=1
    elif (kullanıcı_adı==sys_kullanıcı_adı and parola!=sys_parola):
        print("Kullanıcı Adı veya Parola Hatalı")
        giriş_hakkı-=1
    elif (kullanıcı_adı!=sys_kullanıcı_adı and parola!=sys_parola):
        print("Kullanıcı Adı veya Parola Hatalı...")
        giriş_hakkı-=1
    else:
        print("Sisteme Başarıyla Giriş Yaptınız...")
        break
    if (giriş_hakkı==0):
        print("Giriş Hakkınız Bitti...")
        break
# çıktı:
#*************************
# Kullanıcı Girişi Programı
# *************************
#
# Kullanıcı Adı:mehmet
# Parola:12345
# Kullanıcı Adı veya Parola Hatalı...

# ilk olarak print ile fonksiyonun adı ekrana bastırılıyor.
# daha sonra sisteme kullanıcı adı kullanıcı soy adı ve ilk başta kullanıcının kaç dene hakkı olduğunu tanımlıyoruz.
# while True döngüsü ile bu döngü altında kullanıcıdan input fonksiyonu ile kullanıcı adı ve parolasını istiyoruz.
# daha sonra if elif ve else bloklarında tek tek kullanıcının girdiği kullanıcı adı ve şifre kontorl edilip hangi blokta doğru olarak döngü döndü ise o blok içinde yer alan prin fonksiyonu ile ekrana bastırılıp ve giriş hakkı sayısı 1 azaltılıyor.
# programın sonunda tanımlanan if koşulu içinde yer alan giriş hakkı eşit sıfır şartı sağlandığında ise ekrana prit ile giriş hakkınız birmiştir yazıp break şe döngü sonlandırılmıştır.
