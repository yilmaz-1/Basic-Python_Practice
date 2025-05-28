pdiller=["C","Java","Python","Kotlin"] # burada pdiller isminde liste veri tipinde bir değişken tanımladık.
index =0 # index isminde bir değişken tanımladık ve sıfır olarak belirledik. sıfır olmasının sebebi bu index while
# döngüsüne girecek orada hatalı sonuç almamak için sıfırdan başlatıldı. listeler de index ler sıfırdan başladığı için
newlist=[] # burada newlist isminde bir değişken tanımldık ve bunu boş liste olarak atadık.
while (index<len(pdiller)): # burada bir while döngüsü kurduk. bu döngüde,index değişkeni pdiller listeisnin boyundan
    # küçük olduğu sürece devamlı çalışmasını istedik.
    newlist.append((index, pdiller[index])) # yularıda belirlediğimiz boş newlist isimli listeye append fonskiyonunu
    # kullanarak her döngüde elde ettiğimiz index bilgisini ve o index bilgisinde yer alan elemanı newlist isimli boş
    # listeye gönderdik.
    index +=1 # burada index değişkenini her döngü sonunda 1 artırdık. sebebi de şu: eğer biz bu döngünün sonsuza kadar
    # gitmesini istemiyorsak ve while bloğundaki koşulun sağlıklı bir şekilde çalışmasını istiyorsak bu yapılmalı.
print(newlist) # döngü bittikten sonra elde edilen newlist isimli yeni liste ekrana yazsırılıyor.

# çıktı
#[(0, 'C'), (1, 'Java'), (2, 'Python'), (3, 'Kotlin')]



print(*enumerate(pdiller)) # yukarıda yaptığımız işi enumerate fonksiyonu ile rahat rahat yapabiliyoruz.
#çıktı
#(0, 'C') (1, 'Java') (2, 'Python') (3, 'Kotlin')

print(list(enumerate(pdiller))) # while döngüsü ile yaptığımız işlemi sadece enumerate fonskiyonu ile tek satırda
# yapabiliyoruz.
# çıktı
#[(0, 'C'), (1, 'Java'), (2, 'Python'), (3, 'Kotlin')]


print(list(enumerate(pdiller,0))) # burada enumerate fonskiyonuna 2 adet argüman yolladık. bu argümanlardan birincisi
# (pdiller) iterable olan yani yenilebilir olanı pdiller listesinden aldık. ikinci argümanı ise yani start (başlama)
# noktasını ise kendimiz yazsık belirledik. bu start noktası sıfırdan da balşayabilir. sıfır yazsonra da pdiller
# listesinin ilk elemanın al demek.
# çıktı
#[(0, 'C'), (1, 'Java'), (2, 'Python'), (3, 'Kotlin')]
