liste= [i for i in range(10)] # burada list compression yöntemi ile bir adet liste oluşturduk. bu listenin aralığını da
# range fonksiyonu ile belirledik.
print(liste) # oluşturduğumuz listeyi print ile yazdırdık.
# çıktı
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

liste1= list(range(10)) # yukarıda list compression ile elde ettiğimiz listeyi burada list fonskiyonu ile elde ettik .
print(liste1)# elde ettiğimiz liste ekrana yazdırıldı.
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

liste3= [i for i in range(10) if i%2==0] # burada list compression ile bir liste oluşturuduk fakat ilk örnetten
# farklı olarak şunu da sorguladık. if ile koşul kuruduk. range fonskiyonu kullanarak for döngüsünde elde ettiğimiz
# sayıları if koşuluna sokarak 2 ile bölümünden kalan sıfır olup olmadığını sorguladık.
print(liste3) # elde edilen listeyi ekrana yazdırdık.
# çıktı
# [0, 2, 4, 6, 8]

liste4= [] # boş bir liste oluşturduk.
for i in range(10): # yukarıda list compression yöntemi ile elde ettiğimiz liste yi burada normal yolla for döngüsü
    # kurarak elde eettik.
    if i % 2==0: # if ile bir koşul durumu oluşturduk. for döngüsü ile elde ettiğimiz i değerleinin 2 ile bölümnesi
        # durumunu kontrol ettik.
        liste4.append(i) # if koşuluna uyan i değerlerini ise append fonksiyonu ile boş olan lsite4 içerisine yolladık.
print(liste4) # yeni liste ekrana bastırıldı.
#çıktı
# [0, 2, 4, 6, 8]

liste5= [
    [1,2,3],
    [4,5,6],
    [7,8,9],
    [10,11,12]
] # burada iç içe liste oluşturuldu.

liste6=[] # boş bir liste oluşturuldu.
for i in liste5: # liste5 ile oluşturduğumuz liste içinden for döngüsü ile her döngüde bir elemanı
    # i değeri olarak alınıyor.  bu aldığımız i değerleri liste5 in iç içe liste olduğundan dolayı i değerleri
    # de bir liste oluyor.
    for j in i: # bir önceki liste de elde ettiğimiz liste formatındak i değleri içersinden de for döngüsü ile
        # j değeri olınıyor.
        liste6.append(j) # elde ettiğimiz j değerleri de append fonskiyonu ile boş liste içersine atılıyor.
print(liste6) # erkrana yazdırılıyor.
#çıktı
# [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

liste7= [j for i in liste5 for j in i] # yukarıda for döngüsü kurarak elde ettiğimiz listeyi buradalist compression
# yöntemi ile elde ettik. önce liste5 içerisnden i değerleri olarak elemanlar alındı. sonra o i değerleri içersinden de
# j olarak değerler alındı.
print(liste7) #ve j değerleri ekrana bastırıldı.
# çıktı
# [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]