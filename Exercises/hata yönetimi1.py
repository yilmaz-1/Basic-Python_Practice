# try:  # burada hataya sebep olabilecek kodlar try bloğu altına alınarak hata kontrol edilmiştir.
#     x = int(input("x: "))
#     y = int(input("y: "))
#     print(x / y)
# except ZeroDivisionError:  # burada ise bu kod dan oluşuacak hata türüne yer veriyoruz. burada sıfıra bölünme hatası
#     # oluştuğu için ZerodivisionError hatası yazıldı.
#     print("y için 0 girilemez...") # burada normalde python nın göstermesi gereken hatayı gösterme bizim istediğimiz
#     hata mesajını göster dedik.
# except ValueError:  # burada ki hata türü ise kullanıcıdan integer yani tam sayı istememize rağmen sayı girmediği
#     # durumları yakalamak için kullanılan hata türüdür.
#     print("x ve y için sayısal bir ifade giriniz...")

# yukarıda except ile, gelebilecek veya oluşabilecek haataları tek tek sınırsız bir şekilde aşağıya dığru sıralayarak
# yazabilriiz. fakat bunun yerine tek except komutu ve virgül kullanrak yan yana da yazabiliriz.

# try:
#     x = int(input("x: "))
#     y = int(input("y: "))
#     print(x / y)
# except (ZeroDivisionError,ValueError) : # burada birden fazla hata gelebileceğini tahmin ederek o hataları tek kod
#     # bloğunda yazarak yakalamaya çalıştık.
#     print("Yanlış bilgi girdiniz...")

# try:
#     x = int(input("x: "))
#     y = int(input("y: "))
#     print(x / y)
# except (ZeroDivisionError,ValueError) as e: # burada birden fazla hata gelebileceğini tahmin ederek o hataları tek kod
#     # bloğunda yazarak yakalamaya çalıştık fakat bu hataları e nesnesi olarak tanımladık. yani hata verdiğinde
#     # bu hata hangi hatadandan kaynakladığını e  nesnesi üzerinden bize gösterecek.
#     print("Yanlış bilgi girdiniz...")
#     print(e) # burada bu e hata nesnesini ekrana yazdırdık.



# try:
#     x = int(input("x: "))
#     y = int(input("y: "))
#     print(x / y)
# except: # burada hata türünün ne olduğuna bakılmaksızın hata yakalanıp ekrana sadece print içerisinde yer alan
#     # bilgi yazdırılıyor. genel olarak hata var ama bu hat ne belli değil.
#     print("Yanlış bilgi girdiniz...")

# while True: # burada bir adet döngü oluşturuldu. amaç döngü sağlandığı sürece yani doğru olduğu sürece çalışsın demek.
#     try:
#         x = int(input("x: "))
#         y = int(input("y: "))
#         print(x / y)
#     except (ZeroDivisionError,ValueError) : # burada birden fazla hata gelebileceğini tahmin ederek o hataları tek kod
#         # bloğunda yazarak yakalamaya çalıştık.
#         print("Yanlış bilgi girdiniz...")
#     else: # burada ise except bloğu çalışmaz ise yani hata yakalamaz ise döngüden çıkılsın.
#         # yani tekrar tekrar kullanıcıdan x ve y değeri istenmesin. Eğer except çalışır ise else bloğuna gelinmeyecek
#         # ve döngü başa dönüp tekrar x ve y değeri istenecek. çünkü kullanıcı hatalı veri girişi yapmış olacak
#         # bundan dolayı en başa dönecek
#         print("her şey yolunda...")
#         break # else bloğu çalışır ise döngü kırılacak ve kullanıcıdan tekrar tekrar x ve y değeri istenmesi
#         # durdurulacaktır.çünkü kullıcının girdiği x ve y değeri hatalı olmadığı için except bloğu hata yakalamayacaktır

while True:
    try:
        x = int(input("x: "))
        y = int(input("y: "))
        print(x / y)
    except Exception as ex: # burada exception class kullaıralarak hata mesajları loglandı. Burada olabilecek bütün
        # hatalar exception class ı altından alınacak bu class altından alınacak olan hatalar da ex olarak tanımlandı.
        # Yani burada bir hata nesnesi oluşturulmuş oldu exception class ı altında. biz hangi hatayı yakalarsak,
        # python bu hatayı exception class ı altından alacak ve ex nesnesi olarak ekrana yazdıracak.
        print("Yanlış bilgi girdiniz...", ex) # burada da bu hata nesnesi ekrana yazdırıldı.
    else:
        print("her şey yolunda...")
        break
    finally: # bu blok her zaman çalıştırıldı. yani yukarıdaki hangi blok çalıştırılırsa çalıştırılsın bu blok her
        # zaman çalıştırılır.
        print("try except sonlandırıldı...")


















