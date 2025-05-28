
# futbolcular.txt ismindeki dosya hali hazırda elimizde mevcut olduğunu var sayarak aşağıdaki kod yazılmıştır.

with open("futbolcular.txt", "r", encoding="utf-8") as file: # dosya okuma kipinde açılmıştır.
    gs = list() # gs isminde bir adet boş liste oluşturuldu.
    bjk = list() # bjk isminde bir adet boş bir liste oluşturuldu.
    fb = list()# fb isminde bir adet boş bir liste oluşturuldu.
    for satir in file: # for döngüsü ile dosyanın satırları üzerinde gezinerek her satırı, satır değişkenine atandı.
        satir = satir[:-1] # her döngü de aldımız satır ters çevrildi ve satır değişkenine atandı.
        satir_elemanlari = satir.split(",") # ters çevrilen satır split fonksiyonu ile her virgül olan yerden parçalandı
        # ve satır_elemanları değişkenine atandı. split ile paraçalanan satır, liste formatına dönüştü.
        print(satir_elemanlari) # satır_elemanları ekrana bastırıldı.
        if (satir_elemanlari[1] == "Fenerbahçe"): # eğer satır_elemanlarının 1. indeksindeki eleman fenerbahçe
            # değişkenine eşit ise
            fb.append(satir + "\n")#bu satırı append fonksiyonu ile fb ismindeki boş listeye yolla ve bir alt satıra geç
        elif (satir_elemanlari[1] == "Galatasaray"):# eğer satir_elelmanlari değişkeninin 1. indeksinde yer elaman
            # Galatasaray ifadesine eşit ise
            gs.append(satir + "\n")
        else:
            bjk.append(satir + "\n")
        with open("gs.txt", "w", encoding="utf-8") as file1:
            for i in gs:
                file1.write(i)
        with open("fb.txt", "w", encoding="utf-8") as file2:
            for i in fb:
                file2.write(i)
        with open("bjk.txt", "w", encoding="utf-8") as file3:
            for i in bjk:
                file3.write(i)
