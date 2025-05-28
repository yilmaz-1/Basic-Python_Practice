
a = int("324234dsadsad") # burada bir adet integere fonksiyonu ile bir tam sayı oluşturuldu.
try: # burada try bloğu altında, hataya girebilecek kod bloğunu yazdık.

    a = int("324234dsadsad")  # Burası ValueError hatası veriyor.
    print("Program burada")
except:  # Hatayı belirtmezsek bütün hatalar bu kısma giriyor.
    print("Hata oluştu")  # Burası çalışır.

print("Bloklar sona erdi")