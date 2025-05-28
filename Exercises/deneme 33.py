def bilgilerigöster(ad,soyad,numara): # bilgilerigöster siminde 3 argümanlı bir fonksiyon tanımlanıyor.
    print("Ad:",ad,"Soyad:",soyad,"Numara:",numara) #  burada her argüman ekrana bastırılıyor.


bilgilerigöster("mehmet\n","ışık\n","123456") # fonksiyona 3 argüman gönderilerek çağrılıyor. her argüman sonuna \n ile bitirip bir alt satıra geçme komutu yazılıyor.
# çıktı:
# Ad: mehmet
#  Soyad: ışık
#  Numara: 123456

bilgilerigöster("mehmet","ışık","123456") # burada sadece fonsksiyon 3 argüman ile çağrılıyor.
# çıktı:
# Ad: mehmet Soyad: ışık Numara: 123456