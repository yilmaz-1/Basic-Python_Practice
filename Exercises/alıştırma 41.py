
# aşağıda önemli numaraları bulmada kullanılacak bir program yazıldı.

onemli_Numaralar={

    "Polis": "155",
    "İtfaiye": "110",
    "Ambulans": "112",
    "Jandarma": "156",
    "Trafik": "154"
} # sözlük tanımlandı.

kurumAdi=input("Numarasını Öğrenmek İstediğiniz Kurum Adını Giriniz: ") # kullanıcıdan giriş yapmasının istedik.

deger=onemli_Numaralar.get(kurumAdi,"Bulunamadı") # deger isminde bir adet değişken tanımlandı. bu değişkene
# onemli_Numalar sözlüğünün keys değerleri get() fonksiyonu ile alınarak atandı. eğer kurumAdi değişkeni keys değerleri
# arasında yoksa, Bulunamadı atanacak.

print(f"Öğrenmek İstediğiniz Kurumun Telefon Numarası: {deger}") # ekrana yazıdr.

