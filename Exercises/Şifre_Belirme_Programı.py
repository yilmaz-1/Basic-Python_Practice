print("""
Şifre Belirleme Kuralları
1. En az 6 karakter olmalıdır.
2. En az bir büyük harf içermelidir.
3. En az bir küçük harf içermelidir.
4. En az bir tam sayı içermelidir.
5. En az bir karakter içermelidir(?*/'!). 

""")

# yukarıda, program ilk açıldığında kullanıcının görmesini istediğimiz bilgi mesajını girdik.


buyuk = "ABCDEFGHIJKLMNOPRSTVYZWXQ" # şifre için kullanacağımız büyük harf listesi yer almaktadır.
kucuk = "abcdefghijklmnoprstvyzwxq" # şifre için kullanacağımız küçük harf listesi yer almaktadır.
digit = "0123456789" # şifre için kullanacağımız tam sayıların listesi yer almaktadır.

bhsayi = 0
khsayi = 0
dsayi = 0
# yukarıdaki 3 değişkeni ise döngüde kullanmak için tanımladık.



while True:
    sifreY = input("Yeni Şifrenizi Giriniz : ")  # kullanıcıdan bir şifre girmesini istedik.
    sifreT = input("Yeni Şifrenizi Tekrar Giriniz: ")  # girdiği şifreyi tekrar girmesini istedik
    onay = input("Onaylıyor musununz y/n: ")  # onaylamasının istedik.
    if onay == "y":
        if sifreY == sifreT:
            for i in sifreT:
                if i in buyuk:
                    bhsayi += 1
                if i in kucuk:
                    khsayi += 1
                if i in digit:
                    dsayi += 1
        elif sifreY != sifreT:
            print("Şiferniz farklı girdiğiniz. ")
            continue
        else:
            if (bhsayi == 0) or (khsayi == 0) or (dsayi == 0):
                print("Zayıf şifre Girdiniz. Şifenizi yeniden belirleyiniz.")
            else:
                print("Güvenli Şifre.")
            break
    else:
        print("Şifre Onaylanmadı. Programdan çıkış yapılıyor.")
    break








