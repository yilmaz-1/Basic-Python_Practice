sehirler=["adana","maras"]

def change(n): # burada fonksiyon tanımlandı. n bu fonksiyonun argümanı ve dizisi olarak düşünülmüştür.
    n[0] = "istanbul" # n dizisinin sıfırıncı indeksine "istanbul" değeri atanmış.




change(sehirler)# change fonksiyonun çağırılıyor ve içerisine sehirler dizisi atılıyor. fonksiyondan gelen istanbul bu sehirler dizisinin sıfırıncı indeksine atanıyor.

print(sehirler)
# çıktı:
# ['istanbul', 'maras']

# change(sehirler[:])# bu [:] slicing işlemi yaptığımız zaman orjinal listeyi korumuş oluruz. parçalama işlemi yöntemi ile yeni bir kopyasını oluşturmuş oluruz.
# print(sehirler)
 # çıktı
 # ['adana', 'maras']
