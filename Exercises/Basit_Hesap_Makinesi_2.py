print("****************BASİT DÖRT İŞLEM HESAP MAKİNESİ PROGRAMI****************")

print(""""İşlem Numaraları:
1. Toplama İşlemi
2. Çıkarma İşlemi
3. Çarpma İşlemi
4. Bölme İşlemi
""""")

c=input("Yapmak istedğiniz İşlemin Numarasını Giriniz:")

a=float(input("Birinci Sayıyı Giriniz:"))
b=float(input("İkinci Sayıyı Giriniz:"))

if (c=="1"):
    print("İki Sayının Toplamı:", a+b)
elif (c=="2"):
    print("İki Sayının Farkı:", a-b)
elif (c=="3"):
    print("İki Sayının Çarpımı:", a*b)
elif (c=="4"):
    print("İki Sayının Bölümü:", a/b)
else:
    print("Geçersiz Giriş Yaptınız...")

# bu programda basit dört işlem yapan bir hesap makinesi yazılmıştır.
#  print ile programın adı ekrana bastırılıyor. daha sonra print ile işlem numaraları ekrana bastırılıyor.
#  daha sonra input komutu ile kullanıcıdan yapmasını istediği işlemin numrasını alıyoruz ve bunu c değişkenine
# atıyoruz. daha sonra kullnıcıdan gene input foksiyonu ile a ve be değlerini alıp bunları float fonksiyonu ile
# float a çeviriyoruz.daha sonra if elif else kalıbı ile tek tek c nin hangi işleme eşit olduğu durumlar değerlendirilip
# ekrana o işlem yapılıp sonuç basılıyor.