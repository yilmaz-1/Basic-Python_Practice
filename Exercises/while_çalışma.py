adet= int(input("Kaç Adet Ürün Girmek İstiyorsunuz: ")) # burada kullanıcıdan kaç adet ürün kaydetmek istediği
# bilgisini alıyoruz.
i =0 # döngünün başlaması ve sağlılı bir şekilde çalışması için bir i değeri tanımlıyoruz.
ürünlerListesi=[] # boş bir liste tanımlıoruz. çünkü kullaıcıdan aldığımız bu ürün bilgierini bu listeye yollayacağız.
while i < adet: # burada  i derğeri kullanıcıdan alınan adet bilgisiden küçük olduğu sürece bu döngü devam etmesi
    # koşulu ile bir döngü kurulmulmuştur.
    isim= input("Ürün İsmini Giriniz: ") # burada her döngüde kullanıcıdaan bir adet ürün ismi alıyoruz
    fiyat = input("Ürün Fiyatını Giriniz: ") # burada her döngüde kullnıdan bir adet ürün fiyatı alıyoruz.
    ürünlerListesi.append({
        "Ürün Adı": isim,
        "Ürün Fiyatı": fiyat,
    }) # aldığımız bu ürün ismi ve fiyat bilgilerini appen komutu ile ürünlerlistesine yolluyoruz.
    i+=1 # döngünün devam etmesi için i değeri her döngüde bir adet artırılıyor.
for i in ürünlerListesi: # döngü bittikten sonlandıktan sonra oluşan bu ürünler listesinden ürün biigileri listeden
    # tektek alınarak
    print(f"Ürün Adı: {i['Ürün Adı']} \nÜrün Fiyatı: {i['Ürün Fiyatı']}") # ekrana yazdırılıyor.


# çıktı:
# yukarıda tanımlanan program kullanıcıdan alınan ürün ismi ve fiyat bilgierini ekrana yazdırmamıza yarıyor.
# Kaç Adet Ürün Girmek İstiyorsunuz: 3
# Ürün İsmini Giriniz: makarna
# Ürün Fiyatını Giriniz: 5
# Ürün İsmini Giriniz: süt
# Ürün Fiyatını Giriniz: 10
# Ürün İsmini Giriniz: kola
# Ürün Fiyatını Giriniz: 15
# Ürün Adı: makarna
# Ürün Fiyatı: 5
# Ürün Adı: süt
# Ürün Fiyatı: 10
# Ürün Adı: kola
# Ürün Fiyatı: 15



