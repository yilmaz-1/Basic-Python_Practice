print(" *** Mükemmel Sayıyı Bulma Programına Hoşgeldiniz *** ")


sayı=int(input("Sayı:"))

i=1
toplam=0
while (i < sayı):
    if ( sayı %i == 0):
        print("i:",i)
        toplam+=i
        print("toplam:",toplam)
    i+=1
if (toplam==sayı):
    print("Mükemmel Sayı.")
else:
    print("Mükemmel Sayı Değildir.")

# çıktı:
# *** Mükemmel Sayıyı Bulma Programına Hoşgeldiniz ***
# Sayı:57
# i: 1
# toplam: 1
# i: 3
# toplam: 4
# i: 19
# toplam: 23
# Mükemmel Sayı Değildir.
# bu program kulanıdan aldığımız sayının mükemmel sayı olup olmadığını bulmaya yarar.
#  print ile fonksiyonun adı ekrana basılıyor. daha sonra globalde kullanıcıdan alacağımız sayı input ile kullacıdan isteniyor ve int fonksiyonu ile veri tipi dönüşümü yapılıyor.
# daha sonra while döngüsünde kullanılacak olan i sıfıra eşitlenip tanımlanıyor. program yukarıdan aşağıya doğru okumaya devam ediyor. ve toplam değişkeni sıfır ile tanımlanıyor.
#  while döngüsü i kullanıcıdan gelen sayıdan küçük olana kadar devam etmesi şeklinde tanımlanıyor. çünkü burada ki mükkemle sayı bölenlerinin toplamı kendine eşit ise o sayı mükemmel sayı olduğu için
# kullanıcın verdiği sayıyı geçemez i ve o sayıdan küçük olmak zorunda.
# if bloğu ile mükemmel sayı olma koşulu tanımlanıyor. eğer kullanıcıdan gelen sayının i ile bölümünden kalan sıfıra eşitse devamında tanımlanan toplam değişkenine ekle sonra tekrar döngü başa dönüyor ve bir sonraki sayı içinde bu şart devam ediyor bu şekilde kullanıcıdan gelen sayııya kadar tek tek bütün i değerleri sayı üzerinde deneniyor sağlaynlar toplam değişkeni üzerine atılarak toplanıyor.
# i sayısı sayıya eşit olduğu anda foksiyon duruyor ve if else bloğunda tanımlanan kod çalışmaya başlıyor. çünkü while döngüsü bitti ve toplam değeri son halini aldı.
# if else bloğunda ise while ile tamamlanan döngüde elde edilen toplam değeişkeni if bloğunda kontrol ediliyor ve toplam değişkeni kullanıcıdan aldığımız sayıya eşit ise ekrana mükemmel sayıdır ifadesi basılıyor. eğer eşit değilse
# mükemmel sayı değildir ifadesi ekrana basılıyor.

