
def decorFunc(func):
    def wrapper():
        print("Start wrapper")
        func()
        print("End wrapper")
    return wrapper
def normalFun1():
    print("Hello from normal fun-1")

def normalFun2():
    print("Hello from normal fun-2")

normalFun1 = decorFunc(normalFun1)
normalFun2 = decorFunc(normalFun2)
normalFun1()
normalFun2()
