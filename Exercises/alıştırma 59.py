def sifrele(metin): # sifrele isminde bir argümanlı bir fonksiyon tanımlandı.
    sifrelimetin="" # daha sonra sifrelediğimiz metni saklayabileceğimiz bir boş değişken oluşturduk.
    for harf in metin:# for döngüsü ile şifrelenecek metin içersindeki her harf tek tek alınarak harf değişkenine atandı
        asciikod=ord(harf)# her dögüde alınan bu harf ord() fonskiyonu ile ascii karşılığı olan sayılsal bir
        # değere dönüştürüldü.
        asciikod+=2 # her döngüde her harfe karşılık üretilen ascii kod numrasına burada 2 ekleniyor. bu ekleme
        # yapmamızın sebebi: şifreleme işlemin bu şekilde olsun istediğimiz için . tamamen bize bağlı bir durum yani.
        karakterkod=chr(asciikod)# yeni elde ettiğimiz ascii nuralarını ise chr() fonskiyonu ile tekrardan karakter
        # karşılığına dönüştürüyoruz.
        sifrelimetin+=karakterkod # her döngüse elde edilen yeni karakteri  boş sifrelimetin değişkenine yolluyoruz.
    # döngü burada bitiyor ama sifrele(metin) fonksiyonu bitmiyor.
    f=open("sezar.txt","a") # daha sonra elde ettiğimiz bu metni bir yere kaydetmemiz gerekeceği için burada bir open()
    # fonksiyonu ile sezar.txt isminde bir dosya açıyoruz. fakat bu dosya açma işlemini append modu ile a kipi ile
    # açıyoruz. çünkü elimizde böle bir dosya yok disk üzerinde ve bu dosyaya da birşeyler de kaydetmek
    # istiyoruz aynı zamanda.
    f.write(sifrelimetin) # açtığımız dosyaya da write() fonskiyonu ile  sifrelimetin değişkeninin içerisine
    # yer ala ifadeyi yaz diyoruz.
    f.close() # dosya açıldı, içerisine yazıldı. daha sonra da yani bu kod satırında da dosya kapatıldı.

    print("dosya başarılı bir şekilde kaydedildi.") # fonskiyon sağlıklı hatasız bir şekilde çalıştığı zaman sona
    # gelince print ifadesinin içersinde yer alan ifadeyi ekrana yazdır.

ilkmetin=input("Şifrelenecek Metini Giriniz: ") # kullanıcıdan bir adet metin girmesini istiyoruz.
sifrele(ilkmetin)# yukarıda tanıldığımız fonksiyonu çağırıyoruz.


def sifrecoz(): # burada bir argümansız bir adet sifecoz isminde bir fonskiyon tanımlandı.
    sifresizmetin="" # şifresini çözdüğümüz metini saklamak atamak için kullanacağımz bir sifresizmetin isminde
    # boş bir değişken oluşturuldu.
    f=open("sezar.txt","r") # burada sezar.txt ismindeki dosyanın içersideki verileri okumak amacıyla r kipi ile açıldı.
    metin=f.read() # dosyanın içerisinden okuduğumuz bilgileri metin değişkenine yolladık.
    for harf in metin: # daha sonra meetin değişkeni içerisinde yer alan harfleri for döngüsü ile harf değişkenine her
        # döngüde bir tane olmak üzere alındı.
        asciikod=ord(harf) # her döngüde alınan bu harf ord() fonskiyonu ile ascii numara karşılığına çevrildi.
        # ascikod değişkenine yollandı.
        asciikod-=2 # sonra asciikod değişkeninden 2 çıkarıldı. bir önceki fonksiyonda 2 eklmiştik şifrelemek için.
        # burada da o şifreyi çözmek için 2 çıkardık tekrardan.
        karakterkod=chr(asciikod) # elde edilen ascii numarasının karakter karşılığını chr() fonskiyonu ile elde ettik.
        sifresizmetin+=karakterkod # sifresizmetin değişkenine yolladık.
    f=open("sezar.txt","a") # burada ise sezar.txt dosyası append modu ile açıldı. bu mod ile açılmasını sebebi ise:
    # içerisinde bir ifade bilgi varsa silinmesin ve bizim vereceğimiz yeni bilgi ekrana yazılsın.
    f.write(sifresizmetin) # açtığımız dosya içerisine ise write fonskiyonu ile sifresizmetin ifadesi yazıldı.
    f.close() # dosya kapatıldı.
    print("dosya başaırlı bşr şekilde kaydedildi: ")  # ekrana yazdık.

sifrecoz() # program çağrıldı.












