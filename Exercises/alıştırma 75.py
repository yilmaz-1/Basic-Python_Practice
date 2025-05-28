"""
liste1 = ["elma", "armut", "muz", "kiraz"] # burada liste1 isminde bir değişken oluşturduk

sonuc = list() # aşağıdaki döngüde kullanılmak üzere boş bir liste oluşturuldu.

i = 0 # aşağıdaji döngüde kullanılmak üzrere bir i değişkeni tanımlandı ve sıfır atandı.
for j in liste1: # liste bir içersinden her döngüde bir j değeri alınarak
    sonuc.append((i,j)) # her döngüde i ve j değerleri sonuc isimli boş listeye yollandı
    i+=1 # her döngüde i değeri bir artırıldı.
print(sonuc) # sonuc değişkeni döngü bitince ekrana yazdırıldı.

# yukarıda yer alan kod daha kısa bir şekilde nasıl yazılır ? python da gömüllü bir fonksiyon olan enumerat() fonskiyonu
# ile tek satırda kolaylıkla yazılabilir.

print(list(enumerate(liste1)))


"""


liste = ["a","b", "c", "d", "e","f","g"] # burada bir adet liste oluşturuldu.

for index,eleman in enumerate(liste): # enumerate fonksiyonu  ile oluşturulan (index, eleman) çiftlerinden her döngüde
    # ayrı ayrı alınıyor.
    if (index % 2 == 0): # her döngüde elde edilen index sayısı eğer çift ise
        print("Eleman:", eleman) # ekrana o index de ki elemanı bas.

