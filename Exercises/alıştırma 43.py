import turtle # burada turtle modülü porgrama dahil ediliyor.



def renkli_Kareciz(renk): # burada bir adet 1 parametreli fonksiyon tanımlanıyor.bu şu demek: bir bu fonskiyonu
    # çağırdığımız zaman parametresiz oalrak çağıramayız demektir. illa ki bizden bir parametre bekleyecek.
    turtle.home() # burada çizim yapapn kalemin tekrar başladığı noktaya gelmesini istiyoruz.
    turtle.pencolor(renk) # burada kalemin rengini belirledik. bu rengi direk buraya kednimiz de yazabilirdik ama biz
    # kalem rengini dışarıdan alacağımız için ana fonskiyonun parametresi olan renk değişkeni atandı.
    for i in range(4): # bir adet for döngüsü tanımlandı. bu döngüde range fonskiyonu yardımı ile 4 defa dönmesi
        # sağlandı. her döngüde de aşağıda tanımlanan işlemler yapılacak.
        turtle.fd(100) # 100 birim ileri
        turtle.left(90) # 90 derece sola dön

# yukarıda yer alan fonskiyonun tanımlanması burada bitiyor. artık bundan sonra fonskiyondan bağımsız kodlar yazılıyor.

kullanici_rengi = input("LÜtfen İstediğiniz Rengi Yazınız: ") # kullanıcıdan bir adet renk girmesini istiyoruz.

renkli_Kareciz(kullanici_rengi) # yularıda tanımladığımız fonskiyon parametresi de verilerek çağrılıyor. kullanici_rengi
# değişkeni bu çağırdığımız renkli_kareciz fonskiyonun parametresi olarak atanıyor. bu atanan paramtre aynı zaman
# fonskiyon da tanımlanan renk parametresi yerine geçiyor.

