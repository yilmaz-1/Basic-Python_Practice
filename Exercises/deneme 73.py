# def add(a,b):
#     return sum((a,b)) # sum() fonksiyonu içerisine gönderilen değerlerin toplamaya yarıyor.
# # çift parantez önemli.
#
# print(add(5,3))

# ****************

# def add(a,b,c=0): # burada c=0 yapılmasının eşitlenmesinin sebebi: fonksiyon çağrıldığında hem 2 hem 3 parametre iile çağrılabilir olmasıdır.
#
#     return sum((a,b,c))
#
# print(add(1,2))
# # çıktı:
# # 3
# print(add(1,2,3))
# # çıktı
# # 6
# *****************

# def add(a,b,c=0,e=0,d=0): # burada c e ve f değişkenleri sıfıra eşitelnemsinin sebebi bu fonksiyon çağrıldığı zaman bu foksyonu en az 2 en fazla 5 değişkenli olarak kullanbilmemize olanak sağlıyor mantık şu şekilde:
#     return sum((a,b,c,d,e))
#
# # biz burada c e d ye sıfır varsayılan oralak sıfır atadık. eğer ki biz bu foksiyonu bu 3 değişkenden biri olmadan çağırdığımızda gonksiyon otomatik olarak bu değişkene sıfır atayacak ve sıfır ile toplaması sonucu değiştirmeyecek.
#
# print(add(1,2))
# # çıktı:
# # 3
#
# print(add(1,2,3))
# # çıktı:
# # 6
#
# print(add(1,2,3,4))
# # çıktı:
# # 10
#
# print(add(1,2,3,4,5))
# # çıktı:
# # 15

# **********************

# diyelim ki biz 6 parametre veya 150 prametre yollamak istiyoruz bu add fonksiyonun içine.
# burada * ifadesini kullanacağız. tek yıldız, liste göndereceğimiz anlamına gelir.
#
# def add(*parameters): # tek tek yazmak yerine * ifadesi ile istediğimiz kadar paramtre gönderebiliyoruz.
#     return sum(parameters) # sum foksiyonu da bu gönderdiğimiz bütün parametreleri toplamamızı sağlıyor.
#
# print(add(1))
# # çıktı:
# # 1
# print(add(1,2))
# # çıktı:
# # 3
# print(add(1,2,3,5,6,4,7,8,9,4,5,6,3,2,12,35,6324,2546))
# # çıktı:
# # 8982

# *********************************************

# def add(*parameters): # burada sum() fonksiyonunu kullanmadık. normal for döngüsü ile yaptık
#     toplam=0
#     for i in parameters:
#         toplam+=i
#     print(toplam)
#     return toplam
#
# add(1,2,3,4,5,6)

# **************************************************

# def displayUser(**argumans): # ** kullanılmasının amacı sözlük veri tipinde veriler geleceği anlamına gelir. bu yüzden ** kullanıldı.
#     for key, value in argumans.items():
#         print("{} is {}".format(key,value))
#
#
#
# displayUser(name="mehmet",age="12",city="adana")
# displayUser(name="ali",age="15", city="maraş",phone="12345")
# displayUser(name="hasan",age="17", city="antep",phone="123456",mail="mehmet@gmail.com")

# *************************************************************
#
# def myFunc(a,b,*args,**kwargs):# burada normal olarak a ve b prametresi bekliyoruz. dah sonra *args lı yerde bir liste bekliyoruz.  daha sonra da **kwargs ile de sözlük belediğimizi ifade ediyor.
#     print(a)
#     print(b)
#     print(args)
#     print(kwargs)
#
# myFunc(1,2,3,4,5,6,7,8,key1="value1",key2="value2")

# çıktı:
# 1 a ya karşılık geliyor.
# 2 b ye karşılık geliyor
# (3, 4, 5, 6, 7, 8) *args a karşılk geliyor
# {'key1': 'value1', 'key2': 'value2'} **kwargs karşılk geliyor

# *************************************************************














