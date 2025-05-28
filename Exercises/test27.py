x = [1, 2, 3]
y = [1, 2, 3]

print(x is y)  # burada değer olarak ayı olsalar da x ve ye değişkenleri farklı adreslere tanımlandığı için is operatörü
# print ifadesinin sonucunu False yazdırdı.
print(x == y)  # burada x ve ye değişkenin içersinde tanımlanan değerler karşılaştırıldı ve sonuç True çıktı. Burada ==
# ifadesi ile değişkenlerin adresleri kontorl edilmedi. değişken içindeki değerler kontrol edildi ve karşılaştırıldı.

print(x is not y)

x = y = [1, 2, 3]
print(x is y)  # burada x ve ye değişkenleri aynı adrese tanımlandığı için is operatörü print ifadesinin sonucunu True
# yazdırdı.
print(x == y)  # burada x ve y değişkenilerinin içersinde yer alan değerler kontorl edildi ve karşılaştırıldı. x ve y
# değişkenlerinin adresleri ile ilgili bir kontorl yapılmadı. x ve y değişkenleriin içindeki değerler aynı olduğu için
# sonuç True çıktı.

# is opreatörü değişkenlerin adresleri kontrol etmede kullanılır.

# a = [1,2,3,"a","c"]
# b =c= [1,2,3,"a","c"]
#
#
# print(a is b)
#
# print(a == b)
#
# print(a is c)
#
# print(a == c)
#
# print(b is c)
#
# print(b == c)
