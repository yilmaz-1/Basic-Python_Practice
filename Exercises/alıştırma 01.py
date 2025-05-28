class Dosya:

    def __int__(self, bilgiler):

        with open("bilgiler.txt", "r", encoding="utf-8") as file:
            dosya_icerigi = file.read()
            kelimeler = dosya_icerigi.split()

            self.sade_kelimeler = list()

            for kelime in kelimeler:
                kelime = kelime.strip()
                kelime = kelime.strip(".")
                kelime = kelime.strip("\n")

                self.sade_kelimeler.append(i)

    def kelime_bul(self, aranan):

        konum = list()
        say = 1
        for kelime in self.sade_kelimeler:
            if kelime == aranan:
                konum.append(say)
            say += 1
        if (len(konum) == 0):
            print("Dosyada böyle bir kelime bulunmuyor...")
        else:
            print(f"{aranan} kelimesi dosyada şuralar da geçiyor: {konum}")

    def kelime_histogram(self):

        kelime_frekansı = dict()
        kelime_kumesi = set()

        for kelime in self.sade_kelimeler:
            kelime_kumesi.add(kelime)
            if (kelime in kelime_frekansı):
                kelime_frekansı += 1
            else:
                kelime_frekansı[kelime] = 1
            print("Kelimelerin Frekansı ...............")
            for i, j in kelime_frekansı.items():
                print(f"{i} kelimesi metinde {j} defa geçiyor")

            print("tüm kelimeler")
            for i in kelime_kumesi:
                print(i)
                print("************************************")


dosya = Dosya()
print("""

Dosya İşlemleri

1. Tüm Kelime Frekansını Öğren
2. Kelime Ara

Çıkmak için "q" ya bas

""")

while True:
    islem = input("İşlem Numarası Giriniz: ")

    if (islem == "q"):
        print("Programdan Çıkılıyor...")
    elif islem == "1":
        dosya.kelime_histogram()
    elif islem == "2":
        kelime = input("Kelimeyi Giriniz: ")
        dosya.kelime_bul()
    else:
        print("Geçersiz Giriş Yaptınız....")
