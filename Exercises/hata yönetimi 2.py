# x = 10
#
# if x > 5 : # burada if ile bir koşul tanımladık.
#     raise Exception (" x 5 den büyük değer alamaz.") # burada raise komutu ile hata fırlattık yolladık kullaınıcıya.
#     # burada amacımız hata msjını dışarıya yollamak.

# def check_password(psw):  # burada bir adet fonksiyon tanımladın. bu fonskiyon bir argümanlı yani bir objesi vardır.
#
#     import re # bruada bir adet modül import ettik program içerisine. Bu modülün adı Regular Expression.
#     # bu modül düzenli ifadeler anlamına gelmektedir. dağınık bir metin içerisinde istediğimiz formattaki metinleri
#     # yakalayabilmemize imkan tanır. yani girdiğimiz şifre mail adresi yazı vs gibi metinler içerisnde istediğimiz
#     # formattaki ifadeyi yakalamamıza olanak sağlar.
#
#     if len(psw) < 8:  # eğer bu password 8 karakterden küçük ise
#         raise Exception("parola en 8 karakterli olmalıdır.")  # raise Exception komutunu kullanarak kullaıcıya parantez
#         # içinde özel olark tanımladığımız hata mesajını yolla.
#
#     elif not re.search("[a-z]", psw): # burada bir adet elif not bloğu oluşturuldu ve re modülünün search fonskiyonu
#         # ile girilen password içerisinde a dan z ye kadar harf araması yapması isteniyor. if koşulu sağlanmadı ise
#         # program bir sonraki kod bloğuna geçiyor yani elif not kod bloğuna geçiyor. Burada deniyor ki: girilen password
#         # içerisinde arama yaptığında a dan z ye kadar olan harflerden birisi yer almıyor ise "elif not bu demek yani
#         # sağlanmıyorsa " en az bir tane harf olsun diyor girilen password içerisinde. en az bir harf yoksa bu
#         # kod bloğundaki şart sağlanmış olacak böylelikle bu kod bloğunun altında yer alan buna dahil olan
#         # bu kod sağlandığında çalışacak olan diğer kodlara geçiyor program.
#         raise Exception("parola küçük harf içermelidir.") #  elif not kod bloğunda hatayı yakaladığımızda yani elif not
#         # kod bloğu çalışırsa, raise Exception ile kulanıcıya parantez içersinde yer alan
#         # hata mesajını göster fırlat dedik.
#
#     elif not re.search("[A-Z]", psw):
#         raise Exception("parola büyük harf içermelidir.")
#
#     elif not re.search("[0-9]", psw):
#         raise Exception("parola rakam içermelidir.")
#
#     elif not re.search("[_$@]", psw):
#         raise Exception("parola alpha numeric karakterler içermelidir.")
#
#     elif re.search("/s",psw): # burada üst satırlarda yer alan kod bloklarında olduğu gibi fakat bir farkla çalışıyor.
#         # üstte ki kod bloklarında yer almaz ise olmaz ise sağlanmaz ise şartı varken bunda sağlanırsa olursa şartı var.
#         # girilen password içerisnde eğer boşluk varsa bunu bu kod bloğunda yakalıyor, ve bir sonraki devamındaki
#         # bu kod bloğu çalıştığında çalışan kod bloğuna geçiyor program.
#         raise Exception("parola boşluk karakteri içermemelidir.") # raise Exception ile kullanıcıya
#         # prantez içerisinde yer alan hata mesajı fırlatılıyor gönderiliyor.
#
#     else: # eğer burada yukarıdaki hiç bir koşul sağlanmaz ise demek ki kullanıcı bizim istediğimiz bütün koşulları ve
#         # kuralları sağlayan bir parola girdi ve hiç bir kod bloğu çalışmadan bu kod bloğuna geldi program.
#         # Bu kod bloğu çalıştığında print ile ekrana yazdıracak.
#         print("geçerli parola...")
#
#  # yularıdaki fonkiyonun tanımlanması bitti. artık bu fonksiyon çağrılacak.
#
# while True: # burada bir adet döngü oluşturuldu. Bu döngü sağlandığı sürece doğru olduğu sürece döngü çalışsın dedik.
#     password = input("Parola Girniz:")#burada her döngü başında input ile kullanıcıdan bir adet şifre girmesini istedik
#
#     try: # burada try kod bloğu altında deneyeceğimiz fonskiyon çağırdık.
#         check_password(psw=password) # çağırdığımız fonskiyon
#     except Exception as ex: # burada denediğimiz fonksiyon içerisinde bir hata varsa yakalamak için except bloğunda
#         # bu hatayı yakaladık ve bu hatayı Exception as ex diyerek yani yakaladığımız hatayı ex objesi olarak atadık.
#         print(ex) # burada ise except kısmında yakaladığımız ve ex objesi olarak atadığımız hatayı print ile
#         # ekrana yazdırdık.
#     else: # eğerki try bloğunda kontrol ettiğimiz fonksiyon except kısmında hata yakalayamadıysak yani fonksiyon
#         # içerisinde tanımladığımız hataları vermediğiyse bu kod bloğu çalışacak
#         print("parola geçerli") # ekrana yazdırılacak.
#         break # else bloğu çalırsa döngü burada kırılacak ve başa dönmeyecek.
#     finally: # bu blok her durumda çalıştırılıyor.
#         print("validation tamamlandı.")


class Person: # burada bir adet person isminde bir class tanımlandı.
    def __init__(self,name,year): # bu class içerisinde bir adet fonskiyon tanımlandı ve bu foksiyonun objeleri ise
        # name ve year bilgisidir.
        if len(name)>10: # eğer name objesine girilen karakter sayısı 10 dan büyük ise
            raise Exception("name alanı fazla karakter içeriyor...") # raise Exception ile bize bir hata fırlat yolla.
        else: # değilse porgram normal bir şekilde çalışıp bitsin.
            self.name=name



p= Person(name="Aaaaa",year="ngsg") # burada Person class ı üzerinden bir adet p objesi oluşturuldu.































