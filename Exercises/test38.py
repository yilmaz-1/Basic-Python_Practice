def asal_mi (sayı):
    if sayı==1:
        return False
    elif sayı==2:
        return True
    else:
        for i in range(2,sayı):
            if sayı % i ==0:
                return print(f"{sayı}'sayısı asal sayı değildir.")
        return print(f"{sayı}'sayısı asal sayıdır.")

print(asal_mi(15))