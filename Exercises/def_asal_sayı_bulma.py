"""

print(list(filter(lambda x : x % 2 == 0, [1,2,3,4,5,6,7,8,9,10,12,15,16])))

"""


def asal_mi(x): # burada tek argümanlı bir fonksiyon tanımlandı.
    i = 2 # i değişkeni oluşturuldu . bu değişkenin oluşturulmasının sebebi: aşağıda while ile döngü kuracağımız için
    # bunu oluşturduk.

    if (x==1):
        return False
    elif (x==2):
        return True
    else:
        while (i<x):
            if (x % i ==0):
                return False
            i+=1
    return True

print(asal_mi(x=8))



print(list(filter(asal_mi, range(1,100))))