
"""
# kullanım 1 => os modülünü programa dehil ettik. Bundan sonra modül içerisndeki istediğimiz foksiyonu, os.foksiyonismi
şeklinde kullanabiliriz.

import os

if os.name=="nt":
    print("windows")
else:
    print("windows dışında bir işletim sistemi.")

"""


"""
# kullanım 2 => os modülünü programa dahil ettik fakat burada bu kullanım şekli ile yukarıdaki kullanım şekli arasında 
fark yok aynı şey. sadece bu kullanım şeklinde modüladi.foksiyon şeklinde yazmamıza gerek kalmıyor. os.foksiyonadi 
yazmamıza gerek yok. direk fonskiyon ismini yazarak da kullanabilmemizi sağlıyor.

from os import *

if name=="nt":
    print("windows")
else:
    print("windows dışında bir işletim sistemi")



# Not: nt ye eşit yapmamızın sebebi windows cihazlarda ki işletim sisteminin karşığı verdiği cevap nt olduğu için

"""