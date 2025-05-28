x = "mehmet"  # x değişekni tanımlanmış ve bu değişkene mehmet string ifadesi atanmış.
y = x.isalpha()  # y değişkeni tanımlanmış ve bu değişken içinde x değişkeninin bütün indeksleri alfabetik mi değil
# mi kontorl edilmiş.
print(y)  # print ile de y değişkeni ekrana bastırılıyor.

a = "mehmet veli"  # a isminde bir değişken tanımlanıyor ve içerisine mehmet veli değişkeni atanıyor. bu ifadeler
# arasında boşluk da var.
b = a.isalpha()  # b değişkeni tanımlanıyor ve yukarıda tanımlanan a değişkenin bütün
print(b)

c = "mehmet34"  # burada c ile bir değişken tanımlanıyor. değişken içine de string ve rakmlardan oluşan bir ifade
# yerleştiliyor
d = c.isalpha()  # yukarıda tanımlanan ce değişkeni sadece alfabetik karakterlerden mi yoksa başka ifade var mı diye
# kontrol ediliyor. bu kontrol ise isalpha ile kontrol ediliyor.
print(
    d)  # yukarıda yapılan kontrol sonucu ise print ile ekrana yazdırılıyor. sonuç False çıkar sebebi ise ifade
# içersinded 3 ve 4 rakamının olmasıdır.
