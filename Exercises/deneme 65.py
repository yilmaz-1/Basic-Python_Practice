i = 0
toplam=0
while i<100:
    i+=1
    if (i % 2 ==0):# bu satırda tek sayıları toplamı yapılsın dedik.
        continue
    else:
        toplam+=i
print(toplam)

# çıktı:
# 2500


#açıklama: öncelikle globalde i ve toplam değişkelerini 0 olarak tanımladık. çünkü
# bu değişkenler sürekli döngü içerisinde kullanılıp yeni yeni değerler alacakları için
# sonucu doğru çıkması için sıfırdan başlatıldı.
# i değeri 100 den küçük olana kadar devam edecek (i<100 ifadesinde)
#  i ilk olarak sıfır değerini aldı sonra 1 artırılarak bir sonraki if bloğuna geçerek
#  bu i değeri if bloğunda tanımlana şart ile sorgulandı. yani i nin 2 ile bölümünden kalan
# sıfır ise bir sonraki şart olan contionue ifadesine geliniyor. eğer ki i nin
# sıfır ile bölümünden kalan sıfır oluyorsa continue ifadesi şunu yapıyor: bu döngüyü orada bitir
# hiç devam ettirme yani o if bloğu içinde tanımlanan bütün kodları çalıştırma atla ve başa dön
# eğer i nin 2 ile bölümünden kalan sıfır değilse ki if bloğunda bu şart sorgulandığında bu durum ortaya çıkar
# program devam edip continue ifadesi hiç çalışmaz ve devamında ki else bloğun da yer alan codlar çalışır.
# ve toplam her seferinde i kadar artırılıp döngü başa döner. i 100 den büyük olduğu anda döngü biter ve
# print ile ekrana toplam sonuç basılır.

i = 0
toplam=0
while i<100:
    i+=1
    if (i % 2 ==0):# bu satırda tek sayıları toplamı yapılsın dedik.
        continue
    toplam+=i
print(toplam)

# çıktı:
# 2500