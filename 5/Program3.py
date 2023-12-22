def outer():
    def inner():
        print("In inner function")
        return "Shubham"
    return inner
retInn = outer()
print(retInn())
