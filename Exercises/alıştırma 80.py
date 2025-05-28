"""
öle bir fonksiyon yazalım ki kendisine girilen string ifadenin çift indexinde yer alan karakterleri büyütsün
tek indexinde yer alan karakterleri ise küçültsün
bu fonksiyon ise enumerate fonksiyonu ile yazılsın.

"""


def alternating_with_enumerate(string): # bir argümanlı bir fonksiyon tanımlandı. bu argümanı bir dışarıdan fonskiyonna
    # göndereceğiz.
    new_string = "" # bu boş değişkeni, işlem yapıp son halini verdiğimiz string ifadeyi yollamak için kullanacağız.
    for i, letter in enumerate(string): # kullanıcınn fonskiyon içersine gönderdiği string ifadenin hem index hemde
        # karakteri üzerinde gezinebilmek için enumerate fonskiyonu ile for döngüsü kuruldu. burada range(len(string))
        # ile yapabilrdik. ama enumerate fonskiyonu ile daha kısa ve okunabilir olması için daha mantıklı bir yol.
        if i % 2 == 0: # elde ettiğimiz index değerlerinden çift olan varsa
            new_string += letter.upper() # bu indexe karşılık gelen karakteri büyüt be boş stringe ekle
        else: # eğer tek olan indexe denk gelen karakter varsa onu da
            new_string += letter.lower() # küçült ve boş olan stringe ekle
    print(new_string) # ekrana yaz

alternating_with_enumerate(string="mehmet bugün işe gelmedi ama yarın işe erken gelecek")