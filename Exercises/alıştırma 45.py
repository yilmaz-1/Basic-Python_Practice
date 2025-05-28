import turtle # import modülü programa dahil edildi.

def hallkaCiz(x,y,renk): # 3 parametreli halkaCiz isminde bir fonksiyon tanımlandı.
    turtle.pensize(8) # burada çizim yapacak kalemin boyutu yani çizgini kalınlığı belirlendi.
    turtle.pencolor(renk)# çizginin rengi belirlendi. fakat çizgi rengi ise fonsksiyon içerisine yollana renk
    # parametresi ile belirlendi.
    turtle.penup()# burada kalemi kaldır. yani bir şey çizme. çünkü çizdireceğimiz halkanın merkezine yollayacağız
    # kalemi bir sonaki kodda . oraya kalem çizerek gitmemesi lazım. bundan dolayı kalemi kaldır dedik.
    turtle.goto(x,y) # goto fonskiyonu kullanılarak halkanın merkezi olacak x ve y koordinatına git dedik.
    turtle.pendown() # bu x ve y koordinatına gelen kalem hala hava da. çizim yapabilmesi için kalemin yere inmesi lazım.
    # bu kod ile pendown ile kalem yere indirildi.
    turtle.circle(100) # bu x ve ye koodinatında yerde duran kaleme circle fonskiyonu ile 125 yarı çapında
    # bir daire çiz denildi.

wn=turtle.Screen() # burada yukarıda tanımlanan halkaCiz fonskiyonun çalışacağı ve gösterileceği bir grafik penceresi aç
"""

kororinat_x=int(input(" Halkanın x Koordinatını Giriniz: "))
kororinat_y=int(input("Halkanın Y Koordinatını Giriniz: "))
halkaRengi=input("Halkanın Rengini Giriniz: ")

eğer bu 3 tırnak arasında yer alan değişkenleri x  y ve renk parametresine yollyıp programı bu şekilde çağırırsak, 
kullaınıcı her halka için ayrı ayrı ayrı istediği gibi halka çizdirebilir.

"""
# fakat biz aşağıda ki gibi önceden parametreleri girerek çağıracağız programı . zaten amacımız olimpiyat halkası
# çidirmek olduğu için halkaların konumu ve rengi belli olduğu için her defasında bu kullanıcıdan veri alınmasına
# gerek yok.


hallkaCiz(x=-200,y=50,renk="blue") # 3 parametresi de verilen fonksiyon çağrılıyor.
hallkaCiz(x=-50, y=50, renk="black")
hallkaCiz(x=100, y=50,renk="red")
hallkaCiz(x=-125,y=-25, renk="yellow")
hallkaCiz(x=25, y=-25, renk="green")

wn.mainloop() # fonksiyonun çalıştığı ve gösterildiği pencereyi kullanıcı kapatmadan otomatik kapatılmasın.