b= "mehmet" # b değişkeni oluşturuldu.
print(list(b)) #bu b değişkeni list fonksiyonu ile listeye çevrilip ekrana bastırıldı.

for i in range(10): # 0 dan 10 a kadar olan sayıları for döngüse ile range fonksiyonu kullanarak i değerine atandı.
    print(i) # her döngüde i değeri ekrana basıldı.

print(*range(10)) # 0 dan 10 kadar olan sayıları range fonksiyon ile alındı. daha sonra * parametresi ile de parçalanıp
# dışarı çıkarıldı. bu dışarı çıkarılan değerler print ile ekrana yazdırıldı.

print(list(range(10))) # o dan 10 a kadar olan değerler range fonksiyonu ile elde edildi. daha sonra bu değerler
# list fonksiyonu ile liste haline getirildi. son olarak da print fonskiyonu ile de bu liste ekrana bastırıldı.
