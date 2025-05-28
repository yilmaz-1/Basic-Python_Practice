def mükemmelsayı(sayı): # mükemmlsayı isminde ve bir argümana sahip bir fonksiyon tanımlanıyor.
    toplam=0 # değişken tanımlanıyor.
    for i in range(1,sayı):# for döngüsü kullanılarak range fonksiyonu ile, mükemmelsayı fonksiyonu içine gönderdiğimiz argümanı olan sayıya kadar bir liste oluşuturuluyor ve for döngüsü ile de bu liste üzerinde gezinerek i değerleri elde ediliyor
        if (sayı %i ==0): # elde edilen bu i değerleri if bloğu içinde yer alan koşulda kontrol ediliyor. eğer mükkemmelsayı fonksiyonu içine gönderdiğimiz argüman olan sayıyı i değerleri tam bölyorsa kalansız olarak
            toplam+=i # toplam değişkenine atılarak toplanıyor
    return toplam==sayı # return ile, toplam değişkeninin mükemmelsayı değişkeninin argümanı olan sayı ya eşit olması durumunda bize True, değilse de False dönderiyor.

print(mükemmelsayı(6)) # fonksiyon True dönderdi bize
# çıktı:
# Ture

print(mükemmelsayı(10)) # fonksiyon False dönderdi bize.
# çıktı:
# False
