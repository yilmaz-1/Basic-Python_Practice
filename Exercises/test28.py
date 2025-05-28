urunler = []

adet = int(input("Kaç Ürün Eklemek İstiyorsunuz: "))

i = 0

while i < adet:
    name = input("Ürün İsmi: ")
    price = int(input("Ürün Fiyatı: "))
    urunler.append({
        "name": name,
        "price": price
    })

    i += 1
for urun in urunler:
    print(f"ürün adı: {urun['name']}\nürün fiyatı: {urun['price']}")
