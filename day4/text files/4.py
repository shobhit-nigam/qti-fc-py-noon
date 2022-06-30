with open("books.txt", "r") as fa:
    stra = fa.read()

print(stra[15:])
print("-----")
lista = stra.splitlines()
print(lista[2])
