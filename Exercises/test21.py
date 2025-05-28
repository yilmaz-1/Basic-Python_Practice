arabalar = ["Bmw", "mercedes", "opel", "mazda"]  # burada içerisnde string ifadelerin olduuğu bir liste tanımlandı.

result = len(arabalar)  # yukarıda tanımlanan listenin boyu len fonksiyonu ile hesaplandı.

print(result)  # result sonucu ekrana yazdırıldı.
# çıktı:
# 4
print(arabalar[0])  # arabalar listesinin sıfırıncı indeksi ekrana yazdırıldı.
# çıktı:
# Bmw

print(arabalar[1])  # burada arabalar listesinin 1. indeksi ekrana yazdırıldı
# çıktı:
# mercedes

print(arabalar[-1])  # burada arabalar listesinin eksi 1 inci elemanı ekrana yazdırıldı
# çıktı:
# mazda

arabalar[
    -1] = "toyota"  # burada arabalar listesinin eksi birinci indeksinin yerine toyota string ifadesi yerleştirildi.
print(arabalar)  # burada eksi 1 inci indeksi değişen arabalar ifadesi ekrana yazdırıldı.
# çıktı:
# ['Bmw', 'mercedes', 'opel', 'toyota']

result = "mercedes" in arabalar  # "mercedes" değişkeni arabalar listesin içersinde olup olmadığı kontrol edilmiştir.
print(result)
# şağıda çıktı True olduğu için doğru anlamına geliyor ve mercedes string ifadesi arabalar listesi içinde yer var
# Ture

result = "audi" in arabalar  # "audi" string ifadesi arabalr listesi içnde yer alıup olmadığı in operatörü ile
# sorulmaktadır
print(result)
# aşağıda çıktı False olduğu için doğru olmadığı anlamına geliyor. Yani audi string ifadesi arablar listesi içnde yok.
# False

print(arabalar[-2])  # arabalar listesinin eksi 2 inci indeksindeki elemanı ekrana yazdırıyor.
# opel
print(
    arabalar[0:3])  # arabalar listesinin sıfırıncı indeksinden başlayarak üçüncü indeksine kadar (3 dahil değil) al ve
# yazdır diyor.
# çıktı
# ['Bmw', 'mercedes', 'opel']

print(arabalar[:3])  # arabalar listesinin başından yani sıfırıncı indeksinden başlayarak üçüncü indeksine kadar al
# (üç dahil değil) ve ekrana yazdır.
# çıktı
# ['Bmw', 'mercedes', 'opel']

print(arabalar[:-2])  # arabalar listesinin başından yani sıfırıncı indeksinden eksi 2 inci indeksine kadar al ve kerana
# yazdır
# çıktı
# ['Bmw', 'mercedes']

arabalar[-2:] = ["toyata", "Renault"]  # arabalar listesinin sondan eksi 2 inci indekse kadar yeni
# liste içerisinde tanımlanan toyota ve renault string ifadelerini yerlşetir.
print(arabalar)
# çıktı:
# ['Bmw', 'mercedes', 'toyata', 'Renault']

arabalar += ["tofaş", "toros"]  # burada arablar listesine tofaş ve toros string ifadelerini içeren listeyi ekle
print(arabalar)
# çıktı:
# ['Bmw', 'mercedes', 'toyata', 'Renault', 'tofaş', 'toros']

del arabalar[-1]  # arabalar listesinin eksi birinci indeksindeki elemanı sil.
print(arabalar)
# çıktı
# ['Bmw', 'mercedes', 'toyata', 'Renault', 'tofaş']

a = [1, 2, 3, 4, 5, 6, 7, 8, 9]  # a değişkeninde tanımlanan liste
del a[1:5]  # del operatörü ile a listesinin birinci indeksinden başlayarak 5 inci indekse kadar (5 dahil değil) sil.
print(a)
# çıktı
# [1, 6, 7, 8, 9]

print(
    arabalar[-1::])  # arabalar listesinin eksi birinci indeksinden başlayarak sona kadar git ekrana arabalar listesini
# yazdır.
# çıktı
# ['tofaş']

print(arabalar[::-1])  # herhangi bir atlama koşulu verilmeden tüm listeyi al fakat listeyi tersten (-1) yazdır.
# ['tofaş', 'Renault', 'toyata', 'mercedes', 'Bmw']
