def toplama(a,b,c): # toplama isminde 3 argümanlı bir foksiyon tanımlanıyor.
    print("toplamları:",a+b+c) # argümanların toplamı ekrana bastırılıyor.
def ikiylecarp(a): # ikiylecarp tek argümanlı bir fonksiyon tanımlanıyor.
    print("2 ile çarpılmış hali:",a*2) # fonksiyon içindeki argümanın 2 ile çarpılmış hali ekrana bastırılıyor.

toplam=toplama(3,4,5) # fonksiyonlardan bağımsız olarak toplam değişkenine 3 argümanlı toplama fonksiyonu atanıyor ve çağrılıyor.
# çıktı:
# toplamları: 12

ikiylecarp(5) # ikiylecarp fonksiyonu çağrılıyor
# çıktı:
# 2 ile çarpılmış hali: 10
