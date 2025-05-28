while True:
    sayı = input("Hesapamak İstediğiniz Sayıyı Giriniz: ")
    if (sayı=="0"):
        print("Faktöriyel: 1")
    elif (sayı=="1"):
        print("Faktöriyel 1")
    else:
        faktöriyel=1
        try:
            sayı=int(sayı)
        except:
            print("geçersiz giriş...")
            continue
        for i in range(2,sayı+1):
            faktöriyel*=i
        print("Faktöriye: ",faktöriyel)
