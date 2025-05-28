import turtle # modül progama dahil edildi.
turtle.color("white")# çizgi rengi belirlendi
turtle.bgcolor("red")# zemin rengi ayarlandı.

for i in range(200): # burada döngü oluşturuldu. böylelikle döngü her dönmesinde bir adet kare çizildi. Bu döngü 2
    # 00 defa dönerek sonlandı.
    turtle.fd(i) # her döngü de i kadar ileri git yani 1. döngüde 0 birim 2. döngüde 1 birim 3. döngüde 2 birim ileri
    turtle.left(95) # her döngüde 91 derece sola dön

