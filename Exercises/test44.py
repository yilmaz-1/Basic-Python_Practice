birler=["","bir","iki","üç","dört","beş","altı","yedi","sekiz","dokuz"] # birler isminde bir liste tanımladı.
onlar=["","on","yirmi","otuz","kırk","elli","atmış","yetmiş","seksen","doksan"] # onlar isminde bir liste tanımlandı.

def okunus(sayı): # bir argümana sahip okunus isminde bir fonskşyon tanımlandı.
    birinci= sayı % 10 # birinci isminde bir değişken tanımlandı ve bu değişken ise kullanıcıdan alınan
    # sayının 10 ile bölümünden kalana eşitlendi.
    ikinci= sayı // 10 # ikinci isiminde bir değişken tanımlandı ve kullanıcıdan alınan sayının 10 ile bölümünden
    # elde edilen bölüm e eşitlendi. yani mod alındı.
    return onlar[ikinci]+ " " +birler[birinci] # fonksiyon sonucunda bize döndürmesini istediğimiz şey
    # şu: onlar[ikinci] = bu şu demek: yukarıda tanımlanan ikinci değişekninden bir değer gelecek ve bu değer de onlar
    # listesinin kaçıncı indekste yer alan elemanı almamızı belirtecek. örnek: diyelim ki ikinci değişkenin sonucudan
    # 1 ifadesi geldi. bu bize şunu diyor: onlar listesinin 1 inci indeksinde ("yirmi) yer alan ifadeyi al diypor.
    # daha sonra " " iki tırnak içinde yer alan boşluk ifadesi ile bunu birleştir diyor.
    # daha sonra da birler[] ifadesinden gelen ifade ile öncekileri birleştir diyor. ve burada çıkan sonucu da fonksiyon
    # çağrıldığı zamn bize dönder diyor.

while True: # işlem doğru oldupu sürece çalışmasını istiyoruz.
    sayı=int(input("Sayı: ")) # kullanıcıdan bir sayı girmesini istiyoruz.
    print(okunus(sayı)) # print fonksiyou içinde yukarıda tanımladığımız okunus isimli fonksiyonu çağırıyoruz.

#çıktı:
# Sayı: 15
# on beş
# Sayı: 76
# yetmiş altı
# Sayı: 78
# yetmiş sekiz
# Sayı: