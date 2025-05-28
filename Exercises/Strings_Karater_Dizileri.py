a = "python Programlama"  # a değişkeni içerisinde bir adet string ifade olan değişken tanımlandı. Tırnak içerisindeki
# her bir karakteri temsil eden bir indeks vardır. Buna kelime arasındaki boşluk ifadesi de dahildirdir. İndeks
# numaraları sıfırdan başlar sonsuza kadar gider.

# [x:y:z] burada şunu demek istiyoruz: x inci indeksten başla z er z er atlayarak y inci indekse kadar git diyor.

print(a[0:18:1])
# çıktı:
# python Programlama

print(a[:10])  # burada başlangıç ve atlama değeri belirtilmediği için sıfırıncı indeksten başlayıp 1 er 1 er 10.
# indekse kadar alıp yazdırır. 10. indeks dahil değildir.
# çıktı:
# python Pro

print(a[4:])  # burada sadece başlangıc indeks belirtilmş. fakat bitiş ve atlama değeri belirtilmemiş. bundan dolayı
# parçalama işlemi 4. indeks ten başlayıp son indekse kadar 1 er 1 er olacaktır.
# çıktı:
# on Programlama

print(a[:])  # burada ne başlangıç ne bitiş nede atlama değeri belirtilmiştir.
# bundan dolayı string ifadenin tamamı alınır
# çıktı:
# python Programlama

print(a[::2])  # buarada hem başlangıç hemde bitiş değeri verilmemiştir. sadece atlama değeri verilmiştir.
# String ifadenin başından başalyıp sonuna kadar 2 şer 2 şer atlayıp ifadeyi alacaktır.
# çıktı:
# pto rgalm

print(a[:-1])  # string ifadenin sonuna kadar git ama son karakteri alma.
# çıktı:
# python Programlam

print(a[::-1])  # bu ifade a değişkeni içinde tanımlanan string ifadeyi ters çevir diyor.
# çıktı
# amalmargorP nohtyp
