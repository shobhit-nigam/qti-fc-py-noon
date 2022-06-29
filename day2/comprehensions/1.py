def funca(i):
    return i**2

lista = [2, 6, 10, 9, 4, 7]
listb = []

for x in lista:
    y = funca(x)
    listb.append(y)

print(listb)

listc = [x**2 for x in lista ]
print(listc)





