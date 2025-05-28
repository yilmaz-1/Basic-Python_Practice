# aşağıda sözlük uygulaması ile ilgili bir program yapıldı. bu uygulamada önemli numaraları bulmak için kullanılacak.


onemli_Numaralar={

    "Polis": "155",
    "İtfaiye": "110",
    "Ambulans": "112",
    "Jandarma": "156",
    "Trafik": "154"
} # burada bir adet sözlük tanımladı.

kurumAdi=input("Lütfen Numarasını Öğrenmek istediğiniz Kurumun Adını Yazınız: ") # kullanıcıdan kurum adını yazmasını
# istiyoruz.

if kurumAdi in onemli_Numaralar.keys(): # eğer kullanıcının girdiği kurumAdi değişkeni oneml_Numaralar sözlüğünün
    # anahtarları içersinde varsa
    print(f"{kurumAdi}: {onemli_Numaralar[kurumAdi]}") # ekrana yazdır.
else: # değilse
    print("Numara Bulamadı...")

