def outer():
    def inner1(x,y):
        print("In inner 1 function")
        return x+y
    def inner2(a,b):
        print("In inner 2 function")
        return a*b
    return inner1,inner2

retVal = outer()
for i in retVal:
    print(i(10,20))


