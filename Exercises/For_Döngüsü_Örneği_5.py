for i in range(3): # burada 3 defa dönecek olan bir for döngüsü kuruldu. yani her ne olursa olsun bu döngü en fazla
    # 3 defa dönecek ve program sonlanacak.
    parola= input("Lütfen Parolanızı Girin: ") # burada kullanıcıdan bir adet praola değişkeni girmesini istiyoruz.
    if not parola: # burada eğer praola alanı boş bırakılır ise. yani girilmez ise koşulu oluşturuldu.
        print("Parola alanını boş bırakmayın...")
    elif len(parola) in range(8,16): # burada ise girilen parolanın boyunun 5 ile 26 karakter arasında olması isteniyor.
        # bu şart ise range fonksiyonu iile oluşturuldu.
        print("Parolanız:", parola)
        break # program kırılarak sonlanıp bitiyor.
    else: # eğer yukarıdaki şartlardan hiç biri sağlanmıyor
        print("parolanız 5 karakterden büyük 16 karakterden küçük olmalıdır.") # ekrana bu yazılıyor.
