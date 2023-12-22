def outer():
    print("In outer func")
    def inner1():
        print("In inner 1")
    def inner2():
        print("In inner 2")
    return inner1,inner2

ret = outer()
ret[0]()
ret[1]()

