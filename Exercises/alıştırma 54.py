
from datetime import datetime # burada datetime modülünün datetime sınıfını programa dahil ettik.

simdi=datetime.now() # simdi isminde bir değişken tanımladık. bu değişkene de datetime sınıfının now fonskiyonunu
# kullanarak şimdiki tarihi atadık.

print(simdi.year)#simdi değişkenine atanan tarihin yıl bilgisini year fonksiyonunu kullanarak aldık ve ekrana yazdırdık.

print(simdi.month)#simdi değişkenine atanan tarihin ay bilgisini month fonksiyonunu kullanarak aldık ve ekrana yazdırdık

print(simdi.hour)#simdi değişkenine atanan tarihin saat bilgisini hour fonskiyonunu kullanarak aldık ve ekrana yazdık.

print(simdi.minute)#simdi değişkenine atanan tarihin dakika bilgisini minute fonksiyonunu kullanarak aldık ve ekrana yazdık.

print(simdi.second)#simdi değişkenine atanan tarihin saniye bilgisini second fonksiyonunu kullanarak aldık ve ekrana yazdık


