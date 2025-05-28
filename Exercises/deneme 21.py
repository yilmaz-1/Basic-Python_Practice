print("1 den 100 kadar olan sayılardan 3 e bölünenlarin ekrana bastırılması") # burada fonksiyonun adı ekrana bastırılıyor.
for i in range(1,101): # for döngüsü kullanılarak range fonksiyonu ile 1 den 101 e kadar olan sayılar 1 dahil 101 hariç bir elemanlar dizisi oluşturuluyor.
    if (i % 3 == 0): # for döngüsü altında if bloğunda ise bu döngü ile elde edilen sayılardan eğer 3 ile tam bölünen var ise
        print(i) # bunları ekrana bastırılyor.
# çıktı:
# 1 den 100 kadar olan sayılardan 3 e bölünenlarin ekrana bastırılması
# 3
# 6
# 9
# 12
# 15
# 18
# 21
# 24
# 27
# 30
# 33
# 36
# 39
# 42
# 45
# 48
# 51
# 54
# 57
# 60
# 63
# 66
# 69
# 72
# 75
# 78
# 81
# 84
# 87
# 90
# 93
# 96
# 99