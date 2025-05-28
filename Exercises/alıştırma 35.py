
aranan= "MEHMET" # aranan isminde önceden tanımlanan yani globalde tanımlanan bir adet değiken tanımlandı.
# Biz bu kelimeye tahminler yaparak ulaşmaya çalışıyoruz.

gorunen = "?" * len(aranan) # görünen isminde bir adet değişken tanımlandı. Bu değişken aranan kelimesin boyu
# kadar ? işareti ile çarpılası olarak atandı. Yani aranan kelimesi 6 karakterli olduğu için 6 tane soru işaretidir.
# gorunen = ?????? şeklindedir.

while aranan != gorunen: # burada bir adet döngü kuruldu . amacımız her döngüde kullanıcıdan bir tahimn alarak
    # aradaığımız kelimeyi harf harf tahminde bulunarak elde etmektir.
    harf = input(f" {gorunen} Kelimesi İçin Harf Tahmininde Bulunun Lütfen: ") # kullanıcıdan bir adet kelime
    # tahmininde bulunması isteniyor.
    harf1=harf.upper() # burada kullanıcının küçük harf girmesi durumunda otomatik olarak onu büyük harfa çevirdik.

    for i in range(0,len(aranan)): # burada bir iç döngü oluşturulup sıfır ile aranan kelimenin boyu arasındaki sayılar
        # kadar her döngüde bir değeri alınıyor. örneğin: 1. döngüde 0, 2. döngüde 2, 3. döngüde 2 gibi...

        if harf1==aranan[i]: # eğer kullaınıcıdan while döngüsünün başında aldığımız harf ile for döngüsü ile aldığımız
            # i değerine karşılk gelen aranan kelimenin i. indeksindeki harf eşit ise aynı ise
            gorunen=gorunen[:i] + harf1 + gorunen[i+1:]#[:i] =>görünen değişkenin baştan i. indeksine kadar ki kısmını al
            # + kullanıcının girdiği harf i al + [i+1:] => görünen değişkenin i+1. indeksinden sonun kadar olan kısmı al
            # ve topla. Böylelikle yeni görünen değişkeni oluşmuş oluyor.
# yukarıda yapılan işlem while döngüsü sağlandığı sürece  ( aranan kelime ile görünen kelime eşit olmadığı süere
# boyunca devam edeck.

print(f"Bildiniz. {aranan} Kelimesi Doğru Tahmin.")