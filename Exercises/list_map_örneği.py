numbers = [1, 2, 3]# burada bir adet liste tanımlandı.

result = list(map(lambda num: num ** 2, numbers)) # burada result isminde bir adet değişken tanımlandı. bu değişken
# içerisine gönderilecek olan değerler ( yani numbers listesi içerisnden alınan  değerler) lambda ile her bir değerrin
# karasi alınması ifade edildi. daha sonra da map metodu ile de bu karesi alınma işlemi bu liste içersinde yer alan
# bütün değerler üzerine uygulanması istendi.

print(result) # result ekrana yazdırıldı.
# çıktı:
# [1, 4, 9]
