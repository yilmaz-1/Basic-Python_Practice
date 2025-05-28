liste =["ersin","ali","veli","selim","mahmut","erkan"] # burada bir liste tanımladık. içerisnde string ifadeler olan.
liste1=list() # burada boş bir liste1 isimli bir lliste tanımladık.
liste2 =list() # burada boş bir liste2 isimli bir liste tanımladık.
for i in liste: # burada for döngüsü kullanarak yukarıda tanımladığımız liste içerisinden string ifadeleri i ile her döngüde tek tek alıyor.
    if (i.endswith('li')==True): # burada ise for döngüsünde aldığımız i string ifadelerini if koşulunu sağlyan tüm i string ifadelerini
        liste1.append(i) # daha önce yukarıda tanımladığımız liste1 isimli boş liste içine append fonksiyonu ile atıyoruz
    else: # burada ise if bloğunda sağlanmayan koşullar için geçerli olan i string değerleri daha önce boş oalrak tanımlanan liste2 içerisne append komutu ile yollanıyor.
        liste2.append(i)
print(liste1) # burada ise kod çalışıp bittiğine liste1 i in son hali ekrana yazdırılıyor.
print(liste2)# burada ise kod çalışıp bittiğinde liste 2  inin son hali ekrana yazdırılıyor.


