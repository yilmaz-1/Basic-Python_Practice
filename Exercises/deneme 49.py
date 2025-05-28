def pozitifCiftTek(number): # burada pozitifCiftTek isimli bir argümanlı bir fonksiyon tanımlanıyor.
    number=int(number)# fonksiyon içindeki nuöber argümanı int fonksiyonu ile veri tipi dönüşümü yapılıyor.
    if ( number > 0 and number % 2 == 0): # bu blokta number argümanı eğer 0 dan büyük ve aynı zamanda 2 ile bölümünden kalan sıfır ise diye bir koşul oluşturuluyor. bu koşul sağlanır ise blok çalışıyor.
        print("Sayı sıfırdan büyük ve çifttir.")# ekrana print ile yazdırılıyor.
    elif ( number >0 and number % 2 !=0): # yukarıda ki if bloğu çalışmaz ise program bu bloğu okumaya başlıyor. burda number argümanı eğer hem sıfırdan büyük ve hemde 2 ile bölümünden kalan sayı sıfıra eşit değilse bu lok çalışıyor.
        print("Sayı pozitif fakat tektir.")# ekrana yazdırılıyor.
    elif ( number < 0 and number % 2 == 0): # eğer yularıda ki her iki kokd bloğu da çalışmaz ise bu blok program tarafından okunuyor. eğer number argümanı hem sıfırdan küçük hemde 2 ile bölümünden kalan sıfıra eşitse bu kod bloğu çalşıyor.
        print("Sayı negatif ve çifttir.")# ekrana yazdırılıyor.
    elif ( number < 0 and number %2 !=0): # eğer yukarıda ki kod bloklarında yer alan koşullar sağlanmaz ve kodlar çalışmaz ise program bu kod bloğunu okur. Bu kod bloğunda ise eğer number argümanı sıfırdan hem küçük hemde 2 ile bölümünden kalan sıfıra eşit değilse bu kod bloğu çalışıyor.
        print("Sayı negatif ve tektir. ") # print ile ekrana parantez içineki ifade ekrana yazdırılıyor.
    else: # eğer yukarıdaki hiç bir kod bloğu çalışmaz ise bu kod bloğu çalışır.
        print("geçerli giriş yapmadınız.")# ekrana yazdırılıyor.
    return # return ile de bu fonksiyon daha sonra tekrar tekrar farklı argümanlar için ve programın başka yerlerinde kullanılmak üzere döndürülüyor.

pozitifCiftTek(8)
# çıktı:
# Sayı sıfırdan büyük ve çifttir.
# program sonlandı.

pozitifCiftTek(-5)
# çıktı:
# Sayı negatif ve tektir.
# program sonlandı.

# *********************************************

number = int(input("Enter Number: ")) # kullanıcıdan input fonksiyonu ile sayı girmesi isteniyor. girilen sayı int fonksiyonu ile veri tipi dönüşümü yapılıyor.

if ( number > 0 and number % 2 == 0):# bu blokta number değişkeni eğer 0 dan büyük ve aynı zamanda 2 ile bölümünden kalan sıfır ise diye bir koşul oluşturuluyor. bu koşul sağlanır ise blok çalışıyor.
        print("Sayı sıfırdan büyük ve çifttir.") # ekrana print ile yazdırılıyor.
elif ( number >0 and number % 2 !=0):# yukarıda ki if bloğu çalışmaz ise program bu bloğu okumaya başlıyor. burda number değişkeni eğer hem sıfırdan büyük ve hemde 2 ile bölümünden kalan sayı sıfıra eşit değilse bu blok çalışıyor.
        print("Sayı pozitif fakat tektir.") # ekrana yazdırılıyor.
elif ( number < 0 and number % 2 == 0): # eğer yularıda ki her iki kokd bloğu da çalışmaz ise bu blok program tarafından okunuyor. eğer number değişkeni hem sıfırdan küçük hemde 2 ile bölümünden kalan sıfıra eşitse bu kod bloğu çalşıyor.
         print("Sayı negatif ve çifttir.") # ekrana yazdırılıyor.
elif ( number < 0 and number %2 !=0): # eğer yukarıda ki kod bloklarında yer alan koşullar sağlanmaz ve kodlar çalışmaz ise program bu kod bloğunu okur. Bu kod bloğunda ise eğer number değişkeni sıfırdan hem küçük hemde 2 ile bölümünden kalan sıfıra eşit değilse bu kod bloğu çalışıyor.
         print("Sayı negatif ve tektir. ") # print ile ekrana parantez içineki ifade ekrana yazdırılıyor.
