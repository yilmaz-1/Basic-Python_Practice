"""
Python da bir verinin tipinin ne olduğnu öğrenmek çok önemlidir. çünkü veri tipine göre yapacağımız işlemler
kullanacağımız fonksiyonlarda değişmektedir. en önemliside o veri ile ne yapabileceğimizi ne yapamayacağımızı o verinin
tipinden anlayabiliriz.
python da "" çift tırnak içerisnde yazılan her şey karakter olarak kabul edilir ve karakter dizileri üzerinde yapılan
fonksiyonlar işlemler metodlar kullanılır.
örenek

"3" burada  karakter olarak tanımlandı demektir. artık python bundan sonra bu 3 verisi ile ilgili karakter dizisi
işlemlerini yapar. string olarak yani karakter olarak tanımlanmış oldu.

Eğer çift tırnak kullanamdan yazsaydık; 3 ifadesi karakter olmayacaktı. ve böylelikle bu 3 ifadesi sayısal bir ifade
oalcaktı.

"" çift tınak içine yazılan her şey karakter yani string ifade olarak tanımlanır.

Bir verinin tipini öğrenmek istiyorsak type() fonksiyonu ile kolaylıkla öğrenebiliriz

print(type("3"))
<class 'str'>    Görüldüğü üzere sayısal bir ifade tırnak içinde yazılınca karakter dizisi olarak algılandı.

print(type(3))
<class 'int'>   Görüldüğü üzere sayısal bir ifade tırnak içinde yazılamayınca sayılsal olarak algılandı.

Eğer karakterlerden oluşan bir ifadeyi tırnak içinde belirtmez isek, o ifade python tarafından integer olarak
tanımlanmaya çalışılacak. Bundan dolayı program hata verecektir.

print(elma)
NameError: name 'elma' is not defined

print("elma")
elma

Pyton da birçok veri tipi vardır. şu aşamada integer ve string veri tiplerini göreceğiz.


Aşağıdaki Örnekleri Dikkatlice İnceleyelim

"""
print("Mehmet""Işık")

# MehmetIşık

print("Mehmet","Işık")

# Mehmet Işık

print("Mehmet" " " "Işık")

# Mehmet Işık

print("w"*3)

# www

print("3"*3)

# 333   Burada 9 yerine 3 tane 3 ü yan yana yazdı? sebebi şu: ilk 3 ifadesi çift tırnak içerisinde karakter dizini
# olarak tanımlanığı için  python sayılsal işlem yapmadı. 3 tane 3 ü yan yana yana yazdı. Tekrarlama işlemi yaptı

# print("3"+2)

# can only concatenate str (not "int") to str   program hata verdi. Burada diyor ki sadece string ifadeleri birleştirme
# yapabilirsin. string ile integer ifadeyi birleştirme yapamazsın diyor. Ayrıca eksi (-) ve bölü (/) işlemşerini
# karakter dizileri üzerinde kullanamıyoruz.

print("3"+"2")

# 32    Bu örnekte çıktı ifade karakter bir ifade olmuştur. şöle ki eğer istediğimizi yapsaydı sonuç 5 olacaktı ve bu
# ifade de int bir veri tipi olacaktı. ancak program çift tırnaktan dolayı her iki ifadeyi str bir ifade olarak algıladı
# iki str ifadeyi birleştirme yapar gibi yaptı yan yana yazdı. sonuç otuziki değil birleşmiş 32 oldu.

print(3+2)

# 5     her iki ifade veri int bir veri olduğu için sayısal olarak işlem yapıldı. sonuç beş çıktı.


"""
veri tipi dönüşüşmü yaparken bir ondalıklı sayıyı tam sayıyıya vyea tam sayıyı ondalıklı sayıyı çevirmek için
kullandığımız iki fonksiyon vardır. bunlar float ve int fonksiyonlarıdır. int fonksiyonu ondalıklı sayıyı tam sayıya
çevirmek için kullanılır. float fonksiyonnu ise tam sayıyı ondalıklı sayıya çevirmek için kullanılır.

"""
a = 43
b = 12.5

print(int(b))
# çıktı:
# 12

print(float(a))

# çıktı:
# 43.0

"""
Veri tipi dönüşümü yaparken, girilens sayısal ifadeyi string bir ifadeye çevirmek için str() fonksiyonunu kullanırız.
Fakat string bir ifade her zaman integer ifadeye çevrilemeyebilir. string bir ifade integer ifadeye çevrilebilmesi için
string ifadeye içeren her bir karakter 10 luk tabana göre bbir rakam içeremelidir. örenğin: 1234546 doğru 
asddb1253 yanlış ( bu ifade integere çevrilemez )

"""

c = 123  # burada c değişkeni integer bir ifade iken
d = str(c)  # d değişkeni str fonksiyonun ile string bir ifadeye dönüşmüştür.
print(type(d))
# çıktı:
# <class 'str'>
