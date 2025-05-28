# aşağıdaki fonskiyonda ve devamındaki kodda sayının tek mi çift mi olduğunu tespit eden bir yapı yer almaktadır.

cift = [] # burada bir boş liste tanımlandı.
tek = [] # burada bir boş liste tanımlandı.
# yukarıda ki boş liste tanımlanmasının amacı tespit ettiğimiz sayıları ayrı ayrı listelere yollamak. tek olanları tek
# listesine çift olanları ift listesine yollamak.

def tekcift(): # burada argümansız bir tekcift isminde bir fonskiyon tanımlandı.
    if number % 2 == 0: # eğer number isimli değişkenin iki ile bölümünden kalanın sıfır ise
        cift.append(number)# bu number değişkenini cift isimli boş liste olarak tanımanmış listeye append ile yolla.
    else: # eğer bu number isimli değişkenin 2 ile bölümünden kalan sıfır değilse, yani çift değilse
        tek.append(number) # bu number isimli değişkeni append ile tek isimli boş listeye yolla.
    if number == 0: # burada bir if koşulu oluşturuldu. amacımız ise eğer kullanıcı sıfır girerse programdan çıkmasını,
        # programın sonlanmasını sağlamak. Ayrıca, sıfır ne tek ne çift olduğu için sıfır girilme durumunu da ortadan
        # kaldırmış oluyoruz.
        print("Sıfır Ne Tek Ne Çift Bir Sayıdır.") # ekrana yazdırıldı.
        print("Program Sonlandırıldı.") # ekrana yazdırıldı.
        quit() # program sonladırıldı.
    print(f" Girdiğiniz Sayılardan Çift Olanların Listesi {cift}," # çift olanların lisetesi
          f"Girdiğiniz Sayılardan Tek Olanların Listesi {tek}") # tek olanların listesi bir print ile ekrana basıldı.

while True: # yukarıda fonskiyon tanımlandı. şimdi ise bu fonskiyonu çalıştırılack döngü tanımlanacak. Eğer döngü doğru
    # bir şekilde tanımlandığı sürece devam edecek. Yani dönecek.
    try: # burada ise sıkıntı yapabilecek kodlar bu bloğun içersine alınıyor. yani burada hatayı yakalıyoruz.
        number = int(input("Please Enter Number: ")) # burası bize value error hatası çıkarabilir. biz kullanıcıdan
        # rakam istediğimizde kullanıcı bize rakam yerine harf veya başka karakter girerse hata ValueError hatası verir.
        tekcift() # yukarıda tanımladığımız program da aynı şekilde ValueError hatası verebilir. kullınıcnın girdiği
        # değişken rakam yerine harf olduğunda hata verecektir.
    except ValueError: # try bloğunda hatayı yakaladık. burada ise o hatayı pythonda gömülü msj yerine kendi mesajımızı
        # yazdırmak istiyoruz.
        print("Lütfen Rakam Giriniz (1,2,3,4,5)") # ve bizim yazdırmak istediğimiz mesaj ise bu.