else: # eğer yukarıdaki hiç bir kod bloğu çalışmaz ise bu kod bloğu çalışır.
         print("geçerli giriş yapmadınız.") # ekrana yazdırılıyor.

# çıktı:
# Enter Number: 50
# Sayı sıfırdan büyük ve çifttir.

# Enter Number: 47
# Sayı pozitif fakat tektir.

# Enter Number: -42
# Sayı negatif ve çifttir.

# ******************************************************************************************

while True: # while ile döngü oluşturuluyor. bu döngü True ifadesi ile sürekli çalışması sağlanıyor. program çıktısından da anlaşılacağ üzere program doğru çalşıtığı sürece bizden yeni sayı isteyecek. program sürekli çalışacak.
    number = int(input("Enter Number:")) # kullanıcdan input fonksiyonu ile bir sayı girmesi isteniyor. bu girilen sayı int fonksiyonu ile veri tipi dönüşmü yapılıyor.
    if (number > 0 and number % 2 == 0): # bu blokta number değişkeni eğer 0 dan büyük ve aynı zamanda 2 ile bölümünden kalan sıfır ise diye bir koşul oluşturuluyor. bu koşul sağlanır ise blok çalışıyor.
        print("Sayı sıfırdan büyük ve çifttir.") # ekrana print ile yazdırılıyor.
    elif ( number >0 and number % 2 !=0): # yukarıda ki if bloğu çalışmaz ise program bu bloğu okumaya başlıyor. burda number değişkeni eğer hem sıfırdan büyük ve hemde 2 ile bölümünden kalan sayı sıfıra eşit değilse bu blok çalışıyor.
        print("Sayı pozitif fakat tektir.") # ekrana yazdırılıyor.
    elif ( number < 0 and number % 2 == 0): # eğer yularıda ki her iki kokd bloğu da çalışmaz ise bu blok program tarafından okunuyor. eğer number değişkeni hem sıfırdan küçük hemde 2 ile bölümünden kalan sıfıra eşitse bu kod bloğu çalşıyor.
        print("Sayı negatif ve çifttir.") # ekrana yazdırılıyor.
    elif ( number < 0 and number %2 !=0): # eğer yukarıda ki kod bloklarında yer alan koşullar sağlanmaz ve kodlar çalışmaz ise program bu kod bloğunu okur. Bu kod bloğunda ise eğer number değişkeni sıfırdan hem küçük hemde 2 ile bölümünden kalan sıfıra eşit değilse bu kod bloğu çalışıyor.
        print("Sayı negatif ve tektir. ") # print ile ekrana parantez içineki ifade ekrana yazdırılıyor.
    elif ( number == 0 ): # eğer number değişkeni sıfıra eşitse,
        print("Sayı ne ngatif nede pozitiftir fakat çifttir.") # ekrana print ile parantez içinedki ifade yazdırılıyor.
    else: # yularıda ki kod bloklarında yer alan hiç bir şart sağlanmaz ise bu kod bloğu çalışır.
        print("Geçerli giriş yapmadınız.") # ekrana yazdırır.


# çıktı:
# Enter Number:50
# Sayı sıfırdan büyük ve çifttir.
# Enter Number:48
# Sayı sıfırdan büyük ve çifttir.
# Enter Number:-45
# Sayı negatif ve tektir.
# Enter Number:-42
# Sayı negatif ve çifttir.
# Enter Number:0
# Sayı ne ngatif nede pozitiftir fakat çifttir.
# Enter Number:

# *******************************************************************************

def pozitifCiftTek(number):
    if ( number > 0 and number % 2 == 0):
        print("Sayı sıfırdan büyük ve çifttir.")
    elif ( number >0 and number % 2 !=0):
         print("Sayı pozitif fakat tektir.")
    elif ( number < 0 and number % 2 == 0):
         print("Sayı negatif ve çifttir.")
    elif ( number < 0 and number %2 !=0):
        print("Sayı negatif ve tektir. ")
    else:
         print("geçerli giriş yapmadınız.")
    return


while True:
    number=input("Enter Number:")
    if (number == "q"):
        print("sistemeden çıkış yapıldı.")
        break
    else:
        number=int(number)
        print(pozitifCiftTek(number))
