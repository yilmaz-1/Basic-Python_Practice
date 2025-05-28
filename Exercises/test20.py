a="ezgi ışık mehmet ışık tamam bilgi"
b=a.replace(" ","-",3) # 3 üncü indekse kadar boşluk karakteri yerine orta çizgi karakteri koy ve bu işlemi 3 üncü
# indkese kadar yap. 3 üncü indeks dahil.
print(b)
# çıktı
# ezgi-ışık-mehmet-ışık tamam bilgi

c="ezgi ışık mehmet ışık tamam bilgi"
d=c.replace(" ","") # c de tanımlanan string ifadesi boyunca bütün boşluk karakterlerini boşluk olmayan karakter
# ile değiştir. bunu da string boyunca yap
print(d)
# çıktı:
# ezgiışıkmehmetışıktamambilgi