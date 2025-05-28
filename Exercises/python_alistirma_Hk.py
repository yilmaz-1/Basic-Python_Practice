
# Question 1
x = 8
y = 3.2
z = 8j + 18
a = "Hello World"
b = True
c = 23 < 22
l = [1, 2, 3, 4]
d = {"Name": "Jake",
     "Age": 27,
     "Adress": "Downtown"}
t = ("Machine Learning", "Data Science")
s = {"Python", "Machine Learning", "Data Science"}

variables = [x,y,z,a,b,c,l,d,t,s]

[print("type is ", type(each)) for each in variables]

# Question 2

text = "The goal is to turn data into information, and information into insight"
#text = [word.upper() for word in text.split(" ")]
alternatif = text.upper().replace(","," ").replace("."," ").split()
# print(text)
print(alternatif)

# Question 3

lst = ["D", "A", "T", "A", "S", "C", "I", "E", "N", "C", "E"]  #List
print("len of the list is: ", len(lst)) # Length of the list
print("Sıfırıncı index: ", lst[0], " onuncu yani sonuncu index ", lst[-1]) # Zero and ten indexes of the list -1
s_list = lst[0:4] # Slice of the list.
#lst.remove(lst[8]) # Removing the 8. index /alternative > pop
lst.pop(8)
lst.append("N") # Adding the new element to list
lst.insert(8, lst[len(lst)-1]) # Adding "N" to the 8. index.
#lst.insert(8, "N")
lst.pop(-1)

# lst.insert(8, "N") # Adding "N" to the 8. index.

# Question 4

dict_ = {"Christian": ["America", 18],
         "Daisy": ["England", 12],
         "Antonio": ["Spain", 22],
         "Dante": ["Italy", 25],}
dict_.keys()
dict_.values()
dict_["Daisy"] = ["England", 13]
dict_["Daisy"][1]=13
dict_["Ahmet"] = ["Turkey",24]
# dict_.update({"Ahmet": ["Turkey", 24]})
dict_.pop("Antonio")
# del dict_["Antonio"]

#for country, age in dict_.values():
#     print(each, item)

# Question 5

l = [2,13,18,93,22]

even = []
odd = []
def even_odd(l):
    [even.append(each) if each % 2 == 0 else odd.append(each) for each in l]
    return even, odd

#list(filter(lambda x : x%2 == 0, l )):
#list(filter(lambda x : x%2 == 1, l )):

even, odd = even_odd(l)

l = [2,13,18,93,22]

def func(list):

    çift_list = []
    tek_list = []

    for i in list:
        if i % 2 == 0:
            çift_list.append(i)
        else:
            tek_list.append(i)

    return çift_list, tek_list

çift,tek = func(l)

# Question 6

ogrenciler = ["Ali", "Veli", "Ayşe", "Talat", "Zeynep", "Ece"]
muh_ogr = ogrenciler[0:3]
tip_ogr = ogrenciler[3:6]
ogrenciler = [muh_ogr, tip_ogr]

for each in ogrenciler:
     if each == muh_ogr:
          for count, item in enumerate(each, start = 1):
            print("Mühendislik Fakültesi ", count ," . öğrenci: ", item)
     else:
          for count, item in enumerate(each, start = 1):
            print("Tıp Fakültesi ", count ," . öğrenci: ", item)

"""
Alternative 1 
for index, student in enumerate(ogrenciler[0:3]):
    print( "muhendislik kazananlar", index,student)

for index, student in enumerate(ogrenciler[3:7]):
    print( "tıp kazananlar", index,student)
"""


# f string
# ogrenciler = ["Ali","Veli","Ayşe","Talat","Zeynep","Ece"]
# tip_dereceler = ""
# muh_dereceler = ""
#
# for i, ogrenci in enumerate(ogrenciler, 1):
#     if i < 4:
#         muh_dereceler = f"Mühendislik Fakültesi  {i}  . öğrenci:  {ogrenci}"
#         print(muh_dereceler)
#     else:
#         tip_dereceler = f"Tıp Fakültesi  {i - 3}  . öğrenci:  {ogrenci}"
#         print(tip_dereceler)

# List comp.
# students = ["Ali","Veli","Ayşe","Talat","Zeynep","Ece"]
# student_list = [f'Muhendislik Fakultesi: {index}. ogrenci: {student}' if index < 4 else f'Tip Fakultesi {index - 3}. ogrenci: {student}' for index, student in enumerate(students, 1)]
# for i in student_list:
#     print(i)

# Question 7

ders_kodu = ["CMP1005", "PSY1001", "HUK1005", "SEN2204"]
kredi = [3,4,2,4]
kontenjan = [30,75,150,25]

infos = list(zip(ders_kodu, kredi,kontenjan))

for kod, kredi, kontenjan in zip(ders_kodu, kredi,kontenjan):
     print("Kredisi", kredi, "olan",kod, "kodlu dersin kontenjanı",kontenjan, "kişidir.")

# Question 8

kume1 = set(["data", "python"])
kume2 = set(["data","function","qcut", "lambda", "python", "miuul"])

def kume(set1,set2):
    if set1.issuperset(set2):
        print(set1.intersection(set2))
    else:
        print(set2.difference(set1))

kume(kume1,kume2)

"""
if kume2.issubset(kume1):
    print(kume1.intersection(kume2))

else :
    print(kume2.difference(kume1))
"""
