def funca():
    x = "xxxxx"
    print("outer function")

    def funcx():
        nonlocal x
        print("inner function")
        x = 27307
        print ("within inner x =",  x)
    
    funcx()
    print("outerx =", x)
