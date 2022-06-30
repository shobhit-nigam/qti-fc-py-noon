def funca():
    print("outer function")

    def funcx():
        print("inner function")
    
    funcx()
    print("outer again")
