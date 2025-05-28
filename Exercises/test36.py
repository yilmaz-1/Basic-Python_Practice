# liste1 =[1,2,3,4,5]
# liste2 =[]
# for i in liste1:
#     liste2.append(i*2)
# print(liste2)
#
# # çıktı:
# #[2, 4, 6, 8, 10]
#
# liste2 =[i*2 for i in liste1]
# print(liste2)
# # çıtkı:
# # [2, 4, 6, 8, 10]

# yukarıda ki iki kod bloğuda aynı şeyi ifade etmektedir. fakat ilk kod bloğu for döngüsü ile oluştutulmuşken 2. kod
# bloğu ise list compression yöntemi ile oluşturulmuştur.

#*******************************************

# def ikileCarp(a): # bildiğimiz klasik bir fonksiyon tanımlaması yaptık.
#     return a*2 # return ifadesini de fonksiyonu istediğimiz yere çağırmak için kullandık.
# print(ikileCarp(5)) # ekrana fonksiyon çağrılarak içine verdiğimiz değer hesaplatılıp yazdırıldı.
# #çıktı:
# # 10
#
# ikiyleCarp =lambda a: a*2 # yukarıda klsaik yöntem ile tanımladığımız fonksiyon bloğu burada lambda ifadesi ile
# # anımlandı.
# print(ikiyleCarp(3)) # fonksiyon çağrılıp içine yollanan değer hesaplatılarak ekrana basıldı.
# #çıktı:
# # 6

# def toplam(*c): # klasik yöntem ile bir fonksiyon tanımı yaptık. fakat burada yıldız ile esnek sayıda argüman
#     # vereceğimizi belirtmiş olduk.
#     toplama=0 #toplama isminde bir değişken tanımladık. çünkü toplam fonksiyonu içine vereceğimiz sayıları toplamasını
#     # yapacağız ve toplama değişkenine atacapımız için sıfırdan başlamalı
#     for i in c:
#         toplama+=i
#     print(toplama)
#     return # return ile de fonksiyonu nerde çağırısak çağıralım orada kullanmak için tanımladık.
# toplam(1,2,3,4)










