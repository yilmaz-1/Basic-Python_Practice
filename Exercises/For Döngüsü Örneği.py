numbers = [[1,10],[6,60],[12,54],[67,99]] # burada bir adet içerisinde listelerin olduğu bir liste oluşturuldu. numbers
# değişkenine atandı.

for i in numbers: # burada for ile numbers listesi üzerinde bir döngü kuruldu.
    #print(*range(*i)) # (1) # her döngüde elde edilen i değeri range fonksiyonun içersine gönderildi. * işareti ise
    # 1 den i ye kadar yaz demek. i değerini [1, 10] eğer biz 1 den 10 kadar yazdırmak istiyorsak başına yıldız koymamız
    # lazım. aksi halde yazmaz. eğer yıldız kullanamdan yazmak istiyorsak aşağıdaki gibi yazmamız lazım.
    print(*range(i[0],i[1])) # (2)


# Yukarıda verilen kod incelenirse: