# def toplama(a,b,c):
#     return a+b+c
#
#
#
#
# def ikiyleCarp(a):
#     return a*2
#
#
#
# print(toplama(3,4,5))
#
# print(ikiyleCarp(toplama(3,4,5)))
#
#

def ucleCarp(a):
    print("1.fonksiyon çalıştı")
    print(a*3)
    return a*3
def ikiyeBol(a):
    print("2.fonksiyon çalıştı")
    print(a/2)
    return a/2
def dörtleTopla(a):
    print("3. fonksiyon çalıştı")
    print(a+4)
    return a+4

print(ucleCarp(ikiyeBol(dörtleTopla(20))))


