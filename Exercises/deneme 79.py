# x = "global x" # burada bir adet x değişkeni tanımlandı. bu tanımlama globalde tanımlandı. yani istediğimiz zaman
# # istediğimiz yerde kullanabileceiğimiz bir değişken oldu bu.
#
# def function(): # burda ise bir adet argümansız bir fonksiyon tanımlandı.
#     x ="local x" # burada ise fonskiyon bloğu içersinde bir adet x değişkeni tanımlandı. bu fonksiyon bloğu içerisinde
#     # tanımlanan bu değişken yerel yani local de tanımlanmış bir fonksiyon oluyor. bu şu demek: bu yerelde tanımlanan
#     # değişken sadece def ile tanımlana fonksiyon çalıştığı zaman kullanılacak aksi durumda ise hiç bir
#     # şekilde kullanılmayacak.
#     print(x)
#
# function() # burada fonsiyon çağrılıyor. gloabalde tanımlanan x değeri fakat fonksiyon içerisinde tanımlanmış local x
# # değişkeni olduğu için fonksiyon çalıştığında localde tanımlanan x dfeğişkeni kullanılıyor. eğer biz local de bir
# # x tanımlamasaydık ne olurdu? fonksiyon çağrıldığında globalde tanımlanan x değerini kullanacaktı bu sefer de fonskiyon
# print(x) # burada x değişkeni ekrana yazdırılıyor. fakat bu ekrana yazdırılan x değişkeni globalde tanımlanan
# # x değişkeni.
#
# # çıktı
# # local x
# # global x

############################################################
# # global
# name ="cinar" # burada globalde bir adet name isminde değişken tanımlandı.
#
# def ChangeName(new_name): # bir argümanlı bir fonskiyon tanımlandı
#     # local
#     name= new_name # fonskiyon bloğu içerisinde name isminde yeni bir değişken tanımlandı ve bu değişkene ise
#     # fonskiyona gönderilecek olan argüman atandı.
#     print(name) # name değişkeni ekrana yazdırılıyor.
#
# ChangeName("Ada") # fonskiyon çağrıldı ve içerisne ada str ifadesi yollandı.
# print(name) # name değişkeni ekrana yazdırıldı.
#
# # çıktı
#
# # Ada
# # cinar
#
# # yukarıdaki fonksiyon nasıl çalışıyor: fonksiyon çağrılıyor ve içersine gönderilen name değişkenini ekrana basıyor
# # daha sonra ise print ile anem ekrana basılıyor. burada öenmli olan şey şu: fonskiyon çağrıldığında local de
# # tanımlanan name değişkeni ekrana yazdırılırken print fonskiyonu ile de glabelde tanımlanan name değişkeni
# # ekrana yazdırılıyor. eğer def fonskiyon bloğu içerisinde bir adet değişken tanımlanmamış olsa idi bu sefer
# # def fonksiyonu da globalde tanımlanan değişkeni kullanacaktı.


#############################################################
# # global
# name="glabal string" # burada globalde bir adet değişken tanımaldık.
#
# def greeting(): # argümansız bir adet fonskiyon tanımladık.
#     # local
#     name = "Çınar" # fonksiyon bloğu içerisinde bir adet local de değişken tanımladık.
#
#     def hello (): # greeting fonskiyonu içersinde bir adet hello isminde bir fonskiyon daha tanımladık. eğer biz bu
#     fonksiyon içerisine ayrıca bir name değişkeni tanımlarsak bu sefer hello fonksiyonun local de tanımlanmış
#     name değişkeni olur ki print ifadesi içerisnde yer alan name bu local de tanımladığımız name değişkeninin alır.
#         print ("hello " + name) # burada hello fonksiyonu çalıştığında ekrana yazdırılacak ifade tanımlandı.
#
#     hello() # burada greeting fonskiyon bloğu içerisinde hello fonskiyonu çağrılıyor.
#
# greeting() # burada greeting fonskiyonu çağrılıyor.
#
#
#
# # çıktı:
#
# # hello Çınar
#
# # yukarıda ki fonskiyon nasıl çalışıyor: iç içe fonskiyon yapısı mevcuttur. greeting fonskiyon çağrıldığında önce
# # hello fonksiyonu çalışıyor. bu fonskiyon çalışınca print ile ekrana hello string ifadesi ve bir üst fonskiyon
# # içerisnde tanımlanan name değişkenini ekrana basıyor.son olarak da greeting fonskiyonu çalıştığında bu
# # ifade ekrana yazdırılıyor

######################################################################
# global
x= 50 # global de bir adet x değişkeni tanımlandı.
def test(): # bir adet test isminde bir fonskiyon tanımlandı.
    #global x  # biz burada bu global anahtar sözcğünü kullanarak şunu demek istedik: global de tanımlanan
    # x değişkenini kullan
    print(f"x:  {x}") # print ile x değişkeni ekrana yazdırılıyor. fakat burada şöle bir durum oluşuoyr.
    # test ismindeki fonksiyon çağrıldığında kod bloklarını yukarıdan aşağıya okumaya başladığında local de herhangi
    # bir x değişkeni tanımlanmadığı için print fonskiyonu içerisndeki x değişkenini globalde taanımlanan
    # x değişkeninden alıyor ve bu x değişkenin ekrana yazdırıyor.

    x =100 # localde bir adet x değişkeni tanımlanıyor.

    print(f"change x to: {x}") # x eğişkeni ekrana yazdırılıyor fakat burada şöle bir durum oluyor:  test isminde ki
    # bu fonksiyon çağrıldığında kod bloklarını yukarıdan aşağıya dopru okumaya devam ediyor. ve local de tanımlanmış
    # x değerini okuyunca global de tanımlanan x değişkenin local de tanımlanan x değişkeni ile değiştirip
    # o x değişknini ( 100 ) kullanıyor.

test() # fonksiyon çağrılıyor.
print(f"x: {x}") # buradaki print fonskiyonun test isimli fonskiyon ile alakası yok. print ile ekrana yazılan
# x değişkeni ise globalde tanımlanan x değişkenidir.

# çıktı
# x:  50
# change x to: 100
# x: 50





