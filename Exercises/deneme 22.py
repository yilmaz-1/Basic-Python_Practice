# liste = [] # globalde bir boş bir liste tanımlanıyor.
#
# for i in range(1,101): # for döngüssü ile range fonksiyonu kullanılarak 1 den 101 kadar olan 1 dahil 101 hariç sayılardan bir liste oluşturuyor.
#     if (i % 2 ==0): # for döngüsü ile elde edilen liste içinde eğer 2 ile bölümünden kalan sıfır ise
#         liste.append(i)# bu 2 ile bölümünden kalan sıfır olan sayılar append metodu ile golbalde tanımladığımız boş listeye atılıyor.
# print(liste) # döngü dışında yazdığımız print fonksiyonu ile de oluşturulan liste ekrana basılıyor.
# # çıktı:
# # [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50, 52, 54, 56, 58, 60, 62, 64, 66, 68, 70, 72, 74, 76, 78, 80, 82, 84, 86, 88, 90, 92, 94, 96, 98, 100]

# yukarıdaki cod ile aşağıda ki kod aynı işlevi yapıyor. arasında ki fark yazım farkıdır. yukarıda bildiğimiz klasik yöntem ile yazılmıştır. aşağıda ise liste metodu ile yazılmıştır.

liste = [i for i in range(1,101) if i %2 ==0] # burada liste isimli değişken for döngüsü ve if koşulu liste metodu ile tanımlanarak oluşturulmuştur.
print(liste) # liste ekrana basılıyor.
# çıktı
# [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50, 52, 54, 56, 58, 60, 62, 64, 66, 68, 70, 72, 74, 76, 78, 80, 82, 84, 86, 88, 90, 92, 94, 96, 98, 100]