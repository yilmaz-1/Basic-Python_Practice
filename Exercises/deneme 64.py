# name = "mehmet ışık"
# for letter in name:
#     if letter =="ş":
#         break
#     print(letter)

#çıktı : görüldüğü üzere döngü boyunca letter değişkeni sürekli name stringi üzerinde gezinip
# tek tek her bir karakteri alıp kerana bastırdı. fakat letter değişkeni 'ş' ile karşılaştığında
#döngüyü kırıp durduruyor. string teki sornaki karakterlere geçmiyor.
# m
# e
# h
# m
# e
# t
#
# ı

# name = "mehmet ışık"
# for letter in name:
#     if letter =="ş":
#         continue
#     print(letter)
# görüldüğü üzere döngü boyunca letter değişkeni sürekli name stringi üzerinde gezinip
# tek tek her bir karakteri alıp kerana bastırdı. fakat letter değişkeni 'ş' ile
# karşılaştığında, o döngüyü esgeçip o döngüde üzerinde gezmesi gereken karateri 'ş' hiç almayıp
#o döngüyü devam ettirmeyip direk bir sonraki karakterden devam ediyor.

# m
# e
# h
# m
# e
# t
#
# ı
# ı
# k

# x=0
# while x<5:
#     if x==2: # görüldüğü üzere döngü kırıldı ve diğer karakterler üzerine gezinme işlemi yapılmadan sonlandı.
#         break
#     print(x)
#     x+=1

#çıktı:
# 0
# 1

# y=0
# while y<5:
#     if y==2:
#         continue
#     print(y)
#     y+=1

#çıktı: döngü normal çalıştı. '0' bastı y yi 1 artırdı başa döndü. sonra '1' bastırdı y yi 1 artırdı
# başa döndü. sonra y 2 olunca if bolğu çalıştı. if bloğunun altında kalan continue ifadesine gelince
# döngü direk başa döndü. y 1 artırılmadı. buna dikkat. hala 2. sonra y 2 olunca gene if bloğu çalıştı
# gene döngü tamamlanamadan başa döndü. bu sürekli böle devam eder... sonsuz döngüye girer. continue dan
# sonraki kod blokları işletilmedi ve y sürekli 2 de takılı kalıyor.
# 0
# 1


y=0
while y<5:
    y += 1
    if y==2:
        continue
    print(y)
#çıktı: görüldüğü üzere istediğimiz gibi kod çalıştı ve hatasız sonlandı.
#döngü 0 ile başladı. y 1 artırıldı if bloğu kontrol edildi 2 ye eşit olmdığı görüldü ve continue ifadesi
# çalışmadı ve deam edip ekrana 1 basıldı. sonra döngü başa döndü y 1 artırıldı sonra y nin yeni değeri 2 oldu
# if bloğu çalıştı ve kontrol edildi 2 ye eşit olduğu anlaşılınca if bloğunun içerisinde olan continue ifadesi
# çalıştı. sonra continue den sonraki hiç bir kod çalıştırılmadan y nin 2 değeri es geçelim ynai o döngü tamamlanmadan
#direk başa dönüp y zaten 2 idi. 1 artırıldı ve y ni yeni değeri 3 oldu if bloğu kontrol edildi. y 2 ye eşit olmadığı
#için döngü devam edip ekrana 3 bastırıldı ve döngü başa döndü. bu döngü y<5 den küçük olana kadar devam edip sonsuz
#döngüye girmeden sonlandı.
# 1
# 3
# 4
# 5


















