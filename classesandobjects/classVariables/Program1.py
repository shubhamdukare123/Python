class Company:
    compName = "Facebook"
    def __init__(self, empId, empName):
        print("In constructor")
        self.empId = empId
        self.empName = empName

    def compInfo(self):
        print(self.compName)
        print(self.empId)
        print(self.empName)

emp1 = Company(12, "Shubham")
emp2 = Company(15, "Himanshu")
emp1.compInfo()
emp2.compInfo()
emp1.compName = "Meta"
emp2.compName = "Open-AI"
print(Company.compName)
Company.compName = "Google"
print("After changing to google")
emp1.compInfo()
emp2.compInfo()
print(Company.compName)
