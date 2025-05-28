mail_adresi= input("Lütfen Geçerli Bir Mail Adresi Giriniz: ") # burada kullanıcıdan bir adet mail adresi
# girmesini istedik.

at_sayisi=mail_adresi.count("@") # burada kullanıcının girdiği mail adresi içerisinde kaç tane @ işareti olduğunu
# kontrol ettik.

nokta_sayisi=mail_adresi.count(".") # burada ise kullanıcının girdiği mail adresinde kaçtane nokta işareti olduğunu
# kontrol ettik.

if (at_sayisi==1) and (nokta_sayisi>=1): # eğer kullanıcının girdiği mail adresi içerisinde 1 adet @ işareti var
    # ve nokta sayısı da 1 veya 1 den çok ise
    print("Mail adresi doğru") # ekrana yaz.
else: # sağlanmıyorsa
    print("Hatalı Mail adresi girdiniz.") # ekrana yaz.


# burada kısaca bir mail adresi formatının doğru girilip girlmediğinin kontrolünü yapan bir program yazıldı.