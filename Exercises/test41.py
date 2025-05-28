

def ebobBulma(sayı1, sayı2): # burada iki argümana sahip ebobBulma isminde bir fonksiyon tanımlandı.
    liste1 = []
    liste2 = []
    liste3 = []
    for i in range(1,sayı1+1): # for döngüsü ile 1 den kullanıcıdan alınan sayı in 1 fazlasına kadar olan sayılar
        # i değişkeni ile alındı.
        if (sayı1 % i==0): # for değişkeni ile alına sayılardana eğer hernagi biri kullanıcınınn giridği sayı1 değerini
            # tam olarak bölerse
            liste1.append(i) # bunu yukarıda boş liste olarak tanımlanan boş liste işçerisine yolla.
    print(f"{sayı1} sayınısnın tam bölenleri: {liste1}")#for döngüsü bittiğinde print ile ekrana yazdırma
    # işlemi yapılıyor.
    for i in range(1,sayı2+1): # burada başka bir for döngüsü ile range fonksiyonu kullanarak 1 den kullanıcıdan alınan
        # sayı2 değerinin bir fazlasına kadar olan sayıları i değişkeni ile alıyoruz.
        if(sayı2 % i == 0):# for döngüsü ile alına i değerlerinden herhangi bir tanesi eğer kullanıcın giridği
            # sayı2 değerini tam ve kalansız böler ise
            liste2.append(i) # append komutu ile liste2 içerisine yollanıyor.
    print(f"{sayı2} sayısının tambölenleri: {liste2}")# for döngüsü bittiğinde printi ifadesi ile içinde bulunan
    # ifade ekrana yazdırılıyor.
    for a in liste1: # burada başka bir for döngüsü ile a değişkeni ile liste1 içindeki değerler tek tek alınıyor.
        if a in liste2: # eğer for döngüsü ile liste bir içinden alınan değerler liste2 içindeki değeler ile aynı ise
            liste3.append(a)# bu değerler append ile liste3 içine yollanıyor.
    print(f"{sayı1} ve {sayı2} sayılarının ortak bölenleri: {liste3}") # for döngüsü bittiğinde print ile içinde
    # buşlunan ifade ekrana yazdırılıyor.

    return max(liste3) # bu fonksiyon içinde tanımlanan bütün işlemler bititğinde bu fonksiyonu çağırdığımızda bize
    # liste3 içindeki değerlerin maksimum değeri döndürülüyor.



while True: # burada ise yularıda tanımldığımız fonksiyonu çağıracağımız döngü tanımlanıyor. işlem doğru olduğu sürece
    # çalışmaya devam etsin anlamına geliyor.

    sayı1 = int(input("Sayı1 Giriniz: ")) # kullanıcıdan sayı1 değişkenini girmesi isteniyor.
    sayı2 = int(input("Sayı2 Giriniz: ")) # kullanıcıdan sayı2 değişkenini girmesi isteniyor.
    print(f"Girdiğiniz {sayı1,sayı2} sayılarının ebobu: {ebobBulma(sayı1,sayı2)}") # print ifadesi içinde ebobBulma
    # fonksiyonu çağrılarak elde edilen ifade ekrana yazdırılıyor.
    print("************************************************************")

#çıktı:
# Sayı1 Giriniz: 15
# Sayı2 Giriniz: 24
# 15 sayınısnın tam bölenleri: [1, 3, 5, 15]
# 24 sayısının tambölenleri: [1, 2, 3, 4, 6, 8, 12, 24]
# 15 ve 24 sayılarının ortak bölenleri: [1, 3]
# Girdiğiniz (15, 24) sayılarının ebobu: 3
# ************************************************************
# Sayı1 Giriniz: 18
# Sayı2 Giriniz: 12
# 18 sayınısnın tam bölenleri: [1, 2, 3, 6, 9, 18]
# 12 sayısının tambölenleri: [1, 2, 3, 4, 6, 12]
# 18 ve 12 sayılarının ortak bölenleri: [1, 2, 3, 6]
# Girdiğiniz (18, 12) sayılarının ebobu: 6
# ************************************************************
# Sayı1 Giriniz: 5
# Sayı2 Giriniz: 66
# 5 sayınısnın tam bölenleri: [1, 5]
# 66 sayısının tambölenleri: [1, 2, 3, 6, 11, 22, 33, 66]
# 5 ve 66 sayılarının ortak bölenleri: [1]
# Girdiğiniz (5, 66) sayılarının ebobu: 1
# ************************************************************
# Sayı1 Giriniz: