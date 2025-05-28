"""
liste1 = [1,2,3,4,5] # burada bir adet bir liste tanımlandı.
liste2 = [6,7,8,9,10,11] # burada bir adet liste tanımlandı.

i = 0 # aşağıdaki döngüde kullanmak üzere bir adet i değişkeni tanımlandı.
sonuc = list() # döngüde kullanmak üzere bir adet değişken tanımlandı.
while (i<len(liste1) and i < len(liste2)): # bu döngü i değeri listelerin boyundan küçün oluncaya kadar devam etsin
    sonuc.append((liste1[i],liste2[i])) # her döngüde elde ettiğimiz liste1 in i inci indeksinde yer alan karakter ile
    # liste2 nin inci indeksinde yer karakteri birlşetir bir demet yap ve sonuçisimindeki boş listeye at dedik.

    i +=1 # her döngü sonunda i değerini bir artır.
print(sonuc) # sonuc listesini ekrana bas

# yukarıda yer alan kodu daha kısa yoldan nasıl yazabiliriz ? Aşağıda ki fonksiyonu kullanarak daha kısa yoldan
# halledebilirz.

print(list(zip(liste1,liste2))) # yukarıda ki kodu kısa tek satırdabu şekilde de yapabilirz. Buradaki zip() fonskiyonu
# python da gömülü fonksiyondur.


"""


"""
sozluk1 = {"Elma": 1, "Armut": 2, "Kiraz": 3}
sozluk2 = {"Sıfır": 0, "Bir" : 1, "İki": 2}

print(list(zip(sozluk1,sozluk2)))

# yukarıda ki kodda zip fonskiyonu kullanılarak iki sözlük birleştirildi.

print(list(zip(sozluk1.values(),sozluk2.values())))

# yukarıda ki kodda zip fonskiyonu sözlükler üzerinde kullanımını yaptık.

"""

liste1 = [1,2,3,4] # bir liste tanımladık
liste2 = ["python", "php", "java", "javascript"] # bir liste tanımladık

for i,j in zip(liste1,liste2): # burada for döngüsü ile her döngüde i ve j ye atamak üzere liste1 ve liste2 den eleman
    # aldık. i yi liste1 den j yi de liste2 den alarak zip fonksiyonu sayesinde her iki liste üzerinde aynı anda
    # gezinmeyi sağladıkj.
    print(i,j)

"""
for i,j in (liste1,liste2):
    print(i, j)
eğerki yukarıda yer alan döngüyü zip kullanamdan yaparsak hata ile karşılaşacağız. her iki liste üzerinde aynı anda 
gezinmemize izin vermeyecektir.


"""


