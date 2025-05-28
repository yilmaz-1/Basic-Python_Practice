# ortalama hesaplama programı

ortalama = 0 # ortalama isimli değişken tanımlanıyor.

def nothesaplama(vize1,vize2,final): # nothesaplama isimli 3 argümana sahip bir fonksiyon tanımlanıyor.
    if (ortalama >= 50 ): # if ve elif bloğundan oluşan bir koşul durumu tanımlanıyor. bu if bloğunda yer alan ortalama değişkeni eğer 50 ye eşit veya 50 den yüksek olması durumunda
        print("geçti") # ekrana basılıyor.
        if (final <50): # bu if bloğunda ise, yukarıda ki if bloğu çalıştığı zaman çalışıyor ve finalin 50 den küçük olma durumu kontrol ediliyor. final eğer 50 den küçük ise
            print("kaldı") # ekrana yazdırılıyor.
    elif (ortalama > 70):#  eğer  ilk if bloğu çalışmaz ise koşul sağlanmaz ise bu elif bloğu na geliyor program ve buradaki şart kontrol ediliyor. eğer ortalama değişkeni 70 den büyük ise
        print("geçti") # ekrana yazdırılıyor.
    return # fonksiyon daha sonra çağrılmak üzere return ifadesi ile tutuluyor.

while True: # while ile döngü oluşturuluyor. Ture ifadesi ile de döngü doğru olduğu sürece devam etmesi çalışması isteniyor. yani döngü program
    vize1= float("vize1:")
    vize2= float("vize2:")
    final = float("final:")
    if (final<50):