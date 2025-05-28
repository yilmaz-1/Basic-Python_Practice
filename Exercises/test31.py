liste = []

# for i in range(10):
#     liste.append(i)
# print(liste)
# #çıktı:
# # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
#
# liste = [i for i in range(10)]
# print(liste)
# # çıktı:
# # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]


# for i in range(10):
#     liste.append(i**2)
# print(liste)
# # çıktı:
# # [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
#
# numbers = [i**2 for i in range(10)]
# print(numbers)
# #çıktı:
# # [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]


# for i in range(30):
#     if i % 3 ==0:
#         i*=5
#         liste.append(i)
# print(liste)
# # çıktı:
# #[0, 15, 30, 45, 60, 75, 90, 105, 120, 135]
#
# numbers = [i*5 for i in range(30) if i % 3 == 0]
# print(numbers)
# # çıktı:
# # [0, 15, 30, 45, 60, 75, 90, 105, 120, 135]


# string = "merhaba"
#
# for i in string:
#     liste.append(i)
# print(liste)
# # çıktı:
# # ['m', 'e', 'r', 'h', 'a', 'b', 'a']
#
# myString = [i for i in string]
# print(myString)
# # çıktı:
# # ['m', 'e', 'r', 'h', 'a', 'b', 'a']

# years =[1986,1985,1996,2005,1976]

# age = [2021-i for i in years]
# print(age)
# #çıktı:
# # [35, 36, 25, 16, 45]

# for i in years:
#     age = 2021-i
#     liste.append(age)
# print(liste)
# # çıktı:
# # [35, 36, 25, 16, 45]

# numbers =[x if x%2 ==0 else "Tek"  for x  in range(1,10)]
# print(numbers)
# # çıktı:
# # ['Tek', 2, 'Tek', 4, 'Tek', 6, 'Tek', 8, 'Tek']
#
# for x in range(1,10):
#     if x%2 ==0:
#         liste.append(x)
#     else:
#         liste.append("Tek")
# print(liste)
# # çıktı:
# # ['Tek', 2, 'Tek', 4, 'Tek', 6, 'Tek', 8, 'Tek']


for i in range(3):
    for j in range(3):
        liste.append((i, j))
print(liste)
# çıktı:
# [(0, 0), (0, 1), (0, 2), (1, 0), (1, 1), (1, 2), (2, 0), (2, 1), (2, 2)]

numbers = [(i, j) for i in range(3) for j in range(3)]
print(numbers)
# çıktı:
# [(0, 0), (0, 1), (0, 2), (1, 0), (1, 1), (1, 2), (2, 0), (2, 1), (2, 2)]
