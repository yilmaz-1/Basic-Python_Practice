
# before : bu string ifadenin tek indeksindeki karakteri küçük yap çift indeksineki karakterlieri ise büyk yap
# after : Bu sTrInG IfAdEnIn tEk iNdEkSiNdEkI KaRaKtErI KüÇüK YaP ÇiFt iNdEkSiNeKi kArAkTeRlIeRi iSe bÜyK YaP


# yukarıda bizdfen istenen program fonskiyon yazılmadan if else bloğu ve input alma ile de yapılabilirdi. fakat bu her
# program çalıştığında kendini tekrar eden bir şey olmamamsı için fonksiyon yazılarak yapıldı.

def alternating(string): # burada bir argümanlı bir fonskiyon tanımlandı. bu argümanı daha sonmra fonskiyon
    # çağrıldığında içine gönderilerek program çalıştırılacak.
    new_string = "" # burada bir adet boş bir değişken tanımlandı. bu değişken daha sonra kullanılacağı boş olarak
    # tanımlandı. yaptığımız işlem sonucunda elde ettiğimiz string ifadenin son hali bu değişkene yollancak.
    for string_index in range(len(string)): # burası çok önemli. esas işin yapıldığı yer ve başlangıcı burası. burada
        # bir for döngüsü kuruldu. amacımız ise bu fonskiyon çağrıldığında içine argüman olarak gönderilen string
        # ifadenin indexlerine ulaşarak, o indekse karşılık gelen krakter üzerinde işlem yapmaktır. for döngüsünün
        # sınırı range fonskiyonu ile ayarlanmıştır. bu range fonskiyonu string ifadenin boyu kadar olacaktır. yani
        # range fonskiyonu sıfırdan string ifadenin boyuna kadar olan ralıkta bir aralık olarak alacaktır. for döngüsü
        # ile her döngüde sıfırdan string ifadesinin boyu kadar gidip aldığı her rakamı indeks olarak alacaktır.
        if string_index % 2 == 0: # her döngüde aldığı indeks numarasınınn 2 ile bölümünden kalan sıfır ise
            new_string += string[string_index].upper() # bu indekse karşılık gelen karakteri büyüt ve bu yeni karakteri
            # her döngüde boş olan değişkene ata.
        else: # değiles
            new_string += string[string_index].lower() # bu indekse karşılık gelen indeksi küçült.
    print(new_string) # döngü bittikten sonra string ifadenin son halini ekrana yazdır.

alternating("bu string ifadenin tek indeksindeki karakteri küçük yap çift indeksineki karakterlieri ise büyk yap")