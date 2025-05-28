# aşağıda liste içerisnde yer alan elemanların karakterlerden oluşanların alınarak liste içerisine atılıp ekrana
# yazdırılmasıdır.

liste = ["345","sadas","324a","14","kemal"]

list2=[]
list3 = []

for i in liste: # burada bir for döngüsü kuruldu. bu döngü ile liste elemanları üzerinde gezilerek her döngüde liste
    # elemanlarından biri i değişkenine atanarak alınıyor.
    if i.isnumeric()==True: # eğer aldığımız i değiikeninin bütün karakterleri rakamdan oluşuyor ise, yani bu şu demek
        # i.isnumeric ifadesinin sonucu True ise,
        list3.append(i)
        for j in i: # bu if bloğu altında yeniden bir for döngüsü ile bu i elemanının elemanları üzerinde gezerek
            # tek tek alarak
            list2.append(j) # bu aldığımız j elemanlarını boş olan list2 içersine yollamak.
    else: # eğer i nin elemanlarının tamamı rakam değilse
        continue # hiç bir şey yaypma yani direk dngünün başına dön.
print(list2) # döngü bittikten sonra da list2 ifadesini ekrana yazdır.
print(list3)
