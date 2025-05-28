days = int(input("Aracınız kaç gündür trafikte:")) # days isminde değişkene atılmak üzere kullanıcıdan input fonksiyonu ile gün bilgisi alınıyor ve int fonksiyonu ile de veri tipi dönüşümü yapılıyor.

if ( 0 <= days <= 365): # koşul kod blokları oluşturuluyor.
    print("1.servis aralığındasınız.")
elif ( 365 < days <= 365*2):
    print("2.servis aralığındasınız. ")
elif ( 365*2 < days < 365*3 ):
    print("3. servis aralığındasınız.")
else:
    print("hatalı süre girildi")

# çıktı:
# Aracınız kaç gündür trafikte:56
# 1.servis aralığındasınız.