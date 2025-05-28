import numpy as np
rng = np.random.RandomState(123)
for i in np.arrange(1,21):
    deney_sayisi = 2**i
    yazi_turalar = rng.randint(0,2,size = deney_sayisi)
    yazi_olasılıklari = np.mean(yazi_turalar)
    print("Atış Sayısı:",deney_sayisi,"----",'Yazı Olasılığı: %.2f' % (yazi_olasılıklari * 100))