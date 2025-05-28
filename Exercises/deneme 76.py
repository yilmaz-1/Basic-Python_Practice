# a = int(input("sayi1:"))
# b = int(input("sayi2:"))
# liste = []
#
# for sayi in range(a,b+1):
#     if (sayi>1):
#         for i in range(2,sayi):
#             if (sayi%i==0):
#                 break
#         else:
#             liste.append(sayi)
# print(liste)

def asalSayiBulma(a,b):
    liste=[]
    for sayi in range(a,b+1):
        if sayi>1:
            for j in range(2,sayi):
                if (sayi % j ==0):
                    break
                else:
                    liste.append(sayi)
    return liste



print(asalSayiBulma(2,50))

