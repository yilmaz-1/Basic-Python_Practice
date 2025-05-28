# aşağıda sözlük uygulaması ile ilgili bir progam yer almaktadır.

sozluk={
    "Günaydın": "Good Morning",
    "İyi Akşamlar": "Good Morning",
    "Merhaba": "Hello"
    } # burada bir adet sözlük tanımlandı.


silinecek_kelime=input("Lütfen Silinecek Kelimeyi Giriniz: ")# kullanıcıdan silinecek kelimeyi girmesini istiyoruz.



if silinecek_kelime in sozluk.keys(): # eğer silinecek kelime yukarıda tanımlanan sözlük içersindeki keys ( anahtarlar )
    # arasında varsa
    sozluk.pop(silinecek_kelime) # pop metodu ile sözlük listesinden atılıyor.
    print(f"{silinecek_kelime} Kelimesi Sözlükten Silindi...") # atılan kelime ekrana bastırılıyor.
    print(f"Yeni Sözlük: {sozluk}")
else: # eğer sözlük içerisinde olmayan bir kelime girildi ise,
    print("Böyle Bir Kelime Sözükte Bulunmamaktadır...") # ekrana yazdır.