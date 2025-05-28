print("""
**********************
Kullanıcı Giriş Programı
**********************
""")

sys_kullanici_adi= "mehmet"
sys_parola= "123456"
giris_hakkı=3

while True:
    kullanıcı_adı=input("Kullanıcı Adınızı Giriniz:")
    parola= input("Parolanızı Giriniz:")
    if (sys_kullanici_adi==kullanıcı_adı and sys_parola==parola):
        print("Hoşgeldiniz...")
        break
    elif(sys_kullanici_adi!=kullanıcı_adı or sys_parola!=parola):
        giris_hakkı-=1
        try:
            int(parola)
        except:
            print("Geçersiz Giriş Yaptınız...")
            continue
        print("Hatalı Giriş Yaptınız...")
    if(giris_hakkı==0):
        print("Giriş Hakkınız Bitmiştir.")
        break




