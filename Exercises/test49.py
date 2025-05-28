
from math import * # burada math modülü programıza import komutu ile ekledik. sonua yıldız işareti koymamızdaki amaç
# şu: math modülündeki bütün fonksiyonları eklemek istediğimizi söyelmiş oluyoruz. from modül_adi import şeklinde
# yazmamızın sebebi ise daha sonra ki yazımlarda sürekli math ifadesini kullanacağımız fonksiyonun önünde kullanmamak
def factorial(sayi): # burada factorial isminde bir argümanlı bir fonksiyon tanımlandı.
    print("Kendi Faktöriyel Fonksiyonum")
    faktöriyel=1
    if (sayi==1 or sayi==0):
        return 1
    while (sayi>=1):
        faktöriyel*=sayi
        sayi-=1
    return faktöriyel

print(factorial(5))

