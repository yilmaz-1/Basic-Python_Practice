"""
OPERATÖRLER

TOPLAM                          (+)
ÇIKARMA                         (-)
ÇARPMA                          (*)
BÖLME                           (/)
TAM SAYI BÖLME                  (//)
KALAN BULMA ( mod alma )        (%)
ÜST ALMA                        (**)    veya pow (taban, üst) foksiyonu

"""

a = 5
b = 12

print(a + b)
# çıktı:
# 17

print(a - b)
# çıktı:
# -7

print(a * b)
# çıktı:
# 60

print(a / b)
# çıktı:
# 0.4166666666666667

print(a // b)
# çıktı:
# 0

print(a % b)
# çıktı:
# 5

print(b ** a)
# çıktı:
# 248832

print(pow(144,0.5))
# çıktı
# 12.0


"""
Özel Durum

pow(a,b,c) bu durum özel bir durumdur. bu şu demektir: a sayısının b inci kuvvetini al ve çıkan sayının c ile 
bölümünden kalan sayıyı bize ver demek.
pow(taban, üst, mod alma)

"""


print(pow(4,2,6))
#çıktı
# 4