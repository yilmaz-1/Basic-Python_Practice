numbers= 0 # burada numbers isminde bir tane değişken tanımlandı bu değişken sıfır olarak atanda. sebebi ise bu değişken
# while döngüsüne sokulacağı için ve bu döngüde toplam hesaplatılacağı bu şekilde atandı.
i=0 # burad i değişkeni tanımladnı ve sıfır olarak kabul edildi. sebebi ise döngünün baştan başlaması için ve hatalı
# bir söngü sayısı oluşmaması için.
x=1 # burada x isminde bir değişken tanımlandı. bu değişken bize kullanıcıdan kaçınıcı sayıyı aldığımızı belirlemek
# için kullanacağımız bir değişken. bu değişken özellikle 1 e eşitlendi . sebebi ise sırıncı sayı  gibi anlamsız bir
# tanımlama olmamamsı için 1 den başlatıldı.
while i < 11: # burada bir while döngüsü kuruldu ve i değeri 11 den küçük olduğu süre boyunca çalışması istendi.
    numbers +=int(input(f"{x}. Sayıyı Giriniz: ")) # burda input komutu ile kullanıcıdan alınan sayılar int fonksiyonu
    # ile veri tipi ddönüşümü yapılarak her döngüde numbers değişkenine atanarak toplandı.
    print("Toplam: ", numbers)
    x+=1 # x değişkeni her döngüde 1 artırıldı. sebebi de döngüsde istediğimiz kullanıcı giriş sayısını düzgün
    # bir şekilde elde etmektir.
    i+=1 # burada ise i değeri her döngüde bir artırılarak döngünün sağlıklı bir şekilde çalıştırılması ve sonlanması
    # sağlanmıştır.
print("Ortalama: ", numbers/i) # her döngüde kullanıcıdan elde edilen sayıların toplamı en son girilen sayının
# numaraısna bölünerek ortalama değeri print fonksiyonu ekrana yazddırıldı.

# çıktı
# 1. Sayıyı Giriniz: 1
# 2. Sayıyı Giriniz: 2
# 3. Sayıyı Giriniz: 3
# 4. Sayıyı Giriniz: 4
# 5. Sayıyı Giriniz: 5
# 6. Sayıyı Giriniz: 6
# 7. Sayıyı Giriniz: 7
# 8. Sayıyı Giriniz: 8
# 9. Sayıyı Giriniz: 9
# 10. Sayıyı Giriniz: 10
# 11. Sayıyı Giriniz: 11
# Ortalama:  6.0