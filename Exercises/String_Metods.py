"""

capitalize()    Bu metodda string bir ifadeinin ilk harfini büyük hale getirmede kullanılır. fakat ilk karakter
                harf değilse yani alfabetk değilse, o ifade büyütülmez. olduğu gibi kalır.


center()        Bu metod da parantez içerisnde belirtilen sayı kadar string ifadeyi sağdan ve soldan boşluk bırakarak
                ortalar. farklı durumlar örenekler üzerinden anlatılacak.

casefold()      string ifadede ki bütün karakterleri küçük hale getir.

count()         parantez içine verdiğimiz değerin, ifadenin (argüman) o değişken içerisinde
                kaç defa geçtiğini bulmaya yarar


"""

string="mehmet ışık"
print(string.capitalize())
# çıktı:
# Mehmet ışık

string_1="/ mehmet ışık"
print(string_1.capitalize())
#çıktı:
# / mehmet ışık

string_2="hayat"
print(string_2.center(25)) # burada hayat ifadesi ortaya alındı sağdan ve soldan boşluk bırakıldı.
#çıktı:
#          hayat

print(string_2.center(7,"*"))
#çıktı:
# *hayat*

string_3="Mehmet HASAN AhmEt"
print(string_3.casefold())
#çıktı:
# mehmet hasan ahmet

string_4= "4552& MehmEt"

print(string_4.casefold())
# çıktı:
# 4552& mehmet

string_5="mehmet ışık karabük üniversitesi makine mühendisliği bölümü mezun öğrencisi"
print(string_5.count("i"))
#çıktı:
# 9

string_6= "mehmet kaya hasan aykut fatma" # burada string_6 isminde bir string tanımlandı.
substring= "a" # yukarıda tanımlanan string_6 içersinden bir adet alt string ifadesi tanımlandı. substring olarak.
print(string_6.count(substring,12,20)) # burada string_6 ifadesi içersinde substring olarak tanımlanan alt stringi
# 12. indeksten başlayarak 20. inddeksekadar sayacağız. yani bu aralıkta kaç tane olduğunu sayacağız.





