def bilgilerigöster(ad="Bilgi Yok\n",soyad="Bilgi Yok\n",numara="Bilgi Yok\n"): # ters \n komutu ile yan yana yazmak yerine bir alt satıra inmemizi sağladı. Eğer \n komutu silinirse yan yana yazdırır ekrana
    print("Ad:",ad,"Soyad:",soyad,"Numara:",numara,)

bilgilerigöster() #içi boş olduğu için varsayılan olarak ne tanımlandıysa onu basar ekrana.
# çıktı:
# Ad: Bilgi Yok
#  Soyad: Bilgi Yok
#  Numara: Bilgi Yok

bilgilerigöster("mehmet","ışık")
# çıktı:
# Ad: mehmet Soyad: ışık Numara: Bilgi Yok


bilgilerigöster("mehmet","ışık","123456")
# çıktı:
# Ad: mehmet Soyad: ışık Numara: 123456

bilgilerigöster("mehmet\n","ışık\n",)
# çıktı:
# Ad: mehmet
#  Soyad: ışık
#  Numara: Bilgi Yok


bilgilerigöster("mehmet\n","ışık\n","123456")
#çıktı:
# Ad: mehmet
#  Soyad: ışık
#  Numara: 123456

# # burada hep sıralı olarak bilgileri çağırdık. fakat sıralı olarak değilde ad ve soy ad bilgisini girmeden sadece numrayı çağırmak istersek eğer

bilgilerigöster(numara="123456") # şeklinde yazmamız gerekir.
# çıktı:
# Ad: Bilgi Yok
#  Soyad: Bilgi Yok
#  Numara: 123456