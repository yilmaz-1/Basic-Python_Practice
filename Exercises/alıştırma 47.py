
# burada bir önceki programda( alıştırma 46 ) şifrelenmiş metnin şifresinin çözülmesini sağlayan bir program yazılıdı.

def sifrecoz(sifrelimetin): # burada bir adet sifrecoz isminde bir argümanlı ( sifrelimetin ) bir fonskiyon tanımlandı.
    sifresizmetin="" # burada bir adet sifresizmetin isminde boş bir değişken tanımlandı. bu değişkeni daha sonra
    # şifresini çözdüğümüzde ortaya çıkaacak metni saklamak için kullanacağız.
    for harf in sifrelimetin:# burada bir döngü oluşturduk. amacıomız ord fonksiyonu her seferinde bir karakteri
        # dönüştürebildiği için girilen metinde yer alan her arakteri döngü ile tek tek alıp dönüşümünü sağlamak.
        asciikod=ord(harf) # her döngüde sifrelimetin değişkeninin içerisinden harf değişkenine atanan karakter,
        # ord fonskiyonu ile ascii sayılsa karşılığına dönüştürülüp asciikod değişkenine atanıyor.
        asciikod-=3 # yularıda elde edilen sayısal değer den 3 çıkarılarak asciikod değişkenine yeniden atanıyor.
        karakterkod=chr(asciikod)# elde edilen asciikod sayısal değeri chr fonskiyonu ile karakter kaşılığı elde
        # edilyor. bu karakter kaşlığı da karakterkod değişkenine atanıyor.
        sifresizmetin+=karakterkod # elde edilen bu karakterkod değişkeni daha önce yularıda tanımlanan sifreszimetin
        # değişkenine atanıyor.

    print(f"Şifreli Metin: {sifrelimetin}, Şifresiz Metin: {sifresizmetin}") #ekrana yazdırılıyor.

# fonskiyonun tanımlanması burada bitiyor. bundan sonra yazılan kodların fonksiyonun dışında tanımlanmış olacak.

metin=input("Şifresini Çözmek İstediğiniz Metni Giriniz: ") # kullanıcıdan girdi istiyoruz.

sifrecoz(metin) # fonskiyon çağrılıyor.




