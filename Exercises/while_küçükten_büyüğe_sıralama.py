liste=[] # boş bir liste tanımlandı.
i =1 # i değişkeni tanımlandı. while döngüsünü döndürmek için.
while i < 6: # while ile bir adet döngü kuruldu koşulu ise i değeri 6 dan küçük olduğu sürece çalışsın istendi.
    a =int(input("Bir Sayı Giriniz: ")) # her döngüde kullanıcıdan bir adet a değişkeni alındı.
    liste.append(a) # her döngüde alınan bu a değişkeni liste içerisine yollandı.
    i +=1 # her döngüde bu i dğeri 1 artırılarak döngünün dönmesi sağlandı.
liste.sort() # döngü bititp aldığımız bütün a değerleri liste içersine yollandıktan sonra elde edilen bu liste
# sort metodu ile küçükten büyüğe sıralandı.
print(liste) # son olarak liste ekrana yazdırılıyor.

# çıktı:

# yukarıda tanımlanan program while ile kullanıcıdan alınan a değerlerini liste içersine atıp ve onlarıda liste
# içerisnde küçükten büyüğe doğru sırlama yapıyor.







