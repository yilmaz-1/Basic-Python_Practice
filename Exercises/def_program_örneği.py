def yasHesapla(dogumYili): # yas hesapla isminde bir program tanımladı.
    return 2021 - dogumYili # bu tanımlanan program bize return ifadesi ile şuanki yıldan kullanıcının girdiği
    # doğum yılı bilgisini çıkararak programı çalıştırdığımız yere döndürüyor.

def EmekliligeKacYilKaldi(dogumYili,isim): # burda emekliliğe kaç yıl akldığını hesaplayan bir adet program tanımlandı.
    '''
    :param dogumYili: kullanicidan alinan dogum yili bilgisi
    :param isim: kullanicidan alinan kisi ismi
    :return: bu foksiyon bize kullanicinin girdigi veriler ile emekli olma yasini ve durumunu döndürüyor.
    ''' # bu tırnak içersindeki bilgi ifadesi ise bu tanımlana programın ne işe yaraddığı hakkında bilgi veriyor.
    # fakat burada ilginç bir nokta var: biz bu  tırnak ifadalerini bu programın içerisine yazdığımız zaman, program
    # otomatik olarak kendisi bize hangi bilgi ve pramatreleri girmemiz gerektiğini gömülü olarak veriyor. param
    # dogumyili param isim ve return ifadelerini kendisi ototmaitk olarak bize veriyor.
    yas = yasHesapla(dogumYili) # burada yas isminde bir adet değişken tanımladık ve bu değişken içersinde ise yukarıda
    # tanımladığımız yaş hesaplama programını çağırdık.
    emeklilik= 65 - yas # emeklilik isminde bir değişken tanımladık. hesapladığımız bu yaş değerini ise işleme sokarak
    # emeklilik değikenin değerini elde ettik.
    if emeklilik > 0: # eğer emeklilik değeri sıfırdan büyük ise
        print(f"Emekliliğinize {emeklilik} yıl kaldi ") # ekrana yazdırılır.
    else: # değilse
        print("Zaten Emekli Oldunuz.") # ekrana yazdırılır.

EmekliligeKacYilKaldi(1989,"Ahmet") # burada, emeklilik hesaplama ilei ilgili tanımlana program çağrılıp
# çalıştırılmıştır.
print(help(EmekliligeKacYilKaldi)) # burada ise bu program hankkında açıklama nasıl çalıştığı hakkında bilgi girildi
# ise bu bilgieri ekrana yazdırmak için yazılmıştır.