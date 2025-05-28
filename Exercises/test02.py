print("""
**************************
ERŞAN BANKA HOŞ GELDİNİZ
**************************
""")

print("""

""")

mevcut_bakiye=2000

sys_kullanici_adi="mehmet"
sys_parola="12345"
giris_hakki=3

while True:
    kullanici_adi=input("Kullanıcı Adınızı Giriniz: ")
    parola=input("Şifrenizi Giriniz: ")
    if(sys_kullanici_adi==kullanici_adi and sys_parola==parola):
        print("""
    Hoş Geldiniz...
**************************
İŞLEM MENÜSÜ
1. BAKİYE SORGULAMA
2. PARA YATIRMA
3. PARA ÇEKME
4. İŞLEM İPTALİ
**************************
        """)
        islem= input("Yapmak İstediğiniz İşlem Numarasını Giriniz: ")
        if (islem=="1"):
            print("Bakiyeniz:",mevcut_bakiye)
            sorgu= input("Farklı Bir İşlem Yapmak İstiyor musunuz (e/h): ")
            if(sorgu=="e"):
                print("""
                    Hoş Geldiniz...
                **************************
                İŞLEM MENÜSÜ
                1. BAKİYE SORGULAMA
                2. PARA YATIRMA
                3. PARA ÇEKME
                4. İŞLEM İPTALİ
                **************************
                        """)
                islem2 = input("Yapmak İstediğiniz İşlem Numarasını Giriniz: ")

            else:
                print("Çıkış Yapılıyor...")
                break


        elif(islem=="2"):
            yatacak_tutar=input("Yatırmak İstediğiniz Tutarı Giriniz: ")
            mevcut_bakiye+=yatacak_tutar
            print("Bakiyeniz:",mevcut_bakiye)

        elif(islem==3):
            cekilecek_tutar=input("Çekilecek Tutarı Giriniz: ")
            mevcut_bakiye-=cekilecek_tutar
            print("Bakiyeniz:",mevcut_bakiye)

        elif(islem==4):
            print("İşleminiz İptal Edilmiştir...")
            break














