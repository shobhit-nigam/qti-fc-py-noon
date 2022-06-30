listx = [10, 20, 45, 67, 90, 100, 83, 62]
listy = [13, 18, 20, 25, 11, 32, 61]

def funca(x):
    return x%10 == 0

res_m = list(filter(funca, listx))
print("res_m =", res_m)
        


