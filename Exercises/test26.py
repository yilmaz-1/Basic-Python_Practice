number = float(input("sayı: "))
result = (number > 0) and (number <= 100)
print(f"sayı 0 - 100 arasında mı: {result}")

result2 = (number > 0) and (number % 2 == 0)
print(f"girilen {number} sayısı sıfırdan büyük ve çift sayı mı ? : {result2} ")
