x=0
k=[]
l=[]
m=[]
# while x<100:
#     x+=1
#     k.append(x)
# print(k)

# while x<100:
#     print(l) bu kod sağlıklı değil
#     l.append(x)
#     x+=1

# while x<100:
#     if x %2==0:
#         m.append(x)
#         print(f'çift sayı:{x}')
#     else:
#         print(f'sayı tek:{x}')
#     x+=1
# print(m)

name='' # burada ki boşluk karakteri False olarak değerlendirilir.

while not name.strip(): # burda yazılan .strip ifadesi ile kullanıcıdan istenen name de (isminizi giriniz kısmında) eğer boşluk karakteri girildi ise onu sağdan ve soldan silmeye yara böylelikle kullanıcı boşluk girse bile bu girilen boşluk , karakter olarak algılanmaz ve döngü başlamaz.
    name =input("İsminizi Giriniz:")
print(f"Merhaba {name}")

# yukarıda ki kodda şunu demek istiyor: name boşluk olduğu sürece bu döngü başlamayacak
# çünkü başlma şartı name min boşuk olmama durumuna göre yapılmış. biz boşluk girersek
# name direk golbalde tanımlanan ile aynı olacak ve döngü başlamaycak. while döngüsünüsün başlama şartı (not name)
# yani name min boşluk olmama durumunda başlayacak. boşluk haricinde bir karakter giridiğimizde
#not mane kısmı True olarak algılanacak ve döngü başlayacak .
















