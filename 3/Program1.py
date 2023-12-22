def fun():
    def inner1():
        return "inner1"

    def inner2():
        return "inner2"
    return inner1,inner2
retFun = fun()
for x in retFun:
    print(x())

