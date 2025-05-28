def not_hesapla(satir):  # burada bir fonksiyon tanımlandı. bufonksiyon bir not hesaplama işlemi yapacak. bu fonksiyon
    # bir argümanlı bir fonksiyondur.

    satir = satir[:-1]  # satır değişkeninin bu şekilde tanımlanmasındaki amaç şudur: program çağrıldığında satırlar
    # ekrana basıldığında her satır sonunda gizli bir \n ifadesi olduğu için bir sonraki satıra geçileceği zaman bu
    # karakterden dolayı bir satır atalayarak geçiyor. bizde bu durumdan kurtulmak için her satırı tamamen al ama
    # son krakteri alma dedik. baştan son karaktere kadar gidecek. ama son karakteri almayacak.
    liste = satir.split(
        ",")  # burada ise satır içerisindeki verileri virgülden bölerek parçalayıp bir liste değişkenine
    # yolladık. bu split fonksiyonu veri parçalamaya yarayan bir  fonksiyon. split fonksiyonuna verdiğimiz virgül(,)
    # bu satırı her virgül gördüğü yreden parçalayacaktır.

    isim = liste[0]  # burada listenin sıfırıncı indeksinde bulunan elemanı alıp isim, ismindeki değişkene atadık.
    not1 = int(
        liste[1])  # burada listenin 1. indeksinde yer alan elemanın int hali alınınp not1 isimli değişkene atandı
    not2 = int(liste[2])  # burada listenin 2. indeksinde yer alan elemanın int hali alınıp not2 değişkenine atandı.
    not3 = int(liste[3])  # burada listenin 3. indeksinde yer alan elemanın int hali alınıp not3 değişkenine atandı.
    son_not = not1 * (3 / 10) + not2 * (3 / 10) + not3 * (
                4 / 10)  # son_not değişkeni diğer değişkeler ile işleme  yokulup hesaplandı.

    if (son_not >= 90):  # eğer son_not 90 dan büyük ve eşit ise
        harf = "AA"  # ekrana AA yaz.
    elif (son_not >= 85):
        harf = "BA"
    elif (son_not >= 80):
        harf = "BB"
    elif (son_not >= 75):
        harf = "CB"
    elif (son_not >= 70):
        harf = "CC"
    elif (son_not >= 65):
        harf = "DC"
    elif (son_not >= 60):
        harf = "DD"
    elif (son_not >= 55):
        harf = "FD"
    else:  # değilse
        harf = "FF"  # ekrana FF yaz

    print(liste)  # ekrana listeyi bas


with open("dosya.txt", "r", encoding="utf-8") as file:  # dosya okuma kipi ile açıldı. dosya içeriğinde türkçe karakter
    # olduğu içiçn encoding="ytf-8" olarak tanımlandı içerik okuması
    for i in file:  # for döngüsü ile dosyanın içerisindeki bütün satırlar her döngüde tek tek alınarak, i değişkenine
        # atandı.
        not_hesapla(
            i)  # yukarıda tanımladığımız not_hesapla fonksiyonu burada içerisine i değişkeni yollanarak çağrıldı








