import turtle # burada turtle modülü programa eklendi.
turtle.color("white") # burada çizgi rengi belirlendi
turtle.bgcolor("red") # çizdiğimiz karenin zemin rengi belirlendi.
for x in range(4): # burada for döngüsü kurularak her döngü de aşağıda tanımlanan işlemler yapılması sağlandı.
    turtle.write("x:" + str(x)) # burada her döngüde o döngü numarası başalangıç yerine yazdırıldı. str ile de int olan
    # döngü numarası string e çevrildi.
    turtle.fd(100) # 100 birim ileri gidildi.
    turtle.left(90) # 90 derece dönüldü.

# yukarıdaki işlem her döngüde yapıldığı için 4 döngü sonunda bir kare şekli oluştu.