"""
=> divide_students fonskiyonu yazınız.
=> çift indexte yer alan öğrencileri bir isteye alınız.
=> Tek indexte yer alan öğrencileri bir listeye alınız.
=> Fakat bu iki liste tek bir liste olarak return olsun.

"""

students = ["Mehmet", "Ali", "Ahmet", "Hakkı", "Mahmut"]


def divede_students(students): # burada bir argümanlı bir fonskiyon tanımlandı. bir argümanlı olmasının sebebi ise
    # yukarıda ki liste üzerinde işlem yapacağımız için tek argümanlı fonksiyon tanımladık.
    groups = [[], []] # burada groups isminde bir değişken oluşturduk fakat burada bu değişkenin sıfırıncı indeksine
    # ve birinci indeksine students liste içerisinden aldığımız değerler yollanacak.
    for index, student in enumerate(students):# students listesi üzerinde gezineceğiz for döngüsü ile. fakat biz sadece
        # student listesinin elemanları üzerinde gezinmek isteiyoruz ayrıca index bilgisini de almak istiyoruz.
        # bunun için enumerate fonskiyonu ile student listesi üzerinde gezindik. enumerate ile listenin hem elemanlarına
        # hemde indexlerine ulaştık.
        if index % 2 == 0:# aldığımız index değerlerinden çift olanlardaki karakterleri al
            groups[0].append(student) # groups değişkenin sıfırıncı indeksine yolla
        else: # tek index te yer alan elemanları ise
            groups[1].append(student) # gropupsdeğişkeninin 1. indexine yolla
    print(groups)
    return groups


st_0 = divede_students(students)

print(st_0[0])

print(st_0[1])


