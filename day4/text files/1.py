fa = open("books.txt", "r")
stra = fa.read(5)
print(stra)

strb = fa.read(6)
print(strb)
fa.close()
