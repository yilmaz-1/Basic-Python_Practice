liste = ["1", "2", "5a", "10b", "abc", "10", "50"]


# Liste elelmanları içindeki sayılsal değerleri bulunuz.

# for x in liste: # burada for döngüsü ile liste üzerinde geiznerek bütün elemanları tek tek alıp bunu da x olarak
# aldık. try: # bu kod bloğunda hata vereceğini düşündüğümüz kodlar yazılarak deneniyor. result=int(x) # result
# isminde bir değişken tanımlandı. bu değişkenin değeri ise liste içerisinden elde # ettiğimiz x değerlerini int e
# çevirerek elde ettiğimiz değerler. bu kod hata çıkarabilecek bir kod bloğudr. # yani int e çevirirken x değeri eğer
# sayısal bir ifade değilse int fonksiyonu çalıştığında hata verecektir. Y # ani ValueError hatası verecektir ve bir
# alt koda bloğuna yani except bloğuna geçip bu hatayı çalıştıracak. # hata yoksa pirnt ile ekrana değeri yazacak.
# print(result) except ValueError: # bu kod bloğunda ise yukarıda ValueError hatası verrirse bu hatayı burada
# belirtiyoruz. print("hata yakaladı", x) continue # fakat burada, try kısmında bir hata yakaladık ve except bloğu
# çalıştı devamında da contionue bloğu çalışırsa olan şey şu: contione ifadesi diyor ki bu hatalı değeri görem ve
# başa tekrar dön .


# Kullanıcı " q" değerini girmedikçe aldığınız her inputun sayısal olduğundan emin olunuz. Aksi halde hata mesajı yazın.

# while True: # burada bir adet döngü kuruldu . bu döngü şartlar sağlandığı sürece devam edecek ve dönecek.
#     sayi= input("sayı: ") # burada kullanıcıdan her döngünün başında bir adet sayı girmesini istiyoruz input komutu ile.
#     if sayi=="q": # eğer kullanıcıdan aldığımız sayı  q ifadesine eşit ise
#         print("döngü sonlandırıldı.")
#         break # döngü burada kırılıyor ve döngü sonalndırılıyor.
#
#     try: # burda ise kullanıcıdan alına değerler kontorl ediliyor. sıkıntı çıkaracak değeler varsa
#         # burada o değer yakalnıyor ve ekrana yazdırılıyor.
#          result = float(sayi) # kullanıcıdan alınan değer float a çevriliyor. zaten bu değer bu çevirme işlemini
#         # yapamıyor ise sıkıntı var demek
#          print("girdiğiniz sayı: ",result) # ekrana hata mesajı ve sıkıntılı olan sayı ekrana yazdırılıyor.
#     except ValueError: # burada ise yukarıda o değerde hata çıktı ya işte o hata türü ile yakalıyoruz.
#         # yani try çalışınca bu kod bloğuda çalşıyor.
#          print("geçersiz sayı")
#          continue



# Girilen parola içinde türkçe karakter hatsı veriniz.

# def checkPassword(parola): # burada bir adet fonskiyon tanımladık. bu fonskiyon bir argümanlı ve argümanı ise parola dır
#     turkce_karakterler = "ğĞıüÜjşŞİöÖçÇ" # burada ise parolamızda kullanılmasını istemediğimiz karakterleri tanımladık.
#
#     for i in parola: # for ile bir döngü kurduk. girilen parola içerisndeki her karakteri  her döngü de i olarak al.
#         if i in turkce_karakterler: # her döngü de aldğımız bu i değeleri eğer yularıda tanımladığımız turkce_karakter
#             # listesi içerisinde var ise
#             raise TypeError("parola türkçe karakter içeremez.") # raise fonksiyonu ile bu hatayı TypError olarak bize
#             # gönder fırlat.
#         else: # eğer böle bir hata çıkmadıysa pass ile geç direk.
#             pass
#
#     print("geçerli parola") # ekrana bunu yaz.
#
# # yukarıda fonskiyon tanımlandı. şimdi bu fonksiyonu kullanacağımız döngü ve parola alma işlemini tanımlayalım.
#
# while True: # burada bir adet while True döngüsü tanımladık. koşul sağlandığı sürece döngü devam edecek.
#     parola = input("parola: ") # her döngü başında kullanıcıdan bir adet parola istenecek.
#     try: # bu girilen parola yularıda ki fonksiyon içersine gönderilerek orada koşullar kodlar kontrol edilecek. eğer ki
#         # yukarı daki fonskiyondan bize hata msj gönderiliyorsa atılyıorsa (raise ile)
#         checkPassword(parola)
#     except TypeError as err: # bize hata msj verecek bu hata msjı da zaten yularıda fonskiyon içerisinde tanımlamıştık
#         # ( parola türkçe karakter içeremez diye ) biz bu hata msjını da err objesi olarak tanımladık burada.
#         print(err) # bu hata msjını ekrana yazdırıyoruz.
#     else: # parola girildi ve hata msjı vermedi tanımladığımız fonksiyon içerisine gönderilen parola bütün şartları
#         # sağladı ve hata msjı fırlatmadı bize. o zaman bu kod bloğu çalışacak ve
#        break # döngü burada kırılarak program sonlandırılacaktır.



# Faktöriyel fonskiyonu oluşturup fonskiyona gelen değer için hata mesajları verin.

def faktöriyel(x): # biz burada bir adet faktöriyel fonksiyonu tanımladık. bu fonksyon bir argümanlı ve argümanı ise x
    x= int(x) # burada ise bu tanımladığımız fonksiyonun argümanı olan x değerini int fonskiyonu ile sayılsal
    # bir değer çeviriyoruz. tam ondalıksız bir değere.

    if x<0: # burada ise faktöriyel fonskiyonun argümanı olan x değeri eğer sıfırdan küçük ise yani negatif bir sayı ise
        raise ValueError("Negatif değer") # bize bir hata mesajı fırlat demektir bu. bu hata sayılsal bir değer ile
        # alakalı olacağını düşündüğümüz için tahmin ettiğimiz için ValueError hatası yollamasını istedik.
    # yukarıda x ile olabiliecek durumları tanımladık şimdi ise artık faktöriyeli hesaplatacağımız kod bloğunu
    # yazacağız fonksiyon içerisine
    result = 1 # result isminde bir değişken tanımladık ve bunu 1 olarak belirledik. bu değişkeni aşağıdaki faktöriyel
    # işleminde her döngüde tekrar tekrar kullanacağız.

    for i in range(1, x+1): # burada bir adet for dngüsü kurduk. amacımız faktöriyel hesaplatırken bu döngü ile 
        result *=1
    return result

for x in [5,10,20,-3,"10a"]:
    try:
        y = faktöriyel(x)
    except ValueError as err:
        print(err)
        continue
print(y)









