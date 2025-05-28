"""
Print Fonksiyonunun Parametreleri

print fonskiyonu ile birlikte bir çok parametre kullanılmaktadır. Bu bölümde sıklıkla kullanılan bir kaç parametreyi
öğreneceğiz.

"""

"""
sep parametresi

Aslında sep ifadesi ingilizcedeki sperator ayırıcı anlamına gelen kelimenin kısaltılmasından oluşuturulmuş bir kelimedir
Dolayısılya print fonksiyou ile ekrana basılacak olan öğeler arasına hangi karakteri yerleştireceğimizi söyler. 
Bu parametrenin ön tanımlı değeri ise bir adet boşluktur. eğer biz bir tanımlama yapmazsak otomatik olarak 
python programında tanımlı olan boşluk bırakır. 
Aşağıdaki örenkeleri inceleyip daha iyi anlamaya çalışalım.

"""

print(1, 2, 3, 4, 5, 5, sep="-")
# 1-2-3-4-5-5

print("06", "12", "2021", sep="/")
# 06/12/2021

print("T", "B", "M", "M", sep=".")
# T.B.M.M

print(1, 2, 3, 4, 5, 6, sep=" ")
# 1 2 3 4 5 6

print("mehmet", "ışık", "ceyhan", "kayseri",
      sep=" ""-"" ")  # burada sep parametresi içine verdiğimiz parametrede şunu dedik
# print fonksiyonnu içindei her argümandan sonra bir boşluk bırak sonra - işaretini koy sonra
# tekrar bir boşluuk daha bırak
# mehmet - ışık - ceyhan - kayseri

print(1, 2, 3, 4, 5, 6,
      sep=None)  # bu örnekte şunu gördük. sep parametresi çift tırnak içinde olmayıp aldığı tek argüman
# None dır. yukarıda bahsettğimiz şey ön tanımlı değer boşluk vardı ya işte bu boşluğu None ifadesi ile koyabiliyoruz.
# 1 2 3 4 5 6

"""
end parametresi 

sep prametresi print fonksiyonunda verilen prametreleri birleştirirken araya hangi karakterin gireceğini belirliyordu.
end parametresi ise bu parametrelerin sonuna 


"""
