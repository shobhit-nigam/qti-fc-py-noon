fa = open("books.txt", "r")
lista = fa.readlines()
fa.close()

fb = open("new_books.txt", "w")

for line in lista:
    if "and" in line:
        fb.write(line)

fb.close()
