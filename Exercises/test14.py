liste = "mehmet ali şenili ve mehmt ışık"  # burada bir string ifade tanımlanıyor.
liste1 = liste.find(
    "mehmt")  # liste1 bir diye boş bir değişken tanımlanıyor ve bu değişkene yukarıda tanımladığımız string ifade
# içinde mehmt kelimesi varmı kontrol ediliyor. bu kontrol liste de tanımlanan string ifadesinin başından yani
# sıfırıncı indeksinden başlayarak son indekse kadar kontrol ediliyor.
liste2 = liste.find("ve", 3,
                    29)  # yukarıda liste de tanımlanan string ifade içerisnde find() metodu ile 3 indeksten 29 uncu
# indekse kadar kontrol et içerisinde 've' varsa print ile liste1 içinde ekrana yaz
liste3 = liste.find("jk", 0,
                    30)  # burada ise liste de tanımlanan string ifade içerisinde find() metodu ile tüm string boyuna
# taranıp kaçıncı indekste buldu ise indeks numarasını liste3 içerisne atıp ekrana print ile yazdırıyor.
liste4 = liste.rfind(
    "ali")  # burada ise gene liste de tanımlana string ifade içersinde arama bulma yapıyor ama bu sefer sağdan
# başlıyor aramaya . find kelimesinin öününde ki r ifadesi right yani sağ anlamına geliyor. sağndan başlıyor kontrol
# etmeye ilk bulduğu ifadenin kaçıncı indeks te olduğunu liste4 içerisne atıyor ve print ile ekrana basıyor.
print(liste1)  # liste1 ifadesi ekrana print ile yazdırılıyor.
print(liste2)  # liste2 ifadesi ekrana print ile yazdırılıyor.
print(liste3)  # liste3 ifadesi ekrana print ile yazdırılıyor.
print(liste4)  # liste4 ifadesi ekrana print ile yazdırılıyor.
