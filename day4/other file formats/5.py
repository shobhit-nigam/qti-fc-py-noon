import csv
import time

with open('csv_1.csv', 'r', encoding="ISO-8859-1") as fa:
    data = csv.reader(fa)

    for row in data:
        print(row)
        time.sleep(2)
        print("-------")

