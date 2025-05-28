"""
Aşağıdaki örneklerde dosya işlemleri ile ilgili bazı bilgiler uygulamalar yapıldı.

Dosya işlem ile ilgili bazı ön tanımlı ( python da gömülü ) kip'ler vardır. Bunlar dosya işlemleri yaparken bize
kolaylık sağlamaktadır.
python da pek çok kip vardır ama en çok kullanılanlardan bazıları aşağıdaki gibidir.

"r" (read - okuma) => Bu ön tanımlı kiptir. Bu kip dosyayı okuma yetkisiyle açar. Ancak bu kipi kullanabilmemiz için,
ilgili dosyanın disk üzerinde var olması gerekir. Eğer bu kipte açılmak istenen dosya mevcut değilse python bize bir
hata mesajı gönderecektir. Dosya varsa okur yoksa hata verir.

"w" (write - yazma) => Bu kip dosyayı yazma yetkisiyle açar. Eğer belirttiğiniz adda bir dosya disk üzerinde varsa,
python hiçbir şey sormadan dosya içeriğini silecektir. Eğer belirttiğiniz adda bir dosya diskte yoksa python o adda bir
dosyayı otomatik olarak oluşturur. yazma modu. dosya varsa içeriğini siler yoksa oluşturur.

"a" (append - ekleme) => Bu kip dosyayı yazma yetkisyle açar. Eğer dosya zaten disk üzerinde mevcutsa içeriğinde
herhangi bir değişiklik yapılmaz. Bu kipte açtığımız bir dosyaya eklediğiniz veriler var olan verilere ilave edilir.
Eğer belirttiğiniz adda bir dosya yoksa python otomatik olarak o adda bir dosya sizin için oluşturacaktır. dosya varsa
içeriğe ilave eder yoksa oluşturur.

"""

"""

f = open("mehmet.txt", "r") # bu kod hata hata verecek. çünkü mehmet.txt dosyası olamdığı için
# python açıpta okuyacak bir dosya bulamadı disk üzerinde.

f.close()

"""


"""

f = open("mehmet.txt","w") # kod hata vermedi. çünkü biz w kipi ile bu dosya açma işlemi yaptık.  dosya olsa idi
# içeriğini silecekti olmadığı için yeni dosya oluşturdu.
f.close() # mutlaka açılan dosya kapatılmalıdır. çünkü, kapatılmayan dosya kullanılamaz.

"""

"""

f = open("mehmet.txt","a") # bu kod hata vermedi. çünkü biz a kipi ile mevcut dosyaya ilave ettik. dosya olmasaydı 
# oluşturup öle yazardı 

f.close()

"""



"""

f = open("denemeDosyası.txt","a") # append modu ile dosya açtık. denemeDosyası disk üzerinde olmadığı için append ile
# açmayı tercih ettik. write ile de açabilirdik.
f.write("deneme dosaysı içerisine append kipi ile veri yazıyoruz şuan.") # açtığımız dosyanın içersine ise
# " deneme dosaysı içerisine append kipi ile veri yazıyoruz şuan." ifadesini yazdırdık.
f.close() # mutlaka bu dosya kapatılmalıdır. ve biz de kapattık.

f=open("denemeDosyası.txt","r") # yukarıda oluşturduğumuz dosyayı read moduyla açtık.
denemeDosyası_icerigi=f.read() # bu dosyanın içeriğini oku.
print(denemeDosyası_icerigi) # daha sonra bu dosya içeriğini ekrana yazdır.
f.close() # dosyayı kapat

"""







