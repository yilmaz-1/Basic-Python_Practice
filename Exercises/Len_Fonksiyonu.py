"""
Len fonksiyonu python programlama da kullanılan len() ifadesi ile kullanılır. Bir ifadenini değişkenin yada list, tuple
gibi iterasyon yapılarının kaç elemandan oluştuğunu yada kaç karakterden oluştuğunu tespit etmek için kullanılır.

"""

text = "merhaba dünya"
print(len(text))
# çıktı: text değişkeni içerisinde yer aln "merhaba dünya" string ifadesi 13 elemandan oluşmaktadır.
# boşluk karakteeri dahildir.
# 13

list_1 = ['mehmet', 'hasan', 'Türkiye', 5, 6, 63]
print(len(list_1))
# çıktı: burada list_1 değişkeni içersinde yer alan 'mehmet' gibi çift tırnak içerisinde yer alan
# ifadeler 1 eleman olarak tanımlanmaktadır. bundan dolayı 6 elemanlı olarak çıktı vermiştir.
# 6

list_2 = ('Türkiye', 'Fransa', 'Kazakistan', 'Afrika')
print(len(list_2))
# çıktı:
# 4

test = range(1, 11)  # burada test isminde bir değişken tanımlanıyor ama bu değişkenin içine gönderilecek değerler ise
# range fonksiyonu ile elde ediliyor.
print(len(test))  # bu test değişkenin eleman sayısı len fonksiyonu ile elde edilip print ile ekrana yazdırılıyor.
# çıktı:
# 10

ulkeler = {'Türkiye': 1, 'Almanya': 2, 'Fransa': 3, 'Kamboçya': 4}  # bu sözlük (dictionary) yapısında yer alan eleman
# sayısı keys ve values ('Türkiye':1) için bir adet olarak elemanlıdır.
# keys ve values ifadeleri ayrı ayrı ele alınmamalıdır.
print(len(ulkeler))
# çıktı:
# 4

list_3 = ('Çekya', 'ABD', 'Japonya', 'Suriye')  # list_3 değişkeni içerisinde normal bir liste tanımlanmıştır.
print(len(list_3[1]))  # burada list_3 değişkenin 1 inci indeksinde yer alan ifadenin
# len fonksiyonu ile uzunluğu ekrana yazdırılıyor.
print(len(list_3[0]))  # burada list_3 değişkenin 0 ıncı indeksinde yer alan ifadenin uzunluğu
# len fonksiyonu ile ekrana yazdırılıyor.
# çıktı:
# 3
# çıktı:
# 5

list_4 = [[1, 2], ['Türkiye', 'Hasan', 'Araba'], ['a', 'b', 'c', 5, 6, 8]]
print(len(list_4[1]))
# çıktı:
# 3

list_5 = [[5, 6, 7], [['a', 'd', 'f', 't'], [0, 1, 2, 6, 5]]]
print(len(list_5[1][1]))  # burada list_5 listestesinin 1 indeksinde yer alan elemanın 1 indeksindeki elemanın uzunluğu
# len fonksiyonnu ile uzunluğu hesaplanıp print fonksiyonu ile ekrana yazdırılır.

test_1 = {

    'ad': 'Mehmet',
    'soyad': 'Işık',
    'yaş': '33',
    'okul': 'Karabuk',

}
print(len(test_1['okul']))  # burada test_1 sözlük ifadesinin 'okul' anahtar (keys) ifdesine karşılık gelen
# değerin ( values ) uzunluğu len fonksiyonu ile hesaplanıp print fonksiyonu ile ekrana yazdırılıyor.
# çıktı:
# 7


bilgiler = ['Kerem', 'Akdeniz Üniversitesi', 'Yüksek Lisans', '33', 'Son Sınıf']
i = 0  # burada i isminde bir değişken tanımlandı. bu değişken döngü yapısında kullanmak için tanımladık
# ve 0 olarak belirledik
for i in range(0, len(bilgiler)):  # burada for döngüsü ve range fonksiyonu kullanrak i değerlerini elde etmeye çalıtşık
    # range fonksyonu sıfırdan başlayarak bilgiler listesinin boyu kadar giderek ( yani 5 e kadar giderek )
    # her seferinde bir i değeri elde ediyor. 0,1,2,3,4 ( 5 alınmaz)
    print(bilgiler[i])  # burada elde ettiğimiz her i değeri için tek tek bilgiler listesinin o i değerine
    # karşılık gelen indekste ki elemanı ekrana yazdırıyor.
# çıktı
# Kerem
# Akdeniz Üniversitesi
# Yüksek Lisans
# 33
# Son Sınıf

"""
len fonskiyonunu integer veri tipindeki verilerin uzunluğunu ölçmede kullanamazsınız.
"""

print(len(12546))

# TypeError: object of type 'int' has no len()
