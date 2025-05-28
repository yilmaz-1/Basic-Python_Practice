import turtle # burada modül progamın içersine dahil edildi.
turtle.speed(0) # burada şeklin oluşma hızını belirledik.
for i in range(36): # döngü kuruldu ve bu döngü 36 defa çalışacak.
    turtle.left(10) # her döngüde 10 derece sola dönecek
    for j in range(4): # yukarıdaki for döngüsü bir kez döndüğünde bu döngüde bir defa dönecek. toplam da 4 defa dönecek
        turtle.fd(100) # her dönmesinde 100 birim ileri gidecek
        turtle.left(90) # her dönmesinde ise 90 derece sola dönecek.