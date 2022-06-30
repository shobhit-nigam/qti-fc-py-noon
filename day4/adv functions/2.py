listx = [10, 20, 45, 67, 90, 100, 83, 62]
listy = [13, 18, 20, 25, 11, 32, 61]

def funca(x, y):
    return 2*x + y - 20

res = []

if len(listx) < len(listy):
    for i in range(len(listx)):
        res.append(funca(listx[i], listy[i]))
else:
    for i in range(len(listy)):
        res.append(funca(listx[i], listy[i]))

print("res =", res)

res_m = list(map(funca, listx, listy))
print("res_m =", res_m)
        


