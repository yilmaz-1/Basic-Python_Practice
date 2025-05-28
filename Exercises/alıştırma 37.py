# basit ibr iskambil kart oyunu kart tahmini oyunu
import random # burada programa random modülü eklenmiştir. çünkü rastgele seçim yapıp birleştireceğiz.

simgeler= ("karo","kupa", "maca", "sinek") # simgeler isminde bir adet tuple değişkeni tanımlandı. burada demet olarak
# tanımlanmasının sebebi ise, değitirilmesinin istemediğimiz için.

yuzler= ("2","3","4","5","6","7","8","9","10","joker","kız","papaz","as") # aynı şekilde bunun da değiştirilmesini
# istemiyoruz.

simgeniz= random.choice(simgeler) # burada simgeler demetinden rastgele bir seçim yapması için random modlünün choice
# medodu kullanıldı.

yuzunuz= random.choice(yuzler) # aynı şekilde yüzler demetinden rastgele bir seçim yapılıyor.

sanslıKart= simgeniz + " " + yuzunuz # bu rastgele seçimler burada birleştirilip sanslıKArt değişkenine atanıyor.

print(f"Şanslı Kartınız {sanslıKart}") # ekrana sanslıKart numarasının son hali ekrana bastırılıyor.


