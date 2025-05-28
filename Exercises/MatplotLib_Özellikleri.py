"""

Mathplotlib in özellikleri

"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
pd.set_option("display.max_columns", None)
pd.set_option("display.width", 500)

"""
1. Özellik

=> plot özelliği

Veriyi göreselleştirmek için kullandığımız fonskiyonlardan birisidir.

"""

x = np.array([1, 8])
y = np.array([8, 150])

plt.plot(x, y) # burada sadece iki nokta arasına çizgi çekti
plt.show(block=True) # burada block=True diyerek demediğimiz zaman grafik ekrana gelmiyor.


plt.plot(x, y, "o") # burada ise iki nokta arasına hem çizgi çekti hemde nokta koydu
plt.show(block=True)

a = np.array([2, 4, 6, 8, 10])
b = np.array([1, 3, 5, 7, 9])

plt.plot(a, b) # bunun diğerinden yukarıdakinden farkı ise: diğerinde noktaları bileştirmiştik. bunda ise bu noktalar
# zaten çizgi üzerinde.
plt.show(block=True)

plt.plot(a, b, "o") # bu kod çalıştırıldığında bunu açıkça rahat rahat görebiliyoruz.
plt.show(block=True)

"""

2. Özellik
=> Marker özelliği
noktalara içi dolu daire koymak istiyorsak bu özelliği kullanıyoruz.

"""

y = np.array([13, 28, 11, 100])

plt.plot(y, marker ="o") # burada ye noktalarını plot özelliğinden dolayı çizgi ile birleştirdi. aynı zamanda y
# noktalarına ise marker özelliği ile içi dolu daire koy ( o )

plt.show(block=True)

plt.plot(y, marker = "*")
plt.show(block=True)

# çok kullanılan bazı marker lar
# markers = ["o", "*", ".", ",", "x", "X", "+", "P", "s", "D", "d", "p", "H", "h"]


"""

3. Özellik
=> Line özelliği
nokta argümanı değilde çizgi olarak takip etmemiz gerektiğinde kullanıyoruz.

"""

z = np.array([13, 28, 11, 100]) # kod çalşıtırıldığında noktalar çizgi ile birleştirilmiş olacak.
plt.plot(z)
plt.show(block=True)

plt.plot(z, linestyle = "dashed") # kod çalıştırıldığında çizgi özelliği kullanıldı görülecektir. burada kullanılan
# çizginin sitili değişrtirilmiş oldu.
plt.show(block=True)

plt.plot(z, linestyle = "dotted") # burada çizgi özelliği değiştirilmiştir.
plt.show(block=True)

plt.plot(z, linestyle = "dashdot", color = "r") # burada hem çizginin türü hemde çizginin rengini değiştrmiş olduk.
plt.show()

"""

4. Özellik
=> Multiple Lines
Çoklu çizgiler özelliği 
"""

s = np.array([23, 18, 31, 10])
k = np.array([13, 28, 11, 100])

plt.plot(x)
plt.plot(y)
plt.show(block=True)
# yukarıda direk kodu bu şekilde çalıştırdığımızda her iki array deki noktaları ayrı ayrı olarak ve farklı renkte
# göstermektedir.


"""

5. Özellik
=> Labels (etiketler)

"""
# burada dikkat etmemiz ferek şey şu her iki değişkenin de aynı elemanlı olması gereklidir.
g = np.array([80, 85, 95, 100, 105, 110, 115, 120, 125])
h = np.array([240, 250, 270, 280, 290, 300, 310, 320])
plt.plot(g, h)

# başlık
plt.title("Bu deneme grafiği")

plt.xlabel(" X Ekseni İsimlendirilmesi")
plt.ylabel(" Y ekseni İsimlendirilmesi")
plt.grid()
plt.show()


"""

6. özellik
=> Subplots
Birden fazla göreselin birlikte gösterilmesi çalışmaları

"""
# 2 grafiği bir satır 2 sütun olarak konumlamak.
# plot 1
f = np.array([80, 85, 95, 100, 105, 110, 115, 120, 125])
j = np.array([240, 250, 270, 280, 290, 300, 310, 320])
plt.subplot(1, 2, 1) # burada diyoruz ki 1 satırlık 2 sütunluk bir grafiğin 1. parçasını oluştur.
plt.title("1") # 1. parçanın başlığı da 1 dir.
plt.plot(f, j)

# plot 2
f = np.array([80, 85, 95, 100, 105, 110, 115, 120, 125])
j = np.array([240, 250, 270, 280, 290, 300, 310, 320, 330])
plt.subplot(1, 2, 2) # burada diyoruz ki 1 satırlık 2 sütunluk bir grafiğin 2. parçasını oluştur.
plt.title("2") # 2. parçanın başlığı da 2 dir.
plt.plot(f, j)


# 3 grafiği bir satır 3 sütun olarak konumlamak

# plot 1
f = np.array([80, 85, 95, 100, 105, 110, 115, 120, 125])
j = np.array([240, 250, 270, 280, 290, 300, 310, 320, 330])
plt.subplot(1, 3, 1) # burada diyoruz ki 1 satırlık 3 sütunluk bir grafiğin 1. parçasını oluştur.
plt.title("1") # 1. parçanın başlığı da 1 dir.
plt.plot(f, j)

# plot 2
f = np.array([80, 85, 95, 100, 105, 110, 115, 120, 125])
j = np.array([240, 250, 270, 280, 290, 300, 310, 320, 330])
plt.subplot(1, 3, 2) # burada diyoruz ki 1 satırlık 3 sütunluk bir grafiğin 2. parçasını oluştur.
plt.title("2") # 2. parçanın başlığı da 2 dir.
plt.plot(f, j)

# plot 3
f = np.array([80, 85, 95, 100, 105, 110, 115, 120, 125])
j = np.array([240, 250, 270, 280, 290, 300, 310, 320, 330])
plt.subplot(1, 3, 3) # burada diyoruz ki 1 satırlık 3 sütunluk bir grafiğin 3. parçasını oluştur.
plt.title("3") # 3. parçanın başlığı da 3 dir.
plt.plot(f, j)
