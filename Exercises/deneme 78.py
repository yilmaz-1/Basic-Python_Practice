# numbers = [1,3,5,9,10,4] # burada elemanları üzerinde işlem yapmak üzere bir liste tanımlandı.
#
# def check_even(num): # burada fonksiyon tanımlandı.
#     return num % 2 == 0 # tanımlanan fonksiyonun ne işlem yapacağı tanımlandı. num değişkeni nin 2 ile bölümünden kalan sıfır ise bize True değeri gönderecek.
#
# result = list(filter(check_even,numbers)) # burada filter fonksiyonu kullanılarak, numbers listesi üzerinde check_even foknsiyonu kullanılıp buradan elde edilen sunçlar list metodu ile result listesine atılıoyr. numbers değerlieri check_even fonksiyonu ile kontrol ediliyor. eğer 2 ile bölümünden kalan sıfır olan eleman varsa bu elemanlar liste yapılıp result üzerine atılıyor.
# #result = list(filter(lambda num: num % 2, numbers)) # bu yukarıda yazılan result ile aynı işlevi yapmaktadır.
# print(result)# ekrana basılıyor.
# # çıktı:
# # [10, 4]

#  filter () fonksiyonu bize şu işlemleri yapmamaızı sağlar: mevcut liste elemanları üzerinde her elemana değilde istediğimiz elemana  fonksiyon işlem uygulamamızı sağlar. map bütün lemenalara işlem uygularken filter ise bizim filitre ettiğimiz istediğimiz elemanlara işlem yapar.
