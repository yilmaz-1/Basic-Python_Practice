# def toplama(*a):
#     return sum(a)
# print(toplama(3,5,6,4,8))
#çıktı:
#26


# def yazdir(kelime,adet):
#     print(kelime*adet)
#
# yazdir("merhaba\n",3)
#çıktı:
#merhaba
# merhaba
# merhaba


# def listeyeCevir(*args):
#     liste=[]
#     for i in args:
#         liste.append(i)
#     print(liste)
#     return liste
# listeyeCevir(4,3,5,6,"mehmet","hasan")
#çıktı:
# [4, 3, 5, 6, 'mehmet', 'hasan']




# def asalsayı(sayi1,sayi2):
#     for sayi in range(sayi1,sayi2+1):
#         if sayi >1:
#             for i in range(2,sayi):
#                 if sayi % i ==0:
#                     break
#             else:
#                 print(sayi)
#
# sayi1= int(input("Sayı: "))
# sayi2= int(input("sayı2: "))
#
# print(asalsayı(sayi1,sayi2))

# def asal(sayı):
#     if sayı >1:
#         for i in range(2,sayı):
#             if sayı % i ==0:
#                 print(f"{sayı} asal sayı değildir.")
#                 break
#         else:
#             print(f"{sayı} asaldır.")
#     else:
#         print(f"{sayı} asal değildir.")
#     return
#
# while True:
#     sayı=int(input("sayı giriniz: "))
#     asal(sayı)


# def asalSayıtoplam(sayı1,sayı2):
#     liste =[]
#     if sayı1==1:
#         sayı1=1+sayı1
#     if (sayı1 and sayı2)>1:
#         for i in range(sayı1,sayı2):
#             for j in range(2,i):
#                 if i % j ==0:
#                     break
#             else:
#                 liste.append(i)
#         print(liste)
#     else:
#         print("geçersiz giriş")
#     return sum(liste)
#
# while True:
#     sayı1= int(input("Sayı1 Giriniz: "))
#     sayı2= int(input("Sayı2 Giriniz: "))
#     print(asalSayıtoplam(sayı1,sayı2))



# def tambölenler(sayı):
#     liste=[]
#     for i in range(2,sayı+1):
#         if sayı % i ==0:
#             liste.append(i)
#     return liste
#
# while True:
#     sayı1=int(input("Sayı Giriniz: "))
#     print(tambölenler(sayı1))








