sayı1=int(input("Sayı1: "))
sayı2=int(input("Sayı2: "))


# ekok: İki veya daha fazla sayının ortak katlarının en küçüğüne EKOK denir.


def ekokBulma(sayı1,sayı2): # burada 2 argümanlı (sayı1 ve sayı2) ekokBulma isminde bir fonskiyon tanımlanıyor.
    i=2 # burada i değişkenin 2 den başlatılmasının amacı ekok bulunurken sayılar bölünmeye başlarken
    # 2 ile başladığı için.
    ekok=1 # ekok için çarpma işlemi yapılacağı için ekok 1 den başlatıldı.

    while True: # doğru olduğu sürece çalışması isteniyor.
        if (sayı1 %i==0 and sayı2 % i==0): # eğer i değeri kullanıcının girdiği sayı1 ve sayı2 değerlerini aynı anda
            # tam ve kalansız bölüyorsa

            ekok *=i # ekok ifadesini i ile çarp

            sayı1 //=i # sayı1 değerini i ile böl ve bölüm kısmını al

            sayı2 //=i # sayı2 değerini i ile böl ve bölüm kısmını al

        elif (sayı1 %i==0 and sayı2 % i!=0): # eğer sayı1 değerinin i ile bölümünden kalan sıfır ve sayı2 değerinin
            # i ile bölümünden kalan sıfırdan farklı ise bu kod bloğu çalışcak

            ekok*=i # ekok i ile çarpılacak

            sayı1//=i #  sayı1 i ile bölümünden bölüm al

        elif (sayı1 %i!=0 and sayı2 % i==0): # eğer sayı1 değerinin i ile bölümünden kalan sıfırdan farklı ve sayı2
            # değerinin i ile bölümünden kalan sıfır ise bu kod bloğu çalışacak

            ekok*=i # ekok i değeri ile çarp

            sayı2//=i # sayı2 i ile bölümünden bölümü al
        else: # eğer yukarıdaki hiç bir kod bloğu çalışmaz ise
            i+=1 # i iyi bir artır. bu kod bloğu burada bitiyor.
        if (sayı1 ==1 and sayı2 ==1): # burada yeni bir if koşul durumu yazılıyor ve sayı1 ve sayı2 değerleri
            # aynı anda 1 e eşit olursa
            break # fonksiyonu burada bitir.

    return ekok # bu tanımlanan fonksiyon işlemi sonucunda elde ettiğimiz ekok değerini bize döndür

print("ekok:",ekokBulma(sayı1,sayı2)) # print fonksiyonu içinde ekokBulma fonksiyonu çağrılarak ekrana yazdırılıyor.
#çıktı:
# Sayı1: 48
# Sayı2: 56
# ekok: 336