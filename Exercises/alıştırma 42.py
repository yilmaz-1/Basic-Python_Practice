import turtle # burada turtle modülü programa dahil edildi.

def kareciz (): # bruada bir adet parametresiz kareciz isminde bir fonksiyon tanımlandı.
    turtle.home() # burada turtle modülünün home fonksiyonu kullanılarak çizimin tekrar başa dönmesi sağlandı.
    for i in range(4): # burada bir döngü kuruldu. bu döngü range fonksiyonu sayesinde 4 defa dönesmi sağlandı.
        # her döngüde de aşağıda tanımlanan işlemleri yapacak.
        turtle.fd(100) # 100 birim ileri
        turtle.left(90) # 90 derece sola dön

# tanımlana fonksiyon bitti

kareciz() # burada ise yukarı da tanımlanan fonksiyon çağrıldı.a