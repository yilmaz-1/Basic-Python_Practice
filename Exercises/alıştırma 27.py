import turtle # modül progama dahil edildi.
turtle.color("white") # çizgi rengi belirlendi.
turtle.bgcolor("red") # arka plan engi belirlendi.
turtle.home() # başlangıç noktasına yani (0,0) noktasına geri dön dedik.
turtle.pensize(5) # çizgi kalınlığını belirledik.

for x in range(360): # burada döngü kurularak aşağıda tanımlı olan kodların 360 defa tekrarlanması ile daire çizdirildi.
    turtle.fd(1) # 1 adım ileri git
    turtle.left(1) # 1 derece sola dön

# her döngüde 1 adım ileri git bir derece sola dönüş yaparak bu döngü 360 defa çalışarak daire çizildi.



