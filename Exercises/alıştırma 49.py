import turtle # programa turtle modülü dahil edildi.

def ekran(x,y):# burada ekran isminde 2 argümanlı bir fonksiyon tanımlandı.
    turtle.penup() # kalemi kaldır komutu verildi. amacımız gidieceğimiz x,y noktasına çizmeden gitmesini sağlamak.
    turtle.goto(x, y) # x,y noktasına git.
    turtle.pendown()# kalemi indir. çünkü bu noktada bir şeyler yazdırıp çizdirmek istiyoruz.
    turtle.write("MEHMET")# geldiğimiz bu x,,y noktasına write komutu ile mehmet yaz.

wn = turtle.Screen() # yukarıda tanımlanan fonskiyonun çalışabileceği gösterileceği bir pencere aç dedik.

turtle.onscreenclick(ekran) # turtle modülünü kullanarak onscreenclik fonskiyonunu yukarıda tanımlanan ekran isimli
# fonksiyonu çağırdık. ekran isimli fonskiyon 2 argümanlı olmasına rağmen biz argüman vermeden çağırdık ve hata vermedi.
# sebebi: zaten onsecreenclick fonskiyonu ile ekrana tıkaldığımız zaman bize x ve y şeklinde iki nokta bilgisi vereceği
# için o bilgiyi de otomatik olarak goto fonksiyonuna yollayacağı için argüman girmemize gerek yok.

wn.mainloop() # fonksiyonun gösterildiği pencereyi kapat.
