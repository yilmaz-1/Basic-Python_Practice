def kiloendeksi(ad,kilo,boy): # kiloendeksi isimli üç argümana sahip bir fonksiyon tanımlanıyor.
    #isim =input("isim:")
    #kilo_ =float(input("kilo:"))
    #boy_ =float(input("boy:"))
    #indeks = (kilo/boy**2)
    if( indeks >= 0 and indeks <18.6): # eğer indeks değişkeni if koşul bloğunda ki belirtilen şartları sağlıyorsa (her iki şartıda sağladığı zaman True sonucu verir)
        print("zayıf") # ekrana yazdırır.
    elif (indeks > 18.5 and indeks < 25.1): # eğer bloktaki şartlar sağlanıyorsa
        print("normal") # ekrana yazdırır.
    elif (indeks > 25.0 and indeks < 30.0): # eğer bloktaki şartlar sağlanıyorsa
        print("fazla kilolu") # ekrana yazdırır.
    elif (indeks > 29.9 and indeks < 34.9): # eğer bloktaki şartlar sağlanıyorsa
        print("şisman")  # ekrana yazdırır.
    else: # eğer yularıda ki kod bloklarında yer alan şartlardan hiç biri sağlanmaz ise bu else bloğu çalışır.
        print("obez") # ekrana yazdırışır.
    return # return ile bütün program çağrıldığı zaman bize döndürülür.

while True: # while ile döngü oluşturuluyor. True ile de bu döngü doğru çalşıtığı sürece devam edecek ve bizden sürekli yeniden değerler isteyecek.
    isim = input("isim:") # input ile kullanıcının ismi alınıyor.
    kilo_ = float(input("kilo:")) # kullanıcıdan kilo bilgisi alınıp float ile veri tipi dönüşümü yapılıyor.
    boy_ = float(input("boy:")) # kullanıcıdan boy bilgisi alınıp float ile veri tipi dönüşümü yapılıyor.
    indeks = (kilo_ / (boy_ ** 2)) # hesaplanan değer indeks değişkenine atanıyor.
    if(kiloendeksi(isim,kilo_,boy_)): # eğer kiloendeksi fonksiyonu çağrıdığında , düzgün çalşıp sonuç verirse
        continue # döngünün başına dön ve yeniden başla

# çıktı:
# isim:mehmet
# kilo:86
# boy:1.70
# fazla kilolu
# isim: