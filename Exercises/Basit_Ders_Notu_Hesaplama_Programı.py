print("""
****************************
DERS NOTU HESAPLAMA PROGRAMI
****************************
""")

v1 = float(input("Birinci Vize Notunu Giriniz: "))
v2 = float(input("İkinci Vize Notunu Giriniz: "))
f = float(input("Final Notunun Giriniz: "))

g = (v1*0.3)+(v2*0.3)+(f*0.4)

if (g >= 90):
    print("AA")
    print("Geçme Notunuz: ", g)
elif ( 85<= g < 90 ):
    print("BA")
    print("Geçme Notunuz: ", g)
elif ( 80 <= g < 85):
    print("BB")
    print("Geçme Notunuz: ", g)
elif (75 <= g < 80):
    print("CB")
    print("Geçme Notunuz: ", g)
elif (70 <= g < 75):
    print("CC")
    print("Geçme Notunuz: ", g)
elif (65 <= g < 70):
    print("DC")
    print("Geçme Notunuz: ", g)
elif (55 <= g < 60):
    print("FD")
    print("Geçme Notunuz: ", g)
elif (g < 55):
    print("FF")
    print(f"Geçemediniz. Notunuz: {g}")
else:
    print("Geçersiz Giriş Yaptınız")


# bu program da ders notu hesaplama işlemi yapan bir program yazılmıştır.
# daha sonra float tipinde v1 v2 ve f değişkenlerine atanmak üzere vize1 vize2 ve final notları kullanıcıdan input
# fonksiyonu ile alınıyor.
# daha sonra g değişkeni v1 v2 ve f notlarından oluşan işlem ile tanımlanıyor.
# daha sonra if elif ve else kalıbı ile tek tek hesaplanan hotun hangi aralıkta olduğunu kontrol ediliyor.
# o uygun aralıkta ise print fonksiyonu ile notuna karşılık gelen harf ve geçme notu ekrana bastırılıyor.
# en sonda else bloğun da ise print fonksiyonu ile ekrana geçersiz işlem girildi ise o bastırılıyor.