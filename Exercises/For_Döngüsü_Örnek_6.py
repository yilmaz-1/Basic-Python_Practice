liste  = ["mehmet", "hasasn", "osman", 2, 3, 45, 2.5, 45.34] # içersinde int ve str type de elemanların olduğu bir
# liste tanımlandı.

liste_2 = [ "kalem", "silgi", "1234", ["ayeşe", "özge", 1, 23, 45, 2.2]] # içersinde int str ve liste tipinde
# elemanların olduğu bir liste oluşturuldu.

for oge1 in liste: # liste üzerinde bir for döngüsü kuruldu.
    print (f"< {oge1} > elemanının tipi {type(oge1)}.") # bu döngüde elde ettiğimiz her eleman print fonksiyonu ile
    # ekrana yazdırıldı.

print("####################")

for oge2 in liste_2: # liste_2 üzerinde bir for döngüsü kuruldu.
    print(f"< {oge2} > elemanının tipi {type(oge2)}.") # for döngüsü ile elde ettiğimiz her eleman print fonksiyonu
    # ile ekrana yazdırıldı.
