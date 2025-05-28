
# bu subprocess modülü alt işlem anlamına geliyor. yani bunu programa dehil ettiğimizde ve çağırdğımızda bilgisayarda
# var olan programlardan hangisini kullanmak istiyorsak onu çalıştırabiliriz

import subprocess as sp # burada subprocess modülü programa dahil edildi fakat sp kısaltması olarak. yani bundan
# sonraki kullanımlar da uzun uzun subprocess yazmamıza gerek yok. direk sp kısaltması ile kullanabiliriz.

program=input("Çalıştırmak İstediğiniz Programı Yazınız: ") # kullanıcıdan girdi istiyoruz.

sp.call(program) # fonskiyon kullanıcının girdiği girdi ile çağrılıyor.


