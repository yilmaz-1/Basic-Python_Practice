sehiler=["kocalei","istanbul","ankara","izmir","rize"] # sehirler isimli bir liste oluşturuluyor.
k=[] # boş liste oluşturuluyor.
for i in sehiler: # for döngüsü ile sehirler listesi üzerinde gezinerek i değerleri elde ediliyor. bu i değerleri çift tırnak içinde ki string ifadeler.
    if (len(i)<=5): # for döngüsü ile elde edilen bu i lerin uzunluğu len fonksiyonu (uzunluk bulmaya boyu bulmaya yarar.) ile hesaplanır bu koşul içindeki eğer bu hesaplanan boy(uzunluk) 5 e eşit veya küçük ise
        k.append(i) # bu i ler boş olan k listesine atılır.
print(k) # yeni k listesi ekrana yazdırılır.

# çıktı:
# ['izmir', 'rize']

# ****************************************************

sehiler=["kocalei","istanbul","ankara","izmir","rize"]

def a(sehirler): # a isminde bir argümanı olan bir fonksiyon tanımlanıyor.
    l=[] # boş liste tanımlanıyor.
    for i in sehiler: # for döngüsü ile sehirler listesi üzerinde gezinerek i değerleri elde ediliyor. bu i değerleri çift tırnak içinde ki string ifadeler.
        if(len(i)<=5): # for döngüsü ile elde edilen bu i lerin uzunluğu len fonksiyonu (uzunluk bulmaya boyu bulmaya yarar.) ile hesaplanır bu koşul içindeki eğer bu hesaplanan boy(uzunluk) 5 e eşit veya küçük ise
            l.append(i) # bu i ler boş olan l listesine atılır.
    print(l) # yeni l listesi ekrana yazdırılır.
    return # return ile bu fonksiyon çağrılmak üzere döndürülür.

a(sehiler)

# çıktı:
# ['izmir', 'rize']

