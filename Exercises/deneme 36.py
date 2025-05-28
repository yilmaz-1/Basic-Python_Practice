def toplama(*a): # burada önemli olan şey şu '*' parametrenin önüne yıldız koydumuz zaman artık bu foksiyonda ki değerler  esnek oluyor.
    print(a) # fonksiyona gönderilen parametreler ekrana bastırılıyor.

toplama(1,2,3)
# çıktı:
# (1, 2, 3)

toplama(1,2,3,4,5)
# çıktı:
# (1, 2, 3, 4, 5)

toplama(1,2,3,0,45,63,7,8,9,56,6) # görüldüğü üzere yıldız koyunca bu foksiyon esnek sayılar ile çalışmaya başladı.
# çıktı:
# (1, 2, 3, 0, 45, 63, 7, 8, 9, 56, 6)
