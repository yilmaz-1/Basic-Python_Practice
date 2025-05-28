liste1=[1,2,3,4,5] # liste1 tanımlandı.
liste2=[] # liste2 boş olarak tanımlandı.
for i in liste1: # bu yöntem klasik liste oluşturma yöntemi. for döngüsü ile liste1 elemanları üzerinde gezinerek i değerleri elde edilyoruz.
    liste2.append(i*2) # döngü ile elde ettiğimiz i değelerini 2 ile çarpıp append metodu ile boş olan liste2 ye atılıyor.
print(liste2)# döngü bittikten sonra liste2 ekrana basılıyor.
# çıktı:
#[2, 4, 6, 8, 10]

# yukarıda for döngüsü ile yazılan fonksiyon list comprehension yöntemi ile yazıldı aşağıda.

liste1= [1,2,3,4,5] # liste1 tanımlandı.
liste2=[i*2 for i in liste1] # list comprehension yöntemi. liste2 list comprehension yöntemi ile tek satırda yazıldı.
print(liste2)# liste2 ekrana basıldı.
# çıktı:
# [2, 4, 6, 8, 10]


