print("Mükemmmel Sayı Bulma")
sayı = int(input("sayı:"))
i=1
toplam=0

while(i<sayı):
    if (sayı % i == 0):
        print("i:",i)
        toplam+=i
        print("toplam:",toplam)
    i+=1

if (sayı==toplam):
    print("mükemmel sayı")
else:
    print("mükemmel sayı değildir.")
