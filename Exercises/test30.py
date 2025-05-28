# liste= []
#
# string = "merahaba"
#
# for i in enumerate(string):
#     # liste.append(i)
#     print(i)


isim = ["Sinan","Erdinç","Mehmet"]
yas = [30,24,29,40,39]
# print(list(zip(isim,yas)))
# çıktı:
# [('Sinan', 30), ('Erdinç', 24), ('Mehmet', 29)]

liste= []
for i in zip(isim,yas):
    liste.append(i)
print(liste)
# çıktı:
# [('Sinan', 30), ('Erdinç', 24), ('Mehmet', 29)]