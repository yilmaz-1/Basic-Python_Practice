a="mehmet" # burada a isimli bir değişken tanımladı. bu değişeken mehmet strign karakter dizini atıldı.
# bu karakter dizini 6 karakterden oluşmaktadır. kaç karakterden oluştuğu önmeli olacak aşağıdaki örenkleri açıklarken.

print(a.rjust(8,"*")) # burada yapılmak istenen şey şudur: a değişkeni ekrana yazılsın ama bu değişekn sağa yaslansın
# ve yıldız koyulsun sol tarafına. fakat burada önemli nokta şudur: a değişkeni içinde tanımladığımız karakter dizini
# 6 karakterden oluşuyor. biz ise 8 karaket belirttik parantez içinde. bu durumda a değişkeni yani 6 karakterlik dizin
# sağa yaslanacak kalan karakter sayısı 2 olacağı için ifadenin son tarafına 2 yıldız koyulacak. Kısaca biz 8 karakterlik
# dizin tanımladık 6 sı a değişkenine gitti geri kalanı da parantez içinde istediğimiz yıldız için kullnıldı.
#çıktı
# **mehmet

print(a.ljust(8,"*")) # burada yapılmak istenen şudur: yukarıda tanımladığımız a değişkeni ekrana basılacak yazdırılacak
# fakat dikkat etmemiz gereken durum şu: parantez içinde yazdığımız 8 ifadesi ekrana yazdıracağımız karakter dizinin boyunu
# ifade eder.yanında ki çift tırnak içinde ki yıldız ise ifadenin sağına yazdırılacak simgeyi ifade eder. burada deniyor
# 8 karakter boyunda bir dizi oluştur. a değişkenin sola yasla ve gerikalan karakter dizinine ise yıldız simgelerini yaz.
# 6 karakter mehmet ifadesi geri kalan 2 karaktere de yıldız ifadesi yazdırıldı.
# çıktı:
#mehmet**

print(a.center(10,"*")) # burada ise yapılmak istenen şey su: 8 karakterbir dizi oluştur. a değişkenin bu oluşturduğun
# dizinin merkesine koy geri kalan karakter dizinlerine ise çift tırnak içndeki yıldız ifaesini yerleştir. 8 karakter
# boyunda bir dizi oluşturuluyor. 6 karakter boyundaki a değişkeni merkeze yerleştiriliyor. değişkenin sağında ve solunda
#kalan boş karakterlere ise çift tırnak içinde yer alan ifade yazdırılıyor.
#çıktı:
# **mehmet**

print(a.center(9,"*"))
# çıktı
#**mehmet*