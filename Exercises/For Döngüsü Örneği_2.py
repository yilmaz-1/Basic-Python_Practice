a=list() # a isminde bir değişken tanımladık ve bunu de list() fonksiyonu ile boş bir liste haline getirdik.

for i in range(10): # for döngüsü ile range fonskiyonu kullanarak 0 dan 10 kadar olan fakat 10 hariç sayıları aldık ve
    # i değerine atadık.
    a.append(i) # bu i değerlerini append komutu ile boş a listesi içerisine attık.
print(a) # artık içi dolu olan a listesi ekrana bastırıldı.
print(*a) # içi dolu olan a listesi * parameteresi kullanılarak parçalandı ve lsite dışına çıkarıldı.
print(*a, sep=",") # * parametresi ile parçalanıp liste dışarısına çıkarılan her karakter arasına da sep parametresi
# ile de virgül yerleştirildi.