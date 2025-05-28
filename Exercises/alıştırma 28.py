import turtle # programa modülü dahil ettik.
turtle.color("white") # çizgi rengini ayarladık.
turtle.bgcolor("red") # zemin rengini ayarladık.
turtle.pensize(5) # çizgi kalınlığını ayarladık.
for i in range(36): # döngü kuruldu ve bu döngü aşağıdaki 36 defa dönecek.
    turtle.home() # her dönmesinde eve başlangıç noktasına (0,0) noktasına geri gelsin.
    turtle.left(i*10) # burada her turda döneceği dereceyi 10 ile çarparak dön. yani 1. turda 1*10 derece ikinci turda
    # 2*10 derece dön şeklinde.. eğer bu i*10 nu yapmasaydık her seferinde aynı yerde üst üste daireler çizecekti.
    # ama bu kod ile her seferinde *10 derece dönerek şekil oluştu.
    turtle.circle(100) # son olarak da 100 yarıçaplı bir daire oluştur dedik.

# for döngüsü her döngüde bu kodu çalıştıracak ve 36 defa dönecenecği bu kod, 36 tane başlangıçları ortak (0,0)
# daire çizilecek.