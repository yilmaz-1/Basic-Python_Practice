# aşağıda kullanıcının gireceği metni terse çeviren bir fonskiyon tanımlandı.

def terscevir(metin): # burada bir adet bir argümanlı terscevir isminde bir fonksiyon tanımlandı.
    tershali=metin[::-1] # tersine çevrilecek metin burada tersine çevriliyor ve tershali ismindeki değişkene atılıyor.
    # metni terse çevirme kodu: metin[::-1] yani metnin sonundan başla başa kadar tek tek git.
    return tershali # fonksiyon çalışıyor ve bittikten sonra tershali ismindeki değişkeni bize döndür. zaten return
    # ifadesi bize fonskiyon tanımlanması bitti diyor demek yani.

kelime=input("Lütfen Ters Haline Çevirmek İstediiğiniz Metni Gİriniz: ") # kullanıcıdan bir girdi istiyoruz.

print(f"Girdiğiniz Metnin Tersi : {terscevir(kelime)}") # print fonskiyonu içerisinde terscevir fonskiyonuna kelime
# değişkeni gönderilerek çağrılıyor.





