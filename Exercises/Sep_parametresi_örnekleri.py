print("L", "i", "n", "u", "x")  # burada klasik yöntemle Linux ifadesi ekrana yazdırılıdı.
# L i n u x

print("L", "i", "n", "u", "x", sep=".")  # burada Linux ifadesi klasik yöntemle ekrana yazdırıldı ve sep parametresi
# yardımı ile her bir krakter arasına . işareti konuldu.
# L.i.n.u.x

print(*"Linux")  # burada * parametresi kullanılarak Linux ifadesi parçalanarak ekrana yazdırıldı.
# L i n u x

print(*"Linux", sep=".")  # burada * parametresi ile Linux ifadesi kullanılarak ekrana uazdılrıldı ve sep parmetresi ile
# parçalanan Linux ifadesia rasına da nokta işareti konuldu.
# L.i.n.u.x

print("Linux")  # burada klasik olarak bildiğimiz print fonksiyonu ile Linux ifadesi ekrana yazdırıldı.
# Linux
