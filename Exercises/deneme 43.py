# string i ters çevirme lamda ifadesini kullanarak

def terscevir(s): # terscevir isminde ve bir argümanı olan bir fonksiyon tanımlandı.
    return s[::-1] # burada return ile, s[::-1] ifadesi ile ters çevrilen string daha sonra çağrılmak üzere tutuldu.
print(terscevir("python programala dili öğreniyorum"))# burada pirnt fonksiyonu içinde, terscvir fonksiyonu çağrdıldı ve argüman olarak da 'python programlama dili öğreniyorum' gönderildi ve kerana basıldı.
# çıktı:
# muroyinerğö ilid alamargorp nohtyp


# yukarıdaki foksiyonu lambda ile ifade edelim
terscevir=lambda s: s[::-1]
print(terscevir("python programala dili öğreniyorum"))
# çıktı:
# muroyinerğö ilid alamargorp nohtyp


def çifttek(sayı): # çifttek isimli ve bir argümanlı bir fonksiyon tanımlanıyor.
    return sayı %2==0 # fonksiyon içine gönderilen sayının 2 ile bölümünden kalan sıfıra eşit olanalrı return ile tutuyor.
print(çifttek(34)) # print fonksiyonu içinde çağrılan çifttek fonksiyonuna 34 argümanı gönderilip çağırdığımızda return ile yaptığımız işlem doğru oluyosa Ture dönüyor bize return ifadesi ile
# çıktı:
#Ture

print(çifttek(13)) #print fonksiyonu içinde çağrılan çifttek fonksiyonuna 13 argümanı gönderilip çağırdığımızda return ile yaptığımız işlem doğru oluyosa Ture, değilse False dönüyor bize return ifadesi ile
# çıktı:
#False

# yukarıdaki foksiyonu lambda ile ifade edelim

çifttek = lambda sayı : sayı %2==0 # çifttek fonksiyonu lambda ifadesi ile tek satırda yazıldı.

print(çifttek(34))
# çıktı:
# True

print(çifttek(13))
#çıktı:
# False