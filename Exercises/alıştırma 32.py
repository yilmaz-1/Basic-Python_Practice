annesoyad="yılmaz" # burada önceden tanımlı bir adet değişken içersinde annenin soy adı tanımlandı.
parca=annesoyad[1:3] # burada kullanıcıya soralacak olan kısım parça değişkeni olarak tanımlandı. annenin soyadının
# 2. ve 3. harfi parça olarak alındı.

cevap= input("Lütfen Anne Kızlık Soyadınızın 2. ve 3. Harfini Giriniz: ") # kullanıcıdan girdi istendi.

if cevap==parca: # eğer kullanıcının girdiği cevap parça değişkenine eşit ise
    print("Tebrikler Doğru Giriş Yaptınız...") # ekrana yazdır.
else: # değilse
    print("Hatalı Giriş Yaptınız...")

