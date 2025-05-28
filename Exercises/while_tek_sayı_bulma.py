baslangic= int(input("Başlangıç Sayısını Giriniz: ")) # bu kod satırında baslangıc isminde bir adet değişken tanımlandı
# ve bu değişken input fonksiyonu kullanılarak kullanıcıdan alındı.
bitis= int(input("Bitiş Sayısnı Giriniz: ")) # bitiş isminde bir değişken tanımladı ve bu değişken de input fonksiyonu
# kullanılarak kullanıcıdan alındı.
liste= [] # liste isminde bir adet boş bir liste tanımlandı.
i = baslangic # i değişkeni tanımlandı. ve bu değişkene başlangıç değişkeni tanımlandı. burada amaç şu:  sonraki
# yazacağımız while döngüsünde başalngıç ismi yerine i değerini kullanamka. görüntü açısından daha iyi olur.
while i < bitis: # burada bir adet whlie ile bir adet döngü kuruldu. döngünün şartı ise i değerinin yani kullaınıcıdan
    # alınan i değerinin aynı şekilde kullanıcıdan alına bitiş değerinden küçük olana kadar bu döngünün sağlanmasıdır.
    i +=1 # burada ise i değeri her döngü de 1 artırılmıştır. eğer bunu yapmaz isek döngü diğer sayılara geçemeyecektir.
    # i artırma işlemini burada yapmamız sonucunda kullanıcıdan aldığımız başlangıç değerini işleme sokmamış ve bir
    # sonraki sayıdan başlamış oluyoruz değerlendirmeye.
    if (i % 2 ==1): # burada bir adet if ile koşul bloğu oluşturulmuştur. bu koşul bloğunda ise: eğer her döngüde
        # elde edilen i değerleri 2 ile bölümünden kalan sayı 1 ise (ki bu sayının tek olduğunu gösterir)
        liste.append(i) # if bloğndaki koşul sağlanıyor ise bu koşulu sağlayan i değerlerini boş olarak tanımlanan
        # liste ye yolla.
    #i +=1 # eğer i artırma durumunu burada tanımlar isek kullanıcıdan aldığımız başlangıç sayısnın da kontrol etmiş
    # oluruz. başlangıç sayısını da işleme sokmuş oluruz.
print(liste) # en son olarak bu döngü tamamlanıp artık döngü bittikten sonra bu listeyi ekrana bastır.

# çıktı:
# Başlangıç Sayısını Giriniz: 5
# Bitiş Sayısnı Giriniz: 20
# [7, 9, 11, 13, 15, 17, 19]

# yukarıdaki program aslında kullanıcıdan alınan 2 sayı arasındaki tek sayıları tespit etmeye yarıyor.