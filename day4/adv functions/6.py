listx = [10, 20, 45, 67, 90, 100, 83, 62]
listy = [13, 18, 20, 25, 11, 32, 61]


res_m = list(map(lambda x, y: x if x > y else y, listx, listy))
print("res_m =", res_m)
        


