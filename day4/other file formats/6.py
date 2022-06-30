import csv

listx = ["num", "series", "character"]
lista = [1, "fleabag", "fleabag"]
listb = [2, "Saul goodman", "better call Saul"]

with open('csv_2.csv', 'w') as fa:
    objw = csv.writer(fa)
    objw.writerow(listx)
    objw.writerow(lista)
    objw.writerow(listb)
