tup_a = ("xx", ["aa", "bb"], 18, 23, 6)
# no error
tup_a[1][0] = "ff"


#error
tup_a[1] = "ff"
tup_a[1][0][0] = "F"
