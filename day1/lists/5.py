lunch = ["potato", 'dal chawal', 'combo "meals"', "curd rice"]
drink = ["butter milk", "tea", "coffee"]
lunch.append(drink)
print(lunch)
print("0000000000000")
lunch = ["potato", 'dal chawal', 'combo "meals"', "curd rice"]
drink = ["butter milk", "tea", "coffee"]
lunch.extend(drink) 
print(lunch)

a = [200, 300, 400, 500, [100, 200], 200]
print(a.count(200))
print(a[4].count(200))
