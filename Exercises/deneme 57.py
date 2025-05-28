
y1=int(input("yazılı1:"))
y2=int(input("yazılı2:"))
s=int(input("sözlü:"))
ortalama=(y1+y2+s)/3

if (ortalama >=0 and ortalama <25):
    print("Karne notu: 0")
elif (ortalama > 24 and ortalama < 45 ):
    print("karne notu: 1")
elif (ortalama > 44 and ortalama < 55):
    print("karne notu: 2 ")
elif (ortalama > 54 and ortalama < 70):
    print("karne notu: 3")
elif (ortalama > 69 and ortalama < 85):
    print("karne notu: 4 ")
elif (ortalama > 84):
    print("karne notu: 5")

# çıktı:
#yazılı1:56
# yazılı2:65
# sözlü:36
# karne notu: 2

# ********************************************************************

def nothesaplama(y1,y2,s): # nothesaplama isimli üç argümanlı bir fonksiyon oluşturuluyor. aşağıda if elif ve else den oluşan koşul blokalrı oluşturuluyor. program hangi kod bloğunda sağlanırsa o blok çalışıyor.
    if (ortalama >= 0 and ortalama < 25):
        print("Karne notu: 0")
    elif (ortalama > 24 and ortalama < 45):
        print("karne notu: 1")
    elif (ortalama > 44 and ortalama < 55):
        print("karne notu: 2 ")
    elif (ortalama > 54 and ortalama < 70):
        print("karne notu: 3")
    elif (ortalama > 69 and ortalama < 85):
        print("karne notu: 4 ")
    elif (ortalama > 84):
        print("karne notu: 5")
    return # return ile fonksiyon döndürüyor.

while True:
    y1 = int(input("yazılı1:"))
    y2 = int(input("yazılı2:"))
    s = int(input("sözlü:"))
    ortalama = (y1 + y2 + s) / 3
    print("not sonucu")
    nothesaplama(y1, y2, s)

# çıktı:
# yazılı1:10
# yazılı2:20
# sözlü:30
# not sonucu
# Karne notu: 0
# yazılı1:
