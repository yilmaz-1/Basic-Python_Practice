liste=[] # burada bir adet boş bir liste tanımlanlanmıştır.

i =0 # burada bir adet i değişknei tanımlanmıştır. ve bu değişkene 0 atanmıştır.
while i <26: # burada bir adet while döngüsü kurulmuştur. ve döngünün kuralı ise i değeri 26 dan küçük olduğu sürece
    # devam etsin ve çalışsın denmiştir.
    liste.append(i) # her döngüde elde edilen i değerleri append komutu ile boş oaln liste içersine yollanmıştır.
    i +=1 # i değeri her döngü sonun da 1 artırılarak döngünün devamlı çalışarak bir sonraki sayıya geçmsei
    # sağlanmıştır.
liste.reverse() # döngü bittikten sonra elde ettiğimiz liste revers komutu ile tersten yeniden yazdırılmıştır.
print(liste) # son olarak ise liste ekrana bastırılmıştır.

# çıktı:

# [25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]


# yukarıdaki program 0 dan 25 e kadar olan sayıları tersten olacak şekilde bir liste içerisine yollanarak ekrana
# yazdırılmasını sağlamaktadır.
