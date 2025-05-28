liste1=[1,2,3,4,5]
liste2=["mehmet","hasan","ahmet","mahmut","veli"]
liste3=[100,200,300,400,500]


print(list(zip(liste3,liste2,liste1)))

for i in (zip(liste3,liste2,liste1)):
    print(i)

for i,j,k in (zip(liste3,liste2,liste1)):
    print(i,j,k)