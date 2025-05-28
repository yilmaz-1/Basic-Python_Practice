# Aşğıda bir tane taş kağıt makas oyunu programı yazıldı.

import random # program içerisinde lazım olacak olan modül programa import ile dahil edilmiştir.

biz_puan=0 # burada bizim ve pc nin puan durumunu tanımladık. başlangıçta her iki oyuncunun da puanı sıfır.
pc_puan=0

secenekler= ("taş","kağıt","makas") # burada secenekler isminde bir değişken tanımlandı. amacımız oyun içersinde
# kullanıcağımız seçenekleri belirlemek tanımlamak. burada seçenekleri demet olarka tanımlamamızın nedeni: başka seçenek
# yok ve biz bu mevcut seçeneklerin değiştirilmesini de istemiyoruz. liste şeklinde de tanımlama yapabiliridk ama
# o liste içerisindeki veriler ile rahatlıkla oynanabilirdi. değişiklik yapılabilir di.

biz= input("taş ? kağıt ? makas ? çıkmak için q => ") # burada kullanıcıdan hangi seçeneneği seçtiğini girmesi
# istiyoruz. tercihi ne? onu öğrenmek istiyoruz.

while biz!="q":# burada bir adet döngü kurduk. amacımız oyun sürekli devam etsin yani dönsün istiyoruz. yani, biz bir
    # tercih yaptık pc bir tercih yaptı sonra bu tercihler karşılaştırıldı kazanan kaybeden belirlendikten sonra oyun
    # tekrar başlasın ve bu durum kullanıcı q hafrini girene kadar devam etsin istedik ve bir while döngüsü kurduk.
    # biz değişkeni q ifadesine eşit olmadığı sürece devam etmesini istedik bu döngünün.
    pc=random.choice(secenekler) # burada pc nin bir seçim yapmasını istedik. fakat burada önemli olan şey şu: pc
    # seçimi secenekler değişkeni içersinde tanımlanmış ifadelerden seçmesini istedik , daha da önemlisi şu: bu
    # seçimleri ramdom modünü kullanacak ve bu modlünün choice parametresi ile kullanacak. her döngünün başında
    # secenekler değişkeni içerisinden rastgele bir seçim yapacak.

    print(f"Biz: {biz}, Bilgisayar: {pc}") # burada bzim yaptığımız seçim ve pc nin yaptığı seçimi ekrana bastırıyoruz.

    if (biz=="taş" and pc=="kağıt"): # burada bir şart bloğu oluşturuldu. Eğer bizim tercimiz taş ve pc nin tercihi kağıt
        # ise, bu şart aynı anda sağlanıyor ise (and ile bağlanmış)
        print("PC kazandı...")# ekrana yazdır.
        pc_puan+=1
    elif (biz=="taş" and pc=="makas"): # eğer bizim tercihimiz taş  ve pc nin tercihi makas ise
        print("Biz Kazandık...") # ekrana yazdır.
        biz_puan+=1
    elif (biz=="kağıt" and pc=="taş"):
        print("Biz Kazandık...")
        biz_puan+=1
    elif (biz=="kağıt" and pc=="makas"):
        print("Pc Kazandık...")
        pc_puan+=1
    elif (biz=="makas" and pc=="taş"):
        print("Pc Kazandı...")
        pc_puan+=1
    elif (biz=="makas" and pc=="kağıt"):
        print("Pc Kazandı...")
        pc_puan+=1
    else: # yukarıdaki şartlardan hiç biri değilse yani her iki seçim de aynı dır. makas makas , taş taş gibi...
        print("Berabere") # ekrana yazdır.

    biz=input("taş ? kağıt ? makas ? çıkmak için q => ") # burada bu şekilde tekrar bir seçim girmesini istememizin
    # nedeni döngünün sonsuz döngüye girmesini önlemek ve tekrar tekrar başa dönebilmesini sağlamak.

print(f"Bizim Puan : {biz_puan}, Pc Puan: {pc_puan}") # burada döngü bittikten sonra puan durumunu ekrana yazdırdık.

