# Numpy Array i oluşturma örnekleri


import numpy as np

np.array([1, 2, 3, 4]) # buradan bir liste üzerinden bir array oluşturuldu.

np.zeros(10, dtype=int) # burada sıfırlardan bir array oluşturuldu. 10 adet integer veri tipinde bir array oluşturuldu.

np.random.randint(0, 10, size=10) # random mdolünü kulanarak array oluşturuldu.  burada 0 ile 10 arasından rastgele 10
# tane integer tipinde elemanları olan bir array oluştur.

np.random.normal(10, 4, (3, 4)) # burada ramdom modülün normal fonksiyonunu kullanarak normal dağılım şeklinde bir
# array oluşturduk. oluşturmak istediğimiz normal dağılımın kitlenin ortalaması 10, standart sapması 4, boyutu (3, 4)
# olan bir array oluşturduk.

# bunlar bazı örneklerdir. daha fazlası için random modülü içersindeki arrray oluşturma metodları incelenebilir.
