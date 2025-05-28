def tambolenleribulma(sayı):
    tam_bolenler =[]

    for i in range(2,sayı+1):
        if sayı % i==0:
            tam_bolenler.append(i)
    return tam_bolenler

# yukarıda bir sayının tam bölenlerini bulmak için yazılmış bir program bulunmaktadır. öncelikle tambölenleribulma
# isminde bir program tanımlanmıştır. bu program altında ise tam_bolenler isminde bir boş küme tanımlanmıştır.
# daha sonra ise for döngüsü ile range fonksiyonu kullanrak 2 den başlayıp kullanıcın gireceği değere kadar olan
# sayıları alıyoruz (i değeri olarak). for döngü bloğu altında ise if koşul bloğu çalışıyor. eğer alınan bu
# i değerlerinden her hangi bir tanesi kullanıcının giereceği sayıyı tam ve kalansız olarak bölüyorsa bu i değerleri
# tam_bolenler listesine append komutu ile yollanıyor. for döngüsü bittikten sonra da bu fonksiyonu başka bir yerde
# kullanmak elde ettiğimiz tam_bolenler listesini başka bir yer kullanmak üzere return fonksiyon ile çağırıyoruz.

while True:
    sayı= input("Bir Sayı Giiriniz: ")

    if sayı=="q":
        print("İşlem sona erdi.")
        break
    else:
        sayı=int(sayı)
        print(f"Girmiş olduğunuz {sayı} sayısnınn tam bölenleri {tambolenleribulma(sayı)}")

# burada ise while True ile işlem doğru olduğu sürece devam etmesini istediğimiz bir döngü oluşturuyoruz.
# bu döngü yapısı altında ise ilk olarak kullancıdan bir sayı alıyoruz input fonksiyonu ile . hala döngü devam ediyor.
# daha sonra ise bir koşul bloğu oluşturuluyor. if bloğunda eğer kullanıcıdan gelen sayı q string ifadesine eşit ise
# print ile ekrana işlem sona erdi yazacak yukarıda yazdığımız fonksiyon hiç çalışmadan. eğer ki kullanıcı
# q string ifadesi yerine herhangi bir rakam veya sayı girerse bu sefer if bloğundaki şart sağlanmamış olacak ve
# else bloğuna geçecek orayı kontrol edecek while döngüsü. burayı okumaya başlayan program kullanıcadn gelen sayı yı
# ilk olarak integere çevirecek çünkü kullanıcın ilk girdiği değer string olarak kabul ediyor python. daha sonra ise
# print ifadesi içerindeki durumu ekrana yazdıracak. f string ile oluşturmuş olduğumuz ifadede : süslü parantez
# içindeki sayı geliyor ve diğer süslü parantez içindek ise yularıda tanımlamış olduğumuz fonksiyon çalışyor ve
# sonucu geliyor. böylelilkle ifade ekrana yazıdırılıyor.

# çıktı:
# Bir Sayı Giiriniz: 18
# Girmiş olduğunuz 18 sayısnınn tam bölenleri [2, 3, 6, 9, 18]
# Bir Sayı Giiriniz: 36
# Girmiş olduğunuz 36 sayısnınn tam bölenleri [2, 3, 4, 6, 9, 12, 18, 36]
# Bir Sayı Giiriniz:

