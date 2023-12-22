class Me:
    name = "Shubham"
    def __new__(self):
        print("Memory Allocated")
        return super().__new__(self)
    def __init__(self):
        print("In constructor")
    def disp(self):
        print(Me.name)
obj = Me()
obj.disp()

