"""
Aşağıda ki program, klavyedeki yön tuşlarını kullanarak hareket ettirdiğimiz ve rasgele konumlarad ortaya çıkan bir kare
kare yakalama programı tanımlanmıştır.

"""



import turtle # burada programa turtle modülü dahil edildi.
import random # burada programa random modülü dahil edildi.

turtle.setup(400,400) # burada oyun alanının sınırları belirlendi. yani oyun alanımız 400 eni 400 de boyu olan bir alan
# olarak ifade edildi.

okSimgesi= turtle.Turtle() # burada hareket ettireceğimiz ok simgesi nesne olarak Turtle() fonksiyonu kullanarak
# oluşturulmuştur. oluşturuduğumuz bu nesne okSimgesi değişkenine atanmıştır.
okSimgesi.penup()# ok simgesi kaldırılmıştır. amacımız arkasında çizgi bırakmasın. gideceği yere giderken iz bırakmadan
# hareket etsin.

hedefKare= turtle.Turtle() # hedef kare isminde bir değişken tanımlandı. Turtle()  fonksiyonu ile bir kare nesnesi
# oluşturuldu. bu oluşturduğumuz nesne hedefKare ismindeki değişkene atandı.
hedefKare.shape("square") # bu oluşturduğumuz nesnenin şekli shape() fonksiyonu kullanıraka kare olarak belirlendi.

def rastgelekonum(): # burada bir adet argümansız rastgelekonum isminde bir fonksiyon tanımlandı.
    hedefKare.penup() # hedefKare nesnesi kaldırıldı. amacımız gideceği yani ortaya çıkacağı yeni konumuna giderken
    # arkasında çizgi bırakmasını istemiyoruz. bu yüzden havaya kaldırıp o şekilde gitmesini istiyoruz.
    hedefKare.setpos(random.randint(-300,300),random.randint(-300,300)) # burada hedefKare nesnesinin konumunu
    # belirliyoruz. bunu da setpos() fonksiyonunu kullanrak belirliyoruz. konumu koordinatlarıın ise random modülü ile
    # rastgele -300 ile 300 arasından rastgele belirliyoruz. biz buradan x ve y gibi ikili değerler alıyoruz.
    hedefKare.showturtle() # hedefKare nesnesinin o gittiği konumda göstermesini istiyoruz.

def yukari(): # burada argümansız olarak bir adet yukari isminde bir fonksiyon tanımlıyoruz. amacımız klavyedeki
    # tuşları bu tanımlayacağımız fonksiyonlar ile kullanmak.
    okSimgesi.right(15) # okSigesi nesnesini sağa 15 derece döndür.

def asagi(): # asagi isminde argümasız bir fonksiyon tanımlanıyor.
    okSimgesi.left(15) # okSimgesi nesnesi sola 15 derece döndür.

turtle.onkeypress(yukari,"Up") # onkeypress fonksiyonu içerisinde yukarı fonksiyonu çağrılıyor. kullanıcı klavyeden
# yukarı tuşuna basarsa yukarı isimli fonksiyon çalışsın.
turtle.onkeypress(asagi,"Down")# onkeypress fonksiyonu içerisinde asagi isimli fonksiyon çağrılıyor. kullanıcı
# klavyeden aşağı yön tuşuna basar ise asagi isimli fonskiyon çağrılsın ve çalışsın.
turtle.listen() # bu işlemler olmadan ben yapmadan yapma , yani beni dinle diyoruz fonksiyona.

rastgelekonum() # burada rastgele bir konum belirliyoruz.

while True: # döngü sağlandığı sürece doğru olduğu sürece
    okSimgesi.fd(1) # okSimgesi nesnesi 1 birim ileri git her döngüde.

    x=(okSimgesi.xcor()- hedefKare.xcor()) # burada okSimgesi ile hedefKara nesneleri arasındaki x uzaklığının x koordinatının belirliyoruz.
    y=(okSimgesi.ycor()- hedefKare.ycor()) # burada okSimgesi ile hedefKara nesneleri arasındaki y uzaklığının x koordinatının belirliyoruz.
    uzaklik=((x*x)+((y*y)))**0.5 #  # burad pisagor bağlantısı kurularak okSimgesi nesnesi ile hedefKare arasındaki
    # uzaklık pisagor bağlantısı ile elede edilip uzaklık değişkenine atılıyor.

    if uzaklik<15: # eğer uzaklı # eğer uzaklık 15 denküçük ise
        hedefKare.hideturtle() # hedefKare nesnesini gizle
        rastgelekonum()# yeni bir konum elde ettik.

