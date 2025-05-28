# def selamla(isim):
#     print("selam:", isim)
#     print(f"selam {isim}")
#
# selamla("mehmet")
# selamla()

# def selam(isim="isimsiz"):
#     print("selam:",isim)
#     print(f"selam {isim}")
#
# selam()
# selam("mehmet")


def bilgilerigöster(ad= "bilgi yok",soyad="Bilgi yok", numara="bilgi yok"):
    print(f"ad: {ad} soyad: {soyad} numara: {numara}")
    print("mehmet","ışık","123456",sep=" >")


bilgilerigöster()
bilgilerigöster("mehmet","ışık","123456")

# def toplama (*parametler): # yıldız koymamızın amacı şu: istediğimiz kadar argüman tanımlaması yapabilmektir. aksi halde
#     #toplama fonksiyonu içerisine tanımlama yaptığım kadar argüman ile işlem yapmak zorunda kalırım.
#     toplam = 0
#     print("Parametreler:",parametler)
#     for i in parametler:
#         toplam+=i
#     return toplam
#
#
# print(toplama(1,2,3,4,5))
