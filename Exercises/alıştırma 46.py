# aşağıda sezar şifreleme programı yazıldı.

# sezar şifreleme programı kısaca : harflerin yerini değiştirerek şifrelenmiş yeni bir metin elde edilmesidir.

# şifreleme programını yazarken iki adet python da gömülü fonksiyondan faydalanacağız. 1=> ord() , 2=> chr(). ord()
# fonksiyonu bir karakterin ascii standarlarına göre bigisayar dilinde rakam karşılığını verir. chr() fonksiyonu ise
# ascii standarlarına göre bilgisayar dilinde karakter karşılığını veri. örneğin ord("A") = 65 , chr(65)="A" gibi.

def sifreleme(metin):  # burada bir adet sifreleme isminde bir argümanlı bir fonskiyon tanımlandı.
    sifrelimetin = ""  # burada sifrelimetin isminde bir adet boş bir değişken tanımlandı. bu değişkeni daha sonra
    # şifrelenmiş metni saklamak için kullanacağız.

    # biz ord() fonskiyonunu sadece tek bir karakter dönüştürmek için kulanıyoruz. bunan doalyı birden falz karakter
    # içeren metni ord içersinde kullanamayız. zaten sezar şifrelemenin de mantığına aykrırı bu durum. her harf tek tek
    # sönüştürüldüğü iin bizde bu şekilde kullanacaığız.

    for harf in metin:  # yukarıda da bahsettiğim gibi girilen metin içerisinden her harf tek tek alınıp dönüştürülüp
        # tekrar birleştirilmesi lazım. bundan dolayı girilen metin üzerinde bir adet for döngüsü kurularak her döngü
        # de metin den bir adet harf değişkenine atanmak üzere bir adet karakter alınacaktır.
        asciikod = ord(harf)  # her döngüde alınan bu harf değişkenine atanan karakter, ord fonskiyonu ile  asciikod
        # ismindeki değişkenine atanmak üzere ord() fonskiyonu kullanılarak ascii dönüşümü yapılıyor.(sayısal bir değer)

        asciikod += 3  # bu dönüşüm sonrası elde edilen ascii numrasına 3 eklenerek tekrardan asciikod değişkenine atanıyor

        karakterkod = chr(
            asciikod)  # her döngüde ascii standardına dönüştürülen ve asciikod değişkenine atanan asciikod
        # da yer alan rakam chr() fonskiyonu ile tekrardan ascii standardına göre tekrardan harf karakterine
        # dönüştürülüyor

        sifrelimetin += karakterkod  # en son elde ettiğimiz karakterkod değişkeni daha önce globalde tanımlanan ve
        # içi boş olan değişkene atanıyor.
    print(f"Şifresiz Metin: {metin}, Şifreli Metin: {sifrelimetin}")  # ekrana yazdırılıyor...


ilkMetin = input("Lütfen Şifrelenecek Metni Giriniz: ")  # kullanıcıdan şifrelenmek üzrere kullanılacak metin
# girmesi isteniyor.

sifreleme(ilkMetin)  # fonksiyon 1 argümanlı olarak çağrılıyor.









