"""

MANTIKSAL OPERATÖRLER

AND       Her iki değişken veya ifade aynı anda sağlanıyor yani True oluyor ise Genel Sonuç True döner.
          Her hangi biri sağlanmaz ise False döner.
OR        Her iki operant değişken veya ifadelerden herhangi biri sağlanıyor ise Genel Sonuç True döner.
          Her ikisinden birinin sağlanmasa bile True sonucu döner.
NOT       Bu operatör sonucu tersine çevirir. Sonuç True ise False, False ise True yapar.

"""

a = 7
b = 5
c = 6
d = 5
f = 6
text = "mehmet"
tex_1 = "murat"
text_3 = "mehmet"
tex_2 = "hasan"

print(b == d and text == text_3)
# çıktı:
# True

print(c == f and text == tex_2)
# çıktı:
# False

print(c == d and a == tex_1)
# çıktı:
# False

print(a == d or text == text_3)
# çıktı:
# True

print(b == d or text == tex_1)
# çıktı:
# True

print(not (a == b))
# çıktı:
# True

print(not (text == text_3))
# çıktı:
# False
