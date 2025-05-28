while True:  # burada döngü şartları sağlandığı sürece sürekli çalışması istendi.
    sayı = int(input("Sayı giriniz: "))  # kullanıcıdan bir adet sayı girmesi istendi ve bu sayı int e çevrildi.
    if sayı == 0:  # eğer girilen sayı sıfıra eşitse
        break  # programı kır ve bitir.
    elif sayı < 0:  # eğer sayı sıfırdan küçükse
        pass  # hiç bir şey yapmadan başa dön ve tekrar döngüyü başlat.
    else:  # aksi durumlarda
        print(sayı)  # ekrana girilen sayıyı bas




"""

pass deyimi
taslak halinde çalşırken kullanılır genelde. yani programın akışına göre bir kod yazdınız ama henüz kullanmayacaksınız.
ileride lazım olacak. orada pass deyimini kullanarak kodun çalışması engellenmiş olur.

a= input( "meyve gir: ")
if (a == "elma):
    print( "doğru")
elif ( a=="domates")
    pass   # yani burada daha ne yazdıracağımıza karar vermedik. pass deyip geçtik
    


"""





"""
while True:
    sayı = input("Sayı Giriniz: ")
    if sayı == "q":
        print("program sonlandı.")
        break
    sayı = int(sayı)
    if sayı == 0 :
        pass
    elif sayı < 0 :
        print(f"{sayı} Sayısı Negatif Bir Sayıdır.")
    else:
        print(f"{sayı} Sayısı Pozitif Bir Sayıdır.")





"""