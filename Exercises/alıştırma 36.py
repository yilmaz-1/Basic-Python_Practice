# burada rüzgar gülü alıştırması yapmaya çalıştık.


import turtle # turtle modülünü programa dahil ettik.

renkler= ["red","yellow","blue","green"]# burada rüzgar gülünde kullanacağımız renkleri tanımladık.

turtle.pensize(5) # burada kalemin cizgi kalınlığını tanımladık.

turtle.home() # burada her döngü bittiğinde kalem tekrar en başa geri dönmesini istedik.

for i in range(200): # burada bir adet döngü kuruldu. 0 ile 200 arasında .
    siradakirenkindeksi= i%4 # burada bir adet değişken oluşturuldu. bu değişkene ise for döngüsü ile her döngüde elde
    # edilen edilen i değerinin 4 ile bölümünden kalan atandı. Yani: i=0%4=0, i=1%4=1 , i=2%4=2 , i=3%4=3 , i=4%4=0
    # i değeri hep 0,1,2,3 değerleri arasında bir değer alıyor. Neden 4 e böldük, çünkü renkler dizisi 4 karakterli
    # olduğundan dolayı ve ve dizinin içersindeki elemanların indeksi 0,1,2,3 olmasından dolayı. range ile aldığımız
    # aralıkta sayıların döre bölümünden kalan hep 0 ile 3 arasında ve bu dizinin indeks sayısıda 0 ile 3 arasında.

    siradakirenk=renkler[siradakirenkindeksi] # şimdi burada ise şunu yapıyoruz. her turdu bir renk almamız lazım.
    # bu rengi alırken dzinin indeks numarasından faydalanıyoruz. yukarıda 4 ile bölüm ile her turda bir indeks
    # numarası alıyoruz zaten (0,1,2,3)  bu indkes numrasını da renkler[0], renkler[1 ], renkler[2], renkler[3]
    # şeklinde yaparak her turda renkler dizisinin sıfırıncı birinci ikinci üçüncü indeksini alıyoruz. bunu da
    # sıradakirenk olarak atıyoruz.

    turtle.pencolor(siradakirenk) # burada da kalemin rengini belirledik. her turda kalemin rengini renkler dizisi
    # içinden sıradadkirenk değişkeni ile belirledik. her turda sıradakirenk değişkeni ne olduysa kalemin rengide o oluoyr.
    turtle.fd(i) # her turda i kadar ileri gidiyoruz.
    turtle.left(91) # her durda 91 derece sola dönyoruz.