"""
neden değişken tanımlama gereği duyuyoruz?
n=525571191316 gibi bir değişken tanımlayalım ve değişkene 525571191316 değeri atalım. yüzlerce veya binlerce satırdan
oluşan bir program yazdığımızı düşünelim. böle bir programda her defasında sayısal değerini kullanmak yerine
n değişken ifadesini kullanmak ve daha mantıklı olacaktır. bu yüzden değişken tanımlamak çok önemlidir.


python da değişken belirlemek tanımlamak nerdeyse sınırsızdır. ama bazı kurallar çerçevesinde.

1- Değişken adları bir sayılsa veri ile başlayamaz

3_kalem=5   veya
356= "ahmet"

2- Değişken adları mateamtiksel ifadeler ile başlayamaz

+= "kalem" veya
*= 3

3- değişken ifadeleri _ alt tire sembolü ile başlayabilir.

_ahmet="mehmet"
_n=5

4- Değişken tanımlarken türkçe karakter kullanabilirsiniz ama ileride beklenmekdeik bir durum oluşmasına karşın tavisye
edilmez.

5- Pythonda tanımlı ifadeler değiken ismi olarak kullanılamaz. Bunlar programda özel anlam ifade eden kelimeler.

'False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await', 'break', 'class', 'continue', 'def', 'del',
'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal',
'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield'

bu kelimeleri ilk başta ezberlemek oldukça zor olabilir. ama aşağıdaki kodu kullanarak bu listeye ulaşabilirisniz.

import keyword
print(keyword.kwlist)

6- ayrıca python da tanımlı fonksiyonların isimlerini de değişken adı olarka da kullanamazsınınz.

"type" , "len" vb.

bu şekilde bir tanımlama yaptığınız durumda o fonksiyonu kullanamayabilirsiniz. ve bu hatayı bulmak çok zor da oalbilir.
bundan dolayı

del foksiyon ismi yazılarak bu hatadan kurtulabilirisniz. tabi hatanın bundan kaynaklı olduğunu anlayabilirseniz.

7- değişken tanımlama yapılırken kelimeler arasında boşluk bırakılmaz. fakat kelimeler arasında _ işarete konabilir.

ilk sayı = 5    yanlış kullanım

ilk_sayı = 5    doğru kullanım


"""

# Değişken Değerinin Değiştirilmesi

a = 5
b = 6

print(a)
print(b)
# çıktı: a ve b değerlerini 5 ve 6 olarak yazdırıyoruz.
# 5
# 6

a, b = b, a  # burada a ve b değerlerini birbiri ile değiştirip yeniden yazdırıyoruz.
print(a)
print(b)
# çıktı: a ve b değerlerini 6 ve 5 olarak yazdırıyoruz.
# 6
# 5

"""
UYGULAMA

Bu uygulamada yol masraflarımızı en temel öğrendiğimiz yöntemler ile hesaplamaya çalışacağız. Böylelikle üstte 
bahsettiğimiz kurallarıda tekrar etmiş olacağız.

1 - Cumartesi ve pazar günleri çalışmıyoruz.
2 - Ayda 22 gün çalşıyoruz.
3 - Evden işe gitmek için kulldığımız taşıtın ücreti 1.4 tl
4 - İşten eve dönmek iç,in kullandığımız taşıtın ücreti 1.5 tl

"""

calisilan_Gun_sayisi = 22

gidis_ucreti = 1.4

donus_ucreti = 1.5

masraf = calisilan_Gun_sayisi * (gidis_ucreti + donus_ucreti)

print(masraf)

# 63.8

# Not : python da matematikte geçerli olan işlem sırası önceliği vardır.

"""
Değişkenleri birbiri ile değiştirme

bir değişkenin değerini diğerine atamak için yeniden tanımlamaya gerek olmadan yapmanın çok basit bir yöntemi var.


"""

tuncay = "yasli"
mehmet = "genc"

print(tuncay)
print(mehmet)
# yasli
# genc

mehmet, tuncay = tuncay, mehmet

print(tuncay)
print(mehmet)
# genc
# yasli
