liste =["ersin","ali","veli","selim","mahmut","erkan"] # Burada bir içerisinde string ifadeler olan bir liste tanımlanmıştır.
liste1=list() # burada liste1 isimli bir boş bir liste tanımlanmıştır. list() fonksiyonu kullanılmıştır.
liste2 =list() # burada liste2 isimli bir boş liste tanımlanmıştır. list() fonksiyonu kullanılmıştır.
for i in liste: # for döngüsü ile yukarıda tanımlanan liste içerisinden her döngüde i ile string ifadeler alınarak bir alt kod bloğuna geçiliyor
    if(i.startswith('er')== True ): # bir üst satırda for döngüsünde elde edilen her i ile alıona  strng ifadesi bu satırdaki koşul şartında uyuyor mu diye kontrol ediliyor. burada ki koşul şudur: eğer bu alınan i string ifadesi 'er' ile başlıyor ise bu doğrudur (doğrudur  şartı Ture ile sağlanmıştır.) bu i string ifadeleri bitince kontorl edilecek i sring ifadesi kalmayınca bi alt satırda ki kod bloğuna geçiliyor.
        liste1.append(i) # eğer bir üst satırda ki şart sağlandı ise o şartı sağlayan i srting ifadesi append () fonksiyonu ile daha önce kod bloğu dışında tanımladığımız boş liste1 içine gönderiliyor. bu işlem i string değeri kalmayıncaya kadar devam edeiyor.
    else: # burada ise if koşul bloğundaki şart sağlanmaz ise devreye giriyor. yani eğer kısmı if bloğu değilse else bloğu dur. yani if bloğu Ture değilde False oluoyr ise o False olan i string değerleri bir alt satırdaki
        liste2.append(i) # daha önce kod bloğu dışında boş olarak tanımlanan liste2 içerisne append fonksiyonu ile gönderiliyor.

print(liste1) # burada ise kod bloğu çalışıp bütün i değerlerini kontrol ettikten sonra i sttring ifadeleri bitince liste1 ekrana yazdırılıyor.
print(liste2) # burada ise kod bloğu çalışıp bütün i string ifadeleri kontorl edildikten sonra konttol edilecek başka bir i string ifadesi kalmayınca ekrana print ifadesi ile yazdırılıyor.





