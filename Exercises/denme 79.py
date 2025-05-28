x = "global x"

def function ():
    #global x  eğer biz globalde tanımlanmış x i fonksiyon içinde kullanmak isteresek global sözcüğü ile onu belirtmemiz lazım. fonksiyon içinde aynı isimde bir değişken varsa misal hem globalde hemde local x değişkeni var ama her iki değişkenin de değeri farklı veya globalde x lacal de y var ama ben glbaldeki x i kullancak isem fonksiyon içinde glabl sözcüğü ile kullanmam lazım.
    x = "local x"
    print(x)

function()
print(x)

# çıktı:
# local x
# global x
