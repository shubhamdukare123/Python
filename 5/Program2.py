def outer():
    def inner():
        print("In inner function")
    inner()
    print("In outer function")
print("Start Code")
outer()
print("End Code")
