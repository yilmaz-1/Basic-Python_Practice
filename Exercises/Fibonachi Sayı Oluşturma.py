print("Fibonacci Sayı Dizisi Oluşturma")

a=1
b=1
fi=[a,b]

for i in range(10):
    print("a:",a,"b:",b)
    a,b=b,a+b
    fi.append(b)
print(fi)
# çıktı:
# a: 3 b: 5
# a: 5 b: 8
# a: 8 b: 13
# a: 13 b: 21
# a: 21 b: 34
# a: 34 b: 55
# a: 55 b: 89
# [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144]
# bu program fibonachi sayısını bulmak için yazılmıştır.
# kod çalıştırıldığında yukarıdan aşağıya doğru okumaya başlıyor.
# daha sonra ilk olarak print ile programın adı ekrana basılıyor.
# daha sonra golbalde tanımlanmış olan sayıları okumaya başlıyor.
# daha sonra for döngüsü ile karşılaşıyor program ve bu döngü şu şekilde çalışıyor: for döngüsü koşulunda belirtilen şart range fonkisyonu ile tanımlanan aralıkta i değerlerini al ve devamında belirtilen eşitliği uygula.
# a yerine b ve b yerine de a+b yi ata diyor.
# daha sonra golbalde tanımlana fi boş listesinin içine append medotu ile atılıyor.
# en sonda da bu fi listesi ekrana basılıyor.