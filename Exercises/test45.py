def pisagor_bulma(): # burada argüman verilmeden pisagor_bulma isminde bir fonksiyon tanımlanıyor.
    pisagor_liste= [] # aşağıdaki işlemlerde elde ettiğimiz değerleri yollamak için kullancağımız bir adet
    # boş liste oluşturuyoruz.
    for i in range(1,5): # burada for döngüsü ile range fonksiyonu kullanarak 1 den 5 kdar olan sayıları
        # i değişkeni ile alıyoruz.
        for j in range(1,5): # burada ise ikinci bir döngü tanımlıyoruz. bu döngü ile j değişkeni ile range
            # fonksiyonu kullnarak 1 den 5 e kadar olan değerleri alıyoruz.
            print(i,j)
            c= (i**2 +j**2)**0.5 # yukarıda elde ettiğimiz ikilileri bu denklemde yerine koyup c değişkenin buluyoruz.

            if (c==int(c)): # eğer c değişkenin integer ifaddesi kendine eşit ise
                pisagor_liste.append((i,j,int(c))) # bu tüm i j ve integer c değerleri yukarıda tanımladığımız
                # boş pisagor_liste içerisine yollanıyor.
    return pisagor_liste # bu liste return ile bize geri dönüyor.

for i in pisagor_bulma(): # yukarıda tanımladığımız fonskiyon for döngüsü içinde çağırılıyor.
    print(i) # for döngüsü ile elde eidlen değerler ekrana basılıyor.

#çıktı:
# (3, 4, 5)
# (4, 3, 5)

# yukarıda iki adet iç içe döngü kullandık çünkü i ve j değerlerini ikili (i,j) olarak elde etmek için.
# c= (i**2 +j**2)**0.5 denkleminde c yi bulmak için belirtilen aralıklarda ki sayıları ikili olarak elde etmek için
# iç içe döngüler ile
# 1 1
# 1 2
# 1 3
# 1 4
# 2 1
# 2 2
# 2 3
# 2 4
# 3 1
# 3 2
# 3 3
# 3 4
# 4 1
# 4 2
# 4 3
# 4 4
# ikilileri elde ettik ve bu ikilileri kullanarak c değerini bulduk ve böylece (i,j,int(c)) üçlülerini elde ettik.
# (3, 4, 5)
# (4, 3, 5)