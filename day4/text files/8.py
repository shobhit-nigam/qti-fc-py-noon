fa = open("books.txt", "r")
lista = fa.readlines()
fa.close()

fb = open("books_3.txt", "w")

print("line numbers which start with 'The':")
for line in lista:
    if line.startswith("The"):
        fb.write(line)

fb.close()
