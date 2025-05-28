print(""" ***** Welcome To Murat Yildiz Bank Account Login System ***** """)

syspassword="12345"
sysusername="murat.yildiz"

enterusername=input("Please Enter Your User Name (all of character lower case):")
enterpassword=input("Pleas Enter Your Password (only numbers):")

if (syspassword==enterpassword and sysusername!=enterusername):
    print("Ohh Sorry something is wrong. You could not enter the system.Pleas try again")
elif (sysusername!=enterusername and syspassword==enterpassword):
    print("Ohh Sorry something is wrong. You could not enter the system.Pleas try again")
elif (syspassword!=enterpassword and sysusername!=enterusername):
    print("Ohh Sorry something is wrong. You could not enter the system.Pleas try again")
else:
    print("You crayz man :) God luck for you... You enter the system... Enjoy İt :))")
# yukarıda ki programda ilk olarak programın adı print ile bastırılıyor. daha sonra sisteme globalde bir şifre ve
# kullanıcı adı tanımlanıyor. daha sonra kullanıcı adı ve şifresinin girilmesi isteniyor.
# if elif ve else kalıbı ile tek tek girilen şifre ve kullanıcı adının doğru veya yanlış olma durumları
# değerlendiriliyor
# en sonunda ise else bloğunda her şeyin doğru olma durumu ve sisteme giriş msjı ekrana yazdırılıyor.

# yukarıda iki elif kullanmak yerine tek elif ile de bu yapılabilirdi. bunun bize şu şekilde faydası olacaktı.
# çok fazla kod satırı olmamış olacaktı böylelikle program ağırlaşmamış olacaktı.
# (sysusername != enterusernanem) or (syspassword != enterpassword)