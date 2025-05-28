# aşağıdakli kod bloğunda, liste içersinde yer alan elmanlardan hangisinin tamamen rakamlardan hanginin karakterlerden
# oluştuğunu tespit etmeye yarayan bir prgam yer almaktadır.
liste=["345","sadas","324a","14","kemal"] # liste
for eleman in liste: # for döngüsü ile liste içersindeki elemanlar, eleman değişkeni ile alınıyor.
    try: # bu blok içerisine, hata çıkarabilecek kodlar alındı. böylelikle bu kodların sebep olduğu hata yakalanarak
        # bizim istediğimiz hata mesajı ekrana yazdırılacak.
        eleman=int(eleman) # eğer hata ile karşılaşırsak burası hata verecek ve print çalışmayacak
        print(eleman) # ekrana yazdır.
    except:
        pass # pass deyimi bir bloğun hiç bir şey yapmadığı anlamına da gelir. yani bursaı çalışmayacak python ın hata
        # vermemesi için bu pass deyimini kullanabiliriz. except bloğu boş kalmamış olacak. hemde hatavermeden try
        # except çalışmış olacak.
