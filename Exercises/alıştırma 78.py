names = ["mehmet", "hasan", "ahmet", "ali"] # burada bir adet liste tanımlandı.

A = [] # boş bir liste tanımlandı ve A değişkenine atandı.
B = [] # boş bir liste tanımlandı ve B değişkenine atandı.

print(list(enumerate(names))) # bu kodda names listesinin eleman ve indeks numaralarının bir liste şeklinde alıp liste
# haline getirip ekrana yazdırmada kullanıldı.

for index, name in enumerate(names): # burada for döngüsü ile namesa listesinin hem index hemde elemanrı üzerinde
    # enumerate fonskiyonu ile gezip oradan aldığımız indeks numaralarını indeks değişkenine , karakterleri ise name
    # değişkenine atarak her döngüde bunları alarak
    if index % 2 == 0: # eğer her döngüde aldığımız indeks numarısın 2 ile bölümünden kalan sıfır ise yani çift numaralı
        # indeks ise
        A.append(name) # bu indekse karşılık gelen karakteri yani onu temsil eden name değişkenini boş olan A listesine
        # yolla.
    else: # değilse
        B.append(name) # B listesine yolla

print(A)
print(B)

# yukarıdaki koddda enumerate fonskiyonun nasıl kullanıldığını öğrenmeye çalıştık. enumerate fonsiyonu bir lsite
# içerisndeki elemanların hem indeks hemde elemanlarını aynı anda almamıza yradımcı olan bir fonskiyodur.
