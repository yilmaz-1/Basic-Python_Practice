# # eval fonksiyon kullanımı
#
# bilgi= """
#
# İşlemler:
# Toplama : +
# Çıkarma : -
# Çarpma  : *
# Bölme   : /
#
# Yukarıdaki simgeleri kullanarak işlem yapabilirsiniz.
# Örnek : 24 + 4 şeklinde yazınız
#
# """ # burada program hakkında kullanıcıya bilgi veriyoruz.
#
# print(bilgi) # bu bilgiyi erkrana print ile basıyoruz.
#
# islem=input("Lütfen yapmak istedğiniz islemi giriniz : ") # burada islem isminde bir adet degisken tanımlıyoruz.
# # bu değişken içine ise input ile kullanıcıdan aldığımız değeri dönderiyoruz.
#
# hesapla= eval(islem) # burada kullanıcıdan aldığımız ve işlem içerisine yolladığımız ( 3*4 ,2+5 8/4, 3-1 gibi )
# # ifaderleri eval fonksiyonu içersine gönderip oradan gelen sonucu hesapla değişkenine yolluyoruz.
# # burada eval fonksiyonu tam olarak şunu yapıyor, bu eval fonskiyonu kendsine verilen değeri sanki python koduymuş
# # gibi işler.
#
# print(hesapla) # burada hesapla değişkeni ekrana bastırılıyor.

# **********************************************************************************************************

# eval fonksiyonu kullanımı
#
# deger= input("Lütfen istediğiniz python kodunu giriniz: ") # burada kullanıcıdan yapmak istediği işlemin kodunu
# # yazmasını istiyoruz.
#
# isle= eval(deger) # eval fonksiyonuna yukarıda kullanıcıdan aldığımız deger değişkenini yollayarak eval fonksiyonunda
# # işlenmesini sağlıoyruz. çünkü eval fonksiyonu içerisin egönderilen her şeyi python ksiyonu igib algılar ve işlemem
# # tabi tutar
#
# print(isle) # isle değişkeni ekrana bastırılıyor.
#
# # burada evalfonksiyonun şu şekilde bir güzelliği var: eval fonksiyonu içine gönderilen her ifadeyi python kodu gibi
# # algılayıp uygulamaya değerlendirmeye çalıştırmaya çalışıyor. fakat dikkat edilmesi gereken şey şu: eğer bu kod
# # sınırlandırılmaz ise sistemde açık verebilir.

#*************************************************************************************************************

print("""
Basit Bir Hesap Makinesi Uygulamsı.

İşlemler:
Toplama :+
Çıkarma : -
Çarpma  : *
Bölme   : /

Yapmak istediğiniz işlemi yazıp Enter tuşuna basınız.
( örnek: 3 ile 4 rakamının çarpımının sonucunu öğrenmek gibi. 3*4 yazıp Enter tuşuna basınız.)


""")

# veri= input("İşleminiz Giriniz: ") # kullanıcıdan ne işlme yapmak istiyorsa onu girmesini istedik
# hesap= eval(veri) # kulanıcının girdiği işlemi eval fonksiyonuna yolladık. Eval fonksiyonu bu işlemi değerlendirip
# # ne yapması gerektiği kendisi anladı ve sonucu otomatik olarak hesapladı.
# print(hesap)

# çıktı

# Basit Bir Hesap Makinesi Uygulamsı.
#
# İşlemler:
# Toplama :+
# Çıkarma : -
# Çarpma  : *
# Bölme   : /
#
# Yapmak istediğiniz işlemi yazıp Enter tuşuna basınız.
# ( örnek: 3 ile 4 rakamının çarpımının sonucunu öğrenmek gibi. 3*4 yazıp Enter tuşuna basınız.)
#
#
#
# İşleminiz Giriniz: 3*4
# 12

# ************************************************************************************

print("""

Basit bir hesap makinesi uygulaması.

İşlemler:

Toplama : +
Çıkarma : -
Çarpma  : *
Bölme   : /

Yapmak istediğiniz işlemi yazıp Enter tuşuna basın. 
( örneğin 3 ve 4 ün çarpımını öğrenmek içiçn 3*4 yazıp Entere basın)

""")

veriste= "1234567890/*-+,." # burada kullanıcının girmesi gerektiği veya bu listenin dışında birgiriş yaptığında
# programı sonlandırmak istediğimizi ifade ettik. Yani kullanıcı sadece bu listede yer alan işlemler ile ilgili
# işlem yapabilir.
veri=input("Yapmak İstediğiniz İşlemi Giriniz : ")# burada kullanıcıdan yapmak istediği işlemi girmessini istedik.

for i in veri: # burada for döngüsü kurularak kullanıcının girdiği veri içersindeki işlemleri i değişkeni olarak
    # alıyoruz.
    if not i in veriste: # for döngüsü ile aldığımız bu i değişkenleri bu if bloğunda kontrol ediliyor.
        # eğer veri içerisinden alınan bu i değerleri yukarıda önceden tanımlaan veriseti içersinde yok ise
        print("Hatalı İşlem Girişi Yaptınız:") # ekrana bu ifade bastırılıyor.
        quit()# ve program sonlandırılıyor.
    else: # eğer if not bloğu çalışmaz ise  bu lok çalışacak.
        hesap = eval(veri) # hesap isminde bir değişken oluşturuldu. bu değişkene eval fonksiyonu ile elde edilen
        # sonuç atandı
        print(hesap) # hesap değişkeni ekrana bastırıldı.
    break # program tekrar döngüye girmemesi için burada kırılıp sonlandırıldı.
