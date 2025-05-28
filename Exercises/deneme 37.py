def toplama(*a): # ilk 5 satırda foksiyonu tanımladık yazdık. sonraki 7. 8. ve 9. satırlarda ise fonksiyonu hangi argümanlarda çağırmak istediğimizi yazdık
    toplam=0 # değişkeni sıfıra eşitleyip tanımladık. çünkü bu değişkeni for döngüsü içinde kullanacağız.
    for i in a: # for döngüsü ile fonsksiyon içine gönderilen parametreler üzerinde gezinerek i değeleri elde ediyoruz.
        toplam+=i # döngüde elde ettiğimiz i değelerini daha önce sıfıra eşitleyerek tanımladığımız toplam fonksiyonuna göndererek topluyoruz.
    print(toplam) # döngü bittikten sonra toplam değişkenini ekrana bastırıyoruz.

#görüldüğü üzere parametrenin önüne * koyunca artık biz a esnek değerler ile çalışabilir hale geldi.istedğiniz kadar değer ifade verebiliyoruz.

toplama(1,2,3)
# çıktı:
# 6

toplama(1,2,3,4,5,6)
# çıktı:
# 21

toplama(20,30,45,63,75)
# çıktı:
# 233