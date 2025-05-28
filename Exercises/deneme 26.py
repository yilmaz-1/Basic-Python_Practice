def faktoriyel(sayı): # faktöriyel isminde bir fonksiyon tanımlanıyor.
    faktoriyel=1 # faktöriyel değişkeni 1 den başlayacak şekilde tanımlanıyor.
    if(sayı==0 or sayı==1): # koşul bloğu oluşturuluyor. burada eğer faktöriyel fonksiyonu içinde verilen sayı 0 veya 1 ise
        print("Faktöriyel:",faktoriyel) # ekrana fonksiyon altında tanımladığımız ve 1 eşit olan faktöriyel değişkeni yazdırılıyor.
    else: # değilse
        while(sayı>1): # burada while ile şartlı döngüye başlıyor. faktöriyel fonksiyonu içine gönderilen sayı 1 den büyük olana kadar döngü devam etmesi koşulu kuruluyor.
            faktoriyel *= sayı # şartın sağlandığı her döngüde faktöriyel değişkeni foknsiyon içine verilen sayı ile çarpılıyor.
            sayı -= 1 # fonksiyon içine gönderilen sayı her döngüde 1 azaltılıyor. burada ki amaç şu her döngüde sayı 1 azaltırlarak 1 ulaşmak.
        print("Faktöriyel:",faktoriyel) # fakötriyel değişkenin son hali ekrana bastırılıyor.


faktoriyel(5)
faktoriyel(0)
faktoriyel(1)
faktoriyel(6)
# çıktı
# Faktöriyel: 120
# Faktöriyel: 1
# Faktöriyel: 1
# Faktöriyel: 720
