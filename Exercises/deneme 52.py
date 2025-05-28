
# while True: # while ile döngü oluşturuluyor. while yapısı döngü oluşturmak için kullanılır. True ifadesi ise bu döngü durudurulana kadar sürekli çalışmasını sağlar.
#     vize1 = float(input("vize1:")) # kullanıcıdan input ile vize1 notu girilmesi isteniyor. girilen bu değer float ile veri tipi dönüşümü yapılarak vize1 değişkenine atılıyor.
#     vize2= float(input("vize2:")) # kullanıcıdan input ile vize2 notu girilmesi isteniyor. girilen bu değer float ile veri tipi dönüşümü yapılarak vize2 değişkenine atılıyor.
#     final = float(input("final:")) # kullanıcıdan input ile final1 notu girilmesi isteniyor. girilen bu değer float ile veri tipi dönüşümü yapılarak final değişkenine atılıyor.
#     geçmenotu = ((vize1 * 0.4) + (vize2 * 0.4))/2 + (final * 0.6) # geçme notu isminde bir değişken tanımlanıp kullanıcıdan alınan değerler gerekli işlemler yapılırak geçmenotu değişkenine atanıyor.
#     if (final > 70): # koşul durumu tanımlanıyor. eğer filan sonyu 70 den büyükse program bu kodda çalışıyor ve
#         print(f"geçme notu {geçmenotu}") # ekrana yazdırılıyor. fakat burda f string metodu kullanılmıştır. 2 çift tırnak ifadesinden önce f ifadesi konularak süslü prantez içine gelmesini istediğimiz değişken yazılır. böylelikle uzun karamaşık yamak kısalır.
#         print("geçti") # ekrana basılır.
#     elif (final < 70): # yukarıdaki if bloğu çalışmaz ise yani oradaki şart sağlanmaz ise program bir sonraki kod bloğuna geçer. elif bloğundaki kod sağlanırsa eğer bu kod bloğu çalışır ve alt bloklardaki kodlar çalışmaya başlar.
#         if(geçmenotu >= 50): # eğer geçmenotu değişkeni 50 ye eşit ve 50 den büyük ise
#             print(f"geçme notu {geçmenotu}") # ekrana yazsırılır. f string kullanılmıştır.
#             print("geçti")# ekrana yazdırılır.
#         else: # eğer yularıda ki hiç bir kod bloğu çalışmaz ise yani o kod bloğunda ki şartlar sağlanmaz ise else bloğu çalışır.
#             print(f"geçme notu {geçmenotu}") # ekrana yazdırılır.
#             print("kaldı.") # ekrana yazdırılır.
# çıktı:
# vize1:50
# vize2:62
# final:78
# geçme notu 69.19999999999999
# geçti
# vize1:

# *************************************************************************

def notHesaplama(vize1,vize2,final): # notHesaplama isimli ve 3 argümana sahip bir fonksiyon tanımlanıyor.
        #vize1 = float(input("vize1:")) # kullanıcıdan input ile vize1 notu girilmesi isteniyor. girilen bu değer float ile veri tipi dönüşümü yapılarak vize1 değişkenine atılıyor.
        #vize2 = float(input("vize2:")) # kullanıcıdan input ile vize2 notu girilmesi isteniyor. girilen bu değer float ile veri tipi dönüşümü yapılarak vize2 değişkenine atılıyor.
        #final = float(input("final:")) # kullanıcıdan input ile final1 notu girilmesi isteniyor. girilen bu değer float ile veri tipi dönüşümü yapılarak final değişkenine atılıyor.
        #geçmenotu = ((vize1 * 0.4) + (vize2 * 0.4)) / 2 + (final * 0.6) # geçme notu isminde bir değişken tanımlanıp kullanıcıdan alınan değerler gerekli işlemler yapılırak geçmenotu değişkenine atanıyor.
        if (final > 70): # koşul durumu tanımlanıyor. eğer filan sonyu 70 den büyükse program bu kodda çalışıyor ve
            print(f"geçme notu {geçmenotu}") # ekrana yazdırılıyor. fakat burda f string metodu kullanılmıştır. 2 çift tırnak ifadesinden önce f ifadesi konularak süslü prantez içine gelmesini istediğimiz değişken yazılır. böylelikle uzun karamaşık yamak kısalır.
            print("geçti") # ekrana basılır.
        elif (final < 70): # yukarıdaki if bloğu çalışmaz ise yani oradaki şart sağlanmaz ise program bir sonraki kod bloğuna geçer. elif bloğundaki kod sağlanırsa eğer bu kod bloğu çalışır ve alt bloklardaki kodlar çalışmaya başlar.
            if(geçmenotu >= 50):  # eğer geçmenotu değişkeni 50 ye eşit ve 50 den büyük ise
                print(f"geçme notu {geçmenotu}") # ekrana yazsırılır. f string kullanılmıştır.
                print("geçti") # ekrana basılır.
            else: # eğer yularıda ki hiç bir kod bloğu çalışmaz ise yani o kod bloğunda ki şartlar sağlanmaz ise else bloğu çalışır.
             print(f"geçme notu {geçmenotu}")  # ekrana yazdırılır.
             print("kaldı.") # ekrana yazdırılır.
        return # return ile fonksiyon daha sonra programın başka yerlerinde kullanılmak üzere döndürülür.

while True: # while ile döngü oluşturuluyor. while yapısı döngü oluşturmak için kullanılır. True ifadesi ise bu döngü durudurulana kadar sürekli çalışmasını sağlar.
    vize1 = float(input("vize1:"))
    vize2 = float(input("vize2:"))
    final = float(input("final:"))
    geçmenotu = ((vize1 * 0.4) + (vize2 * 0.4)) / 2 + (final * 0.6)
    if (notHesaplama(vize1,vize2,final)):
        continue

# çıktı:
# vize1:52
# vize2:63
# final:66
# geçme notu 62.6
# geçti
# vize1:






