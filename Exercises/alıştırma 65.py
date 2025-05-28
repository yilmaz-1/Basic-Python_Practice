"""

# dosya açma işlemini bir değişkene atmamızın en büyük sebebi ise bu file değişkeni bir imleç görevi görüyor. böylelikle
#dosya satırları ve karakterleri üzerinde rahat rahat gezinmemizi sağlıyor.

file = open("bilgiler.txt", "w")# bilgile isminde bir dosya açtık. bu dosya açma işlemini ise open() fonskiyonunu ve
# yazma kipi olan write (w) kullanarak gerçekleştirdik. bu dosya açma işlemini ise file değişkenine atadık ki bundan
# sonra yapacağımız diğer işlmeleri bunun değişken üzerinden daha rahat yapabilelim diye.
file.close() # dosya üzerinde işlemlerimiz bittikten sonra da dosyayı kapatırıyoruz.

"""


"""
file = open("D:\PYTHON\kotlamalar 3","w") # burada ise dosyayı, özellikle belirttiğimiz bir konuma açmak için o konumun 
# adresni yazdık.
file.close() # her zaman ki gibi dosyayı kapattık.

"""



"""

file=open("bilgiler.txt","w",encoding="utf-8") # burada open() fonksiyonunu kullanarak, yazma kipinde karakter foramtı 
#olarak da utf-8 modunda bir dosya açtık. utf-8 kullanamızın sebebi ise: yazdıracağımız ifadenin içersinde türkçe 
#karakter olduğu için.
file.write("mehmet\nışık\nevli") # file değişkenine atanan dosya yazma fonskiyonu olan write() fonksiyounu ile fonksiyon 
#içersinde belirtilen ifadeler yazdırıldı.
file.close() # dosya kapatıldı.

"""


"""
file = open("bilgiler.txt","a",encoding="utf-8") # yukarıdaki örneklerde olduğu gibi, bir dosya açıldı fakat buradaki
# fark şu: dosya açma kipi "a" append olduğu için mevcut dosyayı silip yeniden dosya açmıyor. mevcut dosyaya hiç
# dokunmuyor. mevcut dosyanın üzerine yazıyor. dosya imleci dosayını sonuna giderek eklemek istediğimiz şeyi ekliyor.
file.write("mehmet\nışık\nevli")
file.close()

"""



"""

try:
    file = open("bilgiler.txt","r") # burada bilgiler.txt dosyası okumakipi olan "r" ile açıldı. bu kip sadece okumak için
    # dosyayı açar. herhangi bir şey ekleme çıkarma yapmaz. eğer bilgiler.txt dosyası yoksa python hata verir.
except FileNotFoundError:
    print("Dosya Bulunamadı..")


"""



"""
file = open("bilgiler.txt","r",encoding="utf-8") # burada okuma kipi kullanılarak bir dosya açıldı. içindeki verilerin
# okunması amacıyla açıldı.
for i in file: # daha sonra for döngüsü ile bu dosyanın üzerinde gezinerek, yani satırları üzerinde, her bir satır her
    # döngüde i değişkenine atanarak alındı.
    print(i) # her döngüde i değişkenine atanan her satır her ddöngü sonunda ekrana yazdırıldı.
file.close() # dosya üzerinde işlemlerimiz bittikten sonra dosya kapatıldı.

# çıktı
#mehmet

#ışık

#evli

# yukarıda çıktı da her satır ekrana yazdırıldıktan sonra bir satır atlanarak yazdırmaya devam edilmiş. burada olan şey
# şu: zaten python da varsayılan olarak \n krakteri koyduğu için her satırın sonuna biz print ifadesi ile bir tane daha
# \n karakteri koyunca (print de varsayılan olarak ) bu durum ortaya çıkıyor. bu durumu düzeltmek için print(i,end="")
# kodu ile şunu demiş olduk. print sen \n karakterini varsayılan olarak koyma onun yerine "" çift tırnak arasında yer
# alan ifadeyi koy demiş olduk. böylelikle gereksiz satır atlamanın önüne geçmiş olduk.

"""




"""
file = open("bilgiler.txt","r",encoding="utf-8") # her zamanki gibi okum akipi ile bir dosya açtık.
icerik = file.read() # read()fonskiyonu ile dosyanın içerisinde ne varsa okuduk. bu read() fonskiyonu bize bir string
# ifade döndürecek. bizde bu string ifadeyi icerik isimli değişkene yolladık.
print(f"Dosya İçeriği\n{icerik}") # daha sonra da bu icerik değişkenine yolladığımız string ifadeyi ekrana yazdık.

"""


"""
file = open("bilgiler.txt","r",encoding="utf-8") # dosya okuma kipi ile açıldı.

icerik1 = file.read() # dosya read() fonksiyonu ile okunup oradan dönen string ifade icerik1 değişkenine yollandı.
print(f"Dosya İçeriği 1\n{icerik1}") # icerik1 değişkeni ekrana basıldı.
# burada kritik bir olay oldu. oda şudur: file değişkeni bizim dosya imlecimiz olmuştu. yani dosya içerisinde satırlarda
# gezdiğimiz imleç oldu. şimdi biz read() fonskiyonu ile dosyayı okuyup içerik1 değişkenine yollayınca file imlecimiz
# dosyanın sonuna gitti. şuan orada. biz hiç bir şekilde dosyayı kapatmadan tekrar okuma yaptırırsak dosyayı buradan
# okumaya devam edecek. eğer dosyanın sonunda bir ifade yoksa bize boş string dönecek.
icerik2 = file.read() # bu durumdan dolayı yeni okuma sonucunda bize bu icerik2 değişkenine yollanacak olan bir string
# ifade olmaycağı için
print(f"Dosya İçeriği 2\n{icerik2}") # ekrana boş string basılacak.
file.cloes()

"""


"""
file = open("bilgiler.txt","r",encoding="utf-8") # dosya okuma kipi ile açıldı.
print(file.readline()) # burada readline() fonksiyonu kullanldı. amacımız program her çalıştığında sadece bir satır
# okumasını sağlamak.
print(file.readline()) # bu fonskiyon her okuma yaptığında bir satır atlayarak diğer satırı okur.
print(file.readline()) # yani ilk print de 1. satırı okudu ekrana bastı. 2. print çalıştığında bir satır atladı ve
# 2. print ile 2. satırı okudu ve ekrana yazdı. daha sonra 3. print çalıştığında bir satır atladı 3. satırı okudu ve
# ekrana yazdı.
file.close() # dosya kapatıldı.
# readline() fonksiyonu okunacak bir şey  kalmayınca boş string döner.
"""




"""
file = open("bilgiler.txt","r",encoding="utf-8")# dosya okuma kipi ile açıldı.
print(file.readlines()) # burada readlines() fonskiyonu ile dosya içeriği okunuyor. bu fonksiyonun özelliği ise şu:
# tek bir satır okumak yerine tüm satırları okuyor. Bize bu stırları bir liste içerisinde gönderiyor.
file.close() # dosya kapatıldı.

"""


"""

with open("bilgiler.txt","r",encoding="utf-8") as file: # bu kalıp çok önemli. bundan sonra her dosya açtığımızda
    # yukarıda ki örneklerde olduğu gibi program sonunda close ile dosyayı kapatmamıza gerek kalmayacak. bu kalıp ile
    # açtığımız dosyalarımız otomatik olarak kapanacaktır. close() fonskiyonu ile tekrar kapatmamıza gerek kalmayacak.
    # burada şunu dedik: bilgiler.txt dosyasını okuma kip ile aç. ama biz dedik ki bu dosya içerisnde türkçe karakater
    # olduğu için bu durumdan dolayı anlasız şekilller veya okuma soun olmasın diye encofing="utf-8" ile içeriği
    # belirttik. daha sonra ise bu bilgiler.txt doyasının bundan sonra file olarak al dedik (as fiile) ifadesiyle.
    for i in file: # burada for döngüsü ile file içerisindeki satırlar üzerinde geziniyoruz. her döngüde bir satırı i 
        # değişkenine atanyor. 
        print(i) # her döngü sonunda bu i değişkeni ekrana bastırılıyor.

"""



"""

with open("bilgiler.txt","r",encoding="utf-8") as file: # yukarıda da anlatıldığı üzere bilgiler.txt dosyasını okuma
    # kipi ile açıyoruz.
    print(file.tell()) # print içerisnde yer alan tell fonksiyonu dosya imlecinin dosya içersinde hangi byte da
    # (kaçıncı byte ta) yani hangi karakter üzerinde olduğunu söylüyor. print ile de kaçıncı byte da ise onu da ekrana
    # bastırıyoruz.
    file.seek(5) # seek() fonksiyonun temel amacı ise şudur: dosya imlecini dosya üzerinde istediğimiz bir yere yollamak
    # yukarıda tell() fonksiyonu ile imlecin yerini 0 (sıfır) olarak öğrenmiştik. file.seek(5) ifadesi ile de dosya
    # imlecini 5. byte yolladık.
    print(file.tell()) # tekrar sorduğumuz da ise imlecin 5. byte olduğunu göreceğiz.

"""


"""
with open("bilgiler.txt","r",encoding="utf-8") as file: # daha önceki örnekler de de olduğu gibi dosya okuma kipi ile
    # açıldı.
    print(file.tell()) # dosya imlecinin dosya üzerinde hangi byte olduğu sorduk. bu kod satırı sadece bilgi almak için
    # yazıldı burada. yazılmasa programın çalışmasına herhangi bir etkisi olmazdı.
    file.seek(14) # seek() fonksiyonu ile dosya imlecini dosya içerisndeki 14. byte yolluyoruz.
    icerik = file.read(10) # burada file dosyası üzerinde read () fonksiyonu ile okuma yapıyoruz. bu okuduğumuz string
    # ifadeyi ise icerik isimli değişkene yolluyoruz. ama burada bir fark var. read(10) fonskiyonu içine 10 sayısı
    # gönderildiği için okuma yaparken dosya imlecinin olduğu yerden başlayarak 10 karakter oku demiş olduk.10 byte yani
    print(icerik) # dosyadan okuduğumuz içeriği ekrana bastırıyoruz.
    print(file.tell()) # burada da dosya imlecinin nerde olduğunu tell() fonksiyonu ile öğreniyoruz ve ekrana
    # yazdırıyoruz.
    file.seek(0) # bu kod ile de dosya imlecini tekrar dosyanın en başına gönderdik.

"""





"""
with open("bilgiler.txt","r+",encoding="utf-8") as file: # burada dosya açma işlemi yapıldı. bu açma işlemi şimdiye
    # kadar gördüğümüz kiplerden farklı bir kip ile yapıldı. r+ kiipi dosyayı hem okumak için açar hemde o dasyaya bir
    # şey eklemek yapmak için kullanılır. bu iki işlemi aynı anda yapar.
    file.seek(178) # seek fonksiyon ile belirtilen byte a gidiliyor. 178 e .
    print(file.write(".....MERHABA DÜNYA.....")) # dosya imleci o byte gelince write() fonksiyonu ile o baytan itibaren
    # azılacak ifade etkleniyor dosyaya.
with open("bilgiler.txt","r+",encoding="utf-8") as file: # dosya hem okuma hem de yazma kipi ile açılıyor.
    print(file.read())# daha sonra dosya okunup ekrana yazdırılıyor.

"""




"""
with open("bilgiler.txt","a",encoding="utf-8") as file: # burada bilgiler.txt ismindeki dosya açıldı. fakat açma kipi
    # append tir. yani "a" ile açıldı. "a" ile açılmasının amacı dosyanın sonuna ekleme yapmak istememizdendir.
    file.write("deneme çalışması") # dosya imleci dosyanın sonuna gittikten sonra write () fonksiyonu ile dosyanın
    # sonuna ekleme yapılıyor.
with open("bilgiler.txt","r",encoding="utf-8") as file: # burada dosya okuma kipi ile r ile açılıyor.
    print(file.read()) # dosya read () fonksiyonu ile okunup içerik ekrana yazdırılıyor.

"""




"""
# burada dosyanın başına bir şeyler eklemenin nasıl yapıldığını öğrendik.
with open("bilgiler.txt","r+",encoding="utf-8") as file:# burada yularıda ki örneklere benzer bir şekilde dosya açıldı.
    # hem okuma hemde yazma yetkisi iel açıldı.
    icerik = file.read() # burada dosya çierği okundu. ve okunan dosya içeriği ise icerik ismindeki değişkene yollandı.
    icerik = "mokoko\n" + icerik # burada ise, dosya içerisinde okuyup elde ettiğimizi içeriği
    # (okunan içerik bize string olarak döndü) "mokoko" string ifadesi ile toplanıyor. ieriğimiz değişmiş oluyor.
    file.seek(0) # okuma işlemi bitti. içeriğe eklenecek ifade de eklendikten sonra, bu kod bloğunda ise dosya imleci
    # seek(0) fonksiyonu ile dosyanın en başına yollanıyor. dosya imleci şuan dosyanın en başındadır.
    file.write(icerik) # dosya imleci dosyanın en başına geldikten sonra, artık buraya, oluşturduğumuz icerik isimli 
    # değişkeni ekleyebiliriz.
    print(icerik) # içeriği ekrana bastırıyoruz.

"""

# readline() fonksiyonu bir dosya içerisinden sadece bir satır okurken, readlines() fonksiyonu ise odsya içerisinde yer
# alan bütün satırları okur.


with open("bilgiler.txt","r+",encoding="utf-8") as file: # burada dosya okuma ve yazma kipi ile açıldı.
    liste = file.readlines() # dosya içerisinde yer alan bütün satırlar readlines() fonksiyonu ile okundu. Okunan bu
    # içerik ise liste ismin deki bir değişkene atandı. okuma sonucunda elde edilen bu içerik liste değişkenine
    # yollanırken bu yollanan verinin tipi liste formatındadır.
    liste.insert(3,"mühendis\n") # yukarı da eldfe ettiğimiz liste formatındaki liste değişkenine insert() fonksiyonu
    # ile "mühendis" string ifadesi eklenecek. bu ekleme şu şekilde oluyor. biz bu eklemeyi insert fonksiyonu ile
    # yapıyor. yaparken de bu fonskyonun içine yollanan argümantları dikkate alıyoruz. burada 3 indeksin yerine
    # fonksiyonun 2. argümanında yer alan mühendis string ifadesi yazılsın deniyor.
    file.seek(0) # istdiğimiz ifadeyi dosaynın içeriğine eklendi. burada ise dosya imleci sayfanın başına yollanıyor.
    for i in liste: # for döngüsü ile liste değişkenin her elemanı i değişkenine atanarak alınıyor.
        file.write(i) # aldığımız o veri yani satır, dosaynın başından itibaren yazılıor.
with open("bilgiler.txt","r+",encoding="utf-8") as file: # doğru yazdığından emin olmak için, dosya okuma ve yazma kipi
    # ile açıldı.
    print(file.read()) # dosya içeriği read fonksiyonu ile okundu. okunan içerik print ile yazıldı.



















