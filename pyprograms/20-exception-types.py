'''
print("Demonstration of zero division error")
n1 = int(input("Enter first number"))
n2 = int(input("Enter second number"))
result = n1/n2
print("result of division ",result)
'''
"""
print("Demonstration of list index out of range")

marks=[10,3,12,4,23,21]

print(marks)
print(marks[0])
print(marks[6])
print("after printing")
"""
print("type error")
class Employee():

    def __init__(self,code,name):
        self.code = code
        self.name = name

    def info(self):
        print("details :Code ",self.code," Name : ",self.name)

emp1 = Employee(1,"raghu")
print(emp1)
emp1.info()
emp2 = Employee()
print(emp2)
emp2.info()
print ("null or None error")
emp1=None #null
print(emp1.info())








