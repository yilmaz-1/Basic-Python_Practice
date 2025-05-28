#######################

# Dict Comprehension
# Mülakat Sorusu

######################

"""
burada ki amacımız belirli bir sayıya kadadr olan listedeki veya dizideki her neyse o sayılar içinde çift olanların
karesi alınarak bir dict (sözlük )yapısına karesi alınmamış hali ile birlikte eklenerek çıktı alınmasını sağlyan  bir
program yazmak.
Yani key değerleri orjinal olacak, values değerleri ise karesi alınmış değerler olacak.

örnek:

normal sayı dizisi:  0,1,2,3,4,5,6,7,8,9,10
karesi alınmış hali: 0,1,4,3,16,5,36,7,64,9,100
dict yapısı : {0: 0, 1:1, 2: 4, 3:3, 4: 16, 5: 5, 6: 36, 7: 7, 8: 64, 9: 9, 10: 100 }

yukarıdaki yapıyı elde etmemizi sağlyan bir kod bloğu yazacağız.

"""

numbers = range(0,10) # burada numbers isminde bir değişkene atanmış bir seri mevcut. bu seri range fonskiyonu ile elde
# elde dilmiş.
new_dict = {} # bir sözlük yapısı şeklinde istediğimiz için burada bir adet boş bir sözlük tanımlandı.

for i in numbers: # numbers değişkeninin elemanları üzerinde gezerek tek tek i değişkenine atayarak elde ediyoruz.
    if i % 2 == 0: # elde ettiğiğmiz bu i değerlerinden 2 ile bölümünden kalan sıfır olan varsa eğer yani çift ise
        new_dict[i] = i**2 # bu i değerinin karesini al ve karesi alınmamış hali olan i değerinin sözlükteki index
        # karşılığına gelen indexe ata
    else: # i değeri tek sayı ise
        new_dict[i] = i # o i değerini, i.inci indexe ata
print(new_dict)

# out
 # {0: 0, 1: 1, 2: 4, 3: 3, 4: 16, 5: 5, 6: 36, 7: 7, 8: 64, 9: 9}

"""
yukarıdaki kodu daha kısa yoldan bir de dict comprehension yöntemi ile yazalım.

"""
print({i: i**2 if i % 2 == 0 else i for i in numbers})