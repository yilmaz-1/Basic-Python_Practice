liste= [] # burada boş bir liste tanımladık.

while True: # burad bir döngü oluşturduk. True ifadesi ile oluşturmamzın sebebi ise whlie döngüsü doğru olduğu sürece
    # döngü kuralları sağlandığı sürece çalışmasını istedik. True ifadesi ile doğru olduğu sürece sağladığı
    # sürece demek.
    sayi = input("Bir sayı giriniz (çıkmak için q ya basın): " ) # burada input ile kullanıcıdan her döngüde bir sayı
    # aldık ve bu sayıyı sayı isminde bir değişkene atadık.
    if sayi=="q": # burada bir koşul ifadesi kurduk. dedikki eğer kullanıcadn alınan sayı q ifadesi olursa
        print(liste) # ekrana bu zaman kadar aldığın ve listeye attığın oluşan listeyi ekrana bas.
        break # döngüyü burada kır ve bitir.
    sayi = int(sayi) # burda her döngüde kullanıcıdan aldığımız sayıyı veri tipi dönüşümü yaparak int e çeviriyoruz.
    # çünkü kullanıcıdan int tipinde bir de değerler istiyoruz fakat kullanıcının girdiği her değer sting olduğu için
    # dönüşüm yapmak zorundayız. peki neden yukarıda ki gibi input alma kısmında veri dönüşümü yapmadıkta burada yaptık?
    # çünkü kullanıcının ne zaman q string ifadesini gireceğimizi bilmediğimiz için burada yaptık. eğer orada yapsaydık
    # kullanıcı q string ifadesini girdiğinde program hata verecekti.

    if sayi not in liste: # burada ise koşul durumu oluşturuldu.fakat bu koşul durumunda kullanıcıdan alınan sayı
        # eğer oluşturulan liste içinde yoksa
        liste.append(sayi) # bu sayıyı append fonskyionu ile boş liste içerisine atıyoruz.
    else: # varsa bu sayı liste içerisine yollanmıyor ve
        print("Bu sayıyı daha önce girdiniz.") # ekrana print ile yazdırılıyor.

# çıktı
# Bir sayı giriniz (çıkmak için q ya basın): 1
# Bir sayı giriniz (çıkmak için q ya basın): 2
# Bir sayı giriniz (çıkmak için q ya basın): 3
# Bir sayı giriniz (çıkmak için q ya basın): q
# [1, 2, 3]