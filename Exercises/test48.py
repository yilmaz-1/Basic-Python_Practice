
MehmetHesap= {
    "ad":"mehmet ışık",
    "hesapNo": "123456",
    "bakiye": 3000,
    "ekHesap": 2000,
    "sifre": "12345"
}

EnginHesap= {
    "ad":"Engin Işık",
    "hesapNo": "12345689",
    "bakiye": 2000,
    "ekHesap": 1000,
    "sifre": "1234"
}

FeritHesap= {
    "ad":"Ferit Işık",
    "hesapNo": "1234568900",
    "bakiye": 2000,
    "ekHesap": 1000,
    "sifre" : "123"
}


print("Güneş Banka Hoşgeldiniz...")
print("****************************")

print("""

İŞLEM MENÜSÜ
1.Hesap Bilgileri Kontrolü
2.Para Yatırma 
3.Para Çekme
4.Bakiye Sorgulama
5.Hesaptan Çıkış

""")

def paraCek(hesap,miktar):

    islemNo=input("Yapmak istediğniz İşlem Numrasının Giriniz: ")

    if islemNo=="1":
        print(f"{hesap}")
    elif islemNo=="2":
            miktar=input(f"Yatırmak İstediğiniz Tutarı Giriniz: ")
            miktar=int(miktar)
            hesap['bakiye']+=miktar
            print(f"Yeni Bakiyeniz {hesap['bakiye']} Türk Lirasıdır.")
    elif islemNo=="3":
        miktar=input(f"Çekmek İstediğiniz Tutarı Giriniz: ")
        miktar=int(miktar)
        if hesap['bakiye'] >= miktar:
            hesap['bakiye'] -= miktar
            print("Paranızı Alabilirsiniz.")
            print(f"Yeni bakiyeniz {hesap['bakiye']} Türk Lirasıdır.")
        else:
            toplam = hesap['bakiye'] + hesap['ekHesap']
            if toplam >= miktar:
                print("Ek Kullanabilirsiniz.")
                ekHesapKullanimi = input("Ek Hesap Kullanılsın mı (e/h)")
                if ekHesapKullanimi == "e":
                    print(f"Yeni Bakiyeniz: 0 Türk Lirasıdır.")
                    hesap['ekHesap']-=miktar
                    print("paranızı alabilrisiniz..")
                else:
                    print(f"{hesap['hesapNo']} nolu hesabınızda {hesap['bakiye']} bulunmaktadır.")
            else:
                print("Bakiye yetersiz.")
    elif islemNo=="4":
        print(hesap)
    elif islemNo=="5":
        print("Çıkış Yapılıyor..")
    else:
        print("Geçersiz Giriş Yaptınız")





paraCek(FeritHesap,500)




