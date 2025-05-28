b="1255487c"
print(b.isdecimal()) # b değişkeninin bütün karakterlerinin ondalık tabanda bir rakam olup olmadığını kontrol eder.
# Yani ( 0 ile 9 arasında ). Aksi durumlarda False döner

print(b.isdigit()) # b değişkeninin sayısal değerlerden oluşup oluşmadığını kontrol eder. Aksi durumda False döner

print(b.isnumeric())# b değişkenini oluşturan bütün karakterler nümerik ise Ture döner

print(b.isalnum()) # b değişkenin hem harf hem rakamlardan oluşup oluşmadığı kontrol eder. Akis durumda False döner

print(b.isascii()) # b değişkeni içerisindeki bütün karakterler ASCII standartında ise True döner
