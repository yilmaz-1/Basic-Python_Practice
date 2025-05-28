import random
tahminSayısı=5
b=random.randint(1,15)
sayac=0
puan=100 # burada kullnıcıya yaptığı doğru tahmin için puan vermek amacı ile tanımlandı.
print("Toplam 5 Tahmin Hakkınız Bulunmaktadır.")
print("Toplam 100 Puanınız Bulunmaktadır.")
print("Her Yanlış Tahmin Yaptığınızda 20 Puanınız Düşecektir.")

while tahminSayısı>0: # while ile bir döngü oluşturulmuştur. fakat burda ki döngünün koşulu: tahminSayısı>0 olana kadardır. bu şart sağlandığı sürece tahmin yapmamızı isteyecek program.
    tahminSayısı -= 1 # burada tahminSayısı değişkeni her döngüde 1 azaltılarak döngü sonsuza kadar devam etmesi engellenmiştir.
    sayac+=1 # sayaç kurmamızın sebebi ise döngü kaçıncı defa da tamamlandı ve tahmin kaçıncı döngüde doğru sonuçlandı onu tespit etmek. sayaç her döngüde 1 artırılarak kaçıcı döngüde doğru tahmin edildiğini tespit etmek.
    puan1=(puan)-(20*(sayac-1)) #burada sayac-1 yazılmasının sebebi sayıyı bilidği turda ki 20 puan düşülmesini önlemektir.
    # aksi taktirde bildiği turda da puan düşer ve yanlış hesaplama yapar.
    a = int(input("1 ile 15 arasında bir sayı tahmin ediniz:")) # kullanıcıdan input ile sayı girmesi isteniyor ve bu sayı int fonksiyonu ile de veri tipi dönüşümü yapılıyor.
    if (b==a): # eğer programın random.randint() fonksiyonu ile elde ettiği sayı , kullanıcının programa girdiği sayı ile aynı ise; program çalışacak ve
        print(f"Tebrikler {sayac}. Tahminde Bildiniz. Toplam Puanınız {puan1} puandır") # print ile ekrana yazdırılacak. burada f string metodu ile sayac ve puan1 değişkenleri alınarak kullanıldı.
        break # bu kod burada sonlanıyor. çünkü doğru tahmin yapılmış oluyor ve programın tekrar tekrar çalışmasına gerek yok. yani döngü tekrar tekrar çalışmasına gerek yok.
    elif (tahminSayısı==0): # burda yeni bir if koşul durumu tanımlanıyor. eğer ki tahminSayısı değişkeni döngü sonunda 0 a eşit olursa, bu kod bloğu çalışıyor ve
        print("Tahmin Hakkınız Bitti Puanınız 0.") # ekrana print ile yazdırılıyor.
        print("Tutulan Sayı:",b) # ekrana print ile yazdırılıyor.
        break # tahmin hakkımız bittiği için program tekrara tekrar bizden sayı istmemesi için döngü tekrar tekrar çalışmaması için burada sonlandırılıyor.
    elif(b>a): # eğer if bloğunda ki kodda yazılmış olan koşul sağlanmaz ise bu kod bloğunda yer alan şart, yani programın ramdom fonksiyonu ile elde ettiği sayı (b) kullanıcının dışarıdan sisteme girdiği sayı (a) dan büyük ise şartı sağlanır ise program çalışıyor.
        print("Daha büyük sayı girniz.") # ekrana print ile bu yazdırılıyor.
    else: # eğer yukarıda yer alan kod bloklarında yer alan şartlardan hiç biri çalışmaz ise bu kod bloğu devreye giriyor ve çalışıyor.
        print("Daha küçük bir sayı giriniz.") # ekrana print ile yazdırılıyor

    # if (tahminSayısı==0): # burda yeni bir if koşul durumu tanımlanıyor. eğer ki tahminSayısı değişkeni döngü sonunda 0 a eşit olursa, bu kod bloğu çalışıyor ve
    #     print("Tahmin Hakkınız Bitti Puanınız 0.") # ekrana print ile yazdırılıyor.
    #     print("Tutulan Sayı:",b) # ekrana print ile yazdırılıyor.
    #     break # tahmin hakkımız bittiği için program tekrara tekrar bizden sayı istmemesi için döngü tekrar tekrar çalışmaması için burada sonlandırılıyor.