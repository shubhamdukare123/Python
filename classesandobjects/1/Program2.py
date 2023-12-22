class Employee:
    def __new__(self):
        print("Memory allocated")
        return super().__new__(self)
    def __init__(self):
        print("In init")


Employee()
