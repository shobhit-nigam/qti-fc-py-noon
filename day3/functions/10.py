ga = 70

def funca():
    global ga
    lb = 90
    ga = 88
    print("inside ga =", ga)
    print("lb =", lb)

print("ga outside =", ga)
funca()
print("ga outside =", ga)



