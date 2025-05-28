"""
def double(x): # burada bir argümanlı double isminde bir fonksiyon tanımlandı.
    return x*2 # bu fonskiyondan elde edilen çıktıyı istediğimiz yere döndürmek için return kullanıldı.
print(list(map(double, [1,2,3,4,5,6,7,8,9]))) # print içersinde yukarıda tanımlanan fonksiyon çağrıldı.

"""


"""
print(list(map(lambda x : x*2, [0,1,2,3,4,5,6,7,8,9]))) # yukarıda kod lambda ile yazıldı

"""



liste1 = [1,2,3,4]
liste2 = [5,6,7,8]
liste3 = [9,10,11,12,13]

print(list(map(lambda x,y : x*y, liste1,liste2))) # burada liste1 ile liste2 elemanları bire bir eşleşti ve çarpımı
# liste olarak döndü

print(list(map(lambda x,y,z : x*y*z, liste1,liste2,liste3))) # burada ise liste1 liste2 liste3 elemanları sırası ile
# birbiri ile eşleşti ve çarpıldı. ancak burada şöylw bir duruım oluştu: liste1 ve liste2 nin eleman sayısı eşit ama
# liste3 ün elleman sayısı farzla olduğu için eleman sayısı az olana göre eşleşme yapıldı ve ekrana yazdırıldı.

print(list(map(lambda x,y : x*y, liste1,liste3))) # burada da aynı üste ki kod bloğunda olduğu gibi eleman sayıları az
# olana göre eşleşme yapılıp çarpıldı. fazla olan eleman dışarıda kaldı